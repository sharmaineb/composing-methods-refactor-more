# By Kami Bigdely
# Remove assignment to method parameter.

class Distance:
    def __init__(self, value, unit):
        self.unit = unit
        self.value = value

class Mass:
    def __init__(self, value, unit):
        self.value = value
        self.unit = unit

def convert_distance_to_km(distance):
    if distance.unit == "ly": 
        return Distance(distance.value * 9.461e12, "km")
    elif distance.unit == 'km':
        return distance
    else:
        print("Distance unit is Unknown")
        return None

def convert_mass_to_kg(mass):
    if mass.unit == "solar-mass":  # solar mass to kg
        return Mass(mass.value * 1.98892e30, 'kg')
    elif mass.unit == 'kg':
        return mass
    else:
        print("Mass unit is Unknown")
        return None

def calculate_kinetic_energy(mass, distance, time):
    converted_distance = convert_distance_to_km(distance)
    if not converted_distance:
        return None

    converted_mass = convert_mass_to_kg(mass)
    if not converted_mass:
        return None

    speed = converted_distance.value / time 
    kinetic_energy = 0.5 * converted_mass.value * speed ** 2
    return kinetic_energy

mass = Mass(2, "solar-mass")
distance = Distance(2, 'ly')
print(calculate_kinetic_energy(mass, distance, 3600e20))