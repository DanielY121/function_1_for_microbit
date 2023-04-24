let led2 = 0
input.onGesture(Gesture.Shake, function () {
    led2 = randint(0, 10)
    if (led2 == 0) {
        basic.showIcon(IconNames.Heart)
    } else if (led2 == 1) {
        basic.showIcon(IconNames.SmallHeart)
    } else if (led2 == 2) {
        basic.showIcon(IconNames.Yes)
    } else if (led2 == 3) {
        basic.showIcon(IconNames.No)
    } else if (led2 == 4) {
        basic.showIcon(IconNames.Happy)
    } else if (false) {
    	
    } else {
    	
    }
})
