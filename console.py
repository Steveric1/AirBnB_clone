#!/usr/bin/python3

"""Air bnb clone command interpreter"""
import cmd
from models.base_model import BaseModel
from models import storage
# import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime


class HBNBCommand(cmd.Cmd):
    '''This is the main class for the module.'''

    prompt = "(hbnb) "

    __classes = {
        "BaseModel",
        "User",
        "State",
        "City",
        "Amenity",
        "Place",
        "Review"
        }

    def emptyline(self):
        '''Nothing will be executed if an empty line is passed.'''
        pass

    def do_quit(self, line):
        '''Quit command to exit the program'''
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program\n")

    def do_EOF(self, line):
        '''This will quit the program'''
        return True

    def do_create(self, line):
        """Creates a new instance of BaseModel and saves it to json file"""
        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        else:
            instance = eval(args[0])()
            instance.save()
            print(instance.id)

    def do_show(self, line):
        """Prints the string representation of an instance"""
        args = line.split()

        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                print(storage.all()[key])

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file).
        """

        args = line.split()
        if not args:
            print("** class name missing **")
        elif args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
        elif len(args) < 2:
            print("** instance id missing **")
        else:
            key = f"{args[0]}.{args[1]}"
            if key not in storage.all():
                print("** no instance found **")
            else:
                del storage.all()[key]
                storage.save()

    def do_all(self, line):
        """Prints all string representation of all instances."""
        args = line.split()
        all_inst = storage.all()

        if not args or args[0] not in HBNBCommand.__classes:
            print(all_inst)
            return

        if args[0] not in HBNBCommand.__classes:
            print("** class name doesn't exist **")
            return

        all_instances = storage.all()
        class_name = args[0]

        for all_instance in all_instances.values():
            if (len(args) > 0 and
                    class_name == all_instance.__class__.__name__):
                all_inst.append(all_instance.__str__())

            elif len(args) == 0:
                all_inst.append(all_instance.__str__())

        print(all_inst)

    def do_update(self, line):
        """Updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file).
        """
        my_args = line.split()

        if not line:
            print("** class name missing **")
            return

        _class = my_args[0]
        if _class not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return

        if len(my_args) < 2:
            print("** instance id missing **")
            return

        inst_id = my_args[1]
        keys = "{}.{}".format(_class, inst_id)
        all_inst = storage.all()

        if keys not in all_inst:
            print("** no instance found **")
            return

        if len(my_args) < 3:
            print("** attribute name missing **")
            return

        attr_name = my_args[2]
        if len(my_args) < 4:
            print("** value missing **")
            return

        value = my_args[3]

        _inst = all_inst[keys]
        if hasattr(_inst, attr_name):
            attr_type = type(getattr(_inst, attr_name))
            try:
                setattr(_inst, attr_name, attr_type(value))
                _inst.save()
            except (ValueError, TypeError):
                print("** invalid value **")
        else:
            print("** attribute doesn't exist **")


if __name__ == "__main__":
    HBNBCommand().cmdloop()
