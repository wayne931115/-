# BMI 計算器應用程式

## 專案概述

這是一個基於 PyQt5 開發的圖形化使用者介面 (GUI) BMI 計算應用程式。使用者可以輸入身高和體重，程式會計算 BMI 值並提供個性化的健康建議。此外，程式還具有體重追蹤圖表功能，能夠記錄每次計算的體重數據並以折線圖視覺化呈現。

## 主要功能

✅ **BMI 計算** - 根據身高(cm)和體重(kg)計算 BMI 值  
✅ **健康建議** - 根據 BMI 值提供個性化的飲食和運動建議  
✅ **體重追蹤** - 記錄每次計算的體重數據  
✅ **圖表視覺化** - 顯示體重變化的折線圖  
✅ **輸入驗證** - 防止無效輸入（非數字、負數等）  

## 專案結構

```
程式設計三期末報告/
├── main.py              # 主程式進入點，GUI 應用程式啟動
├── bmi_logic.py         # BMI 計算的核心邏輯
├── bmi_engine.py        # 工廠模式：根據 BMI 值決定對應的健康建議
├── chart_tool.py        # matplotlib 圖表顯示工具
├── bmi_ui.ui            # PyQt5 UI 設計檔案
└── README.md            # 本文件
```

## 技術棧

- **Python 3.x**
- **PyQt5** - GUI 框架
- **matplotlib** - 數據視覺化
- **Qt Designer** - UI 設計工具

## 安裝步驟

### 1. 安裝必要的套件

```bash
pip install PyQt5 matplotlib
```

### 2. 驗證安裝

```bash
python -c "import PyQt5, matplotlib; print('安裝成功')"
```

## 執行程式

### 方式一：直接執行

```bash
python main.py
```

### 方式二：使用 Python IDE

在 IDE (如 VS Code、PyCharm) 中打開 `main.py`，點擊執行按鈕。

## 程式碼架構說明

### 1. **main.py** - 主程式
- 定義 `MyBMIApp` 類別，繼承自 `QtWidgets.QMainWindow`
- 載入 `bmi_ui.ui` 的 GUI 設計
- 連接按鈕事件至計算邏輯
- 管理體重紀錄和圖表更新

```python
if __name__ == "__main__":  # 程式進入點
    app = QtWidgets.QApplication(sys.argv)
    window = MyBMIApp()
    window.show()
    sys.exit(app.exec_())
```

### 2. **bmi_logic.py** - 計算邏輯
- `calculate_bmi_value(height_cm, weight_kg)` 函式
- 計算公式：BMI = 體重(kg) / 身高(m)²
- 包含錯誤處理（ValueError、ZeroDivisionError）

### 3. **bmi_engine.py** - 工廠模式
實現了四種健康狀態的建議類別：
- `Underweight` - 體重過輕
- `Normal` - 體重正常
- `Overweight` - 體重過重
- `Obese` - 肥胖

`AdviceFactory` 根據 BMI 值動態創建對應的物件。

### 4. **chart_tool.py** - 圖表工具
- `BMIChart` 類別繼承自 `FigureCanvas`
- 使用 matplotlib 生成折線圖
- `update_chart(weight_history)` 方法更新圖表

## 使用流程

1. 啟動應用程式 → 執行 `python main.py`
2. 輸入身高 (cm) 和體重 (kg)
3. 點擊「計算」按鈕
4. 查看 BMI 結果和健康建議
5. 體重數據自動添加至圖表進行追蹤

## 測試方式

### 測試用例

#### 測試 1：正常輸入
```
身高：170 cm
體重：65 kg
預期結果：BMI ≈ 22.49，「體重正常」
```

#### 測試 2：輸入驗證（非數字）
```
身高：abc
體重：65 kg
預期結果：提示錯誤訊息
```

#### 測試 3：輸入驗證（負數）
```
身高：170 cm
體重：-50 kg
預期結果：提示「身高和體重都必須大於 0」
```

#### 測試 4：多筆記錄
```
第一筆：身高 170 cm，體重 70 kg (BMI 24.22 - 過重)
第二筆：身高 170 cm，體重 65 kg (BMI 22.49 - 正常)
第三筆：身高 170 cm，體重 60 kg (BMI 20.76 - 正常)
預期結果：圖表顯示三個點 (1,70), (2,65), (3,60)
```

#### 測試 5：BMI 邊界值
```
BMI < 18.5：體重過輕
18.5 ≤ BMI < 25：體重正常
25 ≤ BMI < 30：體重過重
BMI ≥ 30：肥胖
```

### 手動測試步驟

```bash
# 1. 安裝套件
pip install PyQt5 matplotlib

# 2. 執行程式
python main.py

# 3. 在 GUI 介面輸入不同的值測試

# 4. 驗證結果是否符合預期
```

## 設計模式

### 簡單工廠模式 (Simple Factory Pattern)

#### 📌 模式概述
工廠模式是一種創建型設計模式，用於隱藏物件的具體創建過程。在本專案中，根據 BMI 值自動選擇並創建對應的健康建議物件，避免客戶端直接依賴具體的類別。

#### ✅ 為什麼使用工廠模式？

| 優點 | 說明 |
|------|------|
| **解耦** | 客戶端不需要知道具體的健康建議類別 |
| **可擴展** | 新增健康狀態時，只需新增類別和修改工廠 |
| **集中管理** | 所有物件創建邏輯集中在 `AdviceFactory` |
| **易於維護** | 修改建議內容時只需改變對應類別 |

#### 🔧 實現結構

**基類（抽象）：**
```python
class HealthAdvice:
    def get_info(self, bmi):
        pass  # 虛擬方法
```

**具體實現類：**
```python
class Underweight(HealthAdvice):
    def get_info(self, bmi):
        return f"BMI {bmi}: 您的體重過輕\n飲食建議：..."

class Normal(HealthAdvice):
    def get_info(self, bmi):
        return f"BMI {bmi}: 您的體重正常\n飲食建議：..."

class Overweight(HealthAdvice):
    def get_info(self, bmi):
        return f"BMI {bmi}: 您的體重過重\n飲食建議：..."
```

**工廠類：**
```python
class AdviceFactory:
    @staticmethod
    def create_advice(bmi):
        if bmi < 18.5:
            return Underweight()
        elif 18.5 <= bmi < 24:
            return Normal()
        else:
            return Overweight()
```

#### 💡 功能情境（使用場景）

**情境 1：使用者輸入身高 170cm、體重 60kg**

```
流程分解：
1. main.py 呼叫 bmi_logic.calculate_bmi_value("170", "60")
   → 返回 BMI = 20.76

2. main.py 呼叫 AdviceFactory.create_advice(20.76)
   → 工廠判斷：18.5 <= 20.76 < 24
   → 返回 Normal() 物件實例

3. main.py 呼叫 advice_obj.get_info(20.76)
   → 返回「您的體重正常」的具體建議

結果：顯示該使用者對應的健康建議（飲食、運動等）
```

**情境 2：未來新增「肥胖 (Obese)」等級**

```python
# 新增肥胖類別
class Obese(HealthAdvice):
    def get_info(self, bmi):
        advice = f"BMI {bmi}: 您的體重肥胖\n"
        advice += "飲食建議：醫生監督下的低卡飲食\n"
        advice += "每周運動時長：7+ 小時高強度運動\n"
        advice += "🏥 建議：是，必須就醫"
        return advice

# 只需修改工廠的判斷邏輯
class AdviceFactory:
    @staticmethod
    def create_advice(bmi):
        if bmi < 18.5:
            return Underweight()
        elif 18.5 <= bmi < 24:
            return Normal()
        elif 24 <= bmi < 30:
            return Overweight()
        else:  # BMI >= 30
            return Obese()  # 新增分類
```

**優勢**：
- 客戶端 (main.py) 不需要修改
- 只有工廠和新增的類別需要改變
- 符合「開放-關閉原則」（對擴展開放，對修改關閉）

#### 🎯 設計流程圖

```
使用者輸入 (身高、體重)
    ↓
計算 BMI (bmi_logic.py)
    ↓
AdviceFactory.create_advice(bmi)
    ├─→ if bmi < 18.5 → Underweight()
    ├─→ elif 18.5 ≤ bmi < 24 → Normal()
    └─→ else → Overweight()
    ↓
呼叫 advice_obj.get_info(bmi)
    ↓
返回個性化健康建議
    ↓
在 GUI 顯示結果
```

#### 📝 程式碼示例（如何在 main.py 中使用）

```python
from bmi_engine import AdviceFactory
from bmi_logic import calculate_bmi_value

# 使用者輸入
bmi_result = calculate_bmi_value(height_cm="170", weight_kg="60")

# 工廠模式：根據 BMI 自動創建對應的建議物件
advice_obj = AdviceFactory.create_advice(bmi_result)

# 取得具體的健康建議
advice_message = advice_obj.get_info(bmi_result)

# 顯示結果
print(advice_message)
```

## 常見問題

**Q: 執行時出現 "ModuleNotFoundError: No module named 'PyQt5'"**
> A: 請執行 `pip install PyQt5` 安裝套件

**Q: bmi_ui.ui 檔案找不到**
> A: 確保 `bmi_ui.ui` 檔案與 `main.py` 在同一個目錄

**Q: 圖表無法顯示**
> A: 確認 matplotlib 已安裝，並且 matplotlib backend 設為 'Qt5Agg'

## 程式進入點說明

`if __name__ == "__main__":` 的用途：
- 只有當此檔案被**直接執行**時，才會啟動 GUI 應用程式
- 如果此檔案被其他程式 **import**，不會自動啟動應用程式
- 符合 Python 模組化最佳實踐

## 版本資訊

- 版本：1.0
- 最後更新：2026 年 1 月
- Python 版本：3.x+

## 許可證

本專案僅供報告用途。

---

**提示**：若要修改 UI 介面，請使用 Qt Designer 編輯 `bmi_ui.ui` 檔案。
