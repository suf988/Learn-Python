# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
#  MULTIPLE INHERITANCE
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

# a class can inherit attributes and methods from more than one classes. i.e. a class can have multiple parents

class Company:
    company = "Tesla"
    country = "USA"
    owner_country = "South Africa"

    def detail(self):
        print(f"The company {self.company} is based in {self.country}")

class Owner:
    name = "Elon Musk"
    age = 47

    def ownerInfo(self):
        print(f"The owner's name is {self.name} and is {self.age} years old.")

class ChildClass(Company, Owner):   # inherited two classes as parents.
    company2 = "SpaceX"

    def get_all_data(self):
        print(f"{self.name} belongs to {self.owner_country} and is the owner of companies {self.company} and {self.company2}.")
        print(f"He is {self.age} and now lives in the {self.country}.")

a = Company()
b = Owner()
c = ChildClass()

c.get_all_data()    # this method from "ChildClass" has all the inherited attributes from its multiple parents.