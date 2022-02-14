# sci palettes for matplotlib/seaborn


## Installation

```bash
python3 -m pip install sci-palettes
```

## Usage

```python
import seaborn as sns
import matplotlib.pyplot as plt
import sci_palettes


print(sci_palettes.PALETTES.keys())

sci_palettes.register_cmap()          # register all palettes
sci_palettes.register_cmap('aaas')    # register a special palette

# methods for setting palette
plt.set_cmap('aaas')
plt.style.use('aaas')
sns.set_theme(palette='aaas')
sns.set_palette('aaas')

sns.scatterplot(...)

# set palette when plotting
sns.scatterplot(..., palette='aaas')
```

> Full examples in [examples](https://suqingdong.github.io/sci_palettes/examples/test.py)

## Gallery
<details>
    <summary>展开查看</summary>
    <div>
        <h3>AAAS</h3>
        <img src="https://suqingdong.github.io/sci_palettes/examples/aaas.png" />
    </div>
    <div>
        <h3>JAMA</h3>
        <img src="https://suqingdong.github.io/sci_palettes/examples/jama.png" />
    </div>
    <div>
        <h3>NPG</h3>
        <img src="https://suqingdong.github.io/sci_palettes/examples/npg_nrc.png" />
    </div>
    <div>
        <h3>JCO</h3>
        <img src="https://suqingdong.github.io/sci_palettes/examples/jco.png" />
    </div>
    <div>
        <h3>LANCET</h3>
        <img src="https://suqingdong.github.io/sci_palettes/examples/lancet_lanonc.png" />
    </div>
</details>

### Inspired by the R Package [ggsci](https://github.com/nanxstats/ggsci)
