#!/usr/bin/env python3
"""
NLB Prishtina — Combine Modules 1-3 into a single tabbed HTML dashboard
"""
import re, sys
sys.stdout.reconfigure(encoding='utf-8')

def extract_parts(filepath):
    """Extract CSS (inside <style>), body content (inside <body>), and JS (inside <script> after body content)."""
    with open(filepath, encoding='utf-8') as f:
        html = f.read()

    # Extract all <style> content
    styles = re.findall(r'<style[^>]*>(.*?)</style>', html, re.DOTALL)
    css = '\n'.join(styles)

    # Extract body content (between <body> and </body>)
    body_match = re.search(r'<body[^>]*>(.*?)</body>', html, re.DOTALL)
    body = body_match.group(1) if body_match else ''

    # Extract script blocks that are AFTER the body content (inline JS, not CDN)
    # Get all scripts that don't have src attribute
    scripts = re.findall(r'<script>([^<].*?)</script>', html, re.DOTALL)
    js = '\n'.join(scripts)

    # Remove the header from body (we'll use a unified header)
    body = re.sub(r'<div class="header">.*?</div>\s*</div>', '', body, count=1, flags=re.DOTALL)

    return css, body, js

print("Reading Module 1...")
css1, body1, js1 = extract_parts('Module1_Market_Share.html')
print(f"  CSS: {len(css1)} chars, Body: {len(body1)} chars, JS: {len(js1)} chars")

print("Reading Module 2...")
css2, body2, js2 = extract_parts('Module2_Product_Mix.html')
print(f"  CSS: {len(css2)} chars, Body: {len(body2)} chars, JS: {len(js2)} chars")

print("Reading Module 3...")
css3, body3, js3 = extract_parts('Module3_Staff_Efficiency.html')
print(f"  CSS: {len(css3)} chars, Body: {len(body3)} chars, JS: {len(js3)} chars")

# Namespace the CSS to avoid conflicts
# Each module's content will be inside a div with id="module1", "module2", "module3"
# We need to scope some CSS rules

# For Module 1, the CSS uses full class names (not minified shorthand)
# For Modules 2 & 3, the CSS is similar (shared design system)
# We'll use the Module 3 CSS as the base (most complete), then add unique Module 1/2 rules

combined_html = f'''<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>NLB Prishtina — Branch Intelligence Dashboard</title>
<script src="https://cdn.jsdelivr.net/npm/chart.js@4.4.1/dist/chart.umd.min.js"></script>
<script src="https://cdn.jsdelivr.net/npm/chartjs-plugin-annotation@3.0.1/dist/chartjs-plugin-annotation.min.js"></script>
<style>
@import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700;800&display=swap');
:root {{
  --navy:#002B49;--navy-light:#003d66;--steel:#4A6FA5;--charcoal:#1A1A2E;
  --white:#FFF;--bg:#F7F8FA;--bg-card:#FFF;--border:#E2E8F0;
  --text:#1A1A2E;--text-sec:#64748B;--text-secondary:#64748B;
  --green:#059669;--green-bg:#ECFDF5;--amber:#D97706;--amber-bg:#FFFBEB;
  --red:#DC2626;--red-bg:#FEF2F2;--blue-bg:#EFF6FF;--teal:#0D9488;--teal-bg:#F0FDFA;
  --font:'Inter','Segoe UI',system-ui,-apple-system,sans-serif;
  --shadow:0 1px 3px rgba(0,0,0,.08);--shadow-lg:0 4px 16px rgba(0,0,0,.10);--radius:8px;
}}
*{{margin:0;padding:0;box-sizing:border-box}}
body{{font-family:var(--font);background:var(--bg);color:var(--text);line-height:1.6;-webkit-font-smoothing:antialiased}}

/* ============ UNIFIED HEADER ============ */
.master-header{{background:var(--navy);color:#fff;padding:0;position:sticky;top:0;z-index:200;box-shadow:0 2px 12px rgba(0,0,0,.2)}}
.master-header-top{{display:flex;align-items:center;justify-content:space-between;padding:16px 40px}}
.master-header-top .logo{{background:#fff;color:var(--navy);font-weight:800;font-size:20px;padding:6px 16px;border-radius:4px;letter-spacing:1px}}
.master-header-top h1{{font-size:20px;font-weight:700;margin-left:20px;letter-spacing:-.3px}}
.master-header-top .header-meta{{font-size:12px;opacity:.7}}
.master-header-top .badge{{background:rgba(255,255,255,.12);padding:5px 14px;border-radius:20px;font-size:11px;font-weight:500}}

/* ============ TAB NAV ============ */
.tab-nav{{display:flex;gap:0;padding:0 40px;background:rgba(0,0,0,.15)}}
.tab-btn{{padding:12px 28px;font-size:13px;font-weight:600;color:rgba(255,255,255,.6);cursor:pointer;border:none;background:none;font-family:var(--font);letter-spacing:-.2px;border-bottom:3px solid transparent;transition:all .2s}}
.tab-btn:hover{{color:rgba(255,255,255,.9);background:rgba(255,255,255,.05)}}
.tab-btn.active{{color:#fff;border-bottom-color:#fff;background:rgba(255,255,255,.08)}}
.tab-btn .tab-num{{display:inline-block;background:rgba(255,255,255,.15);padding:1px 7px;border-radius:10px;font-size:10px;margin-right:6px}}
.tab-btn.active .tab-num{{background:rgba(255,255,255,.25)}}

/* ============ MODULE PANELS ============ */
.module-panel{{display:none}}
.module-panel.active{{display:block}}

/* ============ SHARED STYLES (all modules) ============ */
.container{{max-width:1520px;margin:0 auto;padding:32px 40px}}
.section-title{{font-size:22px;font-weight:700;color:var(--navy);margin:40px 0 8px;letter-spacing:-.5px}}
.section-title:first-of-type{{margin-top:0}}
.section-sub{{font-size:14px;color:var(--text-sec);margin-bottom:24px;max-width:900px;line-height:1.7}}
.kpi-row{{display:grid;grid-template-columns:repeat(auto-fit,minmax(200px,1fr));gap:16px;margin-bottom:32px}}
.kpi-card{{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:20px 24px;box-shadow:var(--shadow);transition:box-shadow .2s}}
.kpi-card:hover{{box-shadow:var(--shadow-lg)}}
.kpi-label{{font-size:11px;font-weight:600;text-transform:uppercase;letter-spacing:.8px;color:var(--text-sec);margin-bottom:8px}}
.kpi-value{{font-size:28px;font-weight:800;color:var(--navy);letter-spacing:-1px}}
.kpi-context{{font-size:12px;color:var(--text-sec);margin-top:4px}}
.kpi-card.green{{border-left:4px solid var(--green)}}
.kpi-card.amber{{border-left:4px solid var(--amber)}}
.kpi-card.red{{border-left:4px solid var(--red)}}
.kpi-card.navy{{border-left:4px solid var(--navy)}}
.kpi-card.teal{{border-left:4px solid var(--teal)}}
.chart-container,.chart-panel{{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px;margin-bottom:32px;box-shadow:var(--shadow)}}
.chart-title,.chart-panel h3{{font-size:15px;font-weight:700;color:var(--navy);margin-bottom:4px}}
.chart-sub,.chart-panel .chart-sub{{font-size:12px;color:var(--text-sec);margin-bottom:16px}}
.chart-note{{font-size:11px;color:var(--text-sec);margin-top:12px;font-style:italic;border-top:1px solid var(--border);padding-top:10px}}
.two-charts,.two-col{{display:grid;grid-template-columns:1fr 1fr;gap:24px}}
@media(max-width:1100px){{.two-charts,.two-col{{grid-template-columns:1fr}}}}
table{{width:100%;border-collapse:collapse;font-size:12px}}
th{{background:var(--navy);color:#fff;padding:10px 12px;text-align:left;font-weight:600;font-size:11px;text-transform:uppercase;letter-spacing:.5px;position:sticky;top:100px;z-index:10}}
td{{padding:8px 12px;border-bottom:1px solid var(--border);white-space:nowrap}}
tr:hover{{background:var(--blue-bg)}}
.tbl-wrap{{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);overflow:auto;max-height:700px;box-shadow:var(--shadow);margin-bottom:32px}}
.cell-g{{background:#ECFDF5;color:#059669;font-weight:600;text-align:center;border-radius:3px}}
.cell-a{{background:#FFFBEB;color:#D97706;font-weight:600;text-align:center;border-radius:3px}}
.cell-r{{background:#FEF2F2;color:#DC2626;font-weight:600;text-align:center;border-radius:3px}}
.cell-n{{text-align:center;color:var(--text-sec)}}
.tag{{display:inline-block;padding:2px 8px;border-radius:10px;font-size:10px;font-weight:600}}
.tag-green{{background:#ECFDF5;color:#059669}}.tag-amber{{background:#FFFBEB;color:#D97706}}.tag-red{{background:#FEF2F2;color:#DC2626}}.tag-navy{{background:#EFF6FF;color:#002B49}}.tag-teal{{background:#F0FDFA;color:#0D9488}}
.callout{{border-radius:var(--radius);padding:20px 24px;margin-bottom:24px;border-left:4px solid}}
.callout-red{{background:var(--red-bg);border-color:var(--red)}}.callout-amber{{background:var(--amber-bg);border-color:var(--amber)}}.callout-green{{background:var(--green-bg);border-color:var(--green)}}.callout-navy{{background:var(--blue-bg);border-color:var(--navy)}}
.callout h4{{font-size:14px;font-weight:700;margin-bottom:6px}}
.callout p{{font-size:13px;color:var(--text-sec);line-height:1.6}}
.filter-bar{{display:flex;gap:8px;margin-bottom:20px;flex-wrap:wrap}}
.filter-btn{{padding:6px 16px;border:1px solid var(--border);background:var(--bg-card);border-radius:20px;font-size:12px;font-weight:500;cursor:pointer;transition:all .2s;font-family:var(--font)}}
.filter-btn:hover,.filter-btn.active{{background:var(--navy);color:#fff;border-color:var(--navy)}}
.exec-msg{{background:var(--navy);color:#fff;padding:20px 28px;border-radius:var(--radius);margin-bottom:32px;font-size:15px;line-height:1.7}}
.exec-msg strong{{font-weight:700}}
.part-banner{{background:var(--navy);color:#fff;padding:18px 28px;border-radius:var(--radius);margin:48px 0 24px;font-size:16px;font-weight:700;letter-spacing:-.3px;display:flex;align-items:center;gap:12px}}
.part-banner .num{{background:rgba(255,255,255,.2);padding:4px 12px;border-radius:4px;font-size:13px;font-weight:600}}
.link-badge{{display:inline-flex;align-items:center;gap:6px;padding:4px 12px;border-radius:12px;font-size:11px;font-weight:600;margin:2px}}
.link-m1{{background:#EFF6FF;color:#002B49}}.link-m2{{background:#F0FDFA;color:#0D9488}}
.method-box{{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:24px 28px;margin-top:40px;box-shadow:var(--shadow)}}
.method-box h3{{font-size:15px;font-weight:700;color:var(--navy);margin-bottom:12px}}
.method-box p,.method-box li{{font-size:13px;color:var(--text-sec);line-height:1.7}}
.method-box ul{{padding-left:20px;margin-top:8px}}
canvas{{max-height:420px}}

/* ============ MODULE 1 SPECIFIC ============ */
#module1 .city-card{{background:var(--bg-card);border:1px solid var(--border);border-radius:var(--radius);padding:16px 20px;box-shadow:var(--shadow)}}
#module1 .city-card h4{{font-size:13px;font-weight:700;color:var(--navy);margin-bottom:4px}}
#module1 .prishtina-box{{background:linear-gradient(135deg,#EFF6FF,#F0FDFA);border:2px solid var(--steel);border-radius:var(--radius);padding:24px;margin-bottom:32px}}
#module1 .prishtina-box h3{{color:var(--navy);font-size:16px;margin-bottom:8px}}
#module1 .prishtina-box p{{font-size:13px;color:var(--text-sec)}}

/* ============ FOOTER ============ */
.master-footer{{background:var(--navy);color:rgba(255,255,255,.5);padding:20px 40px;text-align:center;font-size:11px;margin-top:60px}}
</style>
</head>
<body>

<!-- ============ UNIFIED HEADER ============ -->
<div class="master-header">
  <div class="master-header-top">
    <div style="display:flex;align-items:center">
      <div class="logo">NLB</div>
      <h1>Branch Intelligence Dashboard</h1>
    </div>
    <div style="display:flex;align-items:center;gap:16px">
      <span class="header-meta">NLB Prishtina | 35 Outlets | 265 FTE | 31 Benchmarked</span>
      <span class="badge">Modules 1-3</span>
    </div>
  </div>
  <div class="tab-nav">
    <button class="tab-btn active" onclick="switchModule(1)"><span class="tab-num">M1</span> Market Share</button>
    <button class="tab-btn" onclick="switchModule(2)"><span class="tab-num">M2</span> Product Mix & Funding</button>
    <button class="tab-btn" onclick="switchModule(3)"><span class="tab-num">M3</span> Staff Efficiency</button>
  </div>
</div>

<!-- ============ MODULE 1 ============ -->
<div class="module-panel active" id="module1">
{body1}
</div>

<!-- ============ MODULE 2 ============ -->
<div class="module-panel" id="module2">
{body2}
</div>

<!-- ============ MODULE 3 ============ -->
<div class="module-panel" id="module3">
{body3}
</div>

<div class="master-footer">
  NLB Prishtina — Branch Network Transformation | Branch Intelligence Dashboard | Modules 1-3 | Confidential — For Management Use Only
</div>

<script>
// ============================================================
// TAB SWITCHING — destroy & recreate charts on module switch
// ============================================================
let currentModule = 1;
let chartsInitialized = {{1: false, 2: false, 3: false}};

function switchModule(n) {{
  // Hide all panels
  document.querySelectorAll('.module-panel').forEach(p => p.classList.remove('active'));
  document.querySelectorAll('.tab-btn').forEach(b => b.classList.remove('active'));

  // Show selected
  document.getElementById('module' + n).classList.add('active');
  document.querySelectorAll('.tab-btn')[n-1].classList.add('active');

  // Initialize charts on first visit
  if (!chartsInitialized[n]) {{
    chartsInitialized[n] = true;
    if (n === 1) initModule1();
    else if (n === 2) initModule2();
    else if (n === 3) initModule3();
  }}

  currentModule = n;
  window.scrollTo(0, 0);
}}

// ============================================================
// MODULE 1 — MARKET SHARE
// ============================================================
function initModule1() {{
{js1}
}}

// ============================================================
// MODULE 2 — PRODUCT MIX
// ============================================================
function initModule2() {{
{js2}
}}

// ============================================================
// MODULE 3 — STAFF EFFICIENCY
// ============================================================
function initModule3() {{
{js3}
}}

// Initialize Module 1 on load
chartsInitialized[1] = true;
initModule1();
</script>
</body>
</html>
'''

# Write combined file
outfile = 'NLB_Branch_Intelligence_v2.html'
with open(outfile, 'w', encoding='utf-8') as f:
    f.write(combined_html)

import os
size = os.path.getsize(outfile)
print(f"\nSaved: {outfile}")
print(f"Size: {size:,} bytes ({size/1024:.0f} KB)")
