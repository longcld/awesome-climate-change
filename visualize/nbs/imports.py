import plotly.graph_objects as go
import plotly.express as px
import matplotlib.pyplot as plt
import pandas as pd
from pathlib import Path

Path.ls = lambda x : [o.name for o in x.iterdir()]
Path.ls_p = lambda x : [str(o) for o in x.iterdir()]
Path.str = lambda x : str(x)

plt.rcParams['figure.figsize'] = (12, 8)