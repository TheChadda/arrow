def on_forever():
    basic.pause(200)
    basic.show_icon(IconNames.HEART)
    basic.pause(200)
    basic.clear_screen()
basic.forever(on_forever)
