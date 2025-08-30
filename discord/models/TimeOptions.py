from enum import Enum

class TimeOptions(Enum):
    SIX_AM = "6:00 am", 6
    SEVEN_AM = "7:00 am", 7
    EIGHT_AM = "8:00 am", 8
    NINE_AM = "9:00 am", 9
    TEN_AM = "10:00 am", 10
    ELEVEN_AM = "11:00 am", 11
    TWELVE_PM = "12:00 pm", 12
    ONE_PM = "1:00 pm", 13
    TWO_PM = "2:00 pm", 14
    THREE_PM = "3:00 pm", 15
    FOUR_PM = "4:00 pm", 16
    FIVE_PM = "5:00 pm", 17
    SIX_PM = "6:00 pm", 18
    SEVEN_PM = "7:00 pm", 19
    EIGHT_PM = "8:00 pm", 20
    NINE_PM = "9:00 pm", 21
    TEN_PM = "10:00 pm", 22
    ELEVEN_PM = "11:00 pm", 23
    TWELVE_AM = "12:00 am", 0 

    def __new__(cls, string_representation, value):
        obj = object.__new__(cls)
        obj._value_ = value
        obj.string_representation = string_representation
        return obj