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
      text: "Research across medical physics, haptics, extended reality, and human-centered technology. Each project combines engineering design, experimental evaluation, and interdisciplinary research."
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
        I work at the seam between **physical hardware and human-centered technology**, developing
        medical-physics, haptics, and XR systems and evaluating them through rigorous experiments.

        - **Engineering.** Custom instrumentation, embedded systems, PCB design, computational modeling, and experimental platforms.
        - **Human-centered evaluation.** Human-subject research, psychophysics, quantitative analysis, and usability studies.
        - **Translation.** Applying interdisciplinary methods to radiation oncology technology, medical imaging, haptics, and XR.
        - **Communication.** Turning findings into publications, demonstrations, and practical technologies.
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
      title: Contact
      subtitle: ""
      text: |
        For research and collaboration inquiries, please get in touch.

        [haokun.wang@utsouthwestern.edu](mailto:haokun.wang@utsouthwestern.edu) · [LinkedIn](https://www.linkedin.com/in/haokun-wang-854548239/) · [Google Scholar](https://scholar.google.com/citations?user=AzitNLgAAAAJ&hl=en)
    design:
      columns: "1"
---
