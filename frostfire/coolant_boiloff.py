import numpy as np
import pint

ureg = pint.UnitRegistry()
Q_ = ureg.Quantity

thrust = Q_(300, 'newton')
