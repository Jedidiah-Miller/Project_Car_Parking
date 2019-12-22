'''
this file handles whether or not the terminal command is valid
'''


from terminal_manager import TerminalManager


def launch_application():
  manager = TerminalManager()
  manager.initialize_terminal_app()


launch_application()