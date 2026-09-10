/*
  Benchy — Kira 03 relay-module bench test

  This sketch tests a 5 V logic-compatible relay module using a momentary
  pushbutton. It does not define the final Benchy power-control circuit.

  Reference connections:
    Nano D2  -> pushbutton -> Nano GND
    Nano D7  -> relay module IN
    Nano 5V  -> relay module VCC
    Nano GND -> relay module GND

  Keep relay COM/NO/NC disconnected during this test.

  Copyright (c) 2026 Erdene Batbayar
  SPDX-License-Identifier: MIT
*/

const byte BUTTON_PIN = 2;
const byte RELAY_PIN = 7;
const byte STATUS_LED_PIN = LED_BUILTIN;

// Many relay modules are active LOW. Change this only after checking the
// markings and documentation for the exact module.
const bool RELAY_ACTIVE_LOW = true;

const unsigned long DEBOUNCE_MS = 35;

bool relayEnabled = false;
bool lastRawButton = HIGH;
bool stableButton = HIGH;
unsigned long lastButtonChangeMs = 0;

byte relayLevel(bool enabled) {
  if (RELAY_ACTIVE_LOW) {
    return enabled ? LOW : HIGH;
  }
  return enabled ? HIGH : LOW;
}

void setRelay(bool enabled) {
  relayEnabled = enabled;
  digitalWrite(RELAY_PIN, relayLevel(relayEnabled));
  digitalWrite(STATUS_LED_PIN, relayEnabled ? HIGH : LOW);
  Serial.println(relayEnabled ? F("Relay ON") : F("Relay OFF"));
}

void setup() {
  // Set the inactive output level before enabling the output driver.
  digitalWrite(RELAY_PIN, relayLevel(false));
  pinMode(RELAY_PIN, OUTPUT);
  pinMode(STATUS_LED_PIN, OUTPUT);
  pinMode(BUTTON_PIN, INPUT_PULLUP);

  Serial.begin(9600);
  setRelay(false);
  Serial.println(F("Benchy relay-module test ready"));
}

void loop() {
  const bool rawButton = digitalRead(BUTTON_PIN);
  const unsigned long now = millis();

  if (rawButton != lastRawButton) {
    lastButtonChangeMs = now;
    lastRawButton = rawButton;
  }

  if ((now - lastButtonChangeMs) >= DEBOUNCE_MS && rawButton != stableButton) {
    stableButton = rawButton;
    if (stableButton == LOW) {
      setRelay(!relayEnabled);
    }
  }
}
