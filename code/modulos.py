### -------------------------------------
### MODULOS PARA LA ACTIVIDAD DE EXOPLANETAS
### L. Cano
### -------------------------------------

# Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt


def show_tab(n = 5):
    """
    Muestra la tabla original de datos con 'n' entradas.
    """
    d = pd.read_csv("../data/data.csv")
    return d.head()

def show_methods():
    d = pd.read_csv("../data/data.csv")

    #print(d.columns)
    methods = d.discoverymethod.unique()
    method_groups = []
    method_counts = []
    for i in methods:
        df = d[d.discoverymethod == i]
        method_groups.append(df)
        method_counts.append(len(df))
        #print(i, "--->", len(df), " exoplanets")


    df = pd.DataFrame(list(zip(methods, method_counts)), columns = ["Method", "Number"])
    return df

def grouped_methods(num = 100):
    d = pd.read_csv("../data/data.csv")

    #print(d.columns)
    methods = d.discoverymethod.unique()
    method_groups = []
    method_counts = []
    other_group = []
    m = []
    for i in methods:
        df = d[d.discoverymethod == i]
        if len(df) < num:
            aux = df.copy()
            aux["m_g"] = "Other"
            other_group.append(aux)
        else:
            aux = df.copy()
            aux["m_g"] = i
            m.append(i)
            method_groups.append(aux)
            method_counts.append(len(df))
            
    other = pd.concat(other_group, ignore_index = True, axis = 0)
    method_groups.append(other)
    m.append("Others")
    method_counts.append(len(other))
    d_grouped = pd.concat(method_groups, ignore_index=True, axis=0)
    met = pd.DataFrame(list(zip(m, method_counts)), columns = ["Method", "Number"])
    return met, d_grouped

def plot_funcs(ax, fig, grid = False, save = False, savename = ''):
    if grid:
        ax.grid()
    if save:
        fig.savefig(f"../figs/{savename}.png", dpi = 300)
    
    return


def gen_year_histo(anual, grid = False, save = False, savename = ''):
    d = pd.read_csv("../data/data.csv")
    fig1, ax = plt.subplots()
    if anual:
        yearmin = d.disc_year.min()
        yearmax = d.disc_year.max()
        bns = range(yearmin, yearmax)
        ax.hist(d.disc_year, bins = bns)
    else:
        ax.hist(d.disc_year)
    ax.set_ylabel("Exoplanetas descubiertos")
    ax.set_xlabel("Año")
    plot_funcs(ax, fig1, grid, save, savename)
    fig1.show()
    return


def sep_year_histo(d_grouped, grid = False, save = False, savename = '', hwc = False):
    """Generates a stacked histogram for exoplanet detection method.

    Args:
        d_grouped (DataFrame): DataFrame from grouped_methods
        grid (bool, optional): Show grid. Defaults to False.
        save (bool, optional): Save plot using savename name. Defaults to False.
        savename (str, optional): Name of the plot to save. Defaults to ''.
        hwc (bool, optional): Only use habitable exoplanets. Defaults to False.
    """
    if hwc:
        d_grouped = d_grouped[d_grouped.hwc == 1]
    yearmin = d_grouped.disc_year.min()
    yearmax = d_grouped.disc_year.max()
    bns = range(yearmin, yearmax)
    ax = d_grouped.pivot(columns='m_g').disc_year.plot(kind = 'hist', bins = bns, stacked=True)
    ax.legend(title = "Metodo")
    ax.set_ylabel("Exoplanetas descubiertos")
    ax.set_xlabel("Año")
    fig = plt.gcf()
    plot_funcs(ax, fig, grid, save, savename)
    return
    
def year_hist(metod):
    d = pd.read_csv("../data/data.csv")
    yearmin = d.disc_year.min()
    yearmax = d.disc_year.max()
    bns = range(yearmin, yearmax)
    aux = d[d.discoverymethod == metod]
    fig, ax = plt.subplots(1,1)
    ax.hist(aux.disc_year, bins = bns)
    ax.set_ylabel("Exoplanetas descubiertos")
    ax.set_xlabel("Año")
    ax.set_title(f"Histograma del método de {metod}")
    return (fig, ax)

def add_event(figu, val, lab = " ", pos = "izq", alt = 75, save = False, savename = ''):
    """Añade una linea vertical a una figura previamente creada

    Args:
        figu (Variable esp): Variable obtenida a través de otra función que genera figuras.
        val (int or float): Valor en el eje x donde añadiremos la linea
        lab (str): Texto que aparecerá sobre la linea. Defaults to " "
        pos (str, optional): Posición "izq" o "der" de la línea. Defaults to "izq".
        alt (int, optional): Altura en porcentaje del texto. Defaults to 75.
    """
    ax = figu[1]
    fig = figu[0]
    a, b = ax.get_ylim()
    x0, xf = ax.get_xlim()
    c = (xf-x0)/100
    ax.axvline(val, ls = "--", c = 'k', alpha = .5)
    if pos == 'izq':
        ax.annotate(lab, (val - (2.3*c), (b-a)*(alt/100)), rotation = 90)
    elif pos == 'der':
        ax.annotate(lab, (val, (b-a)*.75), rotation = 90)
    plot_funcs(ax, fig, False, save, savename)
    fig.show()
    return    


if __name__ == "__main__":
    t, d = grouped_methods()
    sep_year_histo(d)