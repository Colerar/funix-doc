from typing import List
import matplotlib.pyplot as plt
from matplotlib.figure import Figure

import funix

@funix.funix(
        widgets={
                "a": "sheet",
                "b": ["sheet", "slider[0,1,0.1]"]
        }
)

# A simple matplotlib function 
def table_plot(
        a: List[int]=[5,17,29], 
        b: List[float]=[3.1415, 2.6342, 1.98964]
    ) -> Figure:
    fig = plt.figure()
    plt.plot(a, b)
    return fig
