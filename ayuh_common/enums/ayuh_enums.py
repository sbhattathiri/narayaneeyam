from enum import Enum


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
