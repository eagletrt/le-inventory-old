# 𝓛𝓮-inventory

![Logo](docs/le-inventory.png)

![Tags](https://badgen.net/badge/icon/%23LeInventory%20%23py/14406F1?icon=https://icons.getbootstrap.com/assets/icons/bookmarks-fill.svg&label&labelColor=FFF)
![ProjectName](https://badgen.net/badge/Project%20Name/Le-Inventory/0058E7?labelColor=000) ![Version](https://badgen.net/badge/Version/01.01/cyan?labelColor=000) ![Authors](https://badgen.net/badge/Authors/CPR%20Ninis%20Alescs/60C?labelColor=000)

---

## Table of Contents

- [Description](#description)
- [Requirements](#requirements)
- [Directories structure](#directories-structure)
- [Execution examples](#execution-examples)

---

## Description

Le-Inventory is an inventory system, custom-made for the HW team.
It's used to optimize hardwaristi's job.

---

## Requirements

-  ![Language](https://badgen.net/badge/Python/v3.9+/FFD343?labelColor=3776AB&icon=pypi) <sup>([Download](https://www.python.org/downloads/)) <small>[it has to be in the PATH]</small></sup>
---

## Directories structure
	- data

	- docs
		- CHANGELOG.txt
	- requirements
		- requirements.txt
	- src
		- main.py
		- structures.py

	- .gitignore
	- LICENSE
	- README.md
---

## Execution examples

![CLI](https://badgen.net/badge/icon/CLI/B67DFF?icon=terminal&label&labelColor=000)
```bash
# syntax
path/to/le-inventory>py src/main.py [-h] [-i FILEIN] [-o FILEOUT] [-t {Resistor,Capacitor,Diode,Project} [-v]

# example

# 0 - help menu
python3 src/main.py -h
usage: le-inventory/src/main.py [-h] [-i FILEIN] [-o FILEOUT] [-t {Resistor,Capacitor,Diode,Project}] [-v]

A program to manage the stock of electronic components

options:
  -h, --help            show this help message and exit
  -i FILEIN, --filein FILEIN
                        input file
  -o FILEOUT, --fileout FILEOUT
                        output file
  -t {Resistor,Capacitor,Diode,Project}, --type {Resistor,Capacitor,Diode,Project}
                        type of the objects to add
  -v, --verbose         increase output verbosity

# 1 - non-verbose
path/to/le-inventory>python3 src/main.py -i input -o - Capacitors

# 2 - verbose
path/to/le-inventory>python3 src/main.py -i input -o resistors -t Resistor -v

Starting program...
Initializing variables...
Input file: input.csv
Output file: resistors.csv
Objects type: Resistor

Reading csv file data/input.csv...
Creating objects...
Adding object(s) to the dataframe...
Adding object(s) to the dataframe...
Done adding objects to the dataframe!

Serializing data to csv file: data/resistors.csv...
Execution was successful!
```

---

Made with ♡ by [![CPR](https://badgen.net/badge/icon/CPR/B67DFF?icon=github&label&labelColor=000)](https://github.com/chiarasabaini) [![Ninis](https://badgen.net/badge/icon/Ninis/B67DFF?icon=github&label&labelColor=000)](https://github.com/thomasnonis) [![Alescs](https://badgen.net/badge/icon/Alescs/B67DFF?icon=github&label&labelColor=000)](https://github.com/Alescs)
