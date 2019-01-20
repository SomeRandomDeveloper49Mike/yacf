class Yacf:
    def __init__(self, fn):
        f = open(fn, "r")

        lines = f.readlines()

        self.props = []
        self.final = []

        def FileProperty(name, value):
            self.props.append({"name": name.replace("*", ""), "value": value})

        def Property(name, value):
            self.final.append({"name": name, "value": value})

        def Value(value):
            if value[0] == "%":
                f = open(value[1:].replace("\n", ""))
                strr = f.read()
                f.close()
                return strr
            else:
                return value.replace("\n", "")

        for line in lines:
            l = line.split(": ")
            name = l[0]
            value = l[1]
            if name[0] == "*":
                FileProperty(name, Value(value))
            elif name[0] != "*":
                Property(name, Value(value))

##        for prop in self.props:
##            print(prop["name"], ":", prop["value"])
##
##        for prop in self.final:
##            print(prop["name"], ":", prop["value"])

        f.close()