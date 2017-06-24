from microbit import display, Image, pin0, pin1, pin2

zero = Image('09990:'
             '09090:'
             '09090:'
             '09090:'
             '09990')
one = Image('00090:'
            '00990:'
            '09090:'
            '00090:'
            '00090')
two = Image('00990:'
            '09090:'
            '00090:'
            '00900:'
            '09990:')

while True:
    if pin0.is_touched():
        display.show(zero)
    elif pin1.is_touched():
        display.show(one)
    elif pin2.is_touched():
        display.show(two)
    else:
        display.clear()
