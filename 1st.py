import random
import time

# PID Controller Class
class PID:
    def __init__(self, kp: float, ki: float, kd: float, dt: float):
        self.kp = kp
        self.ki = ki
        self.kd = kd
        self.dt = dt
        self.prev_error = 0
        self.integral = 0

    def update(self, error: float):
        self.integral += error * self.dt
        derivative = (error - self.prev_error) / self.dt
        self.prev_error = error
        return (self.kp * error) + (self.ki * self.integral) + (self.kd * derivative)

# Motor control functions
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

def main(ir_values):
    weight = [-2, -1, 0, 1, 2]
    weighted_val = sum(ir_values[i] * weight[i] for i in range(5))

    # PID parameters
    kp = 1.0   # Proportional gain
    ki = 0.1   # Integral gain
    kd = 0.5   # Derivative gain
    dt = 0.1   # Time interval for PID update

    # Create a PID controller instance
    pid = PID(kp, ki, kd, dt)

    # Error calculation
    error = weighted_val
    pid_output = pid.update(error)

    # Calculate motor speeds based on PID output
    base_speed = 50  # Base speed for both motors
    left_speed = base_speed - pid_output
    right_speed = base_speed + pid_output

    # Clamp speeds to [-100, 100]
    left_speed = max(-100, min(100, left_speed))
    right_speed = max(-100, min(100, right_speed))

    set_right_speed(int(left_speed))
    set_left_speed(int(right_speed))

while True:
    f = get_ir_values()
    print(f)
    main(f)
    time.sleep(0.1)
