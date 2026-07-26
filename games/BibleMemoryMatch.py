#!/usr/bin/env python3
"""
📖 BIBLE MEMORY MATCH 📖
A cheesy biblical memory card game!

Match the verses to win!
"""

import tkinter as tk
from tkinter import messagebox
import random
import time

class BibleMemoryMatch:
    def __init__(self, root):
        self.root = root
        self.root.title("📖 Bible Memory Match 📖")
        self.root.configure(bg="#2C3E50")
        
        # Game data - verse beginnings
        self.verses = [
            ("In the beginning", "God created"),
            ("For God so loved", "the world"),
            ("I can do all", "things through Christ"),
            ("The Lord is my", "shepherd"),
            ("For I know the", "plans I have"),
            ("Trust in the Lord", "with all"),
            ("Be strong and", "courageous"),
            ("Love is patient", "love is kind"),
            ("The fruit of the", "Spirit is"),
            ("Do not worry", "about tomorrow"),
            ("Ask and it will", "be given"),
            ("Seek first the", "kingdom of God"),
        ]
        
        self.buttons = []
        self.revealed = []
        self.matched = []
        self.score = 0
        self.moves = 0
        self.first_pick = None
        self.can_click = True
        
        self.setup_ui()
        self.setup_game()
    
    def setup_ui(self):
        """Setup the game UI"""
        # Title
        title = tk.Label(
            self.root,
            text="📖 BIBLE MEMORY MATCH 📖",
            font=("Helvetica", 24, "bold"),
            bg="#2C3E50",
            fg="#F39C12"
        )
        title.pack(pady=20)
        
        subtitle = tk.Label(
            self.root,
            text="Match the verse beginnings!",
            font=("Helvetica", 12),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        subtitle.pack()
        
        # Score frame
        score_frame = tk.Frame(self.root, bg="#2C3E50")
        score_frame.pack(pady=10)
        
        self.score_label = tk.Label(
            score_frame,
            text="Matches: 0/12",
            font=("Helvetica", 16, "bold"),
            bg="#2C3E50",
            fg="#2ECC71"
        )
        self.score_label.pack(side="left", padx=20)
        
        self.moves_label = tk.Label(
            score_frame,
            text="Moves: 0",
            font=("Helvetica", 16),
            bg="#2C3E50",
            fg="#3498DB"
        )
        self.moves_label.pack(side="left", padx=20)
        
        # Timer
        self.timer_label = tk.Label(
            self.root,
            text="Time: 0:00",
            font=("Helvetica", 14),
            bg="#2C3E50",
            fg="#E74C3C"
        )
        self.timer_label.pack(pady=5)
        
        # Game grid
        self.grid_frame = tk.Frame(self.root, bg="#2C3E50")
        self.grid_frame.pack(pady=20)
        
        # Status
        self.status_label = tk.Label(
            self.root,
            text="Click a card to reveal!",
            font=("Helvetica", 12),
            bg="#2C3E50",
            fg="#BDC3C7"
        )
        self.status_label.pack(pady=10)
        
        # New game button
        self.new_game_btn = tk.Button(
            self.root,
            text="🔄 New Game",
            font=("Helvetica", 14, "bold"),
            bg="#27AE60",
            fg="white",
            command=self.new_game,
            width=15
        )
        self.new_game_btn.pack(pady=10)
    
    def setup_game(self):
        """Setup the game board"""
        # Clear previous
        for widget in self.grid_frame.winfo_children():
            widget.destroy()
        
        self.buttons = []
        self.revealed = []
        self.matched = []
        self.score = 0
        self.moves = 0
        self.first_pick = None
        self.can_click = True
        self.start_time = time.time()
        
        # Create pairs
        pairs = []
        for i, (first, second) in enumerate(self.verses):
            pairs.append((first, i, "first"))
            pairs.append((second, i, "second"))
        
        # Shuffle
        random.shuffle(pairs)
        
        # Create buttons
        rows = 4
        cols = 6
        
        for i, (text, pair_id, part_type) in enumerate(pairs):
            row = i // cols
            col = i % cols
            
            btn = tk.Button(
                self.grid_frame,
                text="?",
                font=("Helvetica", 10, "bold"),
                width=15,
                height=3,
                bg="#34495E",
                fg="#ECF0F1",
                activebackground="#5D6D7E",
                wraplength=120
            )
            btn.grid(row=row, column=col, padx=5, pady=5)
            btn.config(command=lambda b=btn, t=text, p=pair_id: self.card_clicked(b, t, p))
            
            self.buttons.append({
                'button': btn,
                'text': text,
                'pair_id': pair_id,
                'revealed': False,
                'matched': False
            })
        
        self.update_score()
        self.update_timer()
    
    def card_clicked(self, button, text, pair_id):
        """Handle card click"""
        if not self.can_click:
            return
        
        # Find button index
        idx = None
        for i, btn in enumerate(self.buttons):
            if btn['button'] == button:
                idx = i
                break
        
        if idx is None or self.buttons[idx]['revealed'] or self.buttons[idx]['matched']:
            return
        
        # Reveal card
        button.config(
            text=text,
            bg="#E67E22",
            fg="#2C3E50"
        )
        self.buttons[idx]['revealed'] = True
        
        if self.first_pick is None:
            # First card
            self.first_pick = idx
            self.status_label.config(text="Pick another card!", fg="#F39C12")
        else:
            # Second card
            self.moves += 1
            self.update_score()
            
            first_idx = self.first_pick
            self.first_pick = None
            
            if self.buttons[first_idx]['pair_id'] == self.buttons[idx]['pair_id']:
                # Match!
                self.buttons[first_idx]['matched'] = True
                self.buttons[idx]['matched'] = True
                self.buttons[first_idx]['button'].config(bg="#27AE60", fg="white")
                self.buttons[idx]['button'].config(bg="#27AE60", fg="white")
                
                self.score += 1
                self.update_score()
                self.status_label.config(text="✅ MATCH!", fg="#2ECC71")
                
                # Check win
                if self.score == len(self.verses):
                    self.win_game()
            else:
                # No match
                self.status_label.config(text="❌ No match!", fg="#E74C3C")
                self.can_click = False
                self.root.after(1000, lambda: self.hide_cards(first_idx, idx))
    
    def hide_cards(self, idx1, idx2):
        """Hide unmatched cards"""
        if not self.buttons[idx1]['matched']:
            self.buttons[idx1]['button'].config(text="?", bg="#34495E", fg="#ECF0F1")
            self.buttons[idx1]['revealed'] = False
        
        if not self.buttons[idx2]['matched']:
            self.buttons[idx2]['button'].config(text="?", bg="#34495E", fg="#ECF0F1")
            self.buttons[idx2]['revealed'] = False
        
        self.can_click = True
        self.status_label.config(text="Try again!", fg="#BDC3C7")
    
    def update_score(self):
        """Update score display"""
        self.score_label.config(text=f"Matches: {self.score}/{len(self.verses)}")
        self.moves_label.config(text=f"Moves: {self.moves}")
    
    def update_timer(self):
        """Update timer"""
        if hasattr(self, 'start_time'):
            elapsed = int(time.time() - self.start_time)
            minutes = elapsed // 60
            seconds = elapsed % 60
            self.timer_label.config(text=f"Time: {minutes}:{seconds:02d}")
            
            if self.score < len(self.verses):
                self.root.after(1000, self.update_timer)
    
    def win_game(self):
        """Player won!"""
        elapsed = int(time.time() - self.start_time)
        minutes = elapsed // 60
        seconds = elapsed % 60
        
        self.status_label.config(
            text="🎉 YOU WON! 🎉",
            fg="#F39C12",
            font=("Helvetica", 16, "bold")
        )
        
        messagebox.showinfo(
            "Victory!",
            f"Congratulations! You matched all verses!\n\n"
            f"Time: {minutes}:{seconds:02d}\n"
            f"Moves: {self.moves}\n\n"
            f"Thanks for playing Bible Memory Match!"
        )
    
    def new_game(self):
        """Start new game"""
        self.setup_game()
        self.status_label.config(text="Click a card to reveal!", fg="#BDC3C7")

def main():
    print("📖 Starting Bible Memory Match...")
    print("Match the verse beginnings!")
    print()
    
    root = tk.Tk()
    game = BibleMemoryMatch(root)
    
    # Center window
    root.update_idletasks()
    width = root.winfo_width()
    height = root.winfo_height()
    x = (root.winfo_screenwidth() // 2) - (width // 2)
    y = (root.winfo_screenheight() // 2) - (height // 2)
    root.geometry(f'{width}x{height}+{x}+{y}')
    
    root.mainloop()

if __name__ == "__main__":
    main()
