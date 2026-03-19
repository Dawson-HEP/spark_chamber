# Hardware

## Source Trigger Unit (STU)

The Source Trigger Unit scales an adjustable DC input into a high-voltage DC output, and provides trigger by means of discharging its output to ground. The following is a detailed explanation of the [schematic](./spark_chamber_schematic.pdf).

### Spark Chamber (p. 5)

When the STU's generated positive voltage is applied on `SW_SPARK`, buffer capacitors charge through 10k resistors to ground. 10k resistors see the full voltage swing until the voltage across them decreases as the capacitors charge.

When `SW_SPARK` is grounded, either by the IGBTs or by the spark gaps, the full voltage is applied across the 10k resistors, on which plates are attached to either end of each resistor. As such, the full voltage swing is applied on the plates, creating sparks aligned with ionization tracks.

## High Voltage Probe


