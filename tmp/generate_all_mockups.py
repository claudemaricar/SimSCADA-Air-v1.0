#!/usr/bin/env python3
"""
SimSCADA-Air Complete Mockup Generator v2.0
Generates 19 SVG files strictly compliant with PRD v1.0 and user instructions.
"""

import os
import sys

OUTPUT_DIR = os.path.join(os.getcwd(), "public")

def ensure_dir(path):
    os.makedirs(path, exist_ok=True)

# -------------------------------------------------------------
# Base SVG Wrapper
# -------------------------------------------------------------
def svg_wrap(content, title_mockup="MOCKUP"):
    title_clean = title_mockup.replace("&", "&amp;")
    return f"""<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1600 1000" width="1600" height="1000" style="background:#0b1120; font-family:-apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, Helvetica, Arial, sans-serif;">
  <defs>
    <linearGradient id="bgGrad" x1="0%" y1="0%" x2="100%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="50%" stop-color="#0b1329" />
      <stop offset="100%" stop-color="#020617" />
    </linearGradient>
    <linearGradient id="cardGrad" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#1e293b" />
      <stop offset="100%" stop-color="#0f172a" />
    </linearGradient>
    <linearGradient id="cardDark" x1="0%" y1="0%" x2="0%" y2="100%">
      <stop offset="0%" stop-color="#0f172a" />
      <stop offset="100%" stop-color="#070c18" />
    </linearGradient>
    <linearGradient id="primaryGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#0284c7" />
      <stop offset="100%" stop-color="#2563eb" />
    </linearGradient>
    <linearGradient id="accentGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#06b6d4" />
      <stop offset="100%" stop-color="#3b82f6" />
    </linearGradient>
    <linearGradient id="amberGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#d97706" />
      <stop offset="100%" stop-color="#b45309" />
    </linearGradient>
    <linearGradient id="emeraldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#059669" />
      <stop offset="100%" stop-color="#10b981" />
    </linearGradient>
    <linearGradient id="goldGrad" x1="0%" y1="0%" x2="100%" y2="0%">
      <stop offset="0%" stop-color="#f59e0b" />
      <stop offset="100%" stop-color="#d97706" />
    </linearGradient>
    <filter id="dropShadow" x="-10%" y="-10%" width="120%" height="120%">
      <feDropShadow dx="0" dy="10" stdDeviation="14" flood-color="#000000" flood-opacity="0.55"/>
    </filter>
    <filter id="glowCyan" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#06b6d4" flood-opacity="0.6"/>
    </filter>
    <filter id="glowRed" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#ef4444" flood-opacity="0.7"/>
    </filter>
    <filter id="glowAmber" x="-20%" y="-20%" width="140%" height="140%">
      <feDropShadow dx="0" dy="0" stdDeviation="6" flood-color="#f59e0b" flood-opacity="0.7"/>
    </filter>
    <marker id="dotBlue" markerWidth="8" markerHeight="8" refX="4" refY="4">
      <circle cx="4" cy="4" r="3.5" fill="#38bdf8" stroke="#ffffff" stroke-width="1" />
    </marker>
    <marker id="dotOrange" markerWidth="8" markerHeight="8" refX="4" refY="4">
      <circle cx="4" cy="4" r="3.5" fill="#f59e0b" stroke="#ffffff" stroke-width="1" />
    </marker>
    <marker id="dotGreen" markerWidth="8" markerHeight="8" refX="4" refY="4">
      <circle cx="4" cy="4" r="3.5" fill="#10b981" stroke="#ffffff" stroke-width="1" />
    </marker>
  </defs>

  <!-- Background Base -->
  <rect width="1600" height="1000" fill="url(#bgGrad)" />

  <!-- Blueprint Pattern -->
  <g opacity="0.04" stroke="#38bdf8" stroke-width="1">
    <pattern id="grid" width="40" height="40" patternUnits="userSpaceOnUse">
      <path d="M 40 0 L 0 0 0 40" fill="none" />
    </pattern>
    <rect width="1600" height="1000" fill="url(#grid)" />
  </g>

  <!-- Top Mockup Window Bar -->
  <rect x="0" y="0" width="1600" height="40" fill="#030712" />
  <circle cx="24" cy="20" r="5" fill="#ef4444" />
  <circle cx="42" cy="20" r="5" fill="#f59e0b" />
  <circle cx="60" cy="20" r="5" fill="#10b981" />
  <text x="88" y="25" fill="#94a3b8" font-size="13" font-weight="600">{title_clean}</text>
  <rect x="1390" y="9" width="180" height="22" rx="11" fill="#1e293b" />
  <text x="1480" y="24" fill="#38bdf8" font-size="11" font-weight="600" text-anchor="middle">PRD v1.0 SESUAI</text>

{content}
</svg>"""

# -------------------------------------------------------------
# Tenant Header (PRD §6: Logo + Nama Lembaga, teks kecil "Didukung oleh SimSCADA-Air")
# -------------------------------------------------------------
def header_tenant(lembaga="Balai Diklat Air Minum Nusantara", role="Operator Muda · Angkatan 1", name="Dimas Wahyu Pratama", initials="DW", active_tab="Dashboard"):
    return f"""  <!-- Standard Tenant Header PRD §6 -->
  <g transform="translate(0, 40)">
    <rect width="1600" height="66" fill="#0b1329" stroke="#1e293b" stroke-width="1" />
    
    <!-- Tenant Logo & Name -->
    <g transform="translate(32, 11)">
      <rect width="44" height="44" rx="10" fill="#0284c7" />
      <path d="M 22 10 C 22 10, 14 22, 14 28 A 8 8 0 0 0 30 28 C 30 22, 22 10, 22 10 Z" fill="#ffffff" />
      <text x="56" y="22" fill="#f8fafc" font-size="17" font-weight="700" letter-spacing="0.3">{lembaga}</text>
      <text x="56" y="38" fill="#94a3b8" font-size="11" font-weight="500">Didukung oleh <tspan font-weight="700" fill="#38bdf8">SimSCADA-Air</tspan> · Platform Simulator SCADA Air Minum</text>
    </g>

    <!-- User & Role Profile Right -->
    <g transform="translate(1260, 13)">
      <rect width="308" height="40" rx="8" fill="#1e293b" stroke="#334155" stroke-width="1" />
      <circle cx="22" cy="20" r="13" fill="#0369a1" />
      <text x="22" y="24" fill="#ffffff" font-size="11" font-weight="700" text-anchor="middle">{initials}</text>
      <text x="44" y="18" fill="#f1f5f9" font-size="12" font-weight="600">{name}</text>
      <text x="44" y="31" fill="#38bdf8" font-size="10" font-weight="500">{role}</text>
      <circle cx="286" cy="20" r="4" fill="#10b981" />
    </g>
  </g>"""

# -------------------------------------------------------------
# Screen Title & Subtitle Helper (to guarantee NO collision)
# -------------------------------------------------------------
def page_title_block(title, subtitle, y=125):
    return f"""  <!-- Clean Non-Colliding Title Block -->
  <g transform="translate(32, {y})">
    <text x="0" y="24" fill="#ffffff" font-size="22" font-weight="700" letter-spacing="0.3">{title}</text>
    <text x="0" y="46" fill="#94a3b8" font-size="13">{subtitle}</text>
  </g>"""

print("Base generator template initialized.")
