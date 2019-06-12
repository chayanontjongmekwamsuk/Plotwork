from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
from matplotlib.dates import DateFormatter

import pandas as pd
from pandas import DataFrame

def graph(request):
    fig = Figure()
    ax = fig.add_subplot(111)
    data_df = pd.read_csv("crime.csv")
    data_df = pd.DataFrame(data_df)
    data_df.plot(ax=ax)
    canvas = FigureCanvas(Fig)
    response = HttpResponse(content_type='image/png')
    canvas.print_png(response)
    return response
