from enum import Enum
from typing import List, Tuple


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        return [(member.value, member.name) for member in cls]


class BloodGroup(ChoiceEnum):
    O_POS = "O +ve"
    O_NEG = "O -ve"
    A_POS = "A +ve"
    A_NEG = "A -ve"
    B_POS = "B +ve"
    B_NEG = "B -ve"
    AB_POS = "AB +ve"
    AB_NEG = "AB -ve"


class Gender(ChoiceEnum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"


class Lifestyle(ChoiceEnum):
    HEAVY_LABOR = "Heavy Labor"
    ACTIVE = "Active"
    SEDENTARY = "Sedentary"
    OTHER = "Other"


class DietaryPreference(ChoiceEnum):
    VEGAN = "Vegan"
    VEGETARIAN = "Vegetarian"
    LACTO_VEGETARIAN = "Lacto-Vegetarian"
    LACTO_OVA_VEGETARIAN = "Lacto-Ova-Vegetarian"
    NON_VEG_POULTRY = "Non-Vegetarian Poultry"
    NON_VEG_SEA_FOOD = "Non-Vegetarian Seafood"
    NON_VEG_RED_MEAT = "Non-Vegetarian Red Meat"
    NON_VEG_MIXED = "Non-Vegetarian Mixed"


class Title(ChoiceEnum):
    MR = "Mr."
    MS = "Ms."
    MRS = "Mrs."
    PROF = "Prof."
    DR = "Dr."


class HabitStatus(ChoiceEnum):
    NEVER = "Never"
    OCCASIONAL = "Occasional"
    REGULAR = "Regular"
    HEAVY = "Heavy"


class StaffRole(ChoiceEnum):
    DOCTOR = "Doctor"
    THERAPIST = "Therapist"
    CLEANER = "Cleaner"
    COOK = "Cook"
