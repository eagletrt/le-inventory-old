__authors__ = "CPR, Ninis, Alescs"
__version__ = "01.01"
__date__ = "2023-03-16"

from dataclasses import dataclass

@dataclass
class Component():
    """
    Class used to represent a component

    ...

    Attributes
    ----------
    id : int
        component id
    PN : str
        part number
    location : str
        location in the warehouse
    package : str
        package type
    stock : int
        number of components in stock
    reserved : int
        number of components reserved for projects
    price : int
        price of one component
    
    Methods
    -------
    get_available()
        Returns the number of available components
    """    
    id : int
    PN : str
    location : str
    package : str
    stock : int
    reserved : int
    price : int


    def get_available(self):
        """
        Returns the number of available components

        Returns
        -------
        int
            number of available components
        """  
        return self.stock - self.reserved
    


@dataclass
class Resistor(Component):
    """
    Class used to represent a resistor

    ...

    Attributes
    ----------
    value : float
        resistance
    tolerance : float
        tolerance
    power : float
        power
    """
    value : float
    tolerance : float
    power : float
    

@dataclass
class Capacitor(Component):
    """
    Class used to represent a capacitor

    ...

    Attributes
    ----------
    value : float
        capacitance
    tolerance : float
        tolerance
    dielectric : str
        dielectric type
    maxVoltage : int
        maximum voltage
    """
    value : float
    tolerance : float
    dielectric : str
    maxVoltage : int


@dataclass
class Diode(Component):
    """
    Class used to represent a diode

    ...

    Attributes
    ----------
    type : str
        diode type
    value : float
        forward voltage
    power : float
        power
    forwardVoltage : float
        forward voltage
    breakdownVoltage : float
        breakdown voltage
    """
    type : str
    value : float
    power : float
    forwardVoltage : float
    breakdownVoltage : float


@dataclass
class Project():
    """
    Class used to represent a project

    ...

    Attributes
    ----------
    name : str
        project name
    version : str
        project version
    date : str
        project date
    projectPath : str
        path to the project
    resistors : list[(Resistor, int)]
        list of tuples, composed of the id of the resistors used in the project and the quantity
    capacitors : list[(Capacitor, int)]
        list of tuples, composed of the id of the capacitors used in the project and the quantity
    diodes : list[(Diode, int)]
        list of tuples, composed of the id of the diodes used in the project and the quantity
    
        
    Methods
    -------
    get_id()
        Returns the project id
    """
    name : str
    version : str
    date : str
    projectPath : str
    resistors : list[(Resistor, int)]
    capacitors : list[(Capacitor, int)]
    diodes : list[(Diode, int)]


    def get_id(self):
        """
        Returns the project id

        Returns
        -------
        str
            project id
        """        
        return f"{self.name}_{self.date}_{self.version.replace('.', '-')}"
