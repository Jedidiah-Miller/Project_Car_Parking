'''
this file handles whether or not the terminal command is valid
'''


from terminal_manager import TerminalManager


def launch_application():
  manager = TerminalManager()
  manager.clear_terminal()
  manager.display_title_bar()
  print('how would you like to use the app?')
  print('1: load data from txt file')
  print('2: interactive mode')
  user_input = input('choose 1 or 2: ')

  if user_input == '1':
    manager.handle_text_file()
  elif user_input == '2':
    manager.initialize_terminal_app()



launch_application()