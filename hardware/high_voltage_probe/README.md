# High Voltage Probe

Compensated 500:1 high voltage probe with 10 MHz bandwidth, adjustable frequency response, and 17.5 kV measurement capability. This probe is meant to recreate the capabilities of a [Tektronix P6015A](https://www.tek.com/en/products/oscilloscopes/oscilloscope-probes/high-voltage-probe-single-ended) while being safe, and reasonably priced.

## Documents

- Testing data, scope traces: [Google Drive](https://drive.google.com/drive/folders/1fRV_-lUVtBa012b_aV9xOPN5UBUo3qJT).
- Probe Schematic: [PDF](../high_voltage_probe.pdf).
- KiCad Project: `./high_voltage_probe.kicad_pro`

## Probe

A PTFE sheating of 1.75 mm (ID) is fitted onto a tinned-nail, with a bonding wire soldered onto its end. A vinyl tube isolates the conductors and increases its diameter to be fit within a standard PTFE 6mm cable gland. PTFE is chosen for its electrical insulation properties, as well as stability.

<p align="center">
<img src="./res/tip_parts.jpg" width="65%">
</p>

Tightening the cable gland cap compresses all layers until friction affixes the probe tip position with respect to the gland. Observing the P6015A, we see that the measurement tip needs to be distanced from other objects other that the one measured due to parasitics. A large enough probe tip ensures mechanical separation, as well as isolation.

<p align="center">
<img src="./res/tip_assembled.jpg" width="65%">
</p>

Hand-soldered attenuation resistors with capacitors are attached onto an acrylic backing for support. A small compensation PCB rests as the end with trimmers adjusted and calibrated. A white PVC tube (3/4") serves as the probe handle. A 4mm banana jack is press-fitted into a drilled hole for the attachment of the grounding lead. The electrical assembly slides into one end of the tube, while 3D-printed end caps are secured by screws to complete the probe.

<p align="center">
<img src="./res/full_probe_assembly.jpg" width="75%">
</p>

## Analysis

FRA is conducted on the probe to establish its frequency response from 1 kHz to 20MHz FRA at 50 points/decade. A 500:1 probe yields in a $20 \log{\frac{1}{500}} = -53.98$ $\mathrm{dB}$ attenuation, as per the gain v. frequency of the FRA, which is flat.

<p align="center">
<img src="./res/fra_probe.png" width="65%">
</p>
