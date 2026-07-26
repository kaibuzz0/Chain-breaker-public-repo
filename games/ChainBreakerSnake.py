#!/usr/bin/env python3
"""
🐍 CHAIN-BREAKER SNAKE 🐍
A cheesy biblical snake game!

Eat the scrolls to grow your chain!
Don't run into walls or yourself!
"""

import tkinter as tk
from tkinter import messagebox
import random

class ChainBreakerSnake:
    def __init__(self, root):
        self.root = root
        self.root.title("🐍 Chain-Breaker Snake 🐍")
        self.root.resizable(False, False)
        
        # Game constants
        self.GAME_WIDTH = 600
        self.GAME_HEIGHT = 400
        self.SPEED = 100
        self.SPACE_SIZE = 20
        self.BODY_SIZE = 2
        self.SCROLL_COLOR = "#F39C12"
        self.SNAKE_COLOR = "#27AE60"
        self.BACKGROUND_COLOR = "#2C3E50"
        self.TEXT_COLOR = "#ECF0F1"
        
        # Score
        self.score = 0
        self.high_score = self.load_high_score()
        self.direction = "down"
        self.next_direction = self.direction
        
        # Setup canvas
        self.canvas = tk.Canvas(
            root,
            bg=self.BACKGROUND_COLOR,
            height=self.GAME_HEIGHT,
            width=self.GAME_WIDTH,
            highlightthickness=0
        )
        self.canvas.pack()
        
        # Score display
        self.score_text = self.canvas.create_text(
            50, 20,
            text="Score: 0",
            fill=self.TEXT_COLOR,
            font=('Helvetica', 16, 'bold'),
            tag="score"
        )
        
        self.high_score_text = self.canvas.create_text(
            self.GAME_WIDTH - 80, 20,
            text=f"High: {self.high_score}",
            fill="#E74C3C",
            font=('Helvetica', 14),
            tag="highscore"
        )
        
        # Instructions
        self.instructions = self.canvas.create_text(
            self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2,
            text="🐍 CHAIN-BREAKER SNAKE 🐍\n\n"
                 "Eat the 📜 to grow your chain!\n"
                 "Don't hit walls or yourself!\n\n"
                 "WASD or Arrow Keys to move\n"
                 "Press SPACE to start!",
            fill=self.TEXT_COLOR,
            font=('Helvetica', 16),
            justify='center',
            tag="instructions"
        )
        
        # Bind keys
        self.root.bind('<Left>', lambda e: self.change_direction('left'))
        self.root.bind('<Right>', lambda e: self.change_direction('right'))
        self.root.bind('<Up>', lambda e: self.change_direction('up'))
        self.root.bind('<Down>', lambda e: self.change_direction('down'))
        self.root.bind('<w>', lambda e: self.change_direction('up'))
        self.root.bind('<s>', lambda e: self.change_direction('down'))
        self.root.bind('<a>', lambda e: self.change_direction('left'))
        self.root.bind('<d>', lambda e: self.change_direction('right'))
        self.root.bind('<space>', lambda e: self.start_game())
        self.root.bind('<Return>', lambda e: self.start_game())
        
        # Game state
        self.snake_positions = []
        self.scroll_position = None
        self.running = False
        self.paused = False
    
    def start_game(self):
        """Start or restart the game"""
        if not self.running:
            self.running = True
            self.score = 0
            self.direction = "down"
            self.next_direction = self.direction
            
            # Clear canvas
            self.canvas.delete("all")
            
            # Recreate score
            self.score_text = self.canvas.create_text(
                50, 20,
                text="Score: 0",
                fill=self.TEXT_COLOR,
                font=('Helvetica', 16, 'bold'),
                tag="score"
            )
            
            self.high_score_text = self.canvas.create_text(
                self.GAME_WIDTH - 80, 20,
                text=f"High: {self.high_score}",
                fill="#E74C3C",
                font=('Helvetica', 14),
                tag="highscore"
            )
            
            # Create snake head
            center_x = self.GAME_WIDTH // 2
            center_y = self.GAME_HEIGHT // 2
            self.snake_positions = [
                [center_x, center_y],
                [center_x, center_y - self.SPACE_SIZE],
                [center_x, center_y - (2 * self.SPACE_SIZE)]
            ]
            
            for i, pos in enumerate(self.snake_positions):
                color = self.SNAKE_COLOR if i == 0 else "#2ECC71"
                self.canvas.create_oval(
                    pos[0], pos[1],
                    pos[0] + self.SPACE_SIZE, pos[1] + self.SPACE_SIZE,
                    fill=color, tag=f"snake_{i}"
                )
            
            # Create first scroll
            self.create_scroll()
            
            # Start game loop
            self.next_turn()
    
    def change_direction(self, new_direction):
        """Change snake direction"""
        if not self.running:
            return
        
        opposite = {
            'left': 'right',
            'right': 'left',
            'up': 'down',
            'down': 'up'
        }
        
        if opposite[new_direction] != self.direction:
            self.next_direction = new_direction
    
    def next_turn(self):
        """Game loop"""
        if not self.running:
            return
        
        self.direction = self.next_direction
        
        # Move head
        head_x, head_y = self.snake_positions[0]
        
        if self.direction == "up":
            head_y -= self.SPACE_SIZE
        elif self.direction == "down":
            head_y += self.SPACE_SIZE
        elif self.direction == "left":
            head_x -= self.SPACE_SIZE
        elif self.direction == "right":
            head_x += self.SPACE_SIZE
        
        new_head = [head_x, head_y]
        
        # Check collisions
        if (head_x < 0 or head_x >= self.GAME_WIDTH or 
            head_y < 0 or head_y >= self.GAME_HEIGHT or
            new_head in self.snake_positions):
            self.game_over()
            return
        
        # Move snake
        self.snake_positions.insert(0, new_head)
        
        # Check scroll collision
        if new_head == self.scroll_position:
            self.score += 1
            self.canvas.itemconfig(self.score_text, text=f"Score: {self.score}")
            
            # Update high score
            if self.score > self.high_score:
                self.high_score = self.score
                self.save_high_score()
                self.canvas.itemconfig(self.high_score_text, text=f"High: {self.high_score}")
            
            self.create_scroll()
        else:
            # Remove tail
            tail = self.snake_positions.pop()
            self.canvas.delete(f"snake_{len(self.snake_positions)}")
        
        # Redraw snake
        self.canvas.delete("snake")
        for i, pos in enumerate(self.snake_positions):
            color = self.SNAKE_COLOR if i == 0 else "#2ECC71"
            self.canvas.create_oval(
                pos[0], pos[1],
                pos[0] + self.SPACE_SIZE, pos[1] + self.SPACE_SIZE,
                fill=color, tag="snake"
            )
        
        self.root.after(self.SPEED, self.next_turn)
    
    def create_scroll(self):
        """Create a new scroll (food)"""
        while True:
            x = random.randint(0, (self.GAME_WIDTH // self.SPACE_SIZE) - 1) * self.SPACE_SIZE
            y = random.randint(0, (self.GAME_HEIGHT // self.SPACE_SIZE) - 1) * self.SPACE_SIZE
            
            if [x, y] not in self.snake_positions:
                self.scroll_position = [x, y]
                break
        
        # Draw scroll
        self.canvas.delete("scroll")
        self.canvas.create_text(
            x + self.SPACE_SIZE // 2, y + self.SPACE_SIZE // 2,
            text="📜",
            font=("Arial", 14),
            tag="scroll"
        )
    
    def game_over(self):
        """End game"""
        self.running = False
        
        # Game over text
        self.canvas.create_text(
            self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2 - 20,
            text="💥 GAME OVER! 💥",
            fill="#E74C3C",
            font=('Helvetica', 32, 'bold'),
            tag="gameover"
        )
        
        self.canvas.create_text(
            self.GAME_WIDTH // 2, self.GAME_HEIGHT // 2 + 20,
            text=f"Final Score: {self.score}\nPress SPACE to play again!",
            fill=self.TEXT_COLOR,
            font=('Helvetica', 16),
            justify='center',
            tag="gameover"
        )
    
    def load_high_score(self):
        """Load high score"""
        try:
            with open('.snake_highscore', 'r') as f:
                return int(f.read().strip())
        except:
            return 0
    
    def save_high_score(self):
        """Save high score"""
        try:
            with open('.snake_highscore', 'w') as f:
                f.write(str(self.high_score))
        except:
            pass

def main():
    print("🐍 Starting Chain-Breaker Snake...")
    print("Eat the scrolls! Don't hit walls!")
    print()
    
    root = tk.Tk()
    game = ChainBreakerSnake(root)
    
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
