'''
this file handles whether or not the terminal command is valid
'''
import parking_lot
from lot_manager import LotManager
from terminal_commands import TerminalCommands


def initialize_terminal_app():
  print('welcome to the parking lot app')
  current_lot_manager = LotManager()
  user_input = input('how many spaces? ')
  create_parking_lot(current_lot_manager, user_input)


def create_parking_lot(current_lot_manager: LotManager , spaces: any):
  # check that the specified quantity is a number
  if not spaces.isdigit():
    return print(f'{spaces} is not a valid number')

  current_lot_manager.create_parking_lot(int(spaces))

  run_application(current_lot_manager)


def run_application(current_lot_manager: LotManager):

  is_running = True

  while is_running:
    user_input = input('what you like to do?: ')
    commands = user_input.split(' ')
    # the result of this determines whether or not we continue
    is_running = handle_terminal_command(current_lot_manager, commands)



def handle_terminal_command(current_lot_manager: LotManager, commands: [str]):
  '''
  * checks whether or not the specific command is valid,
  currently does not check if the additional info ex: plate number, color, slot ... is valid
  I am assuming for now that the user inputs data properly
  
  * TODO:
    check that the user has input data properly
  '''
  action = commands.pop(0)

  if action == TerminalCommands.create_parking_lot:
    print('rn you have got to restart the app :(')

  elif action == TerminalCommands.park:
    current_lot_manager.park(commands[0], commands[1])

  elif action == TerminalCommands.leave:
    current_lot_manager.leave(int(commands[0]))

  elif action == TerminalCommands.status:
    current_lot_manager.status()

  elif action == TerminalCommands.QUIT:
    user_input = input('are you sure you want to quit?: Y/n ')
    if user_input in ['y', 'Y']:
      return False

  elif action == TerminalCommands.registration_numbers_for_cars_with_color:
    current_lot_manager.registration_numbers_for_cars_with_color(commands[0].lower())

  elif action == TerminalCommands.slot_number_for_registration_number:
    current_lot_manager.slot_number_for_registration_number(commands[0])

  elif action == TerminalCommands.slot_numbers_for_cars_with_color:
    current_lot_manager.slot_numbers_for_cars_with_color(commands[0].lower())

  else:
    print(f'{action} is not a valid command')

  return True




initialize_terminal_app()