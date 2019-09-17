import math


class CalculatorEngine:

    def __init__(self, age_years=None, weight_kg=None, height_cm=None, bmi_category=None, is_male=None, exercise_level=None, height_m=None, bmr=None, bmi=None, rdi=None):
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

    def set_bmi(self):
        self.bmi = self.calc_bmi()

    def get_rdi(self):
        return self.rdi

    def set_rdi(self, rdi):
        self.rdi = rdi

    def bmr_rhb(self):
        MEN_BMR_FACTOR = 88.362
        MEN_WEIGHT_FACTOR = 13.397
        MEN_HEIGHT_FACTOR = 4.799
        MEN_AGE_FACTOR = 5.677

        WOMEN_BMR_FACTOR = 447.593
        WOMEN_WEIGHT_FACTOR = 9.247
        WOMEN_HEIGHT_FACTOR = 3.098
        WOMEN_AGE_FACTOR = 4.330

        if self.is_male:
            result = MEN_BMR_FACTOR + (MEN_WEIGHT_FACTOR * self.weight_kg) + (MEN_HEIGHT_FACTOR * self.height_cm) - \
                     (MEN_AGE_FACTOR * self.age_years)
        else:
            result = WOMEN_BMR_FACTOR + (WOMEN_WEIGHT_FACTOR * self.weight_kg) + (WOMEN_HEIGHT_FACTOR * self.height_cm)\
                     - (WOMEN_AGE_FACTOR * self.age_years)
        return result

    # TODO merge this method into "bmr_rhb" for a single method that can calculate BMR with various calculations
    def bmr_hb(self):
        MEN_BMR_FACTOR = 66.47
        MEN_WEIGHT_FACTOR = 13.75
        MEN_HEIGHT_FACTOR = 5.003
        MEN_AGE_FACTOR = 6.755

        WOMEN_BMR_FACTOR = 655.1
        WOMEN_WEIGHT_FACTOR = 9.563
        WOMEN_HEIGHT_FACTOR = 1.850
        WOMEN_AGE_FACTOR = 4.676

        if self.is_male:
            result = MEN_BMR_FACTOR + (MEN_WEIGHT_FACTOR * self.weight_kg) + (MEN_HEIGHT_FACTOR * self.height_cm) - \
                     (MEN_AGE_FACTOR * self.age_years)
        else:
            result = WOMEN_BMR_FACTOR + (WOMEN_WEIGHT_FACTOR * self.weight_kg) + (WOMEN_HEIGHT_FACTOR * self.height_cm) \
                     - (WOMEN_AGE_FACTOR * self.age_years)
        return result

    def calc_bmi(self):
        result = self.weight_kg / math.pow(self.height_m, 2)

        return result
