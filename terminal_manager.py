'''
manages CLI
'''


import os
from time import gmtime, strftime
import parking_lot
from lot_manager import LotManager
from terminal_commands import TerminalCommands


class TerminalManager:

  is_running: bool = False
  current_lot_manager: LotManager = None

  def __init__(self):
    self.current_lot_manager = LotManager()
  
  def initialize_terminal_app(self):
    self.run_interactive_application()

  def clear_terminal(self):
    os.system('clear')

  def display_title_bar(self):
    print("\t**********************************************")
    print("\t******  welcome to the parking lot app  ******")
    print("\t**********************************************")


  def handle_text_file(self):

    user_input = input('specify the file path: ')

    input_file = open(user_input, 'r')
    string_time = strftime("%Y-%m-%d %H:%M:%S", gmtime())
    output_file = open(f'./data/output/output_{string_time}.txt', 'w+')

    for line in input_file.readlines():
      terminal_output = self.handle_terminal_command(line.strip())
      # add the output to the result txt file
      new_line = self.handle_output(terminal_output)
      print(new_line)
      output_file.write(f'\n{new_line}')

    input_file.close()
    output_file.close()


  def run_interactive_application(self):

    self.is_running = True

    while self.is_running:
      user_input = input('what you like to do?: ')
      terminal_output = self.handle_terminal_command(user_input)
      self.display_terminal_output(terminal_output)


  def handle_terminal_command(self, user_input: [str]) -> str:
    '''
    * checks whether or not the specific command is valid,
    currently does not check if the additional info ex: plate number, color, slot ... is valid
    I am assuming for now that the user inputs data properly
    
    * TODO:
      check that the user has input data properly
    '''
    commands = user_input.split(' ')
    action = commands.pop(0)
    output = None

    if action == TerminalCommands.create_parking_lot:
      output = self.current_lot_manager.create_parking_lot(int(commands[0]))

    elif action == TerminalCommands.park:
      output = self.current_lot_manager.park(commands[0], commands[1])

    elif action == TerminalCommands.leave:
      output = self.current_lot_manager.leave(int(commands[0]))

    elif action == TerminalCommands.status:
      output = self.current_lot_manager.status()

    elif action == TerminalCommands.QUIT:
      user_input = input('are you sure you want to quit?: Y/n ')
      if user_input in ['y', 'Y']:
        output = 'quitting the application'
        self.is_running = False
      else:
        output = 'not quitting the application'

    elif action == TerminalCommands.registration_numbers_for_cars_with_color:
      output = self.current_lot_manager.registration_numbers_for_cars_with_color(commands[0].lower())

    elif action == TerminalCommands.slot_number_for_registration_number:
      output = self.current_lot_manager.slot_number_for_registration_number(commands[0])

    elif action == TerminalCommands.slot_numbers_for_cars_with_color:
      output = self.current_lot_manager.slot_numbers_for_cars_with_color(commands[0].lower())

    else:
      output = f'{action} is not a valid command'

    return output

  def display_terminal_output(self, output):
    print(self.handle_output(output))

  def handle_output(self, output) -> str:
    '''
    handle the output,
    if it is a string then we do nothing,
    if not then we turn it into a string for a new line of output
    '''
    if type(output) is list:
      output = ', '.join(output)
    return output


'''
./data/input.txt
'''
