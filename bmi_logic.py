# bmi_logic.py
"""
BMI 計算邏輯模組

此模組提供 BMI（身體質量指數）的核心計算功能。
"""

def calculate_bmi_value(height_cm, weight_kg):
    """
    計算 BMI 值
    
    根據身高和體重計算身體質量指數（Body Mass Index, BMI）。
    公式：BMI = 體重(kg) / [身高(m)]²
    
    Args:
        height_cm (str or float): 身高，單位為公分 (cm)
        weight_kg (str or float): 體重，單位為公斤 (kg)
    
    Returns:
        float: 計算後的 BMI 值，四捨五入至小數點後兩位
        None: 當輸入無效或計算失敗時返回 None
    
    Examples:
        >>> calculate_bmi_value("170", "65")
        22.49
        >>> calculate_bmi_value(175, 70)
        22.86
        >>> calculate_bmi_value("abc", "65")
        None
    
    Note:
        - 身高會自動從公分轉換為公尺
        - 當輸入格式錯誤（非數字）或除以零時，函式會捕捉異常並返回 None
    """
    try:
        height_m = float(height_cm) / 100
        weight = float(weight_kg)
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    except (ValueError, ZeroDivisionError):
        return None