from enum import Enum

class ControlState(Enum):
    UNCALIBRATED = 0x00
    IDLE = 0x01
    BEGIN_INHALATION = 0x02
    INHALATION = 0x03
    BEGIN_HOLD_IN = 0x04
    HOLD_IN = 0x05
    BEGIN_EXHALATION = 0x06
    EXHALATION = 0x07
    HOME = 0x08
    HALT = 0x09
    SENSOR_CALIBRATION = 0x0a
    SENSOR_CALIBRATION_DONE = 0x0b
    
