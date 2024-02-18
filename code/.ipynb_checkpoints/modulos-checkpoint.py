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

def grouped_methods(num):
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
            other_group.append(df)
        else:
            m.append(i)
            method_groups.append(df)
            method_counts.append(len(df))
            
    other = pd.concat(other_group, ignore_index = True, axis = 0)
    method_groups.append(other)
    m.append("Others")
    method_counts.append(len(other))
    met = pd.DataFrame(list(zip(m, method_counts)), columns = ["Method", "Number"])
    return met

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
    if grid:
        ax.grid()
    if save:
        fig1.savefig(f"../figs/{savename}.png", dpi = 300)
    fig1.show()
    return

if __name__ == "__main__":
    show_tab()