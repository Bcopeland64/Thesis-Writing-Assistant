# utils/data_visualization.py
import matplotlib.pyplot as plt
import pandas as pd

def plot_data(file_path, x_column, y_column):
    df = pd.read_csv(file_path)
    plt.figure(figsize=(8, 6))
    plt.plot(df[x_column], df[y_column], marker='o')
    plt.title(f"{y_column} vs {x_column}")
    plt.xlabel(x_column)
    plt.ylabel(y_column)
    plt.grid(True)
    plt.savefig("plot.png")  # Save the plot as an image
    return "plot.png"