#!/usr/bin/env python3
"""
Run all public demos.
"""

import subprocess
import sys

DEMOS = [
    ('Basic Blockchain', 'demo_basic.py'),
    ('Document Anchoring', 'demo_anchor.py --file README.md'),
    ('Mobile Mode', 'demo_mobile.py --mode light'),
]

print("=" * 70)
print("🧪 Chain-Breaker Public Demo Suite")
print("=" * 70)
print()

for name, cmd in DEMOS:
    print(f"\n📦 Running: {name}")
    print("-" * 70)
    try:
        result = subprocess.run(
            f"python {cmd}",
            shell=True,
            capture_output=False,
            timeout=30
        )
        if result.returncode == 0:
            print(f"✅ {name} completed")
        else:
            print(f"❌ {name} failed")
    except Exception as e:
        print(f"⚠️  {name} error: {e}")

print()
print("=" * 70)
print("🎉 All demos completed!")
print("=" * 70)
