from enum import (
    Enum,
)

# TODO: standardize

BLOOD_GROUP_CHOICES = [
    ("A+", "A+"),
    ("A-", "A-"),
    ("B+", "B+"),
    ("B-", "B-"),
    ("AB+", "AB+"),
    ("AB-", "AB-"),
    ("O+", "O+"),
    ("O-", "O-"),
]

GENDER_CHOICES = [
    ("MALE", "Male"),
    ("FEMALE", "Female"),
    ("OTHER", "Other"),
]

MEDICINE_TYPE_CHOICES = [
    ("ARISHTAM", "Arishtam"),
    ("CHOORNAM", "Choornam"),
    ("GHRTAM", "Ghrtam"),
    ("GULIKA", "Gulika"),
    ("KASHAAYAM", "Kashaayam"),
    ("LEPAM", "Lepam"),
    ("LEHYAM", "Lehyam"),
    ("THAILAM", "Thailam"),
]


REFERRAL_SOURCE_CHOICES = [
    ("SEARCH", "search"),
    ("ACQUAINTANCE", "Acquaintance"),
    ("NEWSPAPER", "Newspaper"),
    ("TELEVISION", "TV"),
    ("RADIO", "Radio"),
    ("INSTAGRAM", "Instagram"),
    ("FACEBOOK", "Facebook"),
    ("X", "X"),
]


class ChoiceEnum(Enum):

    @classmethod
    def choices(cls):
        return [(member.value, member.name) for member in cls]


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
