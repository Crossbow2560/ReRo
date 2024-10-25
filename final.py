from time import sleep

import header

def line_follower():
    base_speed = 60
    correction = 30
    
    while True:
        ir_values = get_ir_values()
        dump(f"IR Values: {ir_values}")
        
        if ir_values == [True, True, False, True, True]:
            set_left_speed(base_speed)
            set_right_speed(base_speed)
        
        elif ir_values == [True, False, False, True, True]:
            set_left_speed(base_speed - correction)
            set_right_speed(base_speed + correction)
        
        elif ir_values == [True, True, False, False, True]:
            set_left_speed(base_speed + correction)
            set_right_speed(base_speed - correction)

        elif ir_values == [False, True, True, True, True]:
            set_left_speed(base_speed - correction * 2)
            set_right_speed(base_speed + correction * 2)

        elif ir_values == [True, True, True, False, False]:
            set_left_speed(base_speed + correction * 2)
            set_right_speed(base_speed - correction * 2)
        
        elif ir_values == [True, True, True, True, True]:
            dump("Transition detected")
            set_left_speed(base_speed // 2)
            set_right_speed(base_speed // 2)

            while ir_values != [True, True, False, True, True]:
                ir_values = get_ir_values()
                dump(f"IR Values (Transition): {ir_values}")

        else:
            dump("Lost line, adjusting...")
            set_left_speed(-correction)
            set_right_speed(correction)
        
line_follower()
