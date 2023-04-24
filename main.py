led2 = 0

def on_gesture_tilt_left():
    global led2
    basic.clear_screen()
    led2 = randint(0, 41)
    if led2 == 0:
        basic.show_icon(IconNames.HEART)
    elif led2 == 1:
        basic.show_icon(IconNames.SMALL_HEART)
    elif led2 == 2:
        basic.show_icon(IconNames.YES)
    elif led2 == 3:
        basic.show_icon(IconNames.NO)
    elif led2 == 4:
        basic.show_icon(IconNames.HAPPY)
    elif led2 == 5:
        basic.show_icon(IconNames.SAD)
    elif led2 == 6:
        basic.show_icon(IconNames.SAD)
    elif led2 == 7:
        basic.show_icon(IconNames.CONFUSED)
    elif led2 == 8:
        basic.show_icon(IconNames.ANGRY)
    elif led2 == 9:
        basic.show_icon(IconNames.ASLEEP)
    elif led2 == 10:
        basic.show_icon(IconNames.SURPRISED)
    elif led2 == 11:
        basic.show_icon(IconNames.SILLY)
    elif led2 == 12:
        basic.show_icon(IconNames.FABULOUS)
    elif led2 == 13:
        basic.show_icon(IconNames.MEH)
    elif led2 == 14:
        basic.show_icon(IconNames.TSHIRT)
    elif led2 == 15:
        basic.show_icon(IconNames.ROLLERSKATE)
    elif led2 == 16:
        basic.show_icon(IconNames.DUCK)
    elif led2 == 17:
        basic.show_icon(IconNames.HOUSE)
    elif led2 == 18:
        basic.show_icon(IconNames.TORTOISE)
    elif led2 == 19:
        basic.show_icon(IconNames.BUTTERFLY)
    elif led2 == 20:
        basic.show_icon(IconNames.STICK_FIGURE)
    elif led2 == 21:
        basic.show_icon(IconNames.GHOST)
    elif led2 == 22:
        basic.show_icon(IconNames.SWORD)
    elif led2 == 23:
        basic.show_icon(IconNames.GIRAFFE)
    elif led2 == 24:
        basic.show_icon(IconNames.SKULL)
    elif led2 == 25:
        basic.show_icon(IconNames.UMBRELLA)
    elif led2 == 26:
        basic.show_icon(IconNames.SNAKE)
    elif led2 == 27:
        basic.show_icon(IconNames.RABBIT)
    elif led2 == 28:
        basic.show_icon(IconNames.COW)
    elif led2 == 29:
        basic.show_icon(IconNames.QUARTER_NOTE)
    elif led2 == 30:
        basic.show_icon(IconNames.EIGTH_NOTE)
    elif led2 == 31:
        basic.show_icon(IconNames.PITCHFORK)
    elif led2 == 32:
        basic.show_icon(IconNames.TARGET)
    elif led2 == 33:
        basic.show_icon(IconNames.TRIANGLE)
    elif led2 == 34:
        basic.show_icon(IconNames.LEFT_TRIANGLE)
    elif led2 == 35:
        basic.show_icon(IconNames.CHESSBOARD)
    elif led2 == 36:
        basic.show_icon(IconNames.DIAMOND)
    elif led2 == 37:
        basic.show_icon(IconNames.SMALL_DIAMOND)
    elif led2 == 38:
        basic.show_icon(IconNames.SQUARE)
    elif led2 == 39:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif led2 == 40:
        basic.clear_screen()
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.TILT_LEFT, on_gesture_tilt_left)

def on_gesture_shake():
    global led2
    basic.clear_screen()
    led2 = randint(0, 40)
    if led2 == 0:
        basic.show_icon(IconNames.HEART)
    elif led2 == 1:
        basic.show_icon(IconNames.SMALL_HEART)
    elif led2 == 2:
        basic.show_icon(IconNames.YES)
    elif led2 == 3:
        basic.show_icon(IconNames.NO)
    elif led2 == 4:
        basic.show_icon(IconNames.HAPPY)
    elif led2 == 5:
        basic.show_icon(IconNames.SAD)
    elif led2 == 6:
        basic.show_icon(IconNames.SAD)
    elif led2 == 7:
        basic.show_icon(IconNames.CONFUSED)
    elif led2 == 8:
        basic.show_icon(IconNames.ANGRY)
    elif led2 == 9:
        basic.show_icon(IconNames.ASLEEP)
    elif led2 == 10:
        basic.show_icon(IconNames.SURPRISED)
    elif led2 == 11:
        basic.show_icon(IconNames.SILLY)
    elif led2 == 12:
        basic.show_icon(IconNames.FABULOUS)
    elif led2 == 13:
        basic.show_icon(IconNames.MEH)
    elif led2 == 14:
        basic.show_icon(IconNames.TSHIRT)
    elif led2 == 15:
        basic.show_icon(IconNames.ROLLERSKATE)
    elif led2 == 16:
        basic.show_icon(IconNames.DUCK)
    elif led2 == 17:
        basic.show_icon(IconNames.HOUSE)
    elif led2 == 18:
        basic.show_icon(IconNames.TORTOISE)
    elif led2 == 19:
        basic.show_icon(IconNames.BUTTERFLY)
    elif led2 == 20:
        basic.show_icon(IconNames.STICK_FIGURE)
    elif led2 == 21:
        basic.show_icon(IconNames.GHOST)
    elif led2 == 22:
        basic.show_icon(IconNames.SWORD)
    elif led2 == 23:
        basic.show_icon(IconNames.GIRAFFE)
    elif led2 == 24:
        basic.show_icon(IconNames.SKULL)
    elif led2 == 25:
        basic.show_icon(IconNames.UMBRELLA)
    elif led2 == 26:
        basic.show_icon(IconNames.SNAKE)
    elif led2 == 27:
        basic.show_icon(IconNames.RABBIT)
    elif led2 == 28:
        basic.show_icon(IconNames.COW)
    elif led2 == 29:
        basic.show_icon(IconNames.QUARTER_NOTE)
    elif led2 == 30:
        basic.show_icon(IconNames.EIGTH_NOTE)
    elif led2 == 31:
        basic.show_icon(IconNames.PITCHFORK)
    elif led2 == 32:
        basic.show_icon(IconNames.TARGET)
    elif led2 == 33:
        basic.show_icon(IconNames.TRIANGLE)
    elif led2 == 34:
        basic.show_icon(IconNames.LEFT_TRIANGLE)
    elif led2 == 35:
        basic.show_icon(IconNames.CHESSBOARD)
    elif led2 == 36:
        basic.show_icon(IconNames.DIAMOND)
    elif led2 == 37:
        basic.show_icon(IconNames.SMALL_DIAMOND)
    elif led2 == 38:
        basic.show_icon(IconNames.SQUARE)
    elif led2 == 39:
        basic.show_icon(IconNames.SMALL_SQUARE)
    elif led2 == 40:
        basic.clear_screen()
    else:
        basic.show_icon(IconNames.SCISSORS)
input.on_gesture(Gesture.SHAKE, on_gesture_shake)

def on_button_pressed_ab():
    basic.clear_screen()
input.on_button_pressed(Button.AB, on_button_pressed_ab)
