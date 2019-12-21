'''
Project Car Parking
'''

'''
possible inputs:

create_parking_lot N
  N being the number of spaces

park plate_number color
  plate_number being the liscense plate number
  color being the color of the car

leave N
  N being the number of the slot

status
  shows the status of the lot
a list of each:
  Slot No.
  Registration No.
  Color

'''

import parking_lot

# current_parking_lot: parking_lot.ParkingLot = None

def initialize_terminal_app():
  print('welcome to the parking lot app')
  print('awaiting your reponse: ')
  user_input = input('how many spaces? ')
  create_parking_lot(user_input)


def create_parking_lot(spaces: int):

  if not int(spaces):
    return print(f'{spaces} is not a valid number')

  print('creating new parking lot')
  current_parking_lot = parking_lot.ParkingLot(int(spaces))

  run_application(current_parking_lot)


def run_application(current_parking_lot: parking_lot.ParkingLot):

  is_running = True

  while is_running:

    user_input = input('what you like to do?: ')
    commands = user_input.split(' ')
    is_running = handle_terminal_command(create_parking_lot, commands)



def handle_terminal_command(current_parking_lot: parking_lot.ParkingLot, commands: [str]):

  action = commands[0]

  if action == TerminalCommands.create_parking_lot:
    print('make a new lot')
  elif action == TerminalCommands.park:
    print('park')
  elif action == TerminalCommands.leave:
    print('leave')
  elif action == TerminalCommands.status:
    print('status')
    # current_parking_lot.display_lot()
  elif action == TerminalCommands.QUIT:
    user_input = input('are you sure you want to quit?: Y/n ')
    if user_input in ['y', 'Y']:
      return False
  else:
    print(f'{action} is not a valid command')

  return True



class TerminalCommands(object):
  create_parking_lot = 'create_parking_lot'
  park = 'park'
  leave = 'leave'
  status = 'status'
  QUIT = 'quit'



initialize_terminal_app()