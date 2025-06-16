import matplotlib.pyplot as plt

# Define plotting function
def plot_diagram(step, step_number):
    points = step["points"]
    plt.figure(figsize=(6, 6))

    # Draw connecting sides
    for (start, end) in step["connect"]:
        x_vals = [points[start][0], points[end][0]]
        y_vals = [points[start][1], points[end][1]]
        plt.plot(x_vals, y_vals, 'bo-')

    # Label points
    for label in step["highlight"]:
        x, y = points[label]
        plt.text(x + 0.1, y + 0.1, label, fontsize=12, color='darkred')

    # Format plot
    plt.title(step["title"])
    plt.grid(True)
    plt.axis('equal')
    plt.xlabel("X-axis")
    plt.ylabel("Y-axis")
    plt.savefig(f"step_{step_number}.png")
    plt.close()


# Define sequence of steps
steps = [
    {
        "title": "Step 1: Plot Triangle ABC",
        "points": {"A": (1, 2), "B": (4, 6), "C": (7, 2)},
        "highlight": ["A", "B", "C"],
        "connect": [("A", "B"), ("B", "C"), ("C", "A")]
    },
    {
        "title": "Step 2: Plot Triangle PQR",
        "points": {"P": (2, -1), "Q": (5, 3), "R": (8, -1)},
        "highlight": ["P", "Q", "R"],
        "connect": [("P", "Q"), ("Q", "R"), ("R", "P")]
    },
    {
        "title": "Step 3: Compare Side Lengths for SSS",
        "points": {
            "A": (1, 2), "B": (4, 6), "C": (7, 2),
            "P": (2, -1), "Q": (5, 3), "R": (8, -1)
        },
        "highlight": ["A", "B", "C", "P", "Q", "R"],
        "connect": [
            ("A", "B"), ("B", "C"), ("C", "A"),
            ("P", "Q"), ("Q", "R"), ("R", "P")
        ]
    }
]

# Generate and save all diagrams
for idx, step in enumerate(steps, start=1):
    plot_diagram(step, idx)
