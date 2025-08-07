import streamlit as st
import time

from src.monty_hall import game_simulator

st.image("https://upload.wikimedia.org/wikipedia/commons/thumb/3/3f/Monty_open_door.svg/1200px-Monty_open_door.svg.png", width=1000)

st.title(":zap: Monty Hall Problem Simulation")
number_games = st.number_input("Enter number of games to simulate:", min_value=10, max_value=100000, value=100, key="num_trials")


col1, col2 = st.columns(2)
col1.subheader("Win rate when switching doors")
col2.subheader("Win rate when staying with the initial choice")

chart1 = col1.line_chart(x=None, y=None, width=400, height=300)
chart1.add_rows([1.0])
chart2 = col2.line_chart(x=None, y=None, width=400, height=300)
chart2.add_rows([1.0])

# Create two lists to hold win percentages for both cases
wins_no_switch = 0
wins_switch = 0

for i in range(1, number_games + 1):
    # Simulate one game at a time
    num_wins_switch, num_wins_stay = game_simulator(num_trials=1)

    wins_no_switch += num_wins_stay
    wins_switch += num_wins_switch

    # Display the current win percentages after each game
    chart1.add_rows([wins_switch / i])
    chart2.add_rows([wins_no_switch / i])

    time.sleep(0.01)  # Simulate some delay for better visualization
