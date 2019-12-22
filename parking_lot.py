'''
parking lot holds all of the slots, as specified upon __init__ 
and hold the designated cars in each slot
'''

from parking_space import ParkingSpace

class ParkingLot:

  spaces: [ParkingSpace]

  def __init__(self, slots: int):
    self.spaces = []
    self.add_spaces(slots)

  def add_spaces(self, slots: int):
    for i in range(slots):
      empty_space = ParkingSpace(i + 1) # index + 1 = the space number
      self.spaces.append(empty_space)

  def park_car(self, slot: int, plate: str, color: str):
    i = slot - 1
    space = self.spaces[i]
    space.plate = plate
    # lowercase the color in the event of somthing like 'blue' and 'Blue' not being the same
    space.color = color.lower()
    self.spaces[i] = space

  def first_available_slot(self):

    for space in self.spaces:
      if not space.plate:
        return space.number

    return None

  def remove_car(self, slot: int):
    self.spaces[slot - 1] = ParkingSpace(slot)

  def display_lot(self):
    print('Slot No. --- Registration No. --- Color')
    for space in self.spaces:
      print(f'space: {space.number} plate: {space.plate} color: {space.color}')
