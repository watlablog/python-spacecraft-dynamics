import numpy as np
import matplotlib.pyplot as plt

# Times New Romanを基本フォントに設定
plt.rcParams["font.family"] = "Times New Roman"

# 標準基底ベクトル e_1, e_2, e_3
basis = np.eye(3)

# ダイアディックの係数 D_ij
D = np.array([
    [1.0,  2.0, 0.0],
    [0.0, -1.0, 1.0],
    [2.0,  0.0, 1.0],
])

# 入力ベクトル
v = np.array([1.0, 2.0, -1.0])

# 定義式の各項 D_ij e_i e_j を
# 標準基底上の行列として足し合わせる
D_dyadic = np.zeros((3, 3))

for i in range(3):
    for j in range(3):
        D_dyadic += D[i, j] * np.outer(basis[i], basis[j])

# ダイアディックを入力ベクトルに作用させる
w = D_dyadic @ v

# 入力の各成分から出力への寄与ベクトル c_j
contributions = np.array([
    D[:, j] * v[j]
    for j in range(3)
])

print("入力ベクトル v:", v)
print("出力ベクトル w:", w)
print("各寄与ベクトル c_j:\n", contributions)

fig = plt.figure(figsize=(8, 7))
ax = fig.add_subplot(111, projection="3d")


def draw_vector(start, vector, color, label, linestyle="-", linewidth=2):
    """startを始点とする3次元ベクトルを描く。"""
    start = np.asarray(start, dtype=float)
    vector = np.asarray(vector, dtype=float)

    ax.quiver(
        start[0], start[1], start[2],
        vector[0], vector[1], vector[2],
        color=color,
        linewidth=linewidth,
        linestyle=linestyle,
        arrow_length_ratio=0.12,
    )

    # ラベルを矢印の中ほどに配置
    label_position = start + 0.55 * vector
    ax.text(
        label_position[0],
        label_position[1],
        label_position[2],
        label,
        color=color,
        fontsize=11,
    )


# 入力ベクトル v
draw_vector(
    start=(0, 0, 0),
    vector=v,
    color="C0",
    label=r"$\vec{v}$",
    linewidth=2.5,
)

# 寄与ベクトル c_1, c_2, c_3 を先端から順につなぐ
start = np.zeros(3)
contribution_colors = ["C1", "C2", "C3"]

for j, contribution in enumerate(contributions):
    draw_vector(
        start=start,
        vector=contribution,
        color=contribution_colors[j],
        label=rf"$\vec{{c}}_{j + 1}$",
    )
    start += contribution

# 出力ベクトル w を原点から破線で描く
draw_vector(
    start=(0, 0, 0),
    vector=w,
    color="C4",
    label=r"$\vec{w}$",
    linestyle="--",
    linewidth=2.5,
)

# 入力条件と計算結果を図中に表示
ax.text2D(
    0.03,
    0.97,
    "D = [[1, 2, 0], [0, -1, 1], [2, 0, 1]]\n"
    "v = (1, 2, -1)\n"
    "w = (5, -3, 1)",
    transform=ax.transAxes,
    va="top",
    fontsize=10,
)

ax.set_title("Dyadic operation in 3D", fontsize=14)
ax.set_xlabel("x", fontstyle="italic")
ax.set_ylabel("y", fontstyle="italic")
ax.set_zlabel("z", fontstyle="italic")

# 入力・出力・寄与ベクトルがすべて見える範囲に設定
ax.set_xlim(-1, 6)
ax.set_ylim(-4, 3)
ax.set_zlim(-2, 4)
ax.set_box_aspect((7, 7, 6))
ax.view_init(elev=22, azim=-55)

ax.tick_params(axis="both", which="both", direction="inout")
ax.grid(True, linestyle=":", linewidth=0.7, alpha=0.6)

fig.tight_layout()
plt.show()