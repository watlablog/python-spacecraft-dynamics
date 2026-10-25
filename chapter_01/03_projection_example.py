import matplotlib.pyplot as plt

# Times New Romanを基本フォントに設定
plt.rcParams["font.family"] = "Times New Roman"

# ベクトルの始点と終点
origin = (0, 0)
v = (3, 4)       # 入力ベクトル
v_x = (3, 0)     # x方向への射影ベクトル

fig, ax = plt.subplots(figsize=(6, 5))

# 入力ベクトル v = (3, 4)
ax.annotate(
    "",
    xy=v,
    xytext=origin,
    arrowprops=dict(arrowstyle="->", color="C0", linewidth=2),
)
ax.text(2.5, 4.0, r"$\vec{v}=(3,4)^T$", color="C0", fontsize=13)

# x方向への射影 v_x = (3, 0)
ax.annotate(
    "",
    xy=v_x,
    xytext=origin,
    arrowprops=dict(arrowstyle="->", color="C1", linewidth=2),
)
ax.text(1.35, -0.45, r"$\vec{v}_x=(3,0)^T$", color="C1", fontsize=13)

# 入力ベクトルの終点からx軸への垂線
ax.plot(
    [v_x[0], v[0]],
    [v_x[1], v[1]],
    linestyle="--",
    color="0.4",
    linewidth=1.2,
)

# 射影点を表示
ax.plot(v_x[0], v_x[1], "o", color="C1", markersize=5)

# x軸とy軸を原点に配置
ax.spines["left"].set_position("zero")
ax.spines["bottom"].set_position("zero")
ax.spines["right"].set_color("none")
ax.spines["top"].set_color("none")

# 上下左右に目盛を表示し、内向きにする
ax.tick_params(
    axis="both",
    which="both",
    direction="inout",
    top=False,
    right=False,
)

ax.set_xlim(-0.5, 4.5)
ax.set_ylim(-0.8, 5.0)
ax.set_aspect("equal", adjustable="box")
ax.set_xlabel(
    "x",
    loc="right",
    fontsize=13,
    fontname="Times New Roman",
    fontstyle="italic",
)
ax.set_ylabel(
    "y",
    loc="top",
    fontsize=13,
    fontname="Times New Roman",
    fontstyle="italic",
)
ax.grid(True, linestyle=":", linewidth=0.7, alpha=0.6)

fig.tight_layout()
plt.show()