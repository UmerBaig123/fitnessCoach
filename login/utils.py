#pass all weights in kg and height in centimeters

class Conversions:
    def kg_to_lbs(kg):
        return round(kg * 2.20462, 2)
    def lbs_to_kg(lbs):
        return round(lbs / 2.20462, 2)
    def cm_to_m(cm):
        return round(cm / 100, 2)
    def m_to_cm(m):
        return round(m * 100, 2)
    def feet_inches_to_cm(feet, inches):
        return round(feet * 30.48 + inches * 2.54, 2)
    def cm_to_feet_inches(cm):
        feet = cm // 30.48
        inches = (cm % 30.48) // 2.54
        return [feet, inches]
class BodyStats:
    def BMI(weight, height):
        return round(weight / (Conversions.cm_to_m(height) ** 2), 2)
    def BMR(weight, height,age,gender):
        if gender == 'W':
            return float(655 + (9.6* weight) + (1.8 * height) - (4.7 * age))
        if gender == 'M':
            return float(66 + (13.7* weight) + (5 * height) - (6.8 * age))
    def caloriesIntake(BMR,activity):
        activityMultiplier = [1.2,1.375,1.55,1.725,1.9]
        return round(BMR * activityMultiplier[int(activity)],0)
    def ProteinIntake(calories):
        return round((calories*0.20)/4,0)
    def CarbsIntake(calories):
        return round((calories*0.55)/4,0)
    def FatIntake(calories):
        return round((calories*0.25)/9,0)

    