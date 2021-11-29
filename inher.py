class Person:
    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

    def print_name(self):
        print(self.first_name, self.last_name)


florist = Person("Jane", "Flowers")
florist.print_name()


class Lawyers(Person):
    def __init__(self, first_name, last_name, case_type):
        super().__init__(first_name, last_name)
        self.case_type = case_type
        # self.first_name = first_name
        # self.last_name = last_name
        
    def print_info(self):
        print("Hello my name is", self.first_name, self.last_name)


happy_lawyers = Lawyers("jack", "Smiley", "criminal")
happy_lawyers.print_info()
print(happy_lawyers.case_type)