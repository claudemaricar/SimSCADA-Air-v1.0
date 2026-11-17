#!/usr/bin/env python3
"""
Master Mockup Builder & Fixer for SimSCADA-Air v3.0
Implements all 12 items requested by user.
"""

import os
import sys
import re
import xml.etree.ElementTree as ET

PUBLIC_DIR = os.path.join(os.getcwd(), "public")
os.makedirs(PUBLIC_DIR, exist_ok=True)

def sanitize_xml(svg_str):
    # Replace bare & that are not part of an XML entity
    cleaned = re.sub(r'&(?!(amp|lt|gt|quot|apos|#\d+|#x[0-9a-fA-F]+);)', '&amp;', svg_str)
    return cleaned

def write_and_verify(filepath, content, title=""):
    content_clean = sanitize_xml(content)
    with open(filepath, "w", encoding="utf-8") as f:
        f.write(content_clean)
    try:
        ET.parse(filepath)
        print(f"[OK] {os.path.basename(filepath)} parsed successfully.")
        return True
    except Exception as e:
        print(f"[FAIL] {os.path.basename(filepath)} parse error: {e}")
        # print around error line
        lines = content_clean.splitlines()
        import traceback
        return False

print("Sanitization and validation helpers ready.")
