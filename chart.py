import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
from fatigue-test import coordinates

def plot_chart():
  xValue, yValue = zip(*coordinates)
  "initial data"
  x = [xValue[0]]
  y = [yValue[0]]
  
  "creating the figure and axes object"
  fig, ax = plt.subplots()

  "update function to update data and plot
  def update(frame):
      "updating the data by adding more points"
      for i in range (1,len(coordinates)):
        x.append(xValue[i])
        y.append(yValue[i])
    

      ax.clear()  # clearing the axes
      ax.scatter(x,y, s = y, c = 'b', alpha = 0.5)  # creating new scatter chart with updated data
      fig.canvas.draw()  # forcing the artist to redraw itself
  
  plt.title("Fatigue Data")
  plt.xlabel("Response Time")
  plt.ylabel("Correctness      1: correct, 2: incorrect")

  anim = FuncAnimation(fig, update)
  plt.show()

def user_chart():
  i = 1
  while i>0:
    want_chart = input("Do you want to see a chart of your fatigue data? Type 'yes' or 'no'. Other responses will not work")
    if want_chart == "yes":
      plot_chart()
      i = 0
    elif want_chart == "no":
      i = 0
    else:
      print("Invalid input. Please try again")
      i = 1
  
    
  
