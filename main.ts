let led2 = 0
input.onGesture(Gesture.Shake, function () {
    basic.clearScreen()
    led2 = randint(0, 40)
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
    } else if (led2 == 5) {
        basic.showIcon(IconNames.Sad)
    } else if (led2 == 6) {
        basic.showIcon(IconNames.Sad)
    } else if (led2 == 7) {
        basic.showIcon(IconNames.Confused)
    } else if (led2 == 8) {
        basic.showIcon(IconNames.Angry)
    } else if (led2 == 9) {
        basic.showIcon(IconNames.Asleep)
    } else if (led2 == 10) {
        basic.showIcon(IconNames.Surprised)
    } else if (led2 == 11) {
        basic.showIcon(IconNames.Silly)
    } else if (led2 == 12) {
        basic.showIcon(IconNames.Fabulous)
    } else if (led2 == 13) {
        basic.showIcon(IconNames.Meh)
    } else if (led2 == 14) {
        basic.showIcon(IconNames.TShirt)
    } else if (led2 == 15) {
        basic.showIcon(IconNames.Rollerskate)
    } else if (led2 == 16) {
        basic.showIcon(IconNames.Duck)
    } else if (led2 == 17) {
        basic.showIcon(IconNames.House)
    } else if (led2 == 18) {
        basic.showIcon(IconNames.Tortoise)
    } else if (led2 == 19) {
        basic.showIcon(IconNames.Butterfly)
    } else if (led2 == 20) {
        basic.showIcon(IconNames.StickFigure)
    } else if (led2 == 21) {
        basic.showIcon(IconNames.Ghost)
    } else if (led2 == 22) {
        basic.showIcon(IconNames.Sword)
    } else if (led2 == 23) {
        basic.showIcon(IconNames.Giraffe)
    } else if (led2 == 24) {
        basic.showIcon(IconNames.Skull)
    } else if (led2 == 25) {
        basic.showIcon(IconNames.Umbrella)
    } else if (led2 == 26) {
        basic.showIcon(IconNames.Snake)
    } else if (led2 == 27) {
        basic.showIcon(IconNames.Rabbit)
    } else if (led2 == 28) {
        basic.showIcon(IconNames.Cow)
    } else if (led2 == 29) {
        basic.showIcon(IconNames.QuarterNote)
    } else if (led2 == 30) {
        basic.showIcon(IconNames.EigthNote)
    } else if (led2 == 31) {
        basic.showIcon(IconNames.Pitchfork)
    } else if (led2 == 32) {
        basic.showIcon(IconNames.Target)
    } else if (led2 == 33) {
        basic.showIcon(IconNames.Triangle)
    } else if (led2 == 34) {
        basic.showIcon(IconNames.LeftTriangle)
    } else if (led2 == 35) {
        basic.showIcon(IconNames.Chessboard)
    } else if (led2 == 36) {
        basic.showIcon(IconNames.Diamond)
    } else if (led2 == 37) {
        basic.showIcon(IconNames.SmallDiamond)
    } else if (led2 == 38) {
        basic.showIcon(IconNames.Square)
    } else if (led2 == 39) {
        basic.showIcon(IconNames.SmallSquare)
    } else if (led2 == 40) {
        basic.clearScreen()
    } else {
        basic.showIcon(IconNames.Scissors)
    }
})
input.onButtonPressed(Button.AB, function () {
    basic.clearScreen()
})
