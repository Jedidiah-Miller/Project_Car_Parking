'''
parking lot holds all of the slots, as specified upon __init__ 
and hold the designated cars in each slot
'''

from parking_space import ParkingSpace

class ParkingLot:

  spaces: list

  def __init__(self, slots: int):
    self.spaces = []
    print(f'creating new parking lot with {slots} spaces')
    self.fill_spaces(slots)

  def fill_spaces(self, slots: int):
    for i in range(slots):
      empty_space = ParkingSpace(i + 1) # index + 1 = the space number
      self.spaces.append(empty_space)

  def add_car(self, slot: int, plate: str, color: str):
    space = self.spaces[slot]
    space.plate = plate
    space.color = color

    self.spaces[slot] = space

  def remove_car(self, slot: int):
    print(f'removing car from slot {slot}')
    self.spaces[slot] = ParkingSpace(slot)

  def display_lot(self):
    print('parking lot status')
    for space in self.spaces:
      print(f'{space.number} {space.plate} {space.color}')
