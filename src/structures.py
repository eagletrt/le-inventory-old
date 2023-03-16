__authors__ = "CPR, Ninis, Alescs"
__version__ = "01.01"
__date__ = "2023-03-16"


class Component():
    id : int
    PN : str
    location : str
    package : str
    stock : int
    reserved : int
    cost : int


    def __init__(self, id, PN, location, package, stock, reserved, cost):
        self.id = id
        self.PN = PN
        self.location = location
        self.package = package
        self.stock = stock
        self.reserved = reserved
        self.cost = cost


class Resistor(Component):
    value : float # resistance
    tolerance : float
    power : float


    def __init__(self, id, PN, location, package, stock, reserved, cost, value, tolerance, power):
        super().__init__(id, PN, location, package, stock, reserved, cost)
        self.value = value
        self.tolerance = tolerance
        self.power = power


class Capacitor(Component):
    value : float # capacitance
    tolerance : float
    dielectric : str
    maxVoltage : int


    def __init__(self, id, PN, location, package, stock, reserved, cost, value, tolerance, dielectric, maxVoltage):
        super().__init__(id, PN, location, package, stock, reserved, cost)
        self.value = value
        self.tolerance = tolerance
        self.dielectric = dielectric
        self.maxVoltage = maxVoltage


class Diode(Component):
    type : str
    value : float # forward voltage
    power : float
    forwardVoltage : float
    breakdownVoltage : float


    def __init__(self, id, PN, location, package, stock, reserved, cost, type, value, power, forwardVoltage, breakdownVoltage):
        super().__init__(id, PN, location, package, stock, reserved, cost)
        self.type = type
        self.value = value
        self.power = power
        self.forwardVoltage = forwardVoltage
        self.breakdownVoltage = breakdownVoltage


class Project():
    name : str
    version : str
    date : str
    resistors : list[Resistor]
    projectPath : str


    def __init__(self, name, version, date):
        self.name = name
        self.version = version
        self.date = date

    
    def get_id(self):
        return f"{self.name}_{self.date}_{self.version.replace('.', '-')}"