---
title: "Fiery Hands: Thermal-Tactile Glove for VR Object Manipulation"
date: 2024-10-11
summary: "A wearable thermal glove that renders localized heat and touch across the palm and fingertips during VR interaction — published at ACM UIST 2024."
tags:
  - Unity VR
  - Haptics
  - Wearable
  - User Study
  - ACM UIST

links:
  - name: Paper (UIST 2024)
    url: '/uploads/UIST2024_FieryHands.pdf'
    icon_pack: fas
    icon: file-pdf
  - name: Video
    url: 'https://www.youtube.com/watch?v=M_gZlia0lZ8'
    icon_pack: fab
    icon: youtube

image:
  caption: 'Thermal-tactile glove enabling localized heat feedback during VR interaction'
  focal_point: Smart
  preview_only: false
---

## Overview

How do you make a virtual fire feel real on your hands? **Fiery Hands** answers that question with a custom wearable thermal glove that delivers localized thermal *and* tactile sensations to the palm and all five fingertips — without blocking the hand or preventing natural object manipulation in VR.

Published at **ACM UIST 2024** (the premier venue for novel interactive systems), this project represents a step change in how XR systems can deliver believable thermal touch.

---

## The Problem

Existing haptic gloves either:
- Cover the inner palm and fingertip surfaces, blocking touch and dexterity, or
- Place thermal actuators only on the back of the hand, limiting localized feedback

The challenge: thermal actuators are physically large (Peltier modules), slow (seconds to change temperature), and need direct skin contact. Placing enough of them to cover a hand while preserving freedom of movement seemed contradictory.

**Research Question:** Can we achieve the *perception* of localized thermal feedback across the full hand using fewer actuators cleverly placed on non-obstructive body sites?

---

## Research Approach

We leveraged two perceptual phenomena from psychophysics:

1. **Thermal Referral** — the brain attributes a thermal sensation to a *nearby* tactile stimulus site, not the actual thermal source. Heat felt elsewhere "moves" to where you're touching.
2. **Tactile Masking** — a vibrotactile cue can suppress or redirect the perceived location of a thermal stimulus.

By combining strategically placed Peltier actuators on the *outer* palm and back of fingers with vibrotactile motors at fingertip contact points, we could generate perceived thermal sensations *at the fingertips* without physically touching them.

---

## System Design

### Hardware
- **Thermal actuators**: 4 custom-fabricated Peltier modules (30 × 30 mm) mounted on the outer palm and finger dorsal surfaces
- **Tactile actuators**: 5 coin-type LRA vibration motors placed at the inner fingertip
- **Controller**: Arduino Mega with custom power amplifier board; Bluetooth LE to PC
- **Glove substrate**: Thin spandex with 3D-printed actuator mounts — allows full grip

### Unity VR Integration
- Built in **Unity 2022 LTS** with **OpenXR / XR Interaction Toolkit**
- Custom C# `HapticFeedbackManager` subscribes to XR physics collision events and maps contact surface temperature to actuator commands
- Real-time thermal rendering: fire = sustained warm + rhythmic vibration; ice = sustained cool + gentle pulse; metal = rapid ramp-up on contact
- Deployed on **Meta Quest 2** via Quest Link (PC-tethered for full Peltier power budget)

---

## User Evaluation

### Study 1 — Thermal Localization
- **N = 12 participants**, within-subject design
- **Task**: identify which finger perceived the thermal stimulus while only the dorsal actuators were active
- **Conditions**: palm-only thermal, 4× Peltier positions × 3 temperature levels (warm/hot/neutral)
- **Measure**: accuracy of localization, JND (just-noticeable difference)

### Study 2 — VR Interaction Plausibility
- **N = 16 participants**
- **Task**: interact with three virtual objects (glowing coal, ice block, metal rod) and rate realism
- **Conditions**: thermal-only, tactile-only, thermal+tactile (Fiery Hands), and no-feedback baseline
- **Measures**: NASA-TLX, immersion subscale, perceived temperature match (7-pt Likert)

---

## Results & Key Findings

- **Localization accuracy: 84%** — participants correctly identified the stimulated finger using only dorsal Peltier placement, validating the thermal referral strategy
- **Plausibility rating** of thermal+tactile condition was **significantly higher** than any single-modality condition (F(3,45)=18.4, p<.001, η²=0.55)
- Users reported the coal interaction as "surprisingly convincing" — qualitative themes: warmth buildup over time felt organic, not mechanical
- Power consumption reduced by **60%** vs. placing individual Peltiers at each fingertip while achieving comparable perceptual quality

---

## Impact

- 📄 Published: **ACM UIST 2024** — *Proceedings of the 37th Annual ACM Symposium on User Interface Software and Technology*
- DOI: [10.1145/3654777.3676457](https://doi.org/10.1145/3654777.3676457)
- Inspired follow-on work on thermally-integrated wearables for extended wear XR sessions
