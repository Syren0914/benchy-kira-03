# Benchy firmware

The repository includes a small Arduino Nano sketch for testing the button-to-relay control path before it is integrated with the power supply.

## Relay-module bench test

Source: [`benchy_relay_test/benchy_relay_test.ino`](benchy_relay_test/benchy_relay_test.ino)

The reference sketch starts with the relay commanded off. Each debounced press of a momentary pushbutton toggles the relay state and the Nano's built-in LED. It also prints `Relay ON` or `Relay OFF` at 9600 baud.

### Reference low-energy connections

| Nano | Connect to | Purpose |
|---|---|---|
| `D2` | One side of a momentary pushbutton | Control input; the other button terminal connects to Nano `GND` |
| `D7` | Relay-module `IN` | Logic control output |
| `5V` | Relay-module `VCC` | Only for a verified 5 V logic-compatible relay module |
| `GND` | Relay-module `GND` and button return | Common reference |
| USB | Computer or USB supply during bench test | Nano power and serial monitor |

![Arduino Nano relay-module bench-test connection](../hardware/nano-relay-test.png)

Keep relay `COM`, `NO`, and `NC` disconnected during the bench test. The reference wiring does not define what the relay will switch in the completed power supply.

## Upload

1. Open the `.ino` file in Arduino IDE.
2. Select the exact Nano board and processor/bootloader used by the actual board.
3. Connect the Nano by USB with the relay contacts disconnected.
4. Compile and upload the sketch.
5. Open Serial Monitor at 9600 baud.
6. Confirm `Relay OFF` at startup, then press the button and verify one clean state change per press.

## Configuration and validation

`RELAY_ACTIVE_LOW` is set to `true` because many relay modules use a low-level trigger. Confirm the actual module before powering it. If its documented input is active high, set the constant to `false` and repeat the startup test.

A software command cannot guarantee a safe state while the Nano is booting, reset, disconnected, or unpowered. The final design needs a hardware pull-up or pull-down compatible with the exact relay module so that its input remains inactive when the Nano pin is high impedance. Record the observed relay state during power-up, reset, upload, USB connection/removal, and simulated firmware failure.

A bare relay coil must not be connected directly to `D7`. It requires a correctly designed driver, flyback suppression, power source, and grounding arrangement. Use this reference only with a relay module whose input and supply requirements have been verified.

## Integration boundary

Before connecting `COM`, `NO`, or `NC`, document the exact relay part number, contact ratings, switched circuit, required default state, and protection. Do not use the reference sketch to switch mains voltage. The intended final function—such as controlling a verified low-voltage PSU-enable input or a DC load—must be confirmed and reviewed first.

The firmware in this directory is licensed under the [MIT License](LICENSE).
