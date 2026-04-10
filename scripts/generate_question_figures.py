from __future__ import annotations

import math
from collections import Counter, defaultdict
from pathlib import Path

import numpy as np
from PIL import Image, ImageDraw, ImageFont


ROOT = Path(__file__).resolve().parents[1]
OUT = ROOT / "assets" / "generated-figures"

BG = "#f7f3ec"
PLOT_BG = "#fffdfa"
FRAME = "#e3dbd0"
GRID = "#e8e0d5"
INK = "#2f2720"
MUTED = "#786f64"
ACCENT = "#c98256"
ACCENT_2 = "#7f8bd5"
SUCCESS = "#5a8a74"
WARM = "#c26e49"

FONT_SANS = "/System/Library/Fonts/Supplemental/Arial.ttf"
FONT_SERIF = "/System/Library/Fonts/Supplemental/Times New Roman.ttf"


def font(size: int, *, serif: bool = False, bold: bool = False) -> ImageFont.FreeTypeFont:
    path = FONT_SERIF if serif else FONT_SANS
    if bold and not serif:
        bold_path = "/System/Library/Fonts/Supplemental/Arial Bold.ttf"
        if Path(bold_path).exists():
            path = bold_path
    return ImageFont.truetype(path, size)


def canvas(width: int, height: int) -> tuple[Image.Image, ImageDraw.ImageDraw]:
    image = Image.new("RGBA", (width, height), BG)
    draw = ImageDraw.Draw(image)
    draw.rounded_rectangle((0, 0, width - 1, height - 1), radius=22, outline=FRAME, width=2, fill=PLOT_BG)
    return image, draw


def save(image: Image.Image, name: str) -> None:
    OUT.mkdir(parents=True, exist_ok=True)
    image.save(OUT / name, optimize=True)


def draw_multiline(
    draw: ImageDraw.ImageDraw,
    text: str,
    xy: tuple[float, float],
    *,
    width: int,
    line_height: int,
    fill: str = INK,
    font_obj: ImageFont.ImageFont | None = None,
) -> None:
    font_obj = font_obj or font(18)
    words = text.split()
    lines: list[str] = []
    current = ""
    for word in words:
        proposal = f"{current} {word}".strip()
        if draw.textlength(proposal, font=font_obj) <= width or not current:
            current = proposal
        else:
            lines.append(current)
            current = word
    if current:
        lines.append(current)
    x, y = xy
    for line in lines:
        draw.text((x, y), line, fill=fill, font=font_obj)
        y += line_height


class PlotArea:
    def __init__(self, box: tuple[int, int, int, int], xlim: tuple[float, float], ylim: tuple[float, float]):
        self.left, self.top, self.right, self.bottom = box
        self.xmin, self.xmax = xlim
        self.ymin, self.ymax = ylim

    def x(self, value: float) -> float:
        span = self.xmax - self.xmin or 1
        return self.left + (value - self.xmin) / span * (self.right - self.left)

    def y(self, value: float) -> float:
        span = self.ymax - self.ymin or 1
        return self.bottom - (value - self.ymin) / span * (self.bottom - self.top)


def draw_plot_frame(
    draw: ImageDraw.ImageDraw,
    area: PlotArea,
    *,
    x_ticks: list[float],
    y_ticks: list[float],
    x_label: str | None = None,
    y_label: str | None = None,
    y_format: str = "{:.0f}",
    x_format: str = "{:.0f}",
) -> None:
    draw.rounded_rectangle(
        (area.left, area.top, area.right, area.bottom),
        radius=18,
        outline=FRAME,
        width=1,
        fill="#fffefd",
    )
    for tick in y_ticks:
        y = area.y(tick)
        draw.line((area.left, y, area.right, y), fill=GRID, width=1)
        label = y_format.format(tick)
        draw.text((area.left - 36, y - 8), label, fill=MUTED, font=font(14))
    for tick in x_ticks:
        x = area.x(tick)
        draw.line((x, area.bottom, x, area.top), fill=GRID, width=1)
        label = x_format.format(tick)
        draw.text((x - 10, area.bottom + 8), label, fill=MUTED, font=font(14))
    draw.line((area.left, area.bottom, area.right, area.bottom), fill=INK, width=2)
    draw.line((area.left, area.top, area.left, area.bottom), fill=INK, width=2)
    if x_label:
        draw.text(((area.left + area.right) / 2 - 18, area.bottom + 32), x_label, fill=MUTED, font=font(14))
    if y_label:
        draw.text((area.left - 54, area.top - 26), y_label, fill=MUTED, font=font(14))


def draw_bars(
    draw: ImageDraw.ImageDraw,
    area: PlotArea,
    labels: list[str],
    values: list[float],
    *,
    fill: str = ACCENT,
    max_value: float | None = None,
) -> None:
    max_value = max_value if max_value is not None else max(values)
    n = len(labels)
    slot = (area.right - area.left) / n
    bar_width = slot * 0.62
    for idx, (label, value) in enumerate(zip(labels, values)):
        center = area.left + slot * idx + slot / 2
        x1 = center - bar_width / 2
        x2 = center + bar_width / 2
        y = area.y(value)
        draw.rounded_rectangle((x1, y, x2, area.bottom), radius=10, fill=fill, outline=None)
        draw.text((center - draw.textlength(label, font=font(13)) / 2, area.bottom + 8), label, fill=INK, font=font(13))


def draw_points(
    draw: ImageDraw.ImageDraw,
    area: PlotArea,
    points: list[tuple[float, float]],
    *,
    color: str = ACCENT,
    radius: int = 6,
) -> None:
    for x_value, y_value in points:
        x = area.x(x_value)
        y = area.y(y_value)
        draw.ellipse((x - radius, y - radius, x + radius, y + radius), fill=color, outline="#ffffff", width=1)


def draw_line(
    draw: ImageDraw.ImageDraw,
    area: PlotArea,
    fn,
    *,
    color: str = ACCENT,
    width: int = 3,
    start: float | None = None,
    end: float | None = None,
) -> None:
    start = area.xmin if start is None else start
    end = area.xmax if end is None else end
    samples = np.linspace(start, end, 160)
    mapped = []
    for x_value in samples:
        y_value = fn(float(x_value))
        if area.ymin - 1 <= y_value <= area.ymax + 1:
            mapped.append((area.x(float(x_value)), area.y(float(y_value))))
    if len(mapped) >= 2:
        draw.line(mapped, fill=color, width=width)


def make_pareto_choices() -> None:
    counts = {"A": 750, "MS": 72, "LS": 244, "SS": 827, "S": 29}
    orders = {
        "q5-part1-a.png": ["S", "MS", "LS", "A", "SS"],
        "q5-part1-b.png": ["A", "SS", "S", "MS", "LS"],
        "q5-part1-c.png": ["LS", "S", "MS", "SS", "A"],
        "q5-part1-d.png": ["SS", "A", "LS", "MS", "S"],
    }
    for filename, order in orders.items():
        image, draw = canvas(560, 360)
        area = PlotArea((64, 32, 518, 286), (0, len(order)), (0, 900))
        draw_plot_frame(draw, area, x_ticks=[], y_ticks=[0, 300, 600, 900], y_label="Frequency")
        draw_bars(draw, area, order, [counts[key] for key in order], max_value=900)
        save(image, filename)


def make_stem_leaf_figure() -> None:
    image, draw = canvas(560, 360)
    left = 96
    top = 72
    draw.text((left, top), "Stem", fill=INK, font=font(24, bold=True))
    draw.text((left + 180, top), "Leaf", fill=INK, font=font(24, bold=True))
    draw.line((left, top + 38, left + 360, top + 38), fill=FRAME, width=2)
    rows = [("3", "788"), ("2", "4888"), ("1", "0448"), ("0", "056")]
    y = top + 62
    for stem, leaf in rows:
        draw.text((left + 24, y), stem, fill=INK, font=font(28, serif=True))
        draw.line((left + 130, top + 18, left + 130, y + 38), fill=FRAME, width=2)
        draw.text((left + 176, y), leaf, fill=INK, font=font(28, serif=True))
        y += 54
    save(image, "q6-stem-leaf.png")


def make_dotplot(filename: str, values: list[int]) -> None:
    image, draw = canvas(560, 300)
    area = PlotArea((54, 36, 520, 228), (0, 40), (0, max(Counter(values).values()) + 1))
    draw_plot_frame(draw, area, x_ticks=list(range(0, 41, 10)), y_ticks=[], x_label="Value")
    counts = defaultdict(int)
    for value in sorted(values):
        counts[value] += 1
        x = area.x(value)
        y = area.y(counts[value] - 0.2)
        draw.ellipse((x - 7, y - 7, x + 7, y + 7), fill=ACCENT, outline="#fff", width=1)
    save(image, filename)


def make_q6_dotplots() -> None:
    datasets = {
        "q6-partc-a.png": [0, 5, 6, 10, 14, 18, 24, 28, 28, 37, 37, 38, 38, 38],
        "q6-partc-b.png": [0, 5, 6, 10, 14, 14, 18, 24, 28, 28, 28, 37, 38, 38],
        "q6-partc-c.png": [0, 5, 6, 6, 14, 14, 18, 24, 24, 28, 28, 28, 37, 38],
        "q6-partc-d.png": [6, 10, 14, 16, 18, 20, 22, 24, 26, 28, 30, 32, 34, 36],
    }
    for filename, values in datasets.items():
        make_dotplot(filename, values)


def make_shape_histograms() -> None:
    variants = {
        "q7-partc-a.png": [7, 6, 4, 3, 2, 1],
        "q7-partc-b.png": [1, 2, 3, 4, 6, 7],
        "q7-partc-c.png": [1, 3, 5, 5, 3, 1],
        "q7-partc-d.png": [3, 3, 3, 3, 3, 3],
    }
    for filename, heights in variants.items():
        image, draw = canvas(420, 280)
        area = PlotArea((48, 26, 388, 220), (0, len(heights)), (0, 8))
        draw_plot_frame(draw, area, x_ticks=[], y_ticks=[0, 2, 4, 6, 8], y_label="Freq")
        draw_bars(draw, area, ["" for _ in heights], heights, max_value=8)
        save(image, filename)


def make_q7_histogram_question() -> None:
    data = [
        1.23, 2.86, 1.66, 1.99, 1.31, 1.41, 1.77, 2.91, 2.56, 1.41,
        3.43, 2.34, 3.29, 1.41, 2.01, 1.23, 2.47, 2.14, 2.18, 1.39,
    ]
    bins = np.arange(1.0, 3.81, 0.4)
    counts, _ = np.histogram(data, bins=bins)
    labels = [f"{edge:.1f}" for edge in bins[:-1]]
    image, draw = canvas(600, 340)
    area = PlotArea((62, 34, 556, 258), (0, len(counts)), (0, max(counts) + 1))
    draw_plot_frame(draw, area, x_ticks=[], y_ticks=list(range(0, max(counts) + 2)), x_label="Index")
    draw_bars(draw, area, labels, counts.tolist(), max_value=max(counts) + 1)
    save(image, "q7-question-histogram.png")


def make_line_graph(filename: str, equation) -> None:
    image, draw = canvas(360, 360)
    area = PlotArea((54, 30, 320, 292), (-10, 10), (-10, 10))
    draw_plot_frame(draw, area, x_ticks=[-10, 0, 10], y_ticks=[-10, 0, 10])
    draw.line((area.x(0), area.top, area.x(0), area.bottom), fill=INK, width=2)
    draw.line((area.left, area.y(0), area.right, area.y(0)), fill=INK, width=2)
    draw_line(draw, area, equation, color=ACCENT, width=4)
    save(image, filename)


def make_q13_line_choices() -> None:
    equations = {
        "q13-parta-a.png": lambda x: x + 6,
        "q13-parta-b.png": lambda x: x - 6,
        "q13-parta-c.png": lambda x: 6 - 3 * x,
        "q13-parta-d.png": lambda x: 3 * x - 6,
        "q13-partb-a.png": lambda x: 2 * x - 6,
        "q13-partb-b.png": lambda x: 6 - 3 * x,
        "q13-partb-c.png": lambda x: -x,
        "q13-partb-d.png": lambda x: 3 * x + 6,
        "q13-partc-a.png": lambda x: x - 5,
        "q13-partc-b.png": lambda x: -5 * x,
        "q13-partc-c.png": lambda x: -x + 6,
        "q13-partc-d.png": lambda x: 5 * x,
    }
    for filename, fn in equations.items():
        make_line_graph(filename, fn)


def make_scatter_image(
    filename: str,
    points: list[tuple[float, float]],
    *,
    line=None,
    line_color: str = ACCENT_2,
) -> None:
    image, draw = canvas(400, 320)
    area = PlotArea((56, 28, 360, 258), (-4, 10), (0, 10))
    draw_plot_frame(draw, area, x_ticks=[-4, 0, 5, 10], y_ticks=[0, 5, 10], x_label="x", y_label="y")
    draw.line((area.x(0), area.top, area.x(0), area.bottom), fill=INK, width=2)
    draw.line((area.left, area.y(0), area.right, area.y(0)), fill=INK, width=2)
    if line is not None:
        draw_line(draw, area, line, color=line_color, width=3)
    draw_points(draw, area, points)
    save(image, filename)


def make_q15_scatter_choices() -> None:
    correct = [(5, 3), (4, 5), (-2, 0), (2, 1), (8, 9), (5, 4), (4, 3)]
    options = {
        "q15-parta-a.png": [(1, 1), (2, 3), (3, 4), (4, 5), (5, 7), (6, 8)],
        "q15-parta-b.png": [(0, 9), (1, 1), (3, 3), (4, 5), (5, 4), (8, 0)],
        "q15-parta-c.png": [(-2, 9), (0, 8), (2, 6), (4, 5), (6, 3), (8, 1)],
        "q15-parta-d.png": correct,
    }
    for filename, points in options.items():
        make_scatter_image(filename, points)

    lines = {
        "q15-partc-a.png": lambda x: 0.6 * x + 1.6,
        "q15-partc-b.png": lambda x: -0.85 * x + 6.3,
        "q15-partc-c.png": lambda x: 0.838 * x + 0.458,
        "q15-partc-d.png": lambda x: 4.0,
    }
    for filename, line in lines.items():
        make_scatter_image(filename, correct, line=line)


def make_q18_scatterplots() -> None:
    image, draw = canvas(680, 760)
    panels = [
        ((84, 48, 580, 238), "Cooperation use", [
            (12, 0.42), (20, 0.02), (22, 0.74), (28, -0.24), (30, 0.28), (33, 0.36),
            (37, -0.31), (42, 0.84), (44, -0.04), (46, 0.79), (51, 0.82), (55, 0.39),
            (56, 1.02), (57, -0.22), (59, 0.41), (60, 0.14), (62, -0.14), (71, -0.18),
        ]),
        ((84, 292, 580, 482), "Defection use", [
            (10, 0.1), (14, 0.48), (16, -0.1), (20, 0.3), (22, -0.02), (28, 0.65),
            (31, -0.25), (35, 0.06), (39, -0.34), (44, -0.18), (48, -0.4), (54, 0.51),
            (54, 0.46), (58, 0.21), (61, -0.19), (66, 0.61), (68, 0.28), (77, -0.16),
        ]),
        ((84, 536, 580, 726), "Punishment use", [
            (0.3, 0.74), (0.5, 0.69), (0.9, 0.5), (1.0, 0.25), (2.0, -0.3), (3.1, -0.34),
            (4.2, -0.32), (5.0, -0.27), (6.0, -0.13), (8.7, 0.2), (10.0, -0.21), (12.5, -0.1),
            (15.5, -0.37), (17.0, 0.01), (18.1, -0.2), (19.0, -0.28),
        ]),
    ]
    for box, xlabel, points in panels:
        area = PlotArea(box, (0, 80 if "Punishment" not in xlabel else 20), (-0.4, 0.8))
        draw_plot_frame(
            draw,
            area,
            x_ticks=[0, 20, 40, 60, 80] if "Punishment" not in xlabel else [0, 5, 10, 15, 20],
            y_ticks=[-0.4, 0.0, 0.4, 0.8],
            x_label=xlabel,
            y_label="Avg payoff",
            y_format="{:.1f}",
        )
        if "Punishment" in xlabel:
            draw_line(draw, area, lambda x: 0.18 - 0.03 * x, color=WARM, width=3)
        draw_points(draw, area, points, color=ACCENT_2, radius=5)
        letter = "abc"[panels.index((box, xlabel, points))]
        draw.text((box[0] - 34, box[1] + 4), f"{letter}.", fill=INK, font=font(18, bold=True))
    save(image, "q18-scatterplots.png")


def make_venn(filename: str, mode: str) -> None:
    image, draw = canvas(320, 240)
    box = (42, 40, 278, 196)
    draw.rectangle(box, outline=INK, width=2)
    if mode == "disjoint":
        draw.ellipse((60, 92, 146, 176), outline=INK, width=2)
        draw.ellipse((160, 52, 252, 144), outline=INK, width=2)
    elif mode == "a-in-b":
        draw.ellipse((74, 42, 246, 186), outline=INK, width=2)
        draw.ellipse((116, 84, 204, 168), outline=INK, width=2)
    elif mode == "overlap":
        draw.ellipse((56, 72, 164, 180), outline=INK, width=2)
        draw.ellipse((134, 72, 242, 180), outline=INK, width=2)
    elif mode == "b-in-a":
        draw.ellipse((74, 42, 246, 186), outline=INK, width=2)
        draw.ellipse((124, 82, 212, 166), outline=INK, width=2)
    label_positions = {
        "disjoint": ((90, 124), (196, 84)),
        "a-in-b": ((150, 118), (150, 60)),
        "overlap": ((90, 112), (184, 112)),
        "b-in-a": ((146, 58), (160, 112)),
    }
    pos_a, pos_b = label_positions[mode]
    draw.text(pos_a, "A", fill=INK, font=font(24, bold=True))
    draw.text(pos_b, "B", fill=INK, font=font(24, bold=True))
    save(image, filename)


def make_q21_venn_choices() -> None:
    make_venn("q21-parta-a.png", "disjoint")
    make_venn("q21-parta-b.png", "a-in-b")
    make_venn("q21-parta-c.png", "overlap")
    make_venn("q21-parta-d.png", "b-in-a")


def make_q27_histogram() -> None:
    image, draw = canvas(520, 330)
    values = [22, 23, 24, 25, 26]
    probs = [0.10, 0.15, 0.25, 0.25, 0.25]
    area = PlotArea((58, 34, 480, 252), (0, len(values)), (0, 0.40))
    draw_plot_frame(draw, area, x_ticks=[], y_ticks=[0.0, 0.1, 0.2, 0.3, 0.4], x_label="x", y_label="Relative frequency", y_format="{:.2f}")
    draw_bars(draw, area, [str(v) for v in values], probs, max_value=0.40)
    save(image, "q27-histogram.png")


def make_q31_normality_choices() -> None:
    image, draw = canvas(420, 280)
    left = 74
    top = 50
    draw.text((left, top), "Stem", fill=INK, font=font(20, bold=True))
    draw.text((left + 140, top), "Leaves", fill=INK, font=font(20, bold=True))
    draw.line((left, top + 34, left + 268, top + 34), fill=FRAME, width=2)
    rows = [("3", "0 3 9"), ("4", "2 4 7 7"), ("5", "1 3 4 8 8 9 9 9"), ("6", "0 0 5 6 6 7 8"), ("7", "1 1 5"), ("8", "2 7")]
    y = top + 52
    for stem, leaves in rows:
        draw.text((left + 16, y), stem, fill=INK, font=font(20, serif=True))
        draw.line((left + 86, top + 16, left + 86, y + 22), fill=FRAME, width=2)
        draw.text((left + 112, y), leaves, fill=INK, font=font(18, serif=True))
        y += 30
    save(image, "q31-choice-c.png")

    image, draw = canvas(420, 280)
    area = PlotArea((60, 34, 360, 230), (-2.5, 2.5), (0, 10))
    draw_plot_frame(draw, area, x_ticks=[], y_ticks=[], x_label="Expected z-values", y_label="Ranked observations")
    pts = [(-2.0, 1.4), (-1.6, 2.2), (-1.4, 2.4), (-1.0, 3.2), (-0.6, 3.1), (-0.2, 4.6), (0.0, 4.3), (0.2, 5.2), (0.5, 5.5), (0.8, 6.2), (1.0, 6.7), (1.2, 7.1), (1.4, 7.8), (1.5, 8.1), (1.7, 8.6), (1.9, 8.9)]
    draw.line((area.x(-2.1), area.y(1.0), area.x(2.0), area.y(9.1)), fill=GRID, width=2)
    draw_points(draw, area, pts, color=ACCENT_2, radius=5)
    save(image, "q31-choice-d.png")


def make_q36_sampling_histograms() -> None:
    rng = np.random.default_rng(42)
    population = np.arange(100)
    sample_sizes = [2, 5, 10, 30, 50]
    image, draw = canvas(720, 980)
    panel_height = 160
    top = 40
    for idx, n in enumerate(sample_sizes):
        samples = rng.choice(population, size=(500, n), replace=True)
        means = samples.mean(axis=1)
        counts, edges = np.histogram(means, bins=np.arange(0, 102, 2))
        rel = counts / counts.sum()
        max_rel = max(float(rel.max()), 0.05)
        area = PlotArea((84, top + idx * 178, 640, top + idx * 178 + panel_height), (0, 100), (0, max_rel * 1.18))
        y_ticks = [0.00, round(max_rel / 2, 2), round(max_rel, 2)]
        draw_plot_frame(draw, area, x_ticks=[0, 25, 50, 75, 100], y_ticks=y_ticks, x_label="x̄", y_label="Rel. freq.", y_format="{:.2f}")
        for bar_idx, value in enumerate(rel):
            if value <= 0:
                continue
            x1 = area.x(float(edges[bar_idx]))
            x2 = area.x(float(edges[bar_idx + 1])) - 1
            y = area.y(float(value))
            draw.rounded_rectangle((x1, y, x2, area.bottom), radius=4, fill=ACCENT_2)
        label = f"n = {n}"
        draw.text((area.right - 70, area.top + 12), label, fill=INK, font=font(18, bold=True))
    save(image, "q36-sampling-histograms.png")


def main() -> None:
    make_pareto_choices()
    make_stem_leaf_figure()
    make_q6_dotplots()
    make_shape_histograms()
    make_q7_histogram_question()
    make_q13_line_choices()
    make_q15_scatter_choices()
    make_q18_scatterplots()
    make_q21_venn_choices()
    make_q27_histogram()
    make_q31_normality_choices()
    make_q36_sampling_histograms()
    print(f"Generated figures in {OUT}")


if __name__ == "__main__":
    main()
