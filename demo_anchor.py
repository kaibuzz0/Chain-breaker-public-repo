#!/usr/bin/env python3
"""
Chain-Breaker Demo: Document Anchoring

Demonstrates how documents are anchored to blockchain
for proof of existence.

Run: python demo_anchor.py --file example.txt
"""

import argparse
import hashlib
import json
import time
from pathlib import Path


class DemoDocumentAnchor:
    """
    Demonstrate document anchoring without exposing
    actual blockchain implementation.
    """
    
    def __init__(self):
        self.anchors = []
    
    def hash_file(self, filepath: str) -> str:
        """
        Generate SHA-256 hash of file.
        
        This hash serves as the document fingerprint.
        Any change to file changes hash.
        """
        path = Path(filepath)
        if not path.exists():
            raise FileNotFoundError(f"File not found: {filepath}")
        
        sha256_hash = hashlib.sha256()
        
        # Read in chunks for large files
        with open(path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        
        return sha256_hash.hexdigest()
    
    def anchor_to_blockchain(self, file_hash: str, filename: str) -> dict:
        """
        Simulate anchoring hash to blockchain.
        
        In real Chain-Breaker, this would:
        1. Create transaction with file_hash
        2. Mine block
        3. Propagate to network
        """
        # Simulate mining
        print("⛏️  Mining anchor block...")
        time.sleep(1)  # Simulate work
        
        block_hash = hashlib.sha256(
            f"{file_hash}:{time.time()}".encode()
        ).hexdigest()
        
        anchor = {
            'document_hash': file_hash,
            'filename': filename,
            'block_hash': block_hash,
            'block_height': len(self.anchors) + 1,
            'timestamp': time.time(),
            'status': 'confirmed'
        }
        
        self.anchors.append(anchor)
        return anchor
    
    def verify_existence(self, filepath: str, anchor: dict) -> bool:
        """
        Verify document matches anchored hash.
        
        This proves document existed at anchor time.
        """
        current_hash = self.hash_file(filepath)
        return current_hash == anchor['document_hash']
    
    def generate_certificate(self, anchor: dict) -> str:
        """Generate proof certificate."""
        return f"""
╔══════════════════════════════════════════════════════════════╗
║           CHAIN-BREAKER PROOF OF EXISTENCE                   ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  Document: {anchor['filename'][:40]:<50}║
║  Hash: {anchor['document_hash'][:56]}║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║  Anchored to Blockchain                                      ║
║  Block Height: {anchor['block_height']:<45}║
║  Block Hash: {anchor['block_hash'][:52]}  ║
║  Timestamp: {anchor['timestamp']:<46}║
║                                                              ║
╠══════════════════════════════════════════════════════════════╣
║                                                              ║
║  This certifies the document existed at the stated time.   ║
║  The hash cannot be forged or altered.                     ║
║                                                              ║
║  Verification: Re-hash document, compare to stored hash.    ║
║                                                              ║
╚══════════════════════════════════════════════════════════════╝
"""


def main():
    parser = argparse.ArgumentParser(
        description='Demo: Anchor document to blockchain'
    )
    parser.add_argument('--file', required=True, help='File to anchor')
    parser.add_argument('--verify', action='store_true', 
                       help='Verify anchored document')
    args = parser.parse_args()
    
    print("=" * 70)
    print("📜 Chain-Breaker Demo: Document Anchoring")
    print("=" * 70)
    print()
    
    anchor = DemoDocumentAnchor()
    
    if args.verify:
        # Verify existing anchor (simplified demo)
        print("🔍 Verification Mode")
        print(f"   File: {args.file}")
        print()
        print("   (In real usage, would query blockchain)")
        return
    
    # Hash file
    print(f"1️⃣ Reading file: {args.file}")
    try:
        file_hash = anchor.hash_file(args.file)
        size = Path(args.file).stat().st_size
        print(f"   ✅ File size: {size:,} bytes")
        print(f"   🔐 SHA-256: {file_hash}")
        print()
    except FileNotFoundError as e:
        print(f"   ❌ Error: {e}")
        return
    
    # Anchor
    print("2️⃣ Anchoring to blockchain...")
    result = anchor.anchor_to_blockchain(file_hash, args.file)
    print(f"   ✅ Anchored at block #{result['block_height']}")
    print(f"   ⛏️  Block hash: {result['block_hash'][:40]}...")
    print(f"   🕐 Timestamp: {result['timestamp']}")
    print()
    
    # Certificate
    print("3️⃣ Proof Certificate:")
    print(anchor.generate_certificate(result))
    
    # Verification
    print("4️⃣ Verification:")
    print("   Anyone can verify this document:")
    print("   1. Recompute SHA-256 of document")
    print("   2. Compare to anchored hash")
    print("   3. If match → document is authentic")
    print()
    
    # Test verification
    is_valid = anchor.verify_existence(args.file, result)
    print(f"   Self-verification: {'✅ PASS' if is_valid else '❌ FAIL'}")
    
    print()
    print("=" * 70)
    print("✅ Document anchored successfully!")
    print("=" * 70)


if __name__ == "__main__":
    main()
