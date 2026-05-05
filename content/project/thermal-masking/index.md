---
title: "Thermal Masking: When the Illusion Takes Over the Real"
date: 2024-05-11
summary: "Discovering a new thermal perceptual illusion — thermal masking — where a nearby vibrotactile cue completely overrides perceived thermal location, enabling novel wearable haptic designs. Published at ACM CHI 2024."
tags:
  - Haptics
  - Perceptual Study
  - Psychophysics
  - Illusion
  - ACM CHI

links:
  - name: Paper (CHI 2024)
    url: '/uploads/CHI2024_ThermalMasking.pdf'
    icon_pack: fas
    icon: file-pdf
  - name: Video
    url: 'https://www.youtube.com/watch?v=GklwlCuPwv8'
    icon_pack: fab
    icon: youtube

image:
  caption: 'Experimental setup probing thermal masking across the forearm'
  focal_point: Smart
  preview_only: false
---

## Overview

**Thermal Masking** is a newly characterized perceptual illusion: when a vibrotactile stimulus is applied near a thermal stimulus, the *perceived location* of warmth completely jumps to the tactile site — the original thermal signal vanishes from conscious perception. This "masking" is distinct from previously known thermal referral and has profound implications for wearable haptic design.

Published at **ACM CHI 2024** (the flagship venue for human–computer interaction research), this work provides the first systematic characterization of thermal masking on the human arm.

---

## The Problem

Thermal feedback in wearables is expensive: Peltier modules are bulky, power-hungry, and slow. Covering a large body area (like the back or full arm) with thermal actuators is impractical. Prior work showed that thermal sensations can be "referred" — stretched toward a tactile stimulus. But we suspected a more dramatic effect existed.

**Hypothesis:** A single vibrotactile cue could *completely suppress* the original thermal percept, not just shift it — enabling sparse thermal + dense tactile arrays to cover large body areas affordably.

---

## Research Approach

Three controlled psychophysical experiments on the forearm, each systematically varying one factor:

| Experiment | Manipulated Variable | Key Question |
|---|---|---|
| 1 | Temperature level | Does masking occur more at warm vs. hot vs. cold? |
| 2 | Thermal-to-tactile distance | How far can masking propagate? |
| 3 | Actuator placement (same side vs. opposite side of arm) | Does masking cross body-part boundaries? |

Participants reported where they felt the temperature (thermal site, tactile site, or both) on each trial. Masking was defined as reporting *only* the tactile site despite the thermal actuator being active elsewhere.

---

## Apparatus

- **Thermal actuator**: Single Peltier module (40 × 40 mm), range 20°C – 45°C (cold, neutral, warm, hot conditions)
- **Tactile actuator**: ERM (eccentric rotating mass) motor, 180 Hz, 1.5 G amplitude
- **Placement rig**: 3D-printed sliding rail on the forearm allowing 2–24 cm inter-actuator distance
- All stimuli were synchronized via Arduino with 1 ms timing precision

---

## User Evaluation

- **Total N = 48 participants** (16 per experiment), all naïve to the hypothesis
- **Design**: fully within-subject with counterbalanced ordering
- **Trial structure**: 3 s baseline → simultaneous thermal + tactile onset for 5 s → localization report → 30 s ISI for thermal recovery
- **Measures**: localization accuracy (thermal site / tactile site / both), response time, confidence rating

---

## Results & Key Findings

**Experiment 1 — Temperature Level:**
- Thermal masking rate: **warm: 73%**, hot: 41%, cold: 38%
- Warm conditions produced significantly higher masking than hot or cold (χ²(2)=24.3, p<.001)
- Implication: warm stimulation (≈35–38°C) is the optimal operating zone for masking-based designs

**Experiment 2 — Distance:**
- Masking persisted up to **24 cm** from the thermal actuator — nearly the full forearm length
- Masking rate decayed logarithmically with distance (r²=0.91)
- Practical finding: one thermal module can plausibly cover the entire forearm with tactile array assist

**Experiment 3 — Opposite Side:**
- Masking also occurred when the tactile actuator was placed on the *opposite* side of the arm (dorsal vs. volar)
- Rate: 58% — lower than same-side but still above chance (p<.001)
- Opens door to through-limb sensing designs (e.g., armband with actuators only on outer surface)

---

## Design Implications

These findings directly shaped the actuator placement strategy in [Fiery Hands](/project/fiery-hands/) and [Fabric Thermal Display](/project/fabric-thermal-display/): by exploiting thermal masking, both projects placed thermal actuators exclusively on non-obstructive surfaces while delivering perceived localized warmth at the inner contact points.

---

## Impact

- 📄 Published: **ACM CHI 2024** — *Proceedings of the 2024 CHI Conference on Human Factors in Computing Systems*
- DOI: [10.1145/3613904.3641941](https://doi.org/10.1145/3613904.3641941)
- Citation: Haokun Wang, Yatharth Singhal, Hyunjae Gil, Jin Ryong Kim. "Thermal Masking: When the Illusion Takes Over the Real." CHI '24.
