# bmi_engine.py


class HealthAdvice:
    def get_info(self, bmi):
        pass


class Underweight(HealthAdvice):
    def get_info(self, bmi):
        advice = f"BMI {bmi}: 您的體重過輕\n"
        advice += "飲食建議：增加高蛋白食物（肉類、蛋、豆類）、堅果、乳製品\n"
        advice += "每周運動時長：3-5 小時溫和運動（快走、瑜伽）\n"
        advice += "🏥 建議：是，請看醫生診斷是否有代謝或營養不良問題"
        return advice

class Normal(HealthAdvice):
    def get_info(self, bmi):
        advice = f"BMI {bmi}: 您的體重正常\n"
        advice += "飲食建議：繼續保持均衡飲食，五穀雜糧、蔬果、蛋白質適量\n"
        advice += "每周運動時長：3.5-5 小時中等強度運動（快走、騎單車、游泳）\n"
        advice += "🏥 建議：否，定期體檢即可"
        return advice

class Overweight(HealthAdvice):
    def get_info(self, bmi):
        advice = f"BMI {bmi}: 您的體重過重\n"
        advice += "飲食建議：減少精緻糖、油炸食品；增加蔬菜水果和高纖食物\n"
        advice += "每周運動時長：5-7 小時有氧運動（跑步、快走、健身操）\n"
        advice += "🏥 建議：是，建議就醫評估心血管健康狀況"
        return advice

# 簡單工廠
class AdviceFactory:
    @staticmethod
    def create_advice(bmi):
        if bmi < 18.5:
            return Underweight()
        elif 18.5 <= bmi < 24:
            return Normal()
        else:
            return Overweight()