#!/usr/bin/python3
import cmd
import re
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity",
               "Place", "Review"]

    def emptyline(self):
        pass

    def do_EOF(self, line):
        return True

    def do_quit(self, line):
        return True

    def do_create(self, line):
        if line == "":
            print("** class name missing **")
        elif line in self.classes:
            b = eval(line)()
            b.save()
            print(b.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        token = line.split(" ")
        search = storage.all()
        if token[0] is "":
            print("** class name missing **")
        elif token[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        elif token[0] + "." + token[1] not in search:
            print("** no instance found **")
        else:
            obj = search[token[0] + "." + token[1]]
            print(obj)

    def do_destroy(self, line):
        token = line.split(" ")
        search = storage.all()
        if token[0] is "":
            print("** class name missing **")
        elif token[0] not in self.classes:
            print("** class doesn't exist **")
        elif len(token) < 2:
            print("** instance id missing **")
        elif token[0] + "." + token[1] not in search:
            print("** no instance found **")
        else:
            print(type(search[token[0] + "." + token[1]]))
            del search[token[0] + "." + token[1]]
            b = eval(token[0])()
            b.save()
            print("PEENTAKILLLLLLLLLLLLLLLLLLLLLLLLLLLLL")

    def help_quit(self):
        print("Exit the program")

    def help_EOF(self):
        print("Exit the program")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
