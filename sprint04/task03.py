class Employee:
    def __init__(self, n, **args):
        n = n.split()
        self.name = n[0]
        self.lastname = n[1]
        for key in args:
            setattr(self, key, args[key])


john = Employee("John Doe")
mary = Employee("Mary Major", salary=120000)
richard = Employee("Richard Roe", salary=110000, height=178)
giancarlo = Employee("Giancarlo Rossi", salary=115000, height=182, nationality="Italian")
print(mary.lastname)#
print(richard.height)#
print(giancarlo.nationality)#
print(john.name)#