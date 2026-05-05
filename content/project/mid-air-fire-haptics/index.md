---
title: "Mid-Air Thermo-Tactile Fire: Ultrasound Haptic Display for VR"
date: 2021-09-01
summary: "A mid-air feedback system combining heated airflow with focused ultrasound pressure to simulate the feel of fire and heat without any wearable device — published at ACM VRST 2021."
tags:
  - Unity VR
  - Haptics
  - Mid-Air
  - Ultrasound
  - ACM VRST

links:
  - name: Paper (VRST 2021)
    url: '/uploads/VRST2021_Fire.pdf'
    icon_pack: fas
    icon: file-pdf
  - name: Video
    url: 'https://www.youtube.com/watch?v=CKSEIOUzGK0'
    icon_pack: fab
    icon: youtube

image:
  caption: 'Mid-air thermo-tactile display delivering simultaneous heat and pressure without contact'
  focal_point: Smart
  preview_only: false
---

## Overview

Imagine reaching toward a virtual campfire and actually feeling the heat wash over your hands — no gloves, no controllers, nothing on your skin. **Mid-Air Thermo-Tactile Fire** is a proof-of-concept system that delivers both thermal warmth and vibrotactile pressure to a free hand hovering above a custom device, using a combination of heated airflow channels and a 40 kHz ultrasound haptic array.

Published at **ACM VRST 2021** (ACM Symposium on Virtual Reality Software and Technology), this was the first system to simultaneously characterize thermo-tactile mid-air feedback thresholds and demonstrate them in a VR fire interaction scenario.

---

## The Problem

Mid-air haptics (ultrasound) had proven that focused pressure can be delivered without contact. Thermal mid-air feedback existed in industrial settings (heat lamps). But **simultaneously combining both** — localized, controllable, synchronized — for real-time VR had not been demonstrated.

Key unknowns at project start:
- What temperature range can be achieved mid-air at realistic interaction distances (15–25 cm)?
- Does the ultrasonic pressure signal interfere with thermal perception (or vice versa)?
- What warm detection threshold (WDT) and heat-pain threshold (HPDT) apply to mid-air vs. contact thermal stimulation?

---

## System Design

### Hardware Architecture
- **Ultrasound display**: 16×16 transducer array (256 elements), 40 kHz carrier, capable of focusing pressure at 10–25 cm above surface
- **Thermal channel**: open-top acrylic chamber with 4 heating coils; a low-speed centrifugal fan directs warm air up through the focus zone
- **Temperature control**: PID loop via Arduino — thermocouple at the focal plane feeds back to heater PWM, ±1°C stability
- **Integration**: ultrasound focus point and warm airflow column co-aligned within ±5 mm

### Measured System Specs
| Parameter | Value |
|---|---|
| Peak achievable temperature at focal plane | 54.2°C |
| Ultrasound pressure at focus | 3.43 mN (100 Hz, 12 mm radius) |
| Temperature stability (mean error) | 0.25% over 10 min |
| Interaction distance range | 12–22 cm |

### Unity VR Integration
- **Unity 2020 LTS** with SteamVR / OpenVR SDK (HTC Vive)
- Custom C# bridge communicates over USB serial to Arduino controller
- VR scene: virtual campfire with particle system; hand proximity triggers thermal ramp (further = cooler, closer = warmer) while fire flicker drives vibrotactile modulation at 4–12 Hz
- Thermal latency from Unity event to onset at skin: ~120 ms (dominated by airflow thermal inertia)

---

## User Evaluation

### Threshold Study — WDT and HPDT
- **N = 14 participants**
- **Protocol**: method of limits (ascending/descending); 5 trials per direction, 3 interleaved staircases
- **Conditions**: mid-air thermal only (no ultrasound) vs. mid-air thermal + ultrasound (thermo-tactile)
- **Measures**: WDT (°C), HPDT (°C), response time to first detection

### Haptic Pattern Recognition Study
- **N = 14 participants** (same cohort, separate session)
- **Task**: identify 4 spatial haptic patterns (dot, ring, horizontal bar, vertical bar) presented mid-air
- **Conditions**: non-thermal (room temp) vs. thermal-on (heated airflow active)
- **Measure**: identification accuracy, confusion matrix

### VR Experience Study
- **N = 10 participants**
- **Task**: 5-minute campfire scene; ratings on warmth realism, presence, comfort

---

## Results & Key Findings

- **WDT**: mean 32.8°C (SD=1.12) — consistent with contact-based thermal WDT literature (validates mid-air stimulation as perceptually equivalent)
- **HPDT**: mean 44.6°C (SD=1.64) — also matches contact norms; no elevated pain threshold from airflow delivery
- **Pattern accuracy**: 98.1% (non-thermal) vs. **97.2% (thermal)** — no significant degradation (p=.38); thermal channel does not interfere with tactile perception
- Thermo-tactile condition received significantly higher VR realism ratings than tactile-only (p<.05)

---

## Lessons & Evolution

This project established the **core technical finding** that underpins the entire MI Lab thermal haptics research line: thermal and tactile cues can coexist mid-air without masking each other, enabling richer multi-modal VR experiences. Every subsequent project (Snow, Fabric Thermal Display, Fiery Hands) built on these baseline thresholds and the dual-channel architecture proven here.

---

## Impact

- 📄 Published: **ACM VRST 2021** — *Proceedings of the 27th ACM Symposium on Virtual Reality Software and Technology*
- DOI: [10.1145/3489849.3489889](https://doi.org/10.1145/3489849.3489889)
- First paper characterizing mid-air thermo-tactile thresholds; foundational reference for the lab's subsequent wearable thermal haptics work
