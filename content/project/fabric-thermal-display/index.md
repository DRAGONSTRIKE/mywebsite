---
title: "Fabric Thermal Display: Ultrasound-Heated Wearable for VR"
date: 2023-09-01
summary: "A fabric-based thermal glove that uses 40 kHz ultrasonic waves to heat thermally-conductive materials, enabling wearable VR thermal feedback without bulky Peltier modules. Published at IEEE ISMAR 2023."
tags:
  - Unity VR
  - Haptics
  - Wearable
  - Ultrasound
  - IEEE ISMAR

links:
  - name: Paper (ISMAR 2023)
    url: '/uploads/ISMAR2023_Ultrasoundglove.pdf'
    icon_pack: fas
    icon: file-pdf
  - name: Video
    url: 'https://www.youtube.com/watch?v=B5AjfdOlMEQ'
    icon_pack: fab
    icon: youtube

image:
  caption: 'Polyester-aluminum glove generating thermal feedback via 40 kHz ultrasonic waves'
  focal_point: Smart
  preview_only: false
---

## Overview

Standard thermal wearables rely on Peltier thermoelectric modules — rigid, thick, and power-intensive. **Fabric Thermal Display** takes a different approach: weave thermally-conductive materials (copper, aluminum mesh) into a fabric glove and excite them with focused ultrasonic waves. The friction heats the conductive fibers, delivering warmth through the fabric itself.

Published at **IEEE ISMAR 2023** (IEEE International Symposium on Mixed and Augmented Reality), this project delivers a proof-of-concept for ultrasound-driven textile thermal displays and demonstrates their use in VR object interaction scenarios.

---

## The Problem

Peltier-based thermal gloves work, but they have hard constraints:
- **Thickness**: modules are 3–5 mm, stiff, and change the hand's natural shape
- **Power**: each Peltier draws 3–10 W continuously
- **Scalability**: covering all fingers requires 5+ modules, complicated wiring, and custom PCBs

Could fabric itself become the thermal actuator — flexible, lightweight, and able to conform to any body shape?

**Research Question:** Which fabric materials respond best to 40 kHz ultrasonic excitation, and can combinations with conductive materials achieve perceptually meaningful warmth for VR?

---

## Research Approach

We started with a **material science study** before touching user testing:

1. **Characterization phase**: apply ultrasonic energy to 5 fabric types (polyester, cotton, nylon, Lycra, carbon-fiber blend), measure temperature rise over 30 s at three amplitude levels
2. **Composite phase**: integrate the best fabric (polyester) with copper mesh and aluminum foil, compare thermal curves
3. **Perceptual phase**: user study on thermal detection and level identification with the best material combination
4. **Application phase**: integrate into a glove form factor, demonstrate VR use cases

---

## System Design

### Ultrasound Setup
- **Ultrasound driver**: Ultrahaptics STRATOS board, 40 kHz carrier, amplitude-modulated 0–100%
- **Focus geometry**: single focal point directed at 15 cm standoff, corresponding to palm contact zone of glove
- **Thermal measurement**: FLIR A315 thermal camera captured surface temperature maps at 9 Hz

### Fabric Samples
| Material | Peak Temp Rise (100% amp, 30s) | Flexibility | Notes |
|---|---|---|---|
| Polyester | +18.4°C | High | Best performance |
| Cotton | +9.1°C | High | Poor — high thermal mass |
| Nylon | +12.3°C | Medium | Acceptable |
| Lycra | +7.8°C | Very high | Too low output |
| Carbon fiber | +21.1°C | Low | Best thermal, too stiff |

**Winner: Polyester + Aluminum** — +22.6°C peak, flexible, washable

### Glove Design
- Polyester base with 0.1 mm aluminum foil laminate on palm zone
- Total glove weight: 28 g (vs. 95 g for Peltier glove baseline)
- No wiring — ultrasound is contactless

### Unity VR Integration
- **Unity 2021 LTS** + Oculus Integration SDK (Quest 2)
- Custom `FabricHapticManager`: maps virtual object surface temperature to ultrasound amplitude via lookup table
- Demonstrated VR scenarios: picking up hot metal ingot, holding warm beverage, touching cold ice sculpture
- Haptic rendering loop runs at 90 Hz, matching display refresh

---

## User Evaluation

### Study 1 — Detection Thresholds
- **N = 12 participants**
- **Task**: signal detection (yes/no) across 5 amplitude levels, 2-AFC paradigm
- **Measure**: warm detection threshold (WDT)
- **Result**: mean WDT = 38% amplitude (≈ +7.2°C skin surface delta)

### Study 2 — Level Identification (Thermal JNDs)
- **N = 16 participants**
- **Task**: categorize warmth into 4 levels (none, low, medium, high) from ultrasound-heated glove
- **Condition**: fabric-only vs. fabric+copper vs. fabric+aluminum
- **Result**: fabric+aluminum achieved **78% accuracy** for 4-level identification, significantly outperforming fabric-only (54%, p<.01) and fabric+copper (66%, p<.05)

---

## Results & Key Findings

- Polyester is the optimal base fabric for ultrasonic thermal generation among tested materials
- Aluminum lamination provides +4.2°C improvement over copper at the same power setting
- Users could reliably distinguish 4 thermal levels through the glove, meeting the threshold needed for meaningful VR thermal rendering
- No participant reported discomfort over 20-minute continuous wear sessions

---

## Impact

- 📄 Published: **IEEE ISMAR 2023** — *IEEE International Symposium on Mixed and Augmented Reality*
- DOI: [10.1145/3489849.3489889](https://doi.org/10.1145/3489849.3489889)
- The material findings fed directly into the Fiery Hands glove substrate design and the broader thermal-wearables research program at MI Lab
