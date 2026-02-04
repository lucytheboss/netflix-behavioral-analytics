import matplotlib.pyplot as plt
import seaborn as sns

NETFLIX_RED = "#E50914"
GRAY = "#BDBDBD"


def set_netflix_theme():
    sns.set_style("whitegrid")

    plt.rcParams.update({

        # backgrounds
        "figure.facecolor": "white",
        "axes.facecolor": "white",

        # text
        "text.color": "#222222",
        "axes.labelcolor": "#222222",
        "xtick.color": "#555555",
        "ytick.color": "#555555",

        # grid
        "grid.color": "#ECECEC",

        # IMPORTANT: neutral palette only
        # (do NOT put red here)
        "axes.prop_cycle": plt.cycler(color=[
            GRAY, GRAY, GRAY, GRAY
        ]),

        "axes.edgecolor": "#DDDDDD",
        "axes.linewidth": 1,
        "font.size": 11,
    })


def highlight_top_n(ax, n=1, color=NETFLIX_RED):
    """
    Highlight top N bars in a bar plot.
    Assumes bars are already sorted descending.
    """
    bars = ax.patches

    for i, bar in enumerate(bars):
        if i < n:
            bar.set_color(color)
        else:
            bar.set_color(GRAY)