from time import sleep
import random

def dump(value: str):
    print(value)

def set_right_speed(speed: int):
    if not (-100 <= speed <= 100):
        return False
    print("Right motor running @ speed", speed)
    return True

def set_left_speed(speed: int):
    if not (-100 <= speed <= 100):
        return False
    print("Left motor running @ speed", speed)
    return True

def get_ir_values():
    return [int(random.choice([True, False])) for _ in range(5)]

def stop_right():
    print("Right motor stopped")

def stop_left():
    print("Left motor stopped")

def line_follower():
    base_speed = 60
    pid_kp = 1.0   # Proportional gain
    pid_ki = 0.0   # Integral gain
    pid_kd = 0.1   # Derivative gain

    integral = 0
    last_error = 0

    while True:
        ir_values = get_ir_values()
        dump(f"IR Values: {ir_values}")
        
        # Calculate error
        position = (ir_values.index(True) - 2) if True in ir_values else 0
        error = position  # Error will be -2 to +2 depending on the position
        
        # PID calculations
        integral += error
        derivative = error - last_error
        
        # Calculate PID output
        output = (pid_kp * error) + (pid_ki * integral) + (pid_kd * derivative)
        
        # Adjust motor speeds based on PID output
        left_speed = base_speed - output
        right_speed = base_speed + output
        
        # Clamp speed values to be within the limits
        left_speed = max(min(left_speed, 100), -100)
        right_speed = max(min(right_speed, 100), -100)
        
        set_left_speed(left_speed)
        set_right_speed(right_speed)
        
        # Update last error
        last_error = error
        
        # Small delay to simulate the loop timing
        sleep(0.1)

# Start line following
line_follower()
