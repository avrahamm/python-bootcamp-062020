import json


class AddressBook:
    def __init__(self, filename):
        self.filename = filename
        self.fp = None
        self.content = {"contacts": None}

    def __enter__(self):
        """
        @link:https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
        """
        print("__enter__")
        try:
            self.fp = open(self.filename, "r")
        except Exception as e:
            self.fp = open(self.filename, "x")
            self.fp.close()
            self.fp = open(self.filename, "r")

        try:
            data = json.load(self.fp)
            self.content["contacts"] = data['contacts']
        except Exception as e:
            self.content["contacts"] = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        with open(self.filename, 'w') as outfile:
            json.dump(self.content, outfile)
        self.fp.close()

    def add(self, name, email):
        self.content["contacts"][name] = email

    def email(self, name):
        return self.content["contacts"][name]

    def __str__(self):
        with open(self.filename) as json_file:
            try:
                data = json.load(json_file)
            except Exception as e:
                pass
            contacts = data['contacts']
            return json.dumps(contacts)


with AddressBook('contacts.json') as ab:
    ab.add('Eve', 'eve@gmail.com')
    ab.add('Alice', 'alice@walla.co.il')

print(ab)

with AddressBook('contacts.json') as ab:
    print(ab.email('Eve'))
