#!/usr/bin/env python3
"""
Test runner to see if we can patch each file cleanly or run an integrated generator.
"""
import os, sys, re, glob
import xml.etree.ElementTree as ET

PUBLIC_DIR = os.path.join(os.getcwd(), "public")
print(f"Target Public Dir: {PUBLIC_DIR}")
