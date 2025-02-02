import matplotlib.pyplot as plt
import numpy as np
import json
from matplotlib.animation import FuncAnimation
import datetime

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

plt.ion()
fig, ax = plt.subplots()
ax.set_title("Fatigue Data")
ax.set_xlabel("Current Time of Day")
ax.set_ylabel("Overall Fatigue Score")
scatter = ax.scatter([], [], s=50, c='b', alpha=0.5)

def plot_chart(coordinates):
    if not coordinates:
        print("No data to plot. Please complete the fatigue test first.")
        return

    xValue, yValue = zip(*coordinates)  # Unpacking the coordinates

    # Creating the figure and axes object
    ax.set_xlim(0,24)  # Set range from 0-24 hrs
    ax.set_ylim(0, max(yValue) + 1)  # Adjust y-axis range based on scores
    ax.set_xticks(np.arange(0, 25, 1)) # One tick for every hour

    scatter.set_offsets(np.column_stack((xValue, yValue)))  # Update points
    plt.draw()  # Redraw the figure
    plt.pause(0.1)


def update_fatigue_chart(new_data):
    """Add new fatigue test data and update the chart."""
    coordinates = load_coordinates()  # Load past data
    coordinates.extend(new_data)  # Add new points
    save_coordinates(coordinates)  # Save updated data
    plot_chart(coordinates)  # Plot updated data



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
