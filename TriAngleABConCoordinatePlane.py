import matplotlib.pyplot as plt

# Coordinates for triangle ABC
A, B, C = (1, 2), (4, 6), (7, 2)
x = [A[0], B[0], C[0], A[0]]
y = [A[1], B[1], C[1], A[1]]

plt.plot(x, y, 'bo-')  # 'bo-' means blue circles with lines
plt.text(*A, 'A', fontsize=12)
plt.text(*B, 'B', fontsize=12)
plt.text(*C, 'C', fontsize=12)
plt.grid(True)
plt.axis("equal")
plt.title("Triangle ABC on Coordinate Plane")
plt.xlabel("X")
plt.ylabel("Y")
plt.show()
