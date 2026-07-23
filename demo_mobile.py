#!/usr/bin/env python3
"""
Chain-Breaker Demo: Mobile Mode

Shows battery-aware operation for mobile devices.

Run: python demo_mobile.py --mode light
"""

import argparse
import time


class MobileNodeDemo:
    """Demo mobile node without exposing internals."""
    
    MODES = {
        'ultra_light': {
            'description': 'Headers only (~50MB)',
            'features': ['Headers', 'Basic sync'],
            'battery_usage': 'Minimal'
        },
        'light': {
            'description': 'Headers + recent blocks (~200MB)',
            'features': ['Headers', 'UTXO set', 'Recent blocks'],
            'battery_usage': 'Low'
        },
        'full': {
            'description': 'Complete blockchain (~2GB)',
            'features': ['Full validation', 'All blocks', 'Index'],
            'battery_usage': 'High'
        }
    }
    
    def __init__(self, mode: str = 'light'):
        self.mode = mode
        self.config = self.MODES.get(mode, self.MODES['light'])
        self.running = False
        self.synced_blocks = 0
        
    def start(self):
        """Start mobile node."""
        print(f"📱 Starting mobile node...")
        print(f"   Mode: {self.mode}")
        print(f"   Storage: {self.config['description']}")
        print(f"   Features: {', '.join(self.config['features'])}")
        print(f"   Battery: {self.config['battery_usage']} usage")
        print()
        
        self.running = True
        
        # Simulate sync
        print("🔄 Syncing with network...")
        for i in range(5):
            if not self.running:
                break
            time.sleep(0.5)
            self.synced_blocks += 100
            print(f"   Synced {self.synced_blocks} blocks...")
        
        print(f"   ✅ Sync complete: {self.synced_blocks} blocks")
        
    def mine_if_charging(self, is_charging: bool = False):
        """Only mine when charging (battery protection)."""
        if not is_charging:
            print("🔋 Not mining (not charging)")
            print("   Connect charger to enable mining")
            return
        
        print("⚡ Mining enabled (charging detected)")
        print("⛏️  Mining blocks...")
        time.sleep(1)
        print("   ✅ Mined 3 blocks")


def main():
    parser = argparse.ArgumentParser(
        description='Demo: Mobile blockchain node'
    )
    parser.add_argument('--mode', choices=['ultra_light', 'light', 'full'],
                       default='light', help='Storage mode')
    parser.add_argument('--mine-when-charging', action='store_true',
                       help='Only mine when charging')
    args = parser.parse_args()
    
    print("=" * 70)
    print("📱 Chain-Breaker Demo: Mobile Mode")
    print("=" * 70)
    print()
    
    # Show modes
    print("Available modes:")
    for mode, config in MobileNodeDemo.MODES.items():
        marker = "▶" if mode == args.mode else " "
        print(f"   {marker} {mode:12} | {config['description']}")
    print()
    
    # Start node
    node = MobileNodeDemo(mode=args.mode)
    node.start()
    
    # Mining demo
    print()
    if args.mine_when_charging:
        print("⛏️  Testing mining with battery protection...")
        node.mine_if_charging(is_charging=False)  # Not charging
        node.mine_if_charging(is_charging=True)     # Charging
    else:
        print("💡 Use --mine-when-charging to test battery-aware mining")
    
    print()
    print("=" * 70)
    print("✅ Mobile demo complete!")
    print("=" * 70)


if __name__ == "__main__":
    main()
