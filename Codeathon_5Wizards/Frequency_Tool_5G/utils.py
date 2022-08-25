import matplotlib.pyplot as plt
import base64
from io import BytesIO

def get_graph():
    buffer=BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    # print(image_png)
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph


def get_plot(x,y,title,namex,namey):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title("Graphed")
    plt.plot(x,y)
    plt.xticks(rotation=45)
    plt.xlabel(namex)
    plt.ylabel(namey) 
    plt.tight_layout()
    graph = get_graph()
    return graph

def get_single_plot(x,title,namex):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title(title)
    plt.plot(x)
    plt.xticks(rotation=45)
    plt.xlabel(namex)
    plt.tight_layout()
    graph = get_graph()
    return graph


def get_scatter(x,y,title):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title(title)
    plt.scatter(x,y)
    plt.xlabel("SCatter")
    plt.ylabel("YLabel")
    plt.tight_layout()
    graph = get_graph()
    return graph
    

def get_line(x,title,namex):
    plt.switch_backend('AGG')
    plt.figure(figsize=(10,5))
    plt.title(title)
    plt.line(x)
    plt.xlabel(namex)
    plt.ylabel("YLabel")
    plt.tight_layout()
    graph = get_graph()
    return graph
    