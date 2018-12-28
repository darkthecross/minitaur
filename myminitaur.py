import math
import numpy as np
import os
import motor


INIT_POSITION = [0, 0, 0.2]
INIT_ORIENTATION = [0, 0, 0, 1]
KNEE_CONSTRINT_POINT_RIGHT = [0, 0.005, 0.2]
KNEE_CONSTRINT_POINT_LEFT = [0, 0.01, 0.2]
OVERHEAT_SHUTDOWN_TORQUE = 2.45
OVERHEAT_SHUTDOWN_TIME = 1.0

LEG_POSITION = ["front_left", "back_left", "front_right", "back_right"]
MOTOR_NAMES = [
    "motor_front_leftL_joint", "motor_front_leftR_joint",
    "motor_back_leftL_joint", "motor_back_leftR_joint",
    "motor_front_rightL_joint", "motor_front_rightR_joint",
    "motor_back_rightL_joint", "motor_back_rightR_joint"
]
LEG_LINK_ID = [2, 3, 5, 6, 8, 9, 11, 12, 15, 16, 18, 19, 21, 22, 24, 25]
MOTOR_LINK_ID = [1, 4, 7, 10, 14, 17, 20, 23]
FOOT_LINK_ID = [3, 6, 9, 12, 16, 19, 22, 25]
BASE_LINK_ID = -1

