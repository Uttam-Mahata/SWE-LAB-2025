import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

def plot_prim_data(filename):
    """
    Plots Prim's algorithm data and theoretical complexity curves.
    """
    df = pd.read_csv(filename)

    # Convert columns to numeric
    df['Number of Nodes'] = pd.to_numeric(df['Number of Nodes'])
    df['Average Time (nanoseconds)'] = pd.to_numeric(df['Average Time (nanoseconds)'])

    # Create the plot
    plt.figure(figsize=(12, 8))

    # Plot the measured data
    plt.plot(df['Number of Nodes'], df['Average Time (nanoseconds)'], marker='o', linestyle='-', markersize=4, label="Prim's Measured Time")

    # Generate data for theoretical curves
    nodes = df['Number of Nodes']
    edges = (nodes * (nodes - 1)) / 2  # Maximum possible edges in a complete graph
    n_log_n = edges * np.log2(nodes)
    n_squared = nodes**2
    n_squared_log_n = nodes**2 * np.log2(nodes)

   # Scale theoretical curves
    scale_nlogn = np.mean(df['Average Time (nanoseconds)'].head(10)) / np.mean(n_log_n.head(10))
    scale_n2 = np.mean(df['Average Time (nanoseconds)'].head(10)) / np.mean(n_squared.head(10))
    scale_n2logn = np.mean(df['Average Time (nanoseconds)'].head(10)) / np.mean(n_squared_log_n.head(10))

    # Plot theoretical curves
    plt.plot(nodes, scale_nlogn * n_log_n, linestyle='--', label="E log(V)")
    plt.plot(nodes, scale_n2 * n_squared, linestyle='-.', label="V^2")
    plt.plot(nodes, scale_n2logn*n_squared_log_n, linestyle=':', label = "V^2log(V)")



    # Plot
    plt.title("Prim's Algorithm Runtime vs. Input Size", fontsize=16)
    plt.xlabel("Number of Nodes", fontsize=14)
    plt.ylabel("Average Time (nanoseconds)", fontsize=14)
    plt.grid(True)
    plt.xticks(fontsize=12)
    plt.yticks(fontsize=12)
    plt.legend(fontsize=12)
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_prim_data("prim_data.csv")  # Replace if needed