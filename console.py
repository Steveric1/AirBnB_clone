#!/usr/bin/python3

import cmd

"""Air bnb clone command interpreter"""


class HBNBCommand(cmd.Cmd):
    """Custom (hbnb cmd prompt) using the cmd module"""

    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb)"

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Simple end of file function with newline"""
        print()
        return True

    def emptyline(self):
        """Empty line + enter implementation of doing nothing"""
        pass


if __name__ == '__main__':
    HBNBCommand().cmdloop()
