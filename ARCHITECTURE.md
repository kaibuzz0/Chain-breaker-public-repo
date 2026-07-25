# System Architecture

How Chain-Breaker works.

## Overview

Chain-Breaker is a distributed scripture preservation system using:
- 50KB file sharding
- SHA-256 hashing
- DHT (Distributed Hash Table)
- Gossip protocol
- E8 quantum-resistant commitments

## Components

1. **Shard Manager** - Splits files into 50KB pieces
2. **DHT Node** - Distributed hash table for discovery
3. **Gossip Protocol** - Network communication
4. **Retrieval System** - Reassembles documents
5. **E8 Engine** - Quantum-resistant signatures

## Data Flow

```
PDF → Shards (50KB) → Hashes → DHT → Network → 5x Replication
```

## Network

- P2P (Peer-to-Peer)
- No central server
- Automatic redundancy
- Censorship resistant
