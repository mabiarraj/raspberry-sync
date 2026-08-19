import RPi.GPIO as GPIO

BUTTONS = {
    5: "A",
    6: "B",
    16: "C",
    24: "D",
}


def setup_buttons(callback):
    GPIO.setmode(GPIO.BCM)

    def handle_press(channel, label):
        print(f"Button {label} pressed (GPIO {channel})")
        callback(label)

    for pin, label in BUTTONS.items():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(
            pin,
            GPIO.FALLING,
            callback=lambda channel, label=label: handle_press(channel, label),
            bouncetime=300,
        )