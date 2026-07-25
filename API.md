# API Documentation

Developer reference.

## Core Classes

### ScriptureVaultNode

```python
from scripture_vault.distributed.node.vault_node import ScriptureVaultNode

node = ScriptureVaultNode(
    data_dir="path/to/data",
    max_storage_gb=100.0
)

node.start()
node.ingest_document("file.pdf", metadata)
node.retrieve_document("doc_id", "output.pdf")
node.stop()
```

### Methods

- `ingest_document(path, metadata)` - Add file
- `retrieve_document(id, output)` - Get file
- `verify_document(id)` - Check integrity

## CLI Commands

- `vault_cli.py --list`
- `vault_cli.py --find "name"`
- `vault_cli.py --verify`
