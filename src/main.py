__authors__ = "CPR, Ninis, Alescs"
__version__ = "01.01"
__date__ = "2023-03-16"


import pandas as pd
import dataclasses as dc
from structures import *


def add_to_df(df, objs):
    """"
    Adds a component or a list of components to a dataframe, then returns the dataframe

    Parameters
    ----------
    df : pandas.DataFrame
        dataframe to add the component(s) to
    objs : structures.Component or list of structures.Component
        component(s) to add to the dataframe

    Returns
    -------
    pandas.DataFrame
        dataframe with the added component(s)
    """
    if(type(objs) == list):
        for o in objs:
            dict = dc.asdict(o)
            df.loc[len(df), dict.keys()] = dict
    else:
        dict = dc.asdict(objs)
        df.loc[len(df), dict.keys()] = dict

    return df


def add_from_csv(path, type):
    """"
    Creates objects from a csv file, adds them to a dataframe, and returns the dataframe

    Parameters
    ----------
    path : str
        path to the csv file
    type : str
        type of the objects to create

    Returns
    -------
    pandas.DataFrame
        dataframe from the csv file
    """
    match type:
        case "Resistor":
            constructor = Resistor
        case "Capacitor":
            constructor = Capacitor
        case "Diode":
            constructor = Diode
        case "Project":
            constructor = Project

    df = pd.DataFrame()
    with open(path, "r") as f:
        header = True
        for line in f:
            if header:
                header = False
                continue

            line = line.strip("\n").split(",")
            obj = constructor(line[0], line[1], line[2], line[3], line[4], line[5], line[6], line[7], line[8], line[9])
            add_to_df(df, obj)
    
    return df


def __init__():

    resistors_df = add_from_csv("data/input.csv", "Resistor")

    resistors_df.to_csv("data/resistors.csv", index=False)


if __name__ == '__main__':
    __init__()













