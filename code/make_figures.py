"""
make_figures.py -- builds every Python graph in the report into figures/.

Run from the repository root:
    python code/make_figures.py

Hebrew note: recent matplotlib versions (3.10+) lay out right-to-left text
correctly by themselves. Older versions draw Hebrew backwards; he() detects
the version and reverses the label only when needed. Keep Hebrew labels free
of numbers and brackets; put those in separate English text.
Fonts: repository-local Noto Sans Hebrew and Noto Sans. Their OFL licenses
and static instances are included in fonts/; no system installation is needed.
"""
from pathlib import Path

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib import font_manager
import numpy as np

ROOT = Path(__file__).resolve().parent.parent
FIG = ROOT / "figures"
FIG.mkdir(exist_ok=True)
for font_name in ("NotoSansHebrew-Regular.ttf", "NotoSansHebrew-Bold.ttf",
                  "NotoSans-Regular.ttf", "NotoSans-Bold.ttf"):
    font_manager.fontManager.addfont(ROOT / "fonts" / font_name)

OURS = "המחקר המוצע"

# One palette for the whole report. Change it here (and in template.cls).
ACCENT = "#820000"   # deep Roman red: our solution
SECONDARY = "#330F53"
GREY = "#8A8A8A"     # existing tools
LIGHT = "#FCFBF4"

plt.rcParams.update({
    "font.family": ["Noto Sans Hebrew", "Noto Sans"],
    "font.size": 10,
    "axes.edgecolor": "#444444",
    "axes.linewidth": 0.8,
    "savefig.bbox": "tight",
})


_MPL = tuple(int(p) for p in matplotlib.__version__.split(".")[:2])


def he(text: str) -> str:
    """Return a Hebrew label that matplotlib will show right-to-left."""
    return text if _MPL >= (3, 10) else text[::-1]


# ------------------------------------------------------------------
# Chapter 4 data: the team's assessment of each tool, scale 1-5.
# These are illustrative scores, explained in chapter 4 -- not measurements.
# ------------------------------------------------------------------
AXES = [
    "כיסוי התקופה",
    "מידע על כנסייה ומדינה",
    "נתונים מובנים",
    "גישה פתוחה",
    "קריאה במחשב",
    "ניתוח טקסט",
]
TOOLS = {
    "Seshat":           [3, 2, 5, 4, 5, 1],
    "Perseus / Scaife": [3, 2, 2, 5, 4, 2],
    "dMGH / openMGH":   [3, 4, 2, 5, 4, 1],
    "Pleiades":         [4, 1, 4, 5, 5, 1],
    OURS:   [5, 5, 5, 4, 5, 5],
}

# x = how much of our question the tool answers, y = effort to use it (1-5)
SCATTER = {
    he("קריאה ידנית"):   (4.0, 5.0),
    "Seshat":           (2.0, 2.0),
    "Perseus / Scaife": (2.0, 4.0),
    "dMGH / openMGH":   (3.0, 4.5),
    "Pleiades":         (1.0, 1.5),
    "ORBIS":            (1.0, 1.0),
    "Ithaca":           (1.5, 3.0),
    OURS:   (5.0, 2.5),
}


def radar():
    n = len(AXES)
    angles = np.linspace(0, 2 * np.pi, n, endpoint=False).tolist()
    angles += angles[:1]
    fig, ax = plt.subplots(figsize=(6.2, 5.2), subplot_kw={"polar": True})
    styles = iter(["--", ":", "-.", (0, (6, 2, 1, 2))])
    for name, vals in TOOLS.items():
        v = vals + vals[:1]
        ours = name == OURS
        ax.plot(angles, v, color=ACCENT if ours else GREY,
                linewidth=2.4 if ours else 1.3,
                linestyle="-" if ours else next(styles), label=he(name) if name == OURS else name)
        if ours:
            ax.fill(angles, v, color=ACCENT, alpha=0.15)
    ax.set_xticks(angles[:-1])
    ax.set_xticklabels([he(a) for a in AXES], fontsize=9)
    ax.tick_params(axis="x", pad=10)
    ax.set_theta_offset(np.pi / 2)
    ax.set_theta_direction(-1)
    ax.set_ylim(0, 5)
    ax.set_yticks([1, 2, 3, 4, 5])
    ax.set_yticklabels(["1", "2", "3", "4", "5"], fontsize=7, color="#666666")
    # push side labels away from the circle so they never touch it
    for lbl, ang in zip(ax.get_xticklabels(), angles[:-1]):
        x = np.cos(np.pi / 2 - ang)
        lbl.set_horizontalalignment("left" if x > 0.1 else "right" if x < -0.1 else "center")
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.08), ncol=3,
              frameon=False, fontsize=8)
    fig.savefig(FIG / "ch4-radar.pdf")
    fig.savefig(FIG / "ch4-radar.png", dpi=150)
    plt.close(fig)


def scatter():
    fig, ax = plt.subplots(figsize=(6.2, 4.2))
    for name, (x, y) in SCATTER.items():
        ours = name == OURS
        ax.scatter(x, y, s=140 if ours else 60,
                   color=ACCENT if ours else GREY, zorder=3,
                   edgecolor="white", linewidth=1)
        ax.annotate(he(name) if name in (OURS,) else name, (x, y), textcoords="offset points", xytext=(7, 5),
                    fontsize=8.5, color=ACCENT if ours else "#333333",
                    fontweight="bold" if ours else "normal")
    ax.set_xlim(0, 5.8)
    ax.set_ylim(0, 5.8)
    ax.set_xlabel(he("כמה מהשאלה שלנו הכלי עונה") + "  (1-5)")
    ax.set_ylabel(he("מאמץ השימוש") + "  (1-5)")
    ax.axvspan(3.5, 5.8, ymin=0, ymax=3.25 / 5.8, color=LIGHT, zorder=0)
    ax.text(4.65, 0.35, he("האזור הרצוי"), ha="center", fontsize=8.5, color=ACCENT)
    ax.grid(color="#DDDDDD", linewidth=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    fig.savefig(FIG / "ch4-scatter.pdf")
    fig.savefig(FIG / "ch4-scatter.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------------------------
# Chapter 5: weighted decision matrix and sensitivity analysis.
# Weights were fixed BEFORE scoring (see chapter 5). Scores 1-5.
# ------------------------------------------------------------------
CRITERIA = ["תוקף מדעי", "יכולת שחזור", "כיסוי המקורות", "עלות", "חדשנות"]
WEIGHTS = [0.30, 0.20, 0.20, 0.15, 0.15]
ALTS = {
    "א: מחקר מקורות קלאסי":      [3, 2, 2, 5, 1],
    "ב: מאגר וקידוד ידני":       [5, 4, 3, 2, 3],
    "ג: מאגר וניתוח AI עם תיקוף": [4, 5, 5, 3, 5],
}
CRIT_COLORS = [ACCENT, SECONDARY, "#A97A4C", "#5B7553", "#4A6C8C"]


def weighted(scores, weights):
    return sum(s * w for s, w in zip(scores, weights))


def decision_bars():
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    names = list(ALTS)
    for i, name in enumerate(names):
        left = 0.0
        for j, (sc, w) in enumerate(zip(ALTS[name], WEIGHTS)):
            part = sc * w
            ax.barh(i, part, left=left, color=CRIT_COLORS[j], edgecolor="white",
                    height=0.55, label=he(CRITERIA[j]) if i == 0 else None)
            left += part
        ax.text(left + 0.06, i, f"{left:.2f}", va="center", fontsize=10,
                fontweight="bold", color="#222222")
    ax.set_yticks(range(len(names)))
    ax.set_yticklabels([he(n) for n in names], fontsize=9)
    ax.invert_yaxis()
    ax.set_xlim(0, 5)
    ax.set_xlabel("Weighted score  (0-5)")
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(loc="upper center", bbox_to_anchor=(0.5, -0.25), ncol=5,
              frameon=False, fontsize=8)
    fig.savefig(FIG / "ch5-decision.pdf")
    fig.savefig(FIG / "ch5-decision.png", dpi=150)
    plt.close(fig)


SENS = 0  # criterion to vary: 0 = scientific validity, where C is weakest vs B


def sensitivity():
    """Vary one criterion's weight from 0 to 0.9; the others shrink in proportion."""
    base_other = [w for k, w in enumerate(WEIGHTS) if k != SENS]
    total_other = sum(base_other)
    ws = np.linspace(0, 0.9, 91)
    fig, ax = plt.subplots(figsize=(6.4, 3.4))
    styles = ["--", ":", "-"]
    results = {}
    for (name, sc), st in zip(ALTS.items(), styles):
        ys = []
        for w in ws:
            weights = [bw * (1 - w) / total_other for bw in base_other]
            weights.insert(SENS, w)
            ys.append(weighted(sc, weights))
        results[name] = ys
        ours = name.startswith("ג")
        ax.plot(ws, ys, st, color=ACCENT if ours else GREY,
                linewidth=2.4 if ours else 1.4, label=he(name))
    ax.axvline(WEIGHTS[SENS], color="#444444", linewidth=0.8)
    ax.text(WEIGHTS[SENS] + 0.01, 4.85, he("המשקל שנבחר"), fontsize=8, color="#444444")
    ax.set_xlabel(he("משקל קריטריון התוקף המדעי"))
    ax.set_ylabel("Weighted score")
    ax.set_ylim(1, 5)
    ax.set_xlim(0, 0.9)
    ax.grid(color="#DDDDDD", linewidth=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    ax.legend(frameon=False, fontsize=8, loc="lower left", bbox_to_anchor=(0.0, 0.0))
    # report where (if anywhere) C stops winning
    names = list(ALTS)
    c = results[names[2]]
    for k, w in enumerate(ws):
        best_other = max(results[names[0]][k], results[names[1]][k])
        if c[k] < best_other:
            print(f"  C loses first at weight {w:.2f}")
            ax.axvline(w, color=ACCENT, linewidth=0.8, linestyle=":")
            break
    else:
        print("  C wins across the whole range")
    fig.savefig(FIG / "ch5-sensitivity.pdf")
    fig.savefig(FIG / "ch5-sensitivity.png", dpi=150)
    plt.close(fig)


def random_weights_check(n=10000, seed=1):
    """Draw random weights around the chosen ones; how often does each alternative win?"""
    rng = np.random.default_rng(seed)
    wins = {k: 0 for k in ALTS}
    for _ in range(n):
        w = rng.dirichlet(np.array(WEIGHTS) * 20)
        best = max(ALTS, key=lambda k: weighted(ALTS[k], w))
        wins[best] += 1
    for k, v in wins.items():
        print(f"  {k}: wins {100 * v / n:.1f}% of random weightings")


# ------------------------------------------------------------------
# Chapter 6: Gantt chart of the 12-month research plan.
# MUST match tab:tasks in chapters/06-workplan.tex. Change both together.
# (id, label, start month, end month, critical path?)
# ------------------------------------------------------------------
TASKS = [
    ("1.1", "רשימת המקורות", 1, 1, False),
    ("1.2", "הורדת הטקסטים", 1, 2, False),
    ("1.3", "חלוקה לקטעים ותיוג", 2, 4, True),
    ("2.1", "ספר הגדרות למדדים", 2, 3, False),
    ("2.2", "משתני פיקוח", 3, 6, False),
    ("3.1", "הנחיות לסוכנים", 3, 3, False),
    ("3.2", "פיילוט ותיקוף", 5, 5, True),
    ("3.3", "סיווג מלא", 6, 7, True),
    ("3.4", "הרצה חוזרת", 8, 8, True),
    ("4.1", "איחוד המאגר", 8, 8, True),
    ("4.2", "בדיקת ההשערות", 9, 9, True),
    ("4.3", "ניתוח רגישות", 10, 10, True),
    ("5.1", "דוח התקדמות", 6, 6, False),
    ("5.2", "דוח סיום ומאמר", 11, 12, True),
    ("5.3", "פרסום פתוח", 12, 12, True),
]
MILESTONES = [(5, "תיקוף עבר"), (8, "המאגר מוכן"), (12, "פרסום")]
GREEN = "#3D7A4A"


def gantt():
    fig, ax = plt.subplots(figsize=(6.6, 5.0))
    n = len(TASKS)
    for i, (tid, label, a, b, crit) in enumerate(TASKS):
        ax.barh(i, b - a + 1, left=a - 0.5, height=0.55,
                color=ACCENT if crit else GREY, edgecolor="white")
    ax.set_yticks(range(n))
    ax.set_yticklabels([f"{he(t[1])}  {t[0]}" for t in TASKS], fontsize=8.5)
    ax.invert_yaxis()
    for m, label in MILESTONES:
        ax.axvline(m + 0.5, color=GREEN, linewidth=1, linestyle="--", zorder=0)
        ax.plot(m + 0.5, -1.0, marker="D", color=GREEN, markersize=8, clip_on=False)
        ax.text(m + 0.5, -1.7, he(label), ha="center", fontsize=8, color=GREEN)
    ax.set_xlim(0.5, 12.9)
    ax.set_ylim(n - 0.4, -2.2)
    ax.set_xticks(range(1, 13))
    ax.set_xlabel(he("חודש"))
    ax.grid(axis="x", color="#E3E3E3", linewidth=0.6)
    ax.spines[["top", "right"]].set_visible(False)
    from matplotlib.patches import Patch
    ax.legend(handles=[Patch(color=ACCENT, label=he("שרשרת משוערת")),
                       Patch(color=GREY, label=he("משימה רגילה"))],
              loc="lower left", frameon=False, fontsize=8)
    fig.savefig(FIG / "ch6-gantt.pdf")
    fig.savefig(FIG / "ch6-gantt.png", dpi=150)
    plt.close(fig)


# ------------------------------------------------------------------
# Chapter 7: risk matrix. Probability and severity 1-5, R = P x S.
# MUST match tab:risks and tab:mitigation in chapters/07-risks.tex.
# (id, probability, severity, residual probability, residual severity)
# ------------------------------------------------------------------
RISKS = [
    ("R1", 4, 4, 3, 3),   # source bias: texts written by churchmen
    ("R2", 3, 5, 2, 3),   # AI classification errors
    ("R3", 4, 3, 2, 2),   # missing data for the 5th-century West
    ("R4", 3, 4, 2, 2),   # anachronistic measures
    ("R5", 2, 4, 1, 3),   # expert not available for validation
    ("R6", 3, 2, 2, 2),   # token costs above budget
]


def risk_matrix():
    fig, ax = plt.subplots(figsize=(5.6, 4.8))
    for p in range(1, 6):
        for sv in range(1, 6):
            r = p * sv
            color = "#E8B4B4" if r >= 12 else "#F3E3C3" if r >= 6 else "#DCE8D5"
            ax.add_patch(plt.Rectangle((sv - 0.5, p - 0.5), 1, 1, color=color,
                                       ec="white", lw=1.5, zorder=0))
            # score in the top-left corner of its own cell
            ax.text(sv - 0.42, p + 0.42, str(r), fontsize=6.5, color="#777777",
                    ha="left", va="top")

    def spread(points):
        """Offsets so several markers in one cell sit side by side."""
        cells = {}
        for rid, x, y in points:
            cells.setdefault((x, y), []).append(rid)
        pos = {}
        for (x, y), ids in cells.items():
            n = len(ids)
            for k, rid in enumerate(ids):
                pos[rid] = (x + (k - (n - 1) / 2) * 0.32, y)
        return pos

    before = spread([(rid, sv, p) for rid, p, sv, rp, rs in RISKS])
    after = spread([(rid, rs, rp) for rid, p, sv, rp, rs in RISKS])
    for rid, *_ in RISKS:
        (x0, y0), (x1, y1) = before[rid], after[rid]
        ax.annotate("", xy=(x1, y1), xytext=(x0, y0),
                    arrowprops=dict(arrowstyle="-|>", color="#555555", lw=0.9,
                                    linestyle=(0, (3, 2)), shrinkA=9, shrinkB=7))
        ax.scatter(x0, y0, s=290, color=ACCENT, zorder=3, edgecolor="white")
        ax.text(x0, y0, rid, ha="center", va="center", fontsize=7.5,
                color="white", fontweight="bold", zorder=4)
        ax.scatter(x1, y1, s=190, facecolor="white", edgecolor="#555555", zorder=3)
        ax.text(x1, y1, rid, ha="center", va="center", fontsize=6.5,
                color="#333333", zorder=4)
    ax.set_xlim(0.5, 5.5); ax.set_ylim(0.5, 5.5)
    ax.set_xticks(range(1, 6)); ax.set_yticks(range(1, 6))
    ax.set_xlabel(he("חומרה"))
    ax.set_ylabel(he("הסתברות"))
    ax.set_aspect("equal")
    for side in ax.spines.values():
        side.set_visible(False)
    from matplotlib.lines import Line2D
    ax.legend(handles=[
        Line2D([], [], marker="o", color="w", markerfacecolor=ACCENT, markersize=10,
               label=he("לפני ההפחתה")),
        Line2D([], [], marker="o", color="w", markerfacecolor="white",
               markeredgecolor="#555555", markersize=9, label=he("אחרי ההפחתה")),
    ], loc="upper center", bbox_to_anchor=(0.5, -0.12), ncol=2, frameon=False, fontsize=8)
    fig.savefig(FIG / "ch7-risk-matrix.pdf")
    fig.savefig(FIG / "ch7-risk-matrix.png", dpi=150)
    plt.close(fig)


if __name__ == "__main__":
    radar()
    scatter()
    for k, v in ALTS.items():
        print(f"  {k}: {weighted(v, WEIGHTS):.2f}")
    decision_bars()
    sensitivity()
    random_weights_check()
    gantt()
    risk_matrix()
    print("figures written to", FIG)
