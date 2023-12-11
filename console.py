#!/usr/bin/python3

"""Air bnb clone command interpreter"""
# import cmd
# from models.base_model import BaseModel
# from models.user import User
# from models.state import State
# from models.city import City
# from models.amenity import Amenity
# from models.place import Place
# from models.review import Review
# 
# from models import storage

import cmd
from models.base_model import BaseModel
from models import storage
import re
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from datetime import datetime

# class HBNBCommand(cmd.Cmd):
#     """Custom (hbnb cmd prompt) using the cmd module"""
# 
#     __classes = {
#         "BaseModel",
#         "User",
#         "State",
#         "City",
#         "Amenity",
#         "Place",
#         "Review"
#     }
# 
#     def __init__(self):
#         super().__init__()
#         self.prompt = "(hbnb) "
# 
#     def do_quit(self, arg):
#         """Quit command to exit the program"""
#         return True
# 
#     def do_EOF(self, arg):
#         """Simple end of file function with newline"""
#         print()
#         return True
# 
#     def emptyline(self):
#         """Empty line + enter implementation of doing nothing"""
#         pass
#     
#     def do_create(self, line):
#         """Creates a new instance of BaseModel and saves it to json file"""
#         args = line.split()
#         if not args[0]:
#             print("** class name missing **")
#         elif args[0] not in HBNBCommand.__classes:
#             print("** class doesn't exist **")
#         else:
#             instance = eval(args[0])()
#             instance.save()
#             print(instance.id)
# 
# #     def do_create(self, line):
# #         """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
# #         Create a new class instance with given keys/values and print its id.
# #         """
# #         try:
# #             if not line:
# #                 raise SyntaxError()
# #             my_list = line.split(" ")
# # 
# #             kwargs = {}
# #             for i in range(1, len(my_list)):
# #                 key, value = tuple(my_list[i].split("="))
# #                 if value[0] == '" "':
# #                     value = value.strip('" "').replace("_", " ")
# #                 else:
# #                     try:
# #                         value = eval(value)
# #                     except (SyntaxError, NameError):
# #                         continue
# #                 kwargs[key] = value
# # 
# #             if kwargs == {}:
# #                 obj = eval(my_list[0])()
# #             else:
# #                 obj = eval(my_list[0])(**kwargs)
# #                 storage.new(obj)
# #             print(obj.id)
# #             obj.save()
# # 
# #         except SyntaxError:
# #             print("** class name missing **")
# #         except NameError:
# #             print("** class doesn't exist **")
# 
#     def do_show(self, arg):
#         """Show created id"""
#         my_args = arg.split()
#         create_inst = storage.all()
#         try:
#             if not arg:
#                 raise ValueError("** class name missing **")
#             elif my_args[0] not in HBNBCommand.__classes:
#                 raise ValueError("** class doesn't exist **")
#             elif len(my_args) < 2:
#                 raise ValueError("** instance id missing **")
#             else:
#                 keys = "{}.{}".format(my_args[0], my_args[1])
#                 if keys not in create_inst:
#                     raise ValueError("** no instance found **")
#                 else:
#                     print(create_inst[keys])
#         except ValueError as e:
#             print(e)
# 
#     def do_destroy(self, arg):
#         """Delete method"""
#         my_args = arg.split()
#         create_inst = storage.all()
#         try:
#             if not arg:
#                 raise ValueError("** class name missing **")
#             elif my_args[0] not in HBNBCommand.__classes:
#                 raise ValueError("** class doesn't exist **")
#             elif len(my_args) < 2:
#                 raise ValueError("** instance id missing **")
#             else:
#                 keys = "{}.{}".format(my_args[0], my_args[1])
#                 if keys not in create_inst:
#                     raise ValueError("** no instance found **")
#                 else:
#                     del create_inst[keys]
#                     storage.save()
#         except ValueError as e:
#             print(e)
# 
#     def do_all(self, args):
#         """all method"""
#         my_args = args.split()
# 
#         if len(my_args) > 0 and my_args[0] not in HBNBCommand.__classes:
#             print("** class name doesn't exist **")
#         else:
#             all_inst = []
# 
#             for i in storage.all().values():
#                 if (len(my_args) > 0 and my_args[0] == i.__class__.__name__):
#                     all_inst.append(i.__str__())
#                 elif len(my_args) == 0:
#                     all_inst.append(i.__str__())
#             print(all_inst)
# 
#     def do_update(self, arg):
#         """Updates an instance"""
#         my_args = arg.split()
#         if not arg:
#             print("** class name missing **")
#             return
# 
#         _class = my_args[0]
#         if _class not in HBNBCommand.__classes:
#             print("** class doesn't exist **")
#             return
# 
#         if len(my_args) < 2:
#             print("** instance id missing **")
#             return
# 
#         inst_id = my_args[1]
#         keys = "{}.{}".format(_class, inst_id)
#         all_inst = storage.all()
# 
#         if keys not in all_inst:
#             print("** no instance found **")
#             return
# 
#         if len(my_args) < 3:
#             print("** attribute name missing **")
#             return
# 
#         attr_name = my_args[2]
#         if len(my_args) < 4:
#             print("** value missing **")
#             return
# 
#         value = my_args[3]
# 
#         _inst = all_inst[keys]
#         if hasattr(_inst, attr_name):
#             attr_type = type(getattr(_inst, attr_name))
#             try:
#                 setattr(_inst, attr_name, attr_type(value))
#                 _inst.save()
#             except (ValueError, TypeError):
#                 print("** invalid value **")
#         else:
#             print("** attribute doesn't exist **")
# 
# 
# if __name__ == '__main__':
#     HBNBCommand().cmdloop()


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
        if not args[0]:
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
