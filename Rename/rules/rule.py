class Rule:
    def __init__(self, init, beginwith, prefix, rulename, suffix, original,extension):
        self.object = {
            'init': init,
            'beginwith': beginwith,
            'prefix': prefix,
            'rulename': rulename,
            'suffix': suffix,
            'original': original,
            'extension': extension # (.jpeg, .txt)
        }

    def getObject(self, option):
        return self.object[option]

    def setObject(self, option, value):
        self.object[option] = value

    def getAll(self):
        return self.object

    def __str__(self):
        return "Amorce: {}\r\nApartirde: {}\r\nPrefix: {}\r\nNom règle: {}\r\nSuffix: {}\r\nOriginal: {} \r\nExtension: {}".format(
                self.object['init'], self.object['beginwith'], self.object['prefix'],
                self.object['rulename'], self.object['suffix'], self.object['original'], self.object['extension']
        )
