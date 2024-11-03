# Hit the Bricks 🧱

A classic arcade-style brick breaker game built with Pygame where players control a paddle to bounce a ball and destroy colorful bricks.

## 🎮 Game Features

- Rainbow-colored brick layout with 224 breakable bricks
- Smooth paddle control using mouse movement
- Dynamic ball physics with collision detection
- Victory and game over conditions
- Interactive restart system
- Clean and minimalist design
- 60 FPS smooth gameplay

## 🛠️ Technical Details

### Prerequisites
- Python 3.x
- Pygame
- tkinter (usually comes with Python)

### Installation
1. Clone the repository
```bash
git clone https://github.com/ChanMeng666/pygame-brick-game.git
```

2. Install required packages
```bash
pip install pygame
```

3. Run the game
```bash
python game.py
```

## 🎯 How to Play

1. Launch the game and click "Yes" when prompted to start
2. Move your mouse left and right to control the paddle
3. Bounce the ball off the paddle to break the bricks
4. Break all bricks to win
5. Don't let the ball fall below the paddle!

## 🎨 Game Elements

- **Paddle**: White rectangular platform controlled by mouse movement
- **Ball**: White circular projectile that bounces off surfaces
- **Bricks**: Rainbow-colored blocks arranged in rows
- **Screen**: 800x600 pixels playing field

## 🔄 Game Flow

1. Start Screen: Confirmation prompt to begin
2. Main Game: Break bricks while keeping the ball in play
3. Game Over: Triggered when ball falls below paddle
4. Victory: Achieved when all bricks are destroyed
5. Restart Option: Available after both game over and victory

## 💻 Technical Implementation

- Built using Pygame framework
- Sprite-based collision detection
- Object-oriented design with separate classes for Ball, Paddle, and Brick
- Frame rate locked at 60 FPS for consistent gameplay
- Message boxes handled through tkinter integration

## 📝 License

This project is open source and available under the MIT License.
