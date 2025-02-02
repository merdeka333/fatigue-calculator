import matplotlib.pyplot as plt
import numpy as np
import json
from matplotlib.animation import FuncAnimation

DATA_FILE = "fatigue_data.json"  # File to store past fatigue test data

def load_coordinates():
    """Load previous coordinates from a file (if available)."""
    try:
        with open(DATA_FILE, "r") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        return []  # Return empty list if file doesn't exist or is corrupted

def save_coordinates(coordinates):
    """Save updated coordinates to a file."""
    with open(DATA_FILE, "w") as file:
        json.dump(coordinates, file)

def plot_chart(coordinates):
    if not coordinates:
        print("No data to plot. Please complete the fatigue test first.")
        return


    xValue, yValue = zip(*coordinates)  # Unpacking the coordinates

    # Creating the figure and axes object
    fig, ax = plt.subplots()
    ax.set_title("Fatigue Data")
    ax.set_xlabel("Response Time")
    ax.set_ylabel("Correctness (1: correct, 2: incorrect)")
    ax.set_xlim(0, max(xValue) + 1)  # Set x-axis limits dynamically
    ax.set_ylim(0.5, 2.5)

    scatter = ax.scatter([], [], s=50, c='b', alpha=0.5)

    # Update function to update data and plot
    def update(frame):
        # Updating the data by adding more points
        x = np.array(xValue[:frame + 1])
        y = np.array(yValue[:frame + 1])
        scatter.set_offsets(np.column_stack((x, y)))
        return scatter,

    anim = FuncAnimation(fig, update, frames=len(coordinates), interval=500, repeat=False)  # Smooth animation
    plt.show()



def user_chart(coordinates):  # Accept coordinates as an argument
    i = 1
    while i > 0:
        want_chart = input("Do you want to see a chart of your fatigue data? Type 'yes' or 'no'. Other responses will not work: ")
        if want_chart.lower() == "yes":
            plot_chart(coordinates)  # Pass coordinates to plot_chart
            i = 0
        elif want_chart.lower() == "no":
            i = 0
        else:
            print("Invalid input. Please try again")
