'''
Toll Booth Simulation
'''
class Vehicle:
    def __init__ (self, ):
        self.vehicles = {
            'Class 1': ['Car', 'Jeepney', 'Van', 'Pickup', 'Motorcycle'],
            'Class 2': ['Bus', 'Truck'],
            'Class 3': ['Tanker', 'Trailer']
        }

    def get_vclass(self):   
        return self.vehicles.keys

    def get_vtype(self):
        for vclass in self.vehicles:                # key
            for vtype in self.vehicles[vclass]:     # value
                return vtype                        # return value

    #   for vclass, vtypes in self.vehicles:
    #       for vtype in vtypes
    #           return vtype

    def check_vtype(self, obj):
        for vclass in self.vehicles:
            for vtype in self.vehicles[vclass]:
                if obj == vtype:
                    return vclass
        else:
            print('Invalid Vehicle Type')

    #   for vclass, vtypes in self.vehicles:
    #       return vclass if obj_type in vtypes
    #   else:
    #       print("Invalid Vehicle Type")

class Ticket:
    def __init__(self, driver, place, vclass, fee):
        self.driver = driver
        self.place = place
        self.vclass = vclass
        self.fee = fee

    def print_tix(self):
        print('✂️ ----- Toll Booth for the Endless Road - Official Receipt ----- ✂️')
        print('✂️ ------------------ OR Number : 0781235534 -------------------- ✂️')
        print('✂️ ------------- "Your destination is just nearby!" ------------- ✂️')
        print(f'>> Name: {self.driver} ')
        print(f'>> Destination: {self.place} ')
        print(f'>> Vehicle Class: {self.vclass} Vehicle')
        print(f'>> Toll Booth Fee: {self.fee}')

# function that will determine Class of the Vehicle Type then assign a correct fee
def assign_fee(vclass):
    fee = 0

    if vclass.lower() == 'Class 1'.lower():
        fee += 50
    elif vclass.lower() == 'Class 2'.lower():
        fee += 100
    elif vclass.lower() == 'Class 3'.lower():
        fee += 150
    else:
        pass

    return fee



### Toll Booth Simulation
while True:

    print('\n••• Toll Booth Simulation •••')

    # Take an input from a User, name, destination, vehicle_type
    name = input('Please enter a name: ')
    destination = input('Please enter a destination: ')
    vehicle_class = None
    while vehicle_class == None:
        vehicle_type = input('Please enter a Vehicle Type: ')
        # Get the Vehicle Type Class
        vehicle_class = Vehicle().check_vtype(vehicle_type)

    # Determine Class of the Vehicle Type then assign a correct fee
    pay = assign_fee(vehicle_class)

    print('\n')
    # Printout a ticket
    Ticket(name, destination, vehicle_class , pay).print_tix()

    new_trans = input('New Transaction? y or n ')

    if new_trans[0].lower() == 'y':
        continue
    else:
        print('Exiting')
        break