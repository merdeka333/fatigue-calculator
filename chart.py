import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

def plot_chart(coordinates):
    if not coordinates:
        print("No data to plot. Please complete the fatigue test first.")
        return

    xValue, yValue = zip(*coordinates)  # Unpacking the coordinates

    # Initial data
    x = [xValue[0]]
    y = [yValue[0]]

    # Creating the figure and axes object
    fig, ax = plt.subplots()

    # Update function to update data and plot
    def update(frame):
        # Updating the data by adding more points
        x.append(xValue[frame])
        y.append(yValue[frame])

        ax.clear()  # Clearing the axes
        ax.scatter(x, y, s=y, c='b', alpha=0.5)  # Creating new scatter chart with updated data
        fig.canvas.draw()  # Forcing the artist to redraw itself

    plt.title("Fatigue Data")
    plt.xlabel("Response Time")
    plt.ylabel("Correctness (1: correct, 2: incorrect)")

    anim = FuncAnimation(fig, update, frames=len(coordinates), repeat=False)  # Update with each frame
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
