#!/usr/bin/env python3
"""
📜 SCRIPTURE SCRAMBLE 📜
A Cheesy Bible Word Game by Chain-Breaker

How to play:
- Unscramble the letters to find the biblical word
- Type your answer and press Enter
- Get 10 right to win!
"""

import tkinter as tk
from tkinter import messagebox, ttk
import random
import time

class ScriptureScramble:
    def __init__(self, root):
        self.root = root
        self.root.title("📜 Scripture Scramble 📜")
        self.root.geometry("600x700")
        self.root.configure(bg="#2C3E50")
        
        # Game data
        self.words = [
            ("bible", "The holy book"),
            ("genesis", "First book"),
            ("exodus", "Leaving Egypt"),
            ("psalms", "Songs and poems"),
            ("proverbs", "Wise sayings"),
            ("gospel", "Good news"),
            ("matthew", "First gospel"),
            ("mark", "Shortest gospel"),
            ("luke", "Doctor's gospel"),
            ("john", "Love gospel"),
            ("acts", "Early church"),
            ("romans", "Paul's letter"),
            ("corinthians", "To the Greeks"),
            ("galatians", "Freedom letter"),
            ("ephesians", "Unity letter"),
            ("philippians", "Joy letter"),
            ("colossians", "Christ is supreme"),
            ("thessalonians", "End times"),
            ("timothy", "Pastoral advice"),
            ("titus", "Church order"),
            ("philemon", "Slave letter"),
            ("hebrews", "Better than"),
            ("james", "Works and faith"),
            ("peter", "Rock"),
            ("jude", "Contend"),
            ("revelation", "Last book"),
            ("moses", "Led Exodus"),
            ("abraham", "Father of many"),
            ("david", "King"),
            ("solomon", "Wisest"),
            ("elijah", "Fire prophet"),
            ("jeremiah", "Weeping prophet"),
            ("isaiah", "Messianic prophet"),
            ("daniel", "Lions den"),
            ("jonah", "Big fish"),
            ("mary", "Jesus' mother"),
            ("joseph", "Dreamer"),
            ("paul", "Apostle"),
            ("peter", "Denier"),
            ("john", "Beloved"),
            ("adam", "First man"),
            ("eve", "First woman"),
            ("noah", "Ark builder"),
            ("cain", "First murderer"),
            ("abel", "First victim"),
            ("enoch", "Walked with God"),
            ("melchizedek", "Priest king"),
            ("sarah", "Laughed"),
            ("isaac", "Laughter"),
            ("jacob", "Deceiver"),
            ("esau", "Hairy"),
        ]
        
        self.current_word = ""
        self.scrambled = ""
        self.score = 0
        self.streak = 0
        self.high_score = self.load_high_score()
        self.used_words = []
        
        self.setup_ui()
        self.new_round()
    
    def setup_ui(self):
        # Title
        title = tk.Label(
            self.root,
            text="📜 SCRIPTURE SCRAMBLE 📜",
            font=("Helvetica", 28, "bold"),
            bg="#2C3E50",
            fg="#F39C12"
        )
        title.pack(pady=20)
        
        subtitle = tk.Label(
            self.root,
            text="Unscramble the biblical words!",
            font=("Helvetica", 12),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        subtitle.pack()
        
        # Score frame
        score_frame = tk.Frame(self.root, bg="#34495E", bd=2, relief="groove")
        score_frame.pack(pady=20, padx=50, fill="x")
        
        self.score_label = tk.Label(
            score_frame,
            text=f"Score: {self.score}",
            font=("Helvetica", 16, "bold"),
            bg="#34495E",
            fg="#2ECC71"
        )
        self.score_label.pack(side="left", padx=20, pady=10)
        
        self.streak_label = tk.Label(
            score_frame,
            text=f"Streak: {self.streak}",
            font=("Helvetica", 16),
            bg="#34495E",
            fg="#3498DB"
        )
        self.streak_label.pack(side="right", padx=20, pady=10)
        
        # High score
        self.high_label = tk.Label(
            self.root,
            text=f"🏆 High Score: {self.high_score}",
            font=("Helvetica", 12),
            bg="#2C3E50",
            fg="#E74C3C"
        )
        self.high_label.pack()
        
        # Word display
        self.word_frame = tk.Frame(self.root, bg="#2C3E50")
        self.word_frame.pack(pady=30)
        
        self.scrambled_label = tk.Label(
            self.word_frame,
            text="",
            font=("Courier", 36, "bold"),
            bg="#2C3E50",
            fg="#E67E22",
            wraplength=500
        )
        self.scrambled_label.pack()
        
        # Hint
        self.hint_label = tk.Label(
            self.root,
            text="",
            font=("Helvetica", 12, "italic"),
            bg="#2C3E50",
            fg="#95A5A6",
            wraplength=500
        )
        self.hint_label.pack(pady=10)
        
        # Entry
        self.entry = tk.Entry(
            self.root,
            font=("Helvetica", 20),
            justify="center",
            bg="#ECF0F1",
            fg="#2C3E50",
            insertbackground="#2C3E50",
            width=20
        )
        self.entry.pack(pady=20)
        self.entry.bind('<Return>', self.check_answer)
        
        # Buttons
        button_frame = tk.Frame(self.root, bg="#2C3E50")
        button_frame.pack(pady=20)
        
        self.submit_btn = tk.Button(
            button_frame,
            text="✓ Submit",
            font=("Helvetica", 14, "bold"),
            bg="#27AE60",
            fg="white",
            activebackground="#2ECC71",
            command=self.check_answer,
            width=12
        )
        self.submit_btn.pack(side="left", padx=5)
        
        self.skip_btn = tk.Button(
            button_frame,
            text="→ Skip",
            font=("Helvetica", 14),
            bg="#E74C3C",
            fg="white",
            activebackground="#C0392B",
            command=self.skip_word,
            width=12
        )
        self.skip_btn.pack(side="left", padx=5)
        
        self.hint_btn = tk.Button(
            button_frame,
            text="💡 Hint",
            font=("Helvetica", 14),
            bg="#F39C12",
            fg="white",
            activebackground="#D68910",
            command=self.show_hint,
            width=12
        )
        self.hint_btn.pack(side="left", padx=5)
        
        # Progress
        self.progress_var = tk.DoubleVar()
        self.progress = ttk.Progressbar(
            self.root,
            variable=self.progress_var,
            maximum=10,
            length=400,
            mode='determinate'
        )
        self.progress.pack(pady=20)
        
        self.progress_label = tk.Label(
            self.root,
            text="Progress to Win: 0/10",
            font=("Helvetica", 10),
            bg="#2C3E50",
            fg="#ECF0F1"
        )
        self.progress_label.pack()
        
        # Status
        self.status_label = tk.Label(
            self.root,
            text="Type your answer and press Enter!",
            font=("Helvetica", 12),
            bg="#2C3E50",
            fg="#BDC3C7"
        )
        self.status_label.pack(pady=10)
    
    def scramble_word(self, word):
        """Scramble a word but keep first and last letter"""
        if len(word) <= 3:
            letters = list(word)
            random.shuffle(letters)
            return ''.join(letters)
        
        middle = list(word[1:-1])
        random.shuffle(middle)
        return word[0] + ''.join(middle) + word[-1]
    
    def new_round(self):
        """Start a new round"""
        if len(self.used_words) >= len(self.words):
            self.used_words = []  # Reset if all words used
        
        # Pick unused word
        available = [w for w in self.words if w[0] not in self.used_words]
        self.current_word, self.current_hint = random.choice(available)
        self.used_words.append(self.current_word)
        
        # Scramble it
        self.scrambled = self.scramble_word(self.current_word)
        
        # Update UI
        self.scrambled_label.config(text=self.scrambled.upper())
        self.hint_label.config(text="")
        self.entry.delete(0, tk.END)
        self.status_label.config(
            text="Type your answer and press Enter!",
            fg="#BDC3C7"
        )
    
    def check_answer(self, event=None):
        """Check if answer is correct"""
        guess = self.entry.get().lower().strip()
        
        if not guess:
            return
        
        if guess == self.current_word.lower():
            # Correct!
            self.score += 1
            self.streak += 1
            self.status_label.config(
                text=f"✅ CORRECT! The answer was: {self.current_word.title()}",
                fg="#2ECC71"
            )
            
            # Update high score
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
                self.high_label.config(text=f"🏆 High Score: {self.high_score}")
                
                if self.score == self.high_score and self.score > 1:
                    self.show_celebration("NEW HIGH SCORE!")
            
            # Update progress
            self.progress_var.set(self.score)
            self.progress_label.config(text=f"Progress to Win: {self.score}/10")
            
            # Check for win
            if self.score >= 10:
                self.win_game()
                return
            
            # Next round after delay
            self.root.after(1500, self.new_round)
        else:
            # Wrong!
            self.streak = 0
            self.status_label.config(
                text=f"❌ Wrong! Try again!",
                fg="#E74C3C"
            )
        
        self.update_score()
    
    def skip_word(self):
        """Skip current word"""
        self.status_label.config(
            text=f"Skipped! The answer was: {self.current_word.title()}",
            fg="#F39C12"
        )
        self.streak = 0
        self.update_score()
        self.root.after(1500, self.new_round)
    
    def show_hint(self):
        """Show a hint"""
        self.hint_label.config(text=f"💡 Hint: {self.current_hint}")
    
    def update_score(self):
        """Update score display"""
        self.score_label.config(text=f"Score: {self.score}")
        self.streak_label.config(text=f"Streak: {self.streak}")
    
    def win_game(self):
        """Player won the game!"""
        self.show_celebration("🎉 YOU WIN! 🎉")
        messagebox.showinfo(
            "Victory!",
            f"Congratulations!

"
            f"You unscrambled 10 biblical words!
"
            f"Final Score: {self.score}
"
            f"Best Streak: {self.streak}

"
            f"Thanks for playing Scripture Scramble!"
        )
        self.reset_game()
    
    def reset_game(self):
        """Reset the game"""
        self.score = 0
        self.streak = 0
        self.used_words = []
        self.progress_var.set(0)
        self.progress_label.config(text="Progress to Win: 0/10")
        self.update_score()
        self.new_round()
    
    def show_celebration(self, message):
        """Show a celebration popup"""
        popup = tk.Toplevel(self.root)
        popup.title("🎉")
        popup.geometry("300x150")
        popup.configure(bg="#2C3E50")
        popup.transient(self.root)
        popup.grab_set()
        
        label = tk.Label(
            popup,
            text=message,
            font=("Helvetica", 20, "bold"),
            bg="#2C3E50",
            fg="#F39C12"
        )
        label.pack(expand=True, pady=20)
        
        self.root.after(2000, popup.destroy)
    
    def load_high_score(self):
        """Load high score from file"""
        try:
            with open('.scripture_scramble_highscore', 'r') as f:
                return int(f.read().strip())
        except:
            return 0
    
    def save_high_score(self):
        """Save high score to file"""
        try:
            with open('.scripture_scramble_highscore', 'w') as f:
                f.write(str(self.high_score))
        except:
            pass

def main():
    print("📜 Starting Scripture Scramble...")
    print("A cheesy Bible word game!")
    print()
    
    root = tk.Tk()
    game = ScriptureScramble(root)
    
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
