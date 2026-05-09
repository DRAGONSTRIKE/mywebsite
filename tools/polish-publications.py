#!/usr/bin/env python3
"""
polish-publications.py
----------------------
One-shot migration that sets every publication to `featured: true`, fixes the
"fasle" typo, and replaces the single 'Haptic' / 'Haptic devices' tag with a
richer, portfolio-friendly tag list per project.

USAGE
-----
    cd /path/to/mywebsite
    python tools/polish-publications.py

Idempotent: safe to run multiple times.
"""

from pathlib import Path
import re

TAGS = {
    "conference-paper-fiery-hands": [
        "AR / VR", "Wearable Haptics", "Hardware Prototyping", "User Study",
    ],
    "conference-paper-fire": [
        "Mid-Air Haptics", "Ultrasound", "VR", "Hardware Prototyping",
    ],
    "conference-paper-thermal-masking": [
        "Perception", "Haptics", "User Study", "Multisensory",
    ],
    "conference-paper-thermal-motion": [
        "AR / VR", "Haptics", "Illusion Design", "User Study",
    ],
    "conference-paper-ultrasound-glove": [
        "Wearable", "AR / VR", "Ultrasound", "Hardware Prototyping",
    ],
    "journal-article-snow": [
        "VR", "Multisensory", "Mid-Air Haptics", "Experience Design",
    ],
    "journal-article-upperbody": [
        "Haptics", "VR", "Perception", "User Study",
    ],
    "journal-paper-Motor-Converter": [
        "Engineering", "Power Electronics",
    ],
}

ROOT = Path(__file__).resolve().parent.parent
PUB = ROOT / "content" / "publication"


def replace_tags_block(text, new_tags):
    new_block = "tags:\n" + "\n".join("  - " + t for t in new_tags)
    pattern = re.compile(r"^tags:\s*\n(?:[ \t]*-[^\n]*\n)*", re.MULTILINE)
    if pattern.search(text):
        return pattern.sub(new_block + "\n", text, count=1)
    return re.sub(r"(^featured:.*$)", new_block + "\n\\1", text, count=1, flags=re.MULTILINE)


def set_featured_true(text):
    return re.sub(
        r"^featured:\s*(false|fasle|true)\s*$",
        "featured: true",
        text,
        count=1,
        flags=re.MULTILINE,
    )


def main():
    if not PUB.exists():
        raise SystemExit("Could not find " + str(PUB) + ". Run this from the repo root.")
    edited = 0
    for folder, tags in TAGS.items():
        path = PUB / folder / "index.md"
        if not path.exists():
            print("  skip  - " + folder + " (not found)")
            continue
        original = path.read_text(encoding="utf-8")
        updated = set_featured_true(replace_tags_block(original, tags))
        if updated != original:
            path.write_text(updated, encoding="utf-8")
            edited += 1
            print("  ok    - " + folder)
        else:
            print("  =     - " + folder + " (already polished)")
    print("\nDone. " + str(edited) + " file(s) updated.")


if __name__ == "__main__":
    main()
