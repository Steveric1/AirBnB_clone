#!/usr/bin/python3

"""Air bnb clone command interpreter"""
import cmd
import re
from models.base_model import BaseModel
from models.arg_format import arg_parse
from models import storage
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review


class HBNBCommand(cmd.Cmd):
    """Custom (hbnb cmd prompt) using the cmd module"""

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

    def default(self, args):
        """The default behaviour of console"""
        args_dict = {
            "all": self.do_all,
            "create": self.do_create,
            "show": self.do_show,
            "destroy": self.do_destroy,
            "update": self.do_update,
            "count": self.do_count
        }

        match = re.search(r"\.", args)
        if match is not None:
            arg_1 = [args[:match.span()[0]], args[match.span()[1]:]]
            match = re.search(r"\((.*?)\)", arg_1[1])
            if match is not None:
                command = [arg_1[1][:match.span()[0]], match.group()[1:-1]]
                if command[0] in args_dict.keys():
                    cmd_call = "{} {}".format(arg_1[0], command[1])
                    return args_dict[command[0]](cmd_call)
                print("*** Unknown syntax: {}".format(arg_1))
        return False

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Simple end of file function with newline"""
        print()
        return True

    def help_quit(self):
        """Help message for the quit command."""
        print("Quit command to exit the program\n")

    def emptyline(self):
        """Empty line + enter implementation of doing nothing"""
        pass

    def do_create(self, line):
        """Usage: create <class> <key 1>=<value 2> <key 2>=<value 2> ...
        Create a new class instance with given keys/values and print its id.
        """
        try:
            if not line:
                raise SyntaxError()
            my_list = line.split(" ")

            kwargs = {}
            for i in range(1, len(my_list)):
                key, value = tuple(my_list[i].split("="))
                if value[0] == '" "':
                    value = value.strip('" "').replace("_", " ")
                else:
                    try:
                        value = eval(value)
                    except (SyntaxError, NameError):
                        continue
                kwargs[key] = value

            if kwargs == {}:
                obj = eval(my_list[0])()
            else:
                obj = eval(my_list[0])(**kwargs)
                storage.new(obj)
            print(obj.id)
            obj.save()

        except SyntaxError:
            print("** class name missing **")
        except NameError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Show created id"""
        my_args = arg.split()
        create_inst = storage.all()
        try:
            if not arg:
                raise ValueError("** class name missing **")
            elif my_args[0] not in HBNBCommand.__classes:
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
        my_args = arg_parse(arg)
        create_inst = storage.all()
        try:
            if not arg:
                raise ValueError("** class name missing **")
            elif my_args[0] not in HBNBCommand.__classes:
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
        my_args = arg_parse(args)

        if len(my_args) > 0 and my_args[0] not in HBNBCommand.__classes:
            print("** class name doesn't exist **")
        else:
            all_inst = []

            for i in storage.all().values():
                if (len(my_args) > 0 and my_args[0] == i.__class__.__name__):
                    all_inst.append(i.__str__())
                elif len(my_args) == 0:
                    all_inst.append(i.__str__())
            print(all_inst)

    def do_count(self, arg):
        """Count the number of instance"""
        my_args = arg_parse(arg)
        count = 0

        for obj in storage.all().values():
            if my_args[0] == obj.__class__.__name__:
                count += 1
        print(count)

    def do_update(self, arg):
        """Updates an instance"""
        my_args = arg_parse(arg)
        all_inst = storage.all()

        if arg == 0:
            print("** class name missing **")
            return False
        if my_args[0] not in HBNBCommand.__classes:
            print("** class doesn't exist **")
            return False
        if len(my_args) < 2:
            print("** instance id missing **")
            return False
        keys = "{}.{}".format(my_args[0], my_args[1])
        if keys not in all_inst.keys():
            print("** no instance found **")
            return False
        if len(my_args) == 2:
            print("** attribute name missing **")
            return

        if len(my_args) == 3:
            try:
                type(eval(my_args[2])) != dict
            except NameError:
                print("** value missing **")
                return False

        if len(my_args) == 4:
            obj = all_inst["{}.{}".format(my_args[0], my_args[1])]
            if my_args[2] in obj.__class__.__dict__.keys():
                valtype = type(obj.__class__.__dict__[my_args[2]])
                obj.__dict__[my_args[2]] = valtype(my_args[3])
            else:
                obj.__dict__[my_args[2]] = my_args[3]
        elif type(eval(my_args[2])) == dict:
            obj = all_inst["{}.{}".format(my_args[0], my_args[1])]
            for k, v in eval(my_args[2]).items():
                if (k in obj.__class__.__dict__.keys() and
                    type(obj.__class__.__dict__[k]) in {str, int, float}):
                    valtype = type(obj.__class__.__dict__[k])
                    obj.__dict__[k] = valtype(v)
        else:
            obj.__dict__[k] = v

        storage.save()


if __name__ == '__main__':
    HBNBCommand().cmdloop()
