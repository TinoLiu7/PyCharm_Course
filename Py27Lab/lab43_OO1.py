class Team:
    member = 7

    def working_hour(self):
        return self.day

    def all_working_hour(self):
        self.day = 5
        return self.member * self.day

    @staticmethod
    def calculate(x, y):
        return (x + y) * (x * y)
    @classmethod
    def get_member(cls):
        return cls.member


t1 = Team()
print t1.all_working_hour()
print t1.working_hour()
print Team().calculate(5, 7)
print t1.get_member(), Team().get_member(),Team.get_member()
