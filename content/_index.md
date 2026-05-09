---
# Leave the homepage title empty to use the site title
title: ""
date: 2024-05-01
type: landing

design:
  # Default section spacing
  spacing: "6rem"

sections:
  # ---------- HERO ----------
  - block: resume-biography-3
    content:
      username: admin
      title: ""
      text: ""
      button:
        text: Download CV
        url: "/uploads/resume.pdf"
    design:
      css_class: dark
      background:
        color: black
        image:
          filename: background.png
          filters:
            brightness: 0.55
          size: cover
          position: center
          parallax: false

  # ---------- SELECTED WORK ----------
  # Featured publications/projects shown as a visual grid.
  # Set `featured: true` in any publication front-matter to surface it here.
  - block: collection
    id: selected
    content:
      title: Selected Work
      subtitle: ""
      text: "Research-driven AR/VR interactions, hardware prototyping, and user studies. Each project is shipped end-to-end — from concept through fabrication and evaluation — and published at top HCI venues (CHI, UIST, IEEE VR, ISMAR)."
      filters:
        folders:
          - publication
        featured_only: true
    design:
      view: article-grid
      fill_image: true
      columns: 3

  # ---------- ALL PUBLICATIONS ----------
  - block: collection
    id: papers
    content:
      title: All Publications
      text: ""
      filters:
        folders:
          - publication
        exclude_featured: false
    design:
      view: citation
      columns: 1

  # ---------- APPROACH / PROCESS ----------
  - block: markdown
    id: approach
    content:
      title: Approach
      subtitle: ""
      text: |
        I work at the seam between **physical hardware and digital interaction**, designing
        wearable haptics, AR/VR feedback systems, and the studies that prove they work.

        - **Research & framing.** Literature review, competitive teardown, formative interviews to scope a real problem.
        - **Prototyping.** Rapid hardware mockups (thermal arrays, ultrasound rigs, gloves, EMG straps) paired with Unity/Unreal interaction prototypes.
        - **User testing.** Within-subject studies, IRB-approved protocols, mixed-methods analysis (quant + think-aloud).
        - **Communication.** Translating findings into design implications, papers, and deck-ready visuals for stakeholders.
    design:
      columns: "1"
      spacing:
        padding: ["3rem", 0, "3rem", 0]

  # ---------- NEWS ----------
  - block: collection
    id: news
    content:
      title: News
      subtitle: ""
      text: ""
      page_type: post
      count: 5
      filters:
        author: ""
        category: ""
        tag: ""
        exclude_featured: false
        exclude_future: false
        exclude_past: false
        publication_type: ""
      offset: 0
      order: desc
    design:
      view: date-title-summary
      spacing:
        padding: [0, 0, 0, 0]

  # ---------- CONTACT ----------
  - block: markdown
    id: contact
    content:
      title: Let's talk
      subtitle: ""
      text: |
        Open to UI/UX, Product Design, and UX Research roles — full-time, internship, or consulting.

        [haokun.wang@utdallas.edu](mailto:haokun.wang@utdallas.edu) · [LinkedIn](https://www.linkedin.com/in/haokun-wang-854548239/) · [Google Scholar](https://scholar.google.com/citations?user=AzitNLgAAAAJ&hl=en)
    design:
      columns: "1"
---
