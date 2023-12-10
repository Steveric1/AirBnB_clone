#!/usr/bin/python3

"""Air bnb clone command interpreter"""
import cmd
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review

from models import storage


class HBNBCommand(cmd.Cmd):
    """Custom (hbnb cmd prompt) using the cmd module"""
    
    __classess = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
    }
    def __init__(self):
        super().__init__()
        self.prompt = "(hbnb) "

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
    
    def do_create(self, arg):
        my_args = arg.split()
        if not arg:
            print("** class name missing **")
        elif my_args[0] not in HBNBCommand.__classess:
            print("** class doesn't exist **")
        else:
            new_inst = eval(my_args[0])()
            new_inst.save()
            print(new_inst.id)
    
    def do_show(self, arg):
        """Show created id"""
        my_args = arg.split()
        create_inst = storage.all()
        try:
            if not arg:
                raise ValueError("** class name missing **")
            elif my_args[0] not in HBNBCommand.__classess:
                raise ValueError("** class doesn't exist **")
            elif len(my_args) < 2:
                raise ValueError("** instance id missing **")
            else:
                keys = "{}.{}".format(my_args[0], my_args[1])
                if keys not in create_inst:
                    raise ValueError("** no instance found **")
                else:
                    print(create_inst[keys])
        except ValueError as e:
            print(e)
        
    def do_destroy(self, arg):
        """Delete method"""
        my_args = arg.split()
        create_inst = storage.all()
        try:
            if not arg:
                raise ValueError("** class name missing **")
            elif my_args[0] not in HBNBCommand.__classess:
                raise ValueError("** class doesn't exist **")
            elif len(my_args) < 2:
                raise ValueError("** instance id missing **")
            else:
                keys = "{}.{}".format(my_args[0], my_args[1])
                if keys not in create_inst:
                    raise ValueError("** no instance found **")
                else:
                    del create_inst[keys]
                    storage.save()
        except ValueError as e:
            print(e)
    
    def do_all(self, args):
        """all method"""
        my_args = args.split()
        all_inst = []
        
        if len(my_args) > 0 and my_args[0] not in HBNBCommand.__classess:
            print("**class name doesn't exist**")
        else:
           all_inst = []
           for all in storage.all().values():
               if len(my_args) > 0 and my_args[0] == all.__class__.__name__:
                   all_inst.append(all.__str__())
               elif len(my_args) == 0:
                   all_inst.append(all.__str__())
           print(all_inst)
            
if __name__ == '__main__':
    HBNBCommand().cmdloop()
