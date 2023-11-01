class student:
    def __init__(self, name, roll_no, branch, amount_paid):
        self.name = name
        self.roll_no = roll_no
        self.branch = branch
        self.amount_paid = amount_paid
    
    def get_summary(self):
        pass

a = student('aaa', 12, 'cse', 10000)