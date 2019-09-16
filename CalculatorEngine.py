class CalculatorEngine:

    def __init__(self, age_years, weight_kg, height_cm, bmi_category, is_male, exercise_level, height_m, bmr, bmi, rdi):
        self.age_years = age_years
        self.weight_kg = weight_kg
        self.height_cm = height_cm
        self.bmi_category = bmi_category
        self.is_male = is_male
        self.exercise_level = exercise_level
        self.height_m = height_m
        self.bmr = bmr
        self.bmi = bmi
        self.rdi = rdi

    def get_age_years(self):
        return self.age_years

    def set_age_years(self, age_years):
        self.age_years = age_years

    def get_weight(self):
        return self.weight

    def set_weight(self, weight_kg):
        self.weight_kg = weight_kg

    def get_height_cm(self):
        return self.height_cm

    def set_height_cm(self, height_cm):
        self.height_cm = height_cm

    def get_bmi_category(self):
        return self.bmi_category

    def set_bmi_category(self, bmi_category):
        self.bmi_category = bmi_category

    def get_is_male(self):
        return self.is_male

    def set_is_male(self, is_male):
        self.is_male = is_male

    def get_exercise_level(self):
        return self.exercise_level

    def set_exercise_level(self, exercise_level):
        self.exercise_level = exercise_level

    def get_height_m(self):
        return self.height_m

    def set_height_m(self, height_m):
        self.height_m = height_m

    def get_bmr(self):
        return self.bmr

    def set_bmr(self, bmr):
        self.bmr = bmr

    def get_bmi(self):
        return self.bmi

    def set_bmi(self, bmi):
        self.bmi = bmi

    def get_rdi(self):
        return self.rdi

    def set_rdi(self, rdi):
        self.rdi = rdi
