import matplotlib.pyplot as plt
import csv
from typing import List

colors = [
    "blue",
    "green",
    "red",
    "cyan",
    "magenta",
    "yellow",
    "black",
    "white",
    "orange",
    "purple"
]

# Example usage
print(colors)

class Figure:
    def __init__(self, x_coords: List, y_coords: List):
        self.__x_coords = x_coords
        self.__y_coords = y_coords
        # todo: change color generation
        self.__color = colors[len(x_coords)-4]

    def draw(self):
        plt.fill(self.__x_coords, self.__y_coords, color=self.__color, edgecolor='black')


figures = []
csv_file_path = "figures.csv"
with open(csv_file_path, mode="r") as file:
    reader = csv.reader(file)
    header = next(reader)  # Skip the header row
    for row in reader:
        # Convert the row into pairs of (x, y)
        # points_x = [float(row[i]) for i in range(0, len(row), 2) if row[i]]
        # points_y = [float(row[i+1]) for i in range(0, len(row), 2) if row[i+1]]       
        points_x = [float(row[i]) for i in range(len(row) // 2) if row[i]]
        points_y = [float(row[i]) for i in range(len(row) // 2, len(row)) if row[i]]   
        print(points_x, points_y)
        figures.append(Figure(x_coords=points_x,y_coords=points_y))



print(figures)

# Plot the filled polygon
plt.figure(figsize=(6, 6))


for figure in figures:
    figure.draw()
plt.title("Random Geometric Figure")
plt.grid(True)
plt.gca().set_aspect('equal', adjustable='box')
plt.show()