"""
圖表工具模組

此模組提供 BMI 計算器的體重追蹤圖表功能，
使用 matplotlib 在 PyQt5 中嵌入折線圖。
"""
import matplotlib
matplotlib.use('Qt5Agg')  # 在 matplotlib 初始化前設定
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class BMIChart(FigureCanvas):
    """
    BMI 體重追蹤圖表類別
    
    繼承自 FigureCanvas，用於在 PyQt5 GUI 中顯示 matplotlib 圖表。
    提供體重變化的折線圖視覺化功能。
    
    Attributes:
        figure (Figure): matplotlib 圖表物件
        ax (Axes): matplotlib 座標軸物件
    """
    def __init__(self, parent=None):
        """
        初始化圖表
        
        Args:
            parent (QWidget, optional): 父容器 widget。預設為 None。
        """
        # 建立畫布，設定緊湊佈局避免文字被切到
        self.figure = Figure(figsize=(5, 4), dpi=100, tight_layout=True)
        self.ax = self.figure.add_subplot(111)
        super().__init__(self.figure)
        self.setParent(parent)

    def update_chart(self, weight_history):
        """
        更新體重追蹤圖表
        
        根據體重歷史數據繪製折線圖。X 軸為記錄次數（1, 2, 3...），
        Y 軸為體重值（公斤）。
        
        Args:
            weight_history (list): 體重記錄列表，每個元素為浮點數（體重值）
        
        Returns:
            None
        
        Note:
            - 如果 weight_history 為空列表，圖表會被清空但不繪製任何內容
            - 每次呼叫此方法時，圖表會完全重繪
        """
        self.ax.clear()
        if not weight_history:
            return
            
        # 繪製體重變化折線圖 - 次數用整數顯示
        records = list(range(1, len(weight_history) + 1))  # 1, 2, 3, ...
        self.ax.plot(records, weight_history, marker='o', color='b', linestyle='-')
        self.ax.set_title("Weight Tracking Trend")
        self.ax.set_xlabel("Records")
        self.ax.set_ylabel("Weight (kg)")
        self.ax.set_xticks(records)  # 確保 X 軸只顯示整數
        self.figure.tight_layout()
        self.draw()
