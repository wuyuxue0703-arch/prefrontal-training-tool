import random
import matplotlib.pyplot as plt
import math
plt.rcParams['font.sans-serif'] = ['Microsoft YaHei']
plt.rcParams['axes.unicode_minus'] = False
points = []
rings = [(2, 1.5), (3, 3.5), (4, 5.4), (6, 7.3)]
for k, rho in rings:
    per_quad = k
    for quad in range(4):
        base_angle = quad * math.pi / 2
        for i in range(per_quad):
            t = (i + 0.5) / per_quad
            theta = base_angle + t * (math.pi / 2)
            x = rho * math.cos(theta)
            y = rho * math.sin(theta)
            points.append((x, y, quad))

nums = list(range(1,61))
random.shuffle(nums)

fig, ax = plt.subplots(figsize = (9,16))
ax.set_facecolor("#fffaf0")
fig.patch.set_facecolor("#fffaf0")
offset = -2.2
quad_colors = ["#5fa8d3" , "#3a7ca5" , "#679436", "#89909f"]
for (x, y, quad), num in zip (points, nums):
    edge_color = quad_colors[quad]
    ax.plot(x, y + offset, marker = "o", markeredgecolor = "none", markersize = 22, markerfacecolor = "none", linestyle = " ")
    ax.text(x, y + offset, str(num), ha = "center", va = "center", fontsize = 12, color = edge_color)
ax.text(0, 8.5, "前额叶顺序寻找训练", ha = "center", fontsize = 22)
ax.text(0, -11.8, "找不完没关系", ha = "center", fontsize = 18)
ax.text(0, -12.6, "坚持做完2分钟", ha = "center", fontsize = 18)
ax.set_aspect('equal')
ax.axis("off")
plt.savefig("train.png", dpi = 300, bbox_inches = "tight")
plt.show()