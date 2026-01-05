import matplotlib
matplotlib.use('Qt5Agg')  # 在 matplotlib 初始化前設定
import matplotlib.pyplot as plt
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure

class BMIChart(FigureCanvas):
    def __init__(self, parent=None):
        # 建立畫布，設定緊湊佈局避免文字被切到
        self.figure = Figure(figsize=(5, 4), dpi=100, tight_layout=True)
        self.ax = self.figure.add_subplot(111)
        super().__init__(self.figure)
        self.setParent(parent)

    def update_chart(self, weight_history):
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
