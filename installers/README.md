# Windows Installers

Quick Windows installation for Chain-Breaker.

---

## 🚀 Quick Start

### Option 1: Easy Install (Recommended)

1. **Download** `ChainBreaker-Setup.bat`
2. **Right-click** → "Run as Administrator"
3. **Follow prompts**
4. Done! ✅

**What it does:**
- Auto-downloads Python if missing
- Downloads Chain-Breaker from GitHub
- Creates shortcuts
- Sets up everything

---

### Option 2: Build .exe Installer

For a professional installer:

1. Download `installer.nsi`
2. Install NSIS from https://nsis.sourceforge.io/
3. Right-click `installer.nsi` → "Compile NSIS Script"
4. Get `ChainBreaker-Setup.exe`

---

## 📁 Files

| File | Purpose |
|------|---------|
| **ChainBreaker-Setup.bat** | Main installer script |
| **quick-install.bat** | Fast install (requires Python) |
| **installer.nsi** | NSIS script for .exe |
| **ChainBreaker.spec** | PyInstaller for standalone app |

---

## ⚠️ Requirements

- Windows 10 or 11 (64-bit)
- Internet connection
- Administrator rights (for main installer)

---

## 🗑️ Uninstall

Run the uninstaller from:
- Start Menu → Chain-Breaker → Uninstall
- Or delete `C:\Program Files\Chain-Breaker\`

---

**Note:** For full 73-text version, install from private repository or request access.
