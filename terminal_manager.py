'''
manages CLI
'''


import os
import parking_lot
from lot_manager import LotManager
from terminal_commands import TerminalCommands


class TerminalManager:

  current_lot_manager: LotManager = None

  def __init__(self):
    pass
  
  def initialize_terminal_app(self):
    self.clear_terminal()
    self.display_title_bar()
    self.current_lot_manager = LotManager()
    user_input = input('how many spaces? ')
    self.create_parking_lot(user_input)

  def clear_terminal(self):
    os.system('clear')

  def display_title_bar(self):
    print("\t**********************************************")
    print("\t******  welcome to the parking lot app  ******")
    print("\t**********************************************")

  def create_parking_lot(self, spaces: any):
    # check that the specified quantity is a number
    if not spaces.isdigit():
      return print(f'{spaces} is not a valid number')

    self.current_lot_manager.create_parking_lot(int(spaces))

    self.run_application(self.current_lot_manager)

  def handle_text_file(self, file):
    for _ in file:
      self.handle_terminal_command(self.current_lot_manager, file.readline())
      # add the output to the result txt file

  def run_application(self, current_lot_manager: LotManager):

    is_running = True

    while is_running:
      user_input = input('what you like to do?: ')
      commands = user_input.split(' ')
      # the result of this determines whether or not we continue
      is_running = self.handle_terminal_command(current_lot_manager, commands)



  def handle_terminal_command(self, current_lot_manager: LotManager, commands: [str]):
    '''
    * checks whether or not the specific command is valid,
    currently does not check if the additional info ex: plate number, color, slot ... is valid
    I am assuming for now that the user inputs data properly
    
    * TODO:
      check that the user has input data properly
    '''
    action = commands.pop(0)

    if action == TerminalCommands.create_parking_lot:
      self.current_lot_manager.create_parking_lot(int(commands[0]))

    elif action == TerminalCommands.park:
      self.current_lot_manager.park(commands[0], commands[1])

    elif action == TerminalCommands.leave:
      self.current_lot_manager.leave(int(commands[0]))

    elif action == TerminalCommands.status:
      self.current_lot_manager.status()

    elif action == TerminalCommands.QUIT:
      user_input = input('are you sure you want to quit?: Y/n ')
      if user_input in ['y', 'Y']:
        return False

    elif action == TerminalCommands.registration_numbers_for_cars_with_color:
      self.current_lot_manager.registration_numbers_for_cars_with_color(commands[0].lower())

    elif action == TerminalCommands.slot_number_for_registration_number:
      self.current_lot_manager.slot_number_for_registration_number(commands[0])

    elif action == TerminalCommands.slot_numbers_for_cars_with_color:
      self.current_lot_manager.slot_numbers_for_cars_with_color(commands[0].lower())

    else:
      print(f'{action} is not a valid command')

    return True
