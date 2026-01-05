import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout
import bmi_logic
from bmi_engine import AdviceFactory
from chart_tool import BMIChart

class MyBMIApp(QtWidgets.QMainWindow):
    def __init__(self):
        super(MyBMIApp, self).__init__()
        uic.loadUi('bmi_ui.ui', self) 
        
        # 設定輸入欄位的提示文字
        self.input_height.setPlaceholderText("請輸入身高 (cm)")
        self.input_weight.setPlaceholderText("請輸入體重 (kg)")
        
        # 初始化圖表與數據紀錄
        self.weight_records = [] 
        self.chart = BMIChart()
        
        # 將圖表放入 UI 中的 chart_container
        layout = QVBoxLayout(self.chart_container)
        layout.addWidget(self.chart)
        layout.setContentsMargins(0, 0, 0, 0)  # 移除邊距
        
        self.btn_calculate.clicked.connect(self.handle_calculation)

    def handle_calculation(self):
        # 1. 從介面抓取文字
        h_text = self.input_height.text()
        w_text = self.input_weight.text()
        
        # 驗證輸入格式與非零值
        try:
            h_value = float(h_text)
            w_value = float(w_text)
            if h_value <= 0 or w_value <= 0:
                QMessageBox.warning(self, "輸入錯誤", "身高和體重都必須大於 0")
                return
        except ValueError:
            QMessageBox.warning(self, "輸入錯誤", "請輸入正確的數字格式")
            return
        
        # 2. 呼叫副程式進行計算
        bmi_result = bmi_logic.calculate_bmi_value(h_text, w_text)
        
        if bmi_result is not None:
            # 使用簡單工廠模式取得對應的健康建議物件
            advice_obj = AdviceFactory.create_advice(bmi_result)
            advice_message = advice_obj.get_info(bmi_result)
            
            # 3. 顯示結果 (包含身高、體重、BMI 和健康建議)
            display_text = f"身高: {h_text} cm  體重: {w_text} kg\n{advice_message}"
            self.label_result.setText(display_text)
            
            # 4. 圖表更新邏輯 - 紀錄體重並更新圖表
            self.weight_records.append(float(w_text))
            self.chart.update_chart(self.weight_records)
        else:
            # 5. 錯誤互動
            QMessageBox.warning(self, "計算錯誤", "計算失敗，請檢查輸入")

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    window = MyBMIApp()
    window.show()
    sys.exit(app.exec_())