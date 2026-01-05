"""
BMI 計算器主程式

這是一個基於 PyQt5 的圖形化 BMI 計算器應用程式。
使用者可以輸入身高和體重，程式會計算 BMI 並提供健康建議。
同時具有體重追蹤圖表功能。

設計模式：簡單工廠模式 (Simple Factory Pattern)
"""
import sys
from PyQt5 import QtWidgets, uic
from PyQt5.QtWidgets import QMessageBox, QVBoxLayout
import bmi_logic
from bmi_engine import AdviceFactory
from chart_tool import BMIChart

class MyBMIApp(QtWidgets.QMainWindow):
    """
    BMI 計算器主應用程式類別
    
    此類別繼承自 QMainWindow，負責：
    - 載入 UI 介面
    - 處理使用者輸入
    - 呼叫 BMI 計算邏輯
    - 顯示健康建議
    - 更新體重追蹤圖表
    
    Attributes:
        weight_records (list): 儲存每次計算的體重記錄
        chart (BMIChart): 體重追蹤圖表物件
    """
    def __init__(self):
        """初始化 BMI 應用程式，載入 UI 並設定圖表"""
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
        """
        處理 BMI 計算按鈕的點擊事件
        
        工作流程：
        1. 從輸入欄位取得身高和體重
        2. 驗證輸入格式與數值有效性
        3. 呼叫 BMI 計算邏輯
        4. 使用工廠模式取得對應的健康建議
        5. 顯示計算結果和建議
        6. 更新體重追蹤圖表
        
        錯誤處理：
        - 非數字輸入：顯示錯誤訊息
        - 零或負數：顯示錯誤訊息
        - 計算失敗：顯示錯誤訊息
        """
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
    """
    程式進入點
    
    只有當此檔案被直接執行時，才會啟動 GUI 應用程式。
    如果此檔案被其他程式 import，不會自動啟動應用程式。
    這符合 Python 模組化最佳實踐。
    """
    app = QtWidgets.QApplication(sys.argv)
    window = MyBMIApp()
    window.show()
    sys.exit(app.exec_())