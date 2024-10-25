from time import sleep

import random

def dump(value:str):
    """
    Print the value to the dashboard console, should be used in place of python default print. 
    Can be used for debugging purposes, does not have the default attributes of the python print function

    @param:
        value: str - Value to be printed to the console

    """
    print(value)


def set_right_speed(speed: int):
    """
    Function to set the speed of the motors
    
    @param:
        speed: int - Speed of the right motor 

    @return:
        bool - Speed set success or failure

    speed  should be a number between -100 and 100,
    speed < 0 : moving backwards
    speed = 0 : stop
    speed > 0 : moving forward

    """

    if not (-100 <= speed <= 100):
        return False
    
    print("Right motor running @ speed", speed)
    return True
    

def set_left_speed(speed: int):
    """
    Function to set the speed of the left motor
    
    @param:
        speed: int - Speed of the left motor 

    @return:
        bool - Speed set success or failure

    speed should be a number between -100 and 100,
    speed < 0 : moving backwards
    speed = 0 : stop
    speed > 0 : moving forward

    """

    if not (-100 <= speed <= 100):
        return False
    
    print("Right motor running @ speed", speed)
    return True
    


def get_ir_values():
    """
    Function to get the color values of the sensor array, left to right
    
    @return:
        color: [bool, bool, bool, bool, bool] - Ground color white or black

        white will be represented by a value of True, 
        and black will be represented by the value False

    """

    global color_sensors
    return [int(random.choice([True, False])) for _ in range(5)]


def stop_right():
    """
    Function to stop the right motor
    """

    print("Right motor stopped")


def stop_left():
    """
    Function to stop the left motor
    """

    print("Left motor stopped")

def line_follower():
    base_speed = 60
    correction = 30
    
    while True:
        # Fetch IR sensor readings
        ir_values = get_ir_values()
        dump(f"IR Values: {ir_values}")
        
        # Identify track segments based on IR values
        # True = White, False = Black (ground color)
        
        # Basic line-following
        if ir_values == [True, True, False, True, True]:
            # Centered on line (normal condition on black track with yellow line in the middle)
            set_left_speed(base_speed)
            set_right_speed(base_speed)
        
        elif ir_values == [True, False, False, True, True]:
            # Slight left turn
            set_left_speed(base_speed - correction)
            set_right_speed(base_speed + correction)
        
        elif ir_values == [True, True, False, False, True]:
            # Slight right turn
            set_left_speed(base_speed + correction)
            set_right_speed(base_speed - correction)

        elif ir_values == [False, True, True, True, True]:
            # Sharper left adjustment
            set_left_speed(base_speed - correction * 2)
            set_right_speed(base_speed + correction * 2)

        elif ir_values == [True, True, True, False, False]:
            # Sharper right adjustment
            set_left_speed(base_speed + correction * 2)
            set_right_speed(base_speed - correction * 2)
        
        # Detect transition areas with white square markers
        elif ir_values == [True, True, True, True, True]:
            dump("Transition detected")
            # Slow down and adjust based on possible line positions in the transition
            set_left_speed(base_speed // 2)
            set_right_speed(base_speed // 2)

            # Wait for the robot to cross the patch, based on sensor feedback
            while ir_values != [True, True, False, True, True]:
                ir_values = get_ir_values()
                dump(f"IR Values (Transition): {ir_values}")

        else:
            # Handle lost line condition
            dump("Lost line, adjusting...")
            set_left_speed(-correction)
            set_right_speed(correction)
        
# Start line following
line_follower()
