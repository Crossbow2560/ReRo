import header
import time

def main(ir_values):
    weight = [-2, -1, 0, 1, 2]
    weighted_val = 0
    for i in range(5):
        weighted_val += ir_values[i] * weight[i]
    left_speed = 45
    right_speed = 45

    if weighted_val < 0:
        right_speed += abs(weighted_val) * 15 # change these values
    elif weighted_val > 0:
        left_speed += abs(weighted_val) * 15 # change these values
    else:
        left_speed = 90
        right_speed = 90

    header.set_right_speed(right_speed)
    header.set_left_speed(left_speed)
while True:
    f = header.get_ir_values()
    print(f)
    print(main(f))
    time.sleep(0.1)