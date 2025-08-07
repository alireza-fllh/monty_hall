# Monty Hall Problem Simulation

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Monty_open_door.svg/1200px-Monty_open_door.svg.png" alt="monty_hall_simulator" style="border-radius: 10px" width=500>

A comprehensive Python project that simulates and visualizes the famous **Monty Hall Problem** - a probability puzzle based on a game show scenario where understanding probability can dramatically improve your chances of winning.

## 🎯 What is the Monty Hall Problem?

The Monty Hall Problem is a probability puzzle named after the host of the game show "Let's Make a Deal". Here's how it works:

1. You're presented with **three doors**
2. Behind one door is a **car** (the prize), behind the other two are **goats**
3. You choose a door (but don't open it yet)
4. The host, who knows what's behind each door, opens one of the remaining doors to reveal a goat
5. You're then given a choice: **stick with your original choice** or **switch to the other unopened door**

**The question:** Should you switch or stay with your original choice?

**The surprising answer:** You should always switch! Switching gives you a ~67% chance of winning, while staying gives you only a ~33% chance.

## 🚀 Features

This project provides multiple ways to explore and understand the Monty Hall Problem:

- **📊 Interactive Streamlit Web App**: Real-time visualization of win rates as simulations run
- **🔬 Python Library**: Clean, well-documented functions for running simulations
- **⚡ High-Performance Simulation**: Run thousands of trials to see the law of large numbers in action

## 📁 Project Structure

```
monty_hall/
├── README.md
└── src/
    ├── app.py              # Streamlit web application
    └── monty_hall.py       # Core simulation library
```

## 🛠️ Installation & Setup

### Prerequisites
- Python 3.7+
- pip

### Install Dependencies
```bash
pip install -r requirements.txt
```

## 🎮 Usage

### 1. Run the Interactive Web App
Launch the Streamlit application for a visual, real-time simulation:

```bash
streamlit run src/app.py
```

This will open a web interface where you can:
- Set the number of games to simulate (10 to 100,000)
- Watch real-time charts showing win rates for both strategies
- See the convergence to theoretical probabilities

### 2. Use the Python Library
```python
from src.monty_hall import monty_hall_game, game_simulator

# Simulate a single game
won = monty_hall_game(switch_door=True)  # Returns True if won
print(f"Won: {won}")

# Run multiple simulations
num_trials = 10000
wins_switch, wins_stay = game_simulator(num_trials)
print(f"Switch strategy: {wins_switch/num_trials:.1%} win rate")
print(f"Stay strategy: {wins_stay/num_trials:.1%} win rate")
```


### 3. Run from Command Line
```bash
cd src
python monty_hall.py
```

## 📊 Expected Results

With a large number of trials, you should see:
- **Switching strategy**: ~66.7% win rate (2/3 probability)
- **Staying strategy**: ~33.3% win rate (1/3 probability)

## 🧮 The Mathematics

### Why Switching Works

When you make your initial choice, you have a **1/3 chance** of picking the car and a **2/3 chance** of picking a goat.

When the host reveals a goat from the remaining doors:
- If your initial choice was correct (1/3 probability), switching loses
- If your initial choice was wrong (2/3 probability), switching wins

Since you're wrong 2/3 of the time initially, switching wins 2/3 of the time!

### Probability Breakdown
- **Initial choice correct**: 1/3 → Switching loses
- **Initial choice wrong**: 2/3 → Switching wins
- **Therefore**: Switching wins 2/3 of the time


## 📚 Further Reading

- [Monty Hall Problem - Wikipedia](https://en.wikipedia.org/wiki/Monty_Hall_problem)
- [The Monty Hall Problem - Brilliant.org](https://brilliant.org/wiki/monty-hall-problem/)
- [Let's Make a Deal - Original Game Show](https://en.wikipedia.org/wiki/Let%27s_Make_a_Deal)

## 📄 License

This project is open source and available under the MIT License.

---

**Try it yourself and prepare to be surprised by the results!** 🎲✨