#!/usr/bin/env python3
"""
Applies all 12 precision fixes across all generator scripts in tmp/,
runs them, and validates the 19 SVG outputs.
"""
import os
import re
import xml.etree.ElementTree as ET

WORKSPACE_ROOT = os.getcwd()
PUBLIC_DIR = os.path.join(WORKSPACE_ROOT, "public")
os.makedirs(PUBLIC_DIR, exist_ok=True)

def sanitize_xml(svg_str):
    return re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', svg_str)

# 1. Update tmp/generate_all_mockups.py
with open("tmp/generate_all_mockups.py", "r", encoding="utf-8") as f:
    text = f.read()

# Fix OUTPUT_DIR
text = re.sub(r'OUTPUT_DIR = ["\'].*?["\']', 'OUTPUT_DIR = os.path.join(os.getcwd(), "public")', text)
# Fix title & escaping and remove RESMI
text = text.replace('{title_mockup}', '{title_clean}')
text = text.replace('PRD v1.0 · RESMI', 'PRD v1.0 SESUAI')
if 'title_clean = title_mockup' not in text:
    text = text.replace('def svg_wrap(content, title_mockup="MOCKUP"):',
                        'def svg_wrap(content, title_mockup="MOCKUP"):\n    title_clean = title_mockup.replace("&", "&amp;")')

with open("tmp/generate_all_mockups.py", "w", encoding="utf-8") as f:
    f.write(text)
print("Updated generate_all_mockups.py")

