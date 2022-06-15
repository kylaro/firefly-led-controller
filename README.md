# firefly-led-controller
PCB for the FireFly LED Controller by kylarLEDs


## Hardware
    The sensors on the board are:
        1. Microphone (not yet supported) -> for sound reactive LEDs
        2. Potentiometer (not yet supported) -> for brightness control
        3. Rotary encoder (not yet supported) -> for color/hue control
        4. Rotary encoder button (not yet supported) -> for changing patterns

    The outputs from the board are:
        1. 2 x WS2812B LED output pins (not yet supported)
            a. Each pin has 2 output pads, one on front and one on back
            b. Each pin has a 0.1 inch header port
        2. 2 x USBC 5V power up to 3A

    The input to the boards are:
        1. Pico programming micro usb port (not meant for power)
        2. 1 x USBC 5V power up to 3A


## Notes
Necessary improvements:
  * Support for 4 pin ws2812b strips, and APA102, 4 outputs
  * More testing capability for the microphone, and maybe other components
  *     -> maybe bottom of board row of headers that another board with a pi can plug into, or row of pads on bottom
  *     -> Or pad groups on the bottom, like this to that type things... every connection could be represented
  *     -> ex. MIC GND <-> GND ... ENC_A <-> GP22 ..., anything that contributes functionality :) 
  * 4 LED outputs
  * Header pins offset

Possibile Improvements to make:
  * Have power pads for screw down crimped ring terminals?
  * Have a hole on the board to weave the LED wire through to add mechanical stability to solder connections
  * Support for 12V on board? (5v regulator, 5v dataline, but 12v power)
  * Support for automatically detecting strip length based on current drawn by strip (either "off" current or turning 1 on at a time, need ammeter)
  * Support for battery charging
  * Support for DMX LEDs input/output

Notes:
  * USB C holes should be more exact so it fits better
