#!/usr/bin/env python3
"""
Chain-Breaker Demo: Basic Blockchain

Demonstrates blockchain fundamentals without exposing
cryptographic internals.

Run: python demo_basic.py
"""

import hashlib
import json
import time
from dataclasses import dataclass
from typing import List, Optional


@dataclass
class DemoBlock:
    """Simplified block for demonstration."""
    index: int
    timestamp: float
    data: str
    previous_hash: str
    nonce: int = 0
    _hash: str = ""
    
    def calculate_hash(self) -> str:
        """Calculate block hash."""
        block_string = json.dumps({
            'index': self.index,
            'timestamp': self.timestamp,
            'data': self.data,
            'previous_hash': self.previous_hash,
            'nonce': self.nonce
        }, sort_keys=True)
        return hashlib.sha256(block_string.encode()).hexdigest()
    
    def hash(self) -> str:
        """Get or compute hash."""
        if not self._hash:
            self._hash = self.calculate_hash()
        return self._hash
    
    def mine(self, difficulty: int = 4):
        """Mine block (find nonce that produces hash with leading zeros)."""
        target = "0" * difficulty
        while not self.hash().startswith(target):
            self.nonce += 1
            self._hash = ""


class DemoBlockchain:
    """Simplified blockchain for demo purposes."""
    
    def __init__(self):
        self.chain: List[DemoBlock] = []
        self.difficulty = 4
        self._create_genesis()
    
    def _create_genesis(self):
        """Create genesis block."""
        genesis = DemoBlock(
            index=0,
            timestamp=time.time(),
            data="Genesis Block",
            previous_hash="0" * 64
        )
        genesis.mine(self.difficulty)
        self.chain.append(genesis)
    
    def add_block(self, data: str) -> DemoBlock:
        """Add new block to chain."""
        previous = self.chain[-1]
        
        block = DemoBlock(
            index=len(self.chain),
            timestamp=time.time(),
            data=data,
            previous_hash=previous.hash()
        )
        
        block.mine(self.difficulty)
        self.chain.append(block)
        return block
    
    def is_valid(self) -> bool:
        """Validate entire chain."""
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            previous = self.chain[i-1]
            
            if current.previous_hash != previous.hash():
                return False
            
            if not current.hash().startswith("0" * self.difficulty):
                return False
        
        return True
    
    def stats(self) -> dict:
        """Chain statistics."""
        return {
            'height': len(self.chain),
            'difficulty': self.difficulty,
            'is_valid': self.is_valid()
        }


def main():
    print("=" * 70)
    print("🎉 Chain-Breaker Demo: Basic Blockchain")
    print("=" * 70)
    print()
    
    # Create blockchain
    print("1️⃣ Creating blockchain...")
    blockchain = DemoBlockchain()
    print(f"   ✅ Genesis block mined: {blockchain.chain[0].hash()[:20]}...")
    print()
    
    # Display genesis
    print("2️⃣ Genesis Block:")
    genesis = blockchain.chain[0]
    print(f"   Index: {genesis.index}")
    print(f"   Timestamp: {int(genesis.timestamp)}")
    print(f"   Hash: {genesis.hash()[:40]}...")
    print(f"   Previous: {genesis.previous_hash[:20]}...")
    print(f"   Nonce: {genesis.nonce}")
    print()
    
    # Mine more blocks
    print("3️⃣ Mining additional blocks...")
    for i in range(3):
        block = blockchain.add_block(f"Block {i+1} data")
        print(f"   ⛏️  Block {block.index}: {block.hash()[:20]}... "
              f"(Nonce: {block.nonce})")
    print()
    
    # Display chain
    print("4️⃣ Blockchain:")
    print("-" * 70)
    for block in blockchain.chain:
        print(f"   #{block.index} | {block.hash()[:16]}... | "
              f"Prev: {block.previous_hash[:8]}... | Nonce: {block.nonce}")
    print()
    
    # Validate
    print("5️⃣ Validation:")
    is_valid = blockchain.is_valid()
    print(f"   Chain is valid: {is_valid}")
    print()
    
    # Stats
    print("6️⃣ Statistics:")
    stats = blockchain.stats()
    for key, value in stats.items():
        print(f"   {key}: {value}")
    
    print()
    print("=" * 70)
    print("✅ Demo complete!")
    print("=" * 70)
    print()
    print("This is a simplified demo. Real Chain-Breaker uses:")
    print("   • Post-quantum cryptography")
    print("   • E8 lattice-based hashing")
    print("   • P2P mesh networking")
    print("   • Mobile-optimized storage")


if __name__ == "__main__":
    main()
