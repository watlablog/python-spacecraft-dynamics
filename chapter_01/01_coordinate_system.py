from itertools import product

import matplotlib.pyplot as plt
import numpy as np


def draw_figure() -> None:
    plt.rcParams.update(
        {
            "font.family": "Times New Roman",
            "mathtext.fontset": "custom",
            "mathtext.rm": "Times New Roman",
            "mathtext.it": "Times New Roman:italic",
            "mathtext.bf": "Times New Roman:bold",
            "mathtext.cal": "Times New Roman:italic",
        }
    )

    # Oblique 2-D projections of the three mutually perpendicular axes.
    # Their 3-D meaning is conveyed by the right-handed coordinate convention.
    basis = np.array(
        [
            [-0.48, -0.50],  # axis 1: down-left
            [0.68, 0.00],  # axis 2: right
            [0.00, 0.67],  # axis 3: up
        ]
    )
    p = np.array([2.0, 2.5, 2.5])
    components = p[:, None] * basis
    vertices = {
        bits: np.sum(np.array(bits)[:, None] * components, axis=0)
        for bits in product((0, 1), repeat=3)
    }

    _, ax = plt.subplots(figsize=(5.2, 4.6), constrained_layout=True)
    ax.set_aspect("equal")
    ax.axis("off")

    # Dashed projection box around P.
    for bits in product((0, 1), repeat=3):
        for dim in range(3):
            if bits[dim] == 0:
                next_bits = list(bits)
                next_bits[dim] = 1
                a, b = vertices[bits], vertices[tuple(next_bits)]
                ax.plot(
                    [a[0], b[0]],
                    [a[1], b[1]],
                    color="0.30",
                    linewidth=0.9,
                    linestyle=(0, (2.2, 2.2)),
                    zorder=1,
                )

    # Coordinate axes, with arrowheads extending past the third tick.
    origin = np.zeros(2)
    axis_length = 3.3
    for i, direction in enumerate(basis):
        end = axis_length * direction
        ax.annotate(
            "",
            xy=end,
            xytext=origin,
            arrowprops={
                "arrowstyle": "-|>",
                "lw": 1.25,
                "color": "black",
                "mutation_scale": 13,
            },
            zorder=3,
        )

        # Unit ticks and their numeric labels.
        normal = np.array([-direction[1], direction[0]])
        normal /= np.linalg.norm(normal)
        for n in (1, 2, 3):
            point = n * direction
            half_tick = 0.075 * normal
            ax.plot(
                [point[0] - half_tick[0], point[0] + half_tick[0]],
                [point[1] - half_tick[1], point[1] + half_tick[1]],
                color="black",
                linewidth=0.8,
                zorder=4,
            )
            offset = 0.19 * normal
            ax.text(
                *(point + offset),
                str(n),
                ha="center",
                va="center",
                fontsize=11,
                zorder=4,
            )

        axis_label_pos = end + 0.18 * direction / np.linalg.norm(direction)
        if i == 0:
            axis_label_pos += np.array([-0.02, -0.02])
        elif i == 1:
            axis_label_pos += np.array([0.02, -0.02])
        else:
            axis_label_pos += np.array([0.00, 0.02])
        ax.text(
            *axis_label_pos,
            str(i + 1),
            ha="center",
            va="center",
            fontsize=14,
            fontweight="bold",
            zorder=5,
        )

    # Origin and point P.
    P = vertices[(1, 1, 1)]
    ax.scatter(*origin, s=13, color="black", zorder=6)
    ax.scatter(*P, s=16, color="black", zorder=6)
    ax.text(0.12, -0.12, r"$O$", ha="left", va="top", fontsize=14)
    ax.text(P[0] + 0.15, P[1] + 0.01, r"$P$", ha="left", va="center", fontsize=14)

    # Coordinate labels are placed beside the corresponding axis projections.
    labels = [r"$p_1$", r"$p_2$", r"$p_3$"]
    offsets = [
        np.array([-0.10, -0.25]),
        np.array([0.05, -0.22]),
        np.array([-0.26, 0.02]),
    ]
    for i, label in enumerate(labels):
        q = p[i] * basis[i]
        ax.text(*(q + offsets[i]), label, ha="center", va="center", fontsize=14)

    ax.set_xlim(-2.1, 2.6)
    ax.set_ylim(-1.95, 2.55)

    plt.show()


if __name__ == "__main__":
    draw_figure()
