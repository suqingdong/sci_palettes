import seaborn as sns
import matplotlib.pyplot as plt

import sci_palettes


sci_palettes.register_cmap()

diamonds = sns.load_dataset("diamonds")
f, ax = plt.subplots(figsize=(6.5, 6.5))
sns.despine(f, left=True, bottom=True)
clarity_ranking = ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]


def scatterplot(palette=None):
    sns.scatterplot(
        x="carat",
        y="price",
        hue="clarity",
        size="depth",
        hue_order=clarity_ranking,
        sizes=(1, 8),
        linewidth=0,
        data=diamonds,
        ax=ax,
        palette=palette,
        legend=False,
    )
    plt.savefig(f'{palette}.png', dpi=300)


for name in sci_palettes.PALETTES.keys():
    scatterplot(name)
