import os
from typing import List

os.chdir(os.path.dirname(__file__))


def files(path):
    for f in os.listdir(path):
        if os.path.isfile(os.path.join(path, f)):
            yield f


def val(value):
    if value[0] == "%":
        return open(value[1:]).read()
    else:
        return value


class Prop:
    def __init__(self, name):
        self.name = name


class Property:
    def __init__(self, name, value):
        self.name = name
        self.value = value


class Yalf(object):
    props = []
    code = []
    properties: List[Prop] = []
    configuration: List[Prop] = []

    @staticmethod
    def execute_property(name, value):
        Yalf.props.append(Property(name, value))

    @staticmethod
    def get_property(name):
        for prop in Yalf.props:
            if prop.name == name:
                return prop.value

    @staticmethod
    def compile(filename):
        f = open(filename)

        lines = f.readlines()

        not_code = lines[:lines.index("start: ?\n")+1]

        for line in not_code:
            lst = line.split(":")
            name = lst[0].lstrip().rstrip()
            value = lst[1].lstrip().rstrip()
            Yalf.execute_property(name, value)
        Yalf.code = lines[lines.index("start: ?\n")+1:]

        def AddConfiguration(n):
            Yalf.configuration.append(Prop(n))

        def AddProperty(n):
            Yalf.properties.append(Prop(n))
        global_props = {
            "AddProperty": AddProperty,
            "AddConfiguration": AddConfiguration,
            "os": None,
            "__builtins__": None,
        }

        local_props = {"Debug": print}

        exec(''.join(Yalf.code), global_props, local_props)


class Yacf(object):
    props = []
    config = []
    default_props = ["name", "version", "info", "lib", "clib", "start", "end"]
    lib_props = []
    lib_config = []

    @staticmethod
    def check_props(prop):
        if prop.name in Yacf.default_props:
            return True
        elif prop.name in Yacf.lib_props:
            return True
        else:
            return False

    @staticmethod
    def check_config(prop):
        if prop.name in Yacf.lib_config:
            return True
        else:
            return False

    @staticmethod
    def add_lib(name):
        for f in files(os.getcwd()):
            if f == name:
                Yalf.compile(f)
                tmp_lib = []
                for c in Yalf.properties:
                    tmp_lib.append(c.name)
                Yacf.lib_props = tmp_lib
                tmp_lib = []
                for c in Yalf.configuration:
                    tmp_lib.append(c.name)
                Yacf.lib_config = tmp_lib

    @staticmethod
    def execute_property(name, value, t="config"):
        if t == "config":
            Yacf.config.append(Property(name, val(value)))
        elif t == "property":
            Yacf.props.append(Property(name, val(value)))
            if name == "lib":
                Yacf.add_lib(value)

    @staticmethod
    def compile(filename):
        f = open(filename)

        lines = f.readlines()
        count = 1
        for line in lines:
            lst = line.split(":")
            name = lst[0].lstrip()
            value = lst[1].lstrip().replace("\n", "").rstrip()
            if name[0] == "*":
                if not Yacf.check_props(Property(name.replace("*", ""), value)):
                    print("ERROR: INCORRECT FILE PROPERTY, LINE " + str(count))
                    exit(0)
                Yacf.execute_property(name.replace("*", ""), value, "property")
            else:
                if not Yacf.check_config(Property(name, value)):
                    print("ERROR: INCORRECT CONFIG PROPERTY, LINE " + str(count))
                    exit(0)
                Yacf.execute_property(name, value, "config")
            count += 1
