import itertools

import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection


# 平行六面体をつくる3つのベクトル
a = np.array([2.0, 0.0, 0.0])
b = np.array([1.0, 3.0, 0.0])
c = np.array([1.0, 1.0, 4.0])

# スカラー三重積と体積
cross_bc = np.cross(b, c)
scalar_triple_product = np.dot(a, cross_bc)
volume = abs(scalar_triple_product)

# b, c が張る底面の面積と、a の底面に垂直な高さ
base_area = np.linalg.norm(cross_bc)
normal = cross_bc / base_area
signed_height = np.dot(a, normal)
height = abs(signed_height)
foot = a - signed_height * normal

# 頂点 i*a + j*b + k*c（i, j, k は 0 または 1）
vertices = {
    bits: bits[0] * a + bits[1] * b + bits[2] * c
    for bits in itertools.product((0, 1), repeat=3)
}

# 6つの面を構成する頂点
faces = [
    [(0, 0, 0), (0, 1, 0), (0, 1, 1), (0, 0, 1)],
    [(1, 0, 0), (1, 1, 0), (1, 1, 1), (1, 0, 1)],
    [(0, 0, 0), (1, 0, 0), (1, 0, 1), (0, 0, 1)],
    [(0, 1, 0), (1, 1, 0), (1, 1, 1), (0, 1, 1)],
    [(0, 0, 0), (1, 0, 0), (1, 1, 0), (0, 1, 0)],
    [(0, 0, 1), (1, 0, 1), (1, 1, 1), (0, 1, 1)],
]

plt.rcParams.update({"font.size": 11, "mathtext.fontset": "stix"})

fig = plt.figure(figsize=(12.5, 7.2))
ax = fig.add_axes([0.02, 0.08, 0.65, 0.82], projection="3d")

# 平行六面体の面を半透明で描画
polygons = [[vertices[index] for index in face] for face in faces]
solid = Poly3DCollection(
    polygons,
    facecolors="#79a9d1",
    edgecolors="#34566f",
    linewidths=1.0,
    alpha=0.16,
)
ax.add_collection3d(solid)

# 12本の辺を描画
for bits in itertools.product((0, 1), repeat=3):
    for axis in range(3):
        if bits[axis] == 0:
            other = list(bits)
            other[axis] = 1

            start = vertices[bits]
            end = vertices[tuple(other)]

            ax.plot(
                [start[0], end[0]],
                [start[1], end[1]],
                [start[2], end[2]],
                color="#34566f",
                linewidth=1.0,
            )

# 原点から出る3つのベクトルを描画
vector_specs = [
    (a, "#c23b32", r"$\vec{a}$"),
    (b, "#27864b", r"$\vec{b}$"),
    (c, "#245b9b", r"$\vec{c}$"),
]

for vector, color, label in vector_specs:
    ax.quiver(
        0, 0, 0,
        vector[0], vector[1], vector[2],
        color=color,
        linewidth=2.4,
        arrow_length_ratio=0.10,
    )
    ax.text(*(vector * 1.05), label, color=color, fontsize=14)

# a の先端から底面に下ろした垂線を描画
ax.plot(
    [a[0], foot[0]],
    [a[1], foot[1]],
    [a[2], foot[2]],
    color="#8a4f9e",
    linestyle="--",
    linewidth=2.0,
)
midpoint = 0.5 * (a + foot)
ax.text(*midpoint, r"$h$", color="#8a4f9e", fontsize=14)
ax.scatter(*foot, color="#8a4f9e", s=24, depthshade=False)

# 原点を表示
ax.scatter(0, 0, 0, color="black", s=18, depthshade=False)
ax.text(0, 0, 0, "  O", color="black")

# 入力条件と計算結果を図の右側に表示
info = (
    "Input vectors\n"
    f"a = {np.array2string(a, precision=1)}\n"
    f"b = {np.array2string(b, precision=1)}\n"
    f"c = {np.array2string(c, precision=1)}\n\n"
    f"b × c = {np.array2string(cross_bc, precision=1)}\n"
    f"a · (b × c) = {scalar_triple_product:.1f}\n"
    f"Volume = |a · (b × c)| = {volume:.1f}\n"
    f"Base area × height = {base_area:.2f} × {height:.2f}"
    f" = {base_area * height:.1f}"
)
fig.text(
    0.70, 0.82, info,
    va="top",
    family="monospace",
    fontsize=10.5,
    linespacing=1.55,
    bbox={
        "boxstyle": "round,pad=0.7",
        "facecolor": "#f7f9fb",
        "edgecolor": "0.6",
    },
)

# 軸・視点などの設定
fig.suptitle("Scalar triple product and parallelepiped volume", y=0.97, fontsize=15)
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.set_zlabel("z")
ax.set_xlim(-0.4, 4.5)
ax.set_ylim(-0.4, 4.5)
ax.set_zlim(-0.4, 4.5)
ax.set_box_aspect((1, 1, 1))
ax.view_init(elev=24, azim=-55)
ax.grid(True, alpha=0.25)

plt.show()

print(f"Scalar triple product: {scalar_triple_product:.1f}")
print(f"Parallelepiped volume: {volume:.1f}")
print(
    f"Base area * height: "
    f"{base_area:.2f} * {height:.2f} = {base_area * height:.1f}"
)