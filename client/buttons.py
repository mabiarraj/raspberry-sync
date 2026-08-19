import RPi.GPIO as GPIO

BUTTONS = {
    5: "A",
    6: "B",
    16: "C",
    24: "D",
}


def setup_buttons(callback):
    GPIO.setmode(GPIO.BCM)

    for pin, label in BUTTONS.items():
        GPIO.setup(pin, GPIO.IN, pull_up_down=GPIO.PUD_UP)

        GPIO.add_event_detect(
            pin,
            GPIO.FALLING,
            callback=lambda channel, label=label: callback(label),
            bouncetime=300,
        )