---
title: "Let It Snow: Cross-Modal Cold & Touch for VR Snowfall"
date: 2024-05-15
summary: "A mid-air haptic interface that combines Peltier cold modules and an ultrasound haptic display to let users catch snowflakes and feel rain on their bare hands in VR — published in ACM IMWUT 2024."
tags:
  - Unity VR
  - Haptics
  - Cross-Modal
  - Mid-Air
  - ACM IMWUT

links:
  - name: Paper (IMWUT 2024)
    url: '/uploads/IMWUT2024_Snow.pdf'
    icon_pack: fas
    icon: file-pdf
  - name: Video
    url: 'https://youtu.be/rPDaRQhBt2Y?si=qSbaclXQT8vvpJSa'
    icon_pack: fab
    icon: youtube

image:
  caption: 'User catching virtual snowflakes with cold + tactile mid-air feedback'
  focal_point: Smart
  preview_only: false
---

## Overview

**Let It Snow** is a hands-free, wearable-free haptic experience: users hold their bare hands over a custom mid-air display that simultaneously fires focused ultrasound pressure points and directed cold airflow to simulate individual snowflakes landing — or rain drops splattering — on their palms.

Published in **ACM IMWUT 2024** (Proceedings of the ACM on Interactive, Mobile, Wearable and Ubiquitous Technologies), the project explores how cross-modal cold–tactile pairing creates emergent sensory illusions greater than either cue alone.

---

## The Problem

Simulating precipitation in VR is a classic immersion gap. Visually, snow and rain can look photorealistic. But without *feeling* the cold, the wet, the gentle impact — users never quite believe it. Existing approaches require worn devices, which break the "bare hand in the weather" fantasy entirely.

**Core Questions:**
- Can cold airflow and ultrasound pressure co-localize in mid-air to synthesize a snowflake or raindrop percept?
- Do cold and tactile cues mask each other, or can they be independently perceived at the same skin location?
- How should aggregated stimuli be rendered for heavy snowfall / rainfall?

---

## Research Approach

We drew on **cross-modal sensory integration** theory: cold and tactile channels are processed by separate neural pathways (thermoreceptors vs. mechanoreceptors), so two signals can coexist without mutual interference — unlike, say, two sounds at the same frequency.

Key hypothesis: a brief cold puff + simultaneous pressure focus = snowflake percept; a sharp cold burst + faster pressure = raindrop percept.

We also designed an **aggregated haptic scheme** for particle-dense scenes: rather than rendering every particle individually (physically impossible), we modulate cold intensity and pressure density proportionally to particle count, exploiting temporal summation in both sensory channels.

---

## System Design

### Hardware
- **Cold array**: 6 Peltier modules (20 × 20 mm) mounted in a ring, each with a micro-fan to direct cold air toward the focus point; temperature range: 5°C–15°C above ambient
- **Ultrasound haptic display**: Ultrahaptics STRATOS Inspire — 256 transducers at 40 kHz, creating mid-air pressure foci up to 200 mN at distances up to 22 cm
- **Depth tracking**: Intel RealSense D435 hand tracking, integrated into Unity for palm position → focus point mapping
- **Control PC**: Custom C++ driver for thermal timing; Unity handles audio, visuals, and hand tracking

### Unity VR Integration
- Built in **Unity 2021 LTS**, standalone VR scene with Oculus Integration SDK
- Particle system drives two managers:
  - `SnowRenderer`: handles visual particles with collision callbacks to trigger haptic events
  - `HapticAggregator`: accumulates per-frame particle counts, applies transfer function to Peltier intensity and ultrasound amplitude
- Snowflake percept: 150 ms cold puff + 40 Hz pressure burst; Raindrop: 60 ms sharp cold + 200 Hz single-pulse
- Scene contains interactive environments: snowy mountain valley, rainstorm on a city rooftop

---

## User Evaluation

### Perceptual Study — Cold × Tactile Independence
- **N = 14 participants**
- **Design**: 2 (cold present/absent) × 2 (tactile present/absent) × 5 repetitions
- **Measure**: detection accuracy per modality, reported interference rating
- **Finding**: No significant cross-modal masking — participants detected cold and tactile independently (d' > 2.5 for both modalities combined)

### Experience Study — Aggregated Rendering Comparison
- **N = 20 participants**, within-subject
- **Conditions**: (1) no haptics, (2) tactile-only, (3) cold-only, (4) Snow (cold+tactile sparse), (5) Snow (cold+tactile aggregated)
- **Measures**: presence subscale (IPQ), realism rating, preference ranking
- **Task**: 3-minute free exploration of snowy mountain scene, 3-minute rainstorm scene

---

## Results & Key Findings

- **Aggregated scheme rated significantly more realistic** than sparse individual-particle scheme (p<.01) for heavy snowfall
- Cold+tactile combination rated **+1.8 points** on 7-pt presence scale vs. tactile-only (p<.001)
- 18/20 participants preferred the full cross-modal condition; primary qualitative theme: "it actually felt cold and real, like being outside"
- System achieved stable cold delivery at ±0.3°C variance across a 10-minute continuous session

---

## Impact

- 📄 Published: **ACM IMWUT 2024** — *Proc. ACM Interact. Mob. Wearable Ubiquitous Technol.*
- DOI: [10.1145/3659587](https://doi.org/10.1145/3659587)
- Framework for aggregated haptic rendering has been adopted in follow-on multi-particle VR haptics research
