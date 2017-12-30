from ast import literal_eval

class RulesList:
    def __init__(self, rule):
        self.rule = rule

    def getRule(self):
        return self.rule

    def setRule(self, newrule):
        self.rule = newrule

    def get(self):
        with open("config/renamer.ini", "r") as get:
            return literal_eval(get.read())

    def load(self):
        with open("config/renamer.ini", "r") as load:
            try:
                read = literal_eval(load.read())
                print(load.read())
                return read
            except SyntaxError:
                print(load.read())
                return {}

    def save(self):
        rules = self.load()
        name = self.getRule().getObject('rulename')
        rules[name] = self.getRule().getAll()
        print(rules)
        with open("config/renamer.ini", "w") as s:
            s.write(str(rules))

    def __str__(self):
        return "Règle actuelle {}".format(self.getRule())
