__authors__ = "CPR, Ninis, Alescs"
__version__ = "01.01"
__date__ = "2023-03-16"


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


    def __init__(self, id, PN, location, package, stock, reserved, price):
        self.id = id
        self.PN = PN
        self.location = location
        self.package = package
        self.stock = stock
        self.reserved = reserved
        self.price = price

    
    def get_available(self):
        """
        Returns the number of available components

        Returns
        -------
        int
            number of available components
        """  
        return self.stock - self.reserved


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


    def __init__(self, id, PN, location, package, stock, reserved, price, value, tolerance, power):
        super().__init__(id, PN, location, package, stock, reserved, price)
        self.value = value
        self.tolerance = tolerance
        self.power = power


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


    def __init__(self, id, PN, location, package, stock, reserved, price, value, tolerance, dielectric, maxVoltage):
        super().__init__(id, PN, location, package, stock, reserved, price)
        self.value = value
        self.tolerance = tolerance
        self.dielectric = dielectric
        self.maxVoltage = maxVoltage


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


    def __init__(self, id, PN, location, package, stock, reserved, price, type, value, power, forwardVoltage, breakdownVoltage):
        super().__init__(id, PN, location, package, stock, reserved, price)
        self.type = type
        self.value = value
        self.power = power
        self.forwardVoltage = forwardVoltage
        self.breakdownVoltage = breakdownVoltage


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
    resistors : list[Resistor]
        list of resistors used in the project
    projectPath : str
        path to the project

    Methods
    -------
    get_id()
        Returns the project id
    """
    name : str
    version : str
    date : str
    resistors : list[Resistor]
    projectPath : str


    def __init__(self, name, version, date):
        """
        Constructor for the Project class

        Args:
            name (str): project name
            version (str): project version
            date (str): project date
        """
        self.name = name
        self.version = version
        self.date = date

    
    def get_id(self):
        """
        Returns the project id

        Returns
        -------
        str
            project id
        """        
        return f"{self.name}_{self.date}_{self.version.replace('.', '-')}"