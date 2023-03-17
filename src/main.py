__authors__ = "CPR, Ninis, Alescs"
__version__ = "01.01"
__date__ = "2023-03-16"


import argparse
import pandas as pd
import dataclasses as dc
from structures import *

VERBOSE = False

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

    if VERBOSE:
        print("Adding object(s) to the dataframe...")

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
    if VERBOSE:
        print(f"Reading csv file {path}...")
    
    match type:
        case "Resistor":
            constructor = Resistor
        case "Capacitor":
            constructor = Capacitor
        case "Diode":
            constructor = Diode
        case "Project":
            constructor = Project

    if VERBOSE:
        print("Creating objects...")

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
    
    if VERBOSE:
        print("Done adding objects to the dataframe!\n")
    
    return df


def get_args():
    """
    Parses the arguments passed to the program

    Returns
    -------
    argparse.Namespace
        arguments passed to the program
    """
    
    parser = argparse.ArgumentParser(prog="le-inventory/src/main.py",
                                     description="A program to manage the stock of electronic components")

    parser.add_argument('-i', '--filein', help="input file")
    parser.add_argument('-o', '--fileout', help="output file")
    parser.add_argument('-t', '--type', help="type of the objects to add", choices=["Resistor", "Capacitor", "Diode", "Project"])
    parser.add_argument('-v', '--verbose', help="increase output verbosity", action="store_true", default=False)
    
    args = parser.parse_args()

    return args


def __init__():
    global VERBOSE
    args = get_args()

    fin = args.filein
    fout = args.fileout
    obj_type = args.type
    VERBOSE = args.verbose

    if VERBOSE:
        print(f"Starting program...\nInitializing variables...")
        print(f"Input file: {args.filein}\nOutput file: {args.fileout}\nObjects type: {args.type}\n")

    resistors_df = add_from_csv(f"data/{fin}.csv", f"{obj_type}")

    if VERBOSE:
        print(f"Serializing data to csv file: data/{fout}.csv...")
    
    if obj_type == "Project":
        path_out = f"data/{fout}.csv" # TODO: handle project type [filename must be the project's id, retrieved using Project.get_id()]
    else:
        path_out = f"data/{fout}.csv"
    resistors_df.to_csv(path_out, index=False)
    
    if VERBOSE:
        print("Execution was successful!")

if __name__ == '__main__':  

    __init__()













