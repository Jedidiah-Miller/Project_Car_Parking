'''
manager for a parking lot,
determines whether the action can be executed,
the input from the terminal command is already valid here
'''

from parking_lot import ParkingLot

class LotManager:

  current_parking_lot: ParkingLot = None

  def __init__(self):
    print('\n')

  def create_parking_lot(self, slots: int):
    self.current_parking_lot = ParkingLot(slots)
    return f'created parking lot with {slots} slots'

  def park(self, plate: str, color: str):
    slot = self.current_parking_lot.first_available_slot()
    if slot:
      # TODO we need to validate the plate and color still
      self.current_parking_lot.park_car(slot, plate, color)
      return f'Allocated slot number: {slot}'
    else:
      return 'the parking lot is full'

  def leave(self, slot: int):
    self.current_parking_lot.remove_car(slot)
    return f'slot number {slot} is free'


# I am storing the slots in memory in case we need the data for something later
  def registration_numbers_for_cars_with_color(self, color: str) -> [str]:

    slots = []

    for x in self.current_parking_lot.spaces:
      # do worry about case sensitive
      if x.color == color:
        slots.append(x)

    if len(slots) < 1:
      print('None Found')
    else:
      return [x.plate for x in slots]

  def slot_number_for_registration_number(self, plate: str):

    slot = None

    for x in self.current_parking_lot.spaces:
      if x.plate == plate:
        slot = x
        break

    return slot.number if slot else 'None Found'

  def slot_numbers_for_cars_with_color(self, color: str) -> [str]:

    slots = []

    for x in self.current_parking_lot.spaces:
      if x.color == color:
        slots.append(x)

    if len(slots) < 1:
      return 'None Found'
    else:
      return [str(x.number) for x in slots]

  def status(self):
    return self.current_parking_lot.display_lot()