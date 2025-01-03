from enum import (
    Enum,
)


class BloodGroup(Enum):
    O_POS = "O +ve"
    O_NEG = "O -ve"
    A_POS = "A +ve"
    A_NEG = "A -ve"
    B_POS = "B +ve"
    B_NEG = "B -ve"
    AB_POS = "AB +ve"
    AB_NEG = "AB -ve"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Gender(Enum):
    MALE = "Male"
    FEMALE = "Female"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Lifestyle(Enum):
    HEAVY_LABOR = "Heavy Labor"
    ACTIVE = "Active"
    SEDENTARY = "Sedentary"
    OTHER = "Other"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class Title(Enum):
    Mr = "Mr"
    Ms = "Ms"
    Mrs = "Mrs"
    Prof = "Prof."
    Dr = "Dr."

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]


class HabitStatus(Enum):
    NEVER = "Never"
    OCCASIONAL = "Occasional"
    REGULAR = "Regular"
    HEAVY = "Heavy"

    @classmethod
    def choices(cls):
        return [(key.value, key.name) for key in cls]
