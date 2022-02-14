import seaborn as sns
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors


from .palettes import PALETTES


color2rgb = mcolors.ColorConverter().to_rgb


def register_cmap(name=None):
    palettes_list = PALETTES.items()
    if name in PALETTES:
        palettes_list = [(name, PALETTES[name])]

    for name, colors in palettes_list:
        cmap = mcolors.ListedColormap(list(map(color2rgb, colors.values())), name=name)
        plt.register_cmap(cmap=cmap)
