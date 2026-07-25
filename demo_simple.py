#!/usr/bin/env python3
"""Chain-Breaker Simple Demo"""

import hashlib

def main():
    print("="*60)
    print("  CHAIN-BREAKER DEMO")
    print("="*60)
    
    # Demo hashing
    text = b"In the beginning was the Word..."
    hash_result = hashlib.sha256(text).hexdigest()
    
    print(f"\nInput: {text}")
    print(f"SHA-256 Hash: {hash_result}")
    print(f"\nThis is how Chain-Breaker protects every 50KB shard!")
    print("="*60)

if __name__ == "__main__":
    main()
