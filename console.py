#!/usr/bin/python3
"the command interpreter"
import cmd
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.base_model import BaseModel
from models import storage


class HBNBCommand(cmd.Cmd):
    "console opening and looping"
    prompt = "(hbnb) "
    classes = ["BaseModel", "User", "State", "City", "Amenity",
               "Place", "Review"]

    def emptyline(self):
        "if the command space enters empty it does nothing"
        pass

    def do_EOF(self, line):
        "methods to close the console"
        return True

    def do_quit(self, line):
        "methods to close the console"
        return True

    def do_create(self, line):
        "method to create a new instance according to the class"
        if line == "":
            print("** class name missing **")
        elif line in self.classes:
            b = eval(line)()
            b.save()
            print(b.id)
        else:
            print("** class doesn't exist **")

    def do_show(self, line):
        "method to display an existing instance according to class and id"
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
        "method to delete an existing instance and save changes to the JSON\
        file according to class and id"
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
            del search[token[0] + "." + token[1]]
            storage.__objects = search
            storage.save()

    def do_update(self, line):
        "method to update the data of an instance and save it in a JSON file\
        according to the class, the id, the data type and the value."
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
        elif len(token) < 3:
            print("** attribute name missing **")
        elif len(token) < 4:
            print("** value missing **")
        else:
            obj = search[token[0] + "." + token[1]]
            storage.__objects = obj.__dict__
            storage.__objects[token[2]] = token[3]
            storage.save()

    def do_all(self, line):
        "method to display the instance of a specific or all classes stored in\
        the JSON file"
        dic = storage.all()
        lis = []
        if line is "":
            for k in dic.keys():
                lis.append(str(dic[k]))
            print(lis)
        elif line not in self.classes:
            print("** class doesn't exist **")
        else:
            for k in dic.keys():
                if line in k:
                    lis.append(str(dic[k]))
            print(lis)

    def help_quit(self):
        "Print the documentation for this command"
        print("Exit the program")

    def help_EOF(self):
        "Print the documentation for this command"
        print("Exit the program")

    def default(self, line):
        "parses the input, if it is not an existing command it enters this\
        method and performs an action depending on its class"
        ltoken = line.split(".")
        if ltoken[0] not in self.classes:
            print("*** Unknown syntax:", line)
        else:
            if ltoken[1] == "all()":
                self.do_all(ltoken[0])
            elif ltoken[1] == "count()":
                dic = storage.all()
                h = 0
                for i in dic.keys():
                    if ltoken[0] in i:
                        h += 1
                print(h)
            elif "show" in ltoken[1]:
                toks = ltoken[1].split("\"")
                conc = ltoken[0]
                try:
                    conc = ltoken[0] + " " + toks[1]
                except IndexError:
                    pass
                self.do_show(conc)
            elif "destroy" in ltoken[1]:
                toks = ltoken[1].split("\"")
                conc = ltoken[0]
                try:
                    conc = ltoken[0] + " " + toks[1]
                except IndexError:
                    pass
                self.do_destroy(conc)
            elif "update" in ltoken[1]:
                comtoken = ltoken[1].split(",")
                toks = comtoken[0].split("\"")
                if " {" in comtoken[1]:
                    comtoken[1] = comtoken[1][1:]
                    i = 1
                    j = 0
                    while i < len(comtoken):
                        puntoken = comtoken[i].split(":")
                        while j < len(puntoken):
                            if "\"" in puntoken[j][1]:
                                toks2 = puntoken[j].split("\"")
                                print(puntoken[j])
                                if j == 0:
                                    key = toks2[1]
                                else:
                                    val = toks2[1]
                            elif "\'" in puntoken[j][1]:
                                print("holi")
                                toks2 = puntoken[j].split("\'")
                                if j == 0:
                                    key = toks2[1]
                                else:
                                    val = toks2[1]
                            else:
                                if puntoken[j][-1] == ")":
                                    if j == 0:
                                        key = puntoken[j][1:-2]
                                    else:
                                        val = puntoken[j][1:-2]
                                else:
                                    if j == 0:
                                        key = puntoken[j][1:]
                                    else:
                                        val = puntoken[j][1:]
                            j += 1
                        conc = ltoken[0] + " " + toks[1] + " " +\
                               key + " " + val
                        print(conc)
                        self.do_update(conc)
                        j = 0
                        i += 1
                else:
                    toks = ltoken[1].split("\"")
                    conc = ltoken[0]
                    try:
                        conc = ltoken[0] + " " + toks[1] + " " + toks[3] + " "\
                               + toks[5]
                    except IndexError:
                        pass
                    print(conc)
                    self.do_update(conc)
            else:
                print("*** Unknown syntax:", line)

if __name__ == '__main__':
    HBNBCommand().cmdloop()
