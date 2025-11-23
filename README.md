# Jupytext and Marimo

[Marimo](https://marimo.io/), in addition to their notebook editor, offers an alternative format for Python notebooks. Each cell of the notebook is saved as a Python function. 

I am planning to add the Marimo format to Jupytext v1.19. Marimo will be directly responsible for the conversion, (Jupytext runs `marimo convert` and `marimo export ipynb --sort top-down` under the hood). Yet I think that an integration of the Marimo format in Jupytext will help Marimo users navigate between their Marimo and their Jupyter notebooks.

With this feature, a `.py` marimo notebook can be opened in Jupyter Lab (with a right click / open with Notebook). Also, an `.ipynb` notebook can now be _paired_ to a `py:marimo` notebook, using either the Jupytext menu, or a Jupytext configuration file with this content:
```
formats = "ipynb,py:marimo"
```

The addition of the Marimo format to Jupytext also means that you can use `jupytext --sync` to maintain paired files in sync.

I am looking for feedback from Marimo users. Do you need to maintain some compatibility with Jupyter? How do you find the proposed integration? You can leave your comments on this dedicated [issue](https://github.com/mwouts/jupytext/issues/1470).

## Installation

To get started with the Marimo format in Jupytext, you will need to get the development version of Jupytext, and a recent version of Marimo, with either
```
pip install 'jupytext>=1.19.0.dev0' marimo
```
or
```
uv add 'jupytext>=1.19.0.dev0' marimo
```

## Example

This repository has a Marimo notebook at [`notebook.mo.py`](notebook.mo.py), in the Marimo format, which is paired to two others notebook files: [`notebook.ipynb`](notebook.ipynb) (classic Jupyter notebook format), and to a standard percent notebook [`notebook.pct.py`](notebook.pct.py).

The most recent edits can be propagated to the others files using
```
jupytext --sync notebook.pct.py  # or any other paired file
```

In our example, we use a custom [`jupytext.toml`](jupytext.toml) file that pairs the three files, but of course you can use just `formats = "ipynb,py:marimo"` if you don't need the percent format.
```
formats = "ipynb,.pct.py:percent,.mo.py:marimo"
```

## Quick tutorial

This is how the example notebook was created and run:
1. Create a dedicated Python environment with `uv init` and `uv add 'jupytext>=1.19.0.dev0' marimo pandas plotly jupyterlab`.
2. Create a `jupytext.toml` file with the content above
3. In VS Code, create a new file `notebook.pct.py` and give the following instruction to Copilot:
> Create a 'percent' notebook that shows the evolution of the world population, using the world bank data and plotly for plots. I want to see the total population as stacked area plots, with one color per continent.
4. Launch Jupyter Lab with `uv run jupyter lab` and open the `notebook.pct.py` notebook with a right click. Run it and save it. This creates the other two files. Or, alternatively, run `uv run jupytext --sync notebook.pct.py`.
5. Run the Marimo version with `uv run marimo edit notebook.mo.py`. If you make changes, these changes will only be reflected on `notebook.mo.py`, but Jupyter will be aware of them the next time it loads the notebook, and you can propagate them manually using `jupytext --sync`, too.

## Reach out

Please leave your comments on the dedicated [issue](https://github.com/mwouts/jupytext/issues/1470), or later on when the feature has shipped, please report any issue on the Jupytext tracker.