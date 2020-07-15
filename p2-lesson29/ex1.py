import json


class AddressBook:
    def __init__(self, filename):
        self.filename = filename
        self.fp = None
        self.contacts = None

    def __enter__(self):
        """
        @link:https://stackoverflow.com/questions/1984325/explaining-pythons-enter-and-exit
        """
        print("__enter__")
        try:
            self.fp = open(self.filename, "r")
        except FileNotFoundError as e:
            self.fp = open(self.filename, "x")
            self.fp.close()
            self.fp = open(self.filename, "r")

        try:
            data = json.load(self.fp)
            self.contacts = data['contacts']
        except Exception as e:
            self.contacts = {}
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print("__exit__")
        if exc_type is None:
            with open(self.filename, 'w') as outfile:
                json.dump({"contacts": self.contacts}, outfile)
                self.fp.close()
        else:
            self.fp.close()
            raise IndexError

    def add(self, name, email):
        self.contacts[name] = email
        # To simulate raising exception
        # raise IndexError("testing")

    def email(self, name):
        return self.contacts[name]

    def __setitem__(self, name, email):
        self.contacts[name] = email

    def __getitem__(self, name):
        return self.contacts[name]

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

# __setitem
with AddressBook('contacts.json') as ab:
    ab['Dan'] = 'dan@gmail.com'

# __getitem
with AddressBook('contacts.json') as ab:
    print(ab['Dan'])
