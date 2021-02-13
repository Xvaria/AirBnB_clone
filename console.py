#!/usr/bin/python3
import cmd
from models.base_model import BaseModel
from models.user import User
from models.engine.file_storage import Storage

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def emptyline(self):
        pass
    def do_EOF(self, line):
        return True
    def do_quit(self, line):
        return True
    def do_create(self, line):
        classes = ["BaseModel", "User", "State", "City", "Amenity",
                   "Place", "Review"]
        if line == "":
            print("** class name missing **")
        elif line in classes:
            b = eval(line)()
            print(b.id)
        else:
            print("** class doesn't exist **")
#    def do_show(self, line):
#
    def help_quit(self):
        print("Exit the program")
    def help_EOF(self):
        print("Exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
