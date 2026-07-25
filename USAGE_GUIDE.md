# Usage Guide

How to use Chain-Breaker.

## Quick Start

```bash
# List documents
python vault_cli.py --list

# Find specific text
python vault_cli.py --find "josephus"

# Verify vault
python vault_cli.py --verify
```

## Commands

### View Library
```bash
python vault_cli.py --list              # All documents
python vault_cli.py --list --category   # By category
python vault_cli.py --info "doc_id"     # Specific doc
```

### Start Node
```bash
python -m scripture_vault.distributed.node.vault_node
```

### Network Status
```bash
python vault_cli.py --status
python vault_cli.py --network-stats
```

## Tips

- Backup your `anchors.json` regularly
- Keep 20% disk space free
- Use SSD for better performance
