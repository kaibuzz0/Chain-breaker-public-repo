# Chain-Breaker Blockchain

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

> **Mobile-Optimized Blockchain for Document Preservation**

A lightweight, quantum-resistant blockchain designed for mobile devices and personal document collections.

---

## 🎯 What is Chain-Breaker?

Chain-Breaker is a minimal blockchain that:
- **Preserves documents** with cryptographic proof of existence
- **Runs on mobile** (Android/Termux, Raspberry Pi)
- **Uses post-quantum cryptography** (future-proof)
- **Syncs peer-to-peer** without centralized servers

---

## 🚀 Quick Start

### Installation

```bash
# Clone repository
git clone https://github.com/kaibuzz0/Chain-breaker-public-repo.git
cd Chain-breaker-public-repo

# Install dependencies
pip install -r requirements.txt

# Run demo
python demo.py
```

### Termux (Android)

```bash
pkg install python python-numpy
pip install ecdsa
python demo.py
```

---

## 🎮 Demo Scripts

### Demo 1: Basic Blockchain (`demo_basic.py`)

```bash
python demo_basic.py
```

Creates a blockchain, mines blocks, displays chain.

**Output:**
```
🎉 Demo: Basic Blockchain
━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━
⛏️  Mining genesis block...
✅ Genesis mined: 0a3f8b2e...
   Height: 1

📦 Block 1: 0a3f8b2e...
   Timestamp: 1699123456
   Hash: 0a3f8b2e...
   Previous: 00000000...

⛏️  Mining block 2...
✅ Mined: 7c9d4e1a...
   Height: 2
   Time: 2.3s

📊 Chain Statistics:
   Height: 2
   Total work: 48 bits
```

---

### Demo 2: P2P Network (`demo_network.py`)

Run in **two separate terminals:**

```bash
# Terminal 1 - Node A
python demo_network.py --port 8333 --mine

# Terminal 2 - Node B  
python demo_network.py --port 8334 --connect 127.0.0.1:8333
```

**What happens:**
- Node A mines blocks
- Node B connects and syncs
- Blocks propagate automatically
- Network stats display

---

### Demo 3: Document Anchoring (`demo_anchor.py`)

```bash
python demo_anchor.py --file my-document.pdf
```

**Output:**
```
📄 Document: my-document.pdf
   Size: 2.4 MB
   
🔐 Hash: a7f3c9d2...
   Algorithm: SHA-256

⛏️  Anchoring to blockchain...
✅ Anchored at block #42
   Timestamp: 2024-01-15 14:32:18 UTC
   
📜 Proof of Existence:
   Document hash: a7f3c9d2...
   Block hash: 9e8d7c6b...
   Block height: 42
   
   This proves the document existed at this timestamp.
   The hash cannot be forged or altered.
```

---

## 📱 Mobile Demo

### Single Device
```bash
python demo_mobile.py --mode full
```

Runs complete blockchain on your phone.

### Battery-Aware Mode
```bash
python demo_mobile.py --mode light --mine-when-charging
```

Only mines when plugged in.

---

## 🔐 Security Features

| Feature | Benefit |
|---------|---------|
| **Post-Quantum** | Resistant to quantum computer attacks |
| **Hybrid Signatures** | ECDSA + quantum-safe commitment |
| **Peer-to-Peer** | No central point of failure |
| **Mobile-Optimized** | Runs on minimal hardware |

---

## 📊 Performance

| Metric | Value |
|--------|-------|
| Block time | ~5 minutes (mobile-friendly) |
| Block size | 256 KB |
| Storage | 50MB - 2GB (configurable) |
| Sync time | ~2s per 100 blocks |

Tested on:
- ✅ Android (Termux)
- ✅ Raspberry Pi 4
- ✅ Linux desktop
- ✅ Windows

---

## 🧪 Testing

```bash
# Run all demos
python test_all.py

# Run specific demo
python demo_basic.py
python demo_network.py
python demo_anchor.py
```

---

## 📚 Learn More

- **Whitepaper:** See `docs/WHITEPAPER.md`
- **API Reference:** See `docs/API.md`
- **Architecture:** See `docs/ARCHITECTURE.md`

---

## 🤝 Contributing

This is a personal research project. For the full implementation, see the private repository.

---

## 📝 License

MIT License - See LICENSE file

---

> **Note:** This is the public demo repository. Core cryptography implementation is private.