# bmi_logic.py
def calculate_bmi_value(height_cm, weight_kg):
    """計算 BMI 的核心邏輯"""
    try:
        height_m = float(height_cm) / 100
        weight = float(weight_kg)
        bmi = weight / (height_m ** 2)
        return round(bmi, 2)
    except (ValueError, ZeroDivisionError):
        return None