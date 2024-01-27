class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # Adding parentheses around p1 and p2 if they are instances of Add, Sub, Mul or Div
        if isinstance(self.p1, (Add, Sub, Mul, Div)):
            p1_repr = "( " + repr(self.p1) + " )"
        else:
            p1_repr = repr(self.p1)

        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            p2_repr = "( " + repr(self.p2) + " )"
        else:
            p2_repr = repr(self.p2)

        return p1_repr + " * " + p2_repr

# The newly added Sub and Div classes
class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # Adding parentheses if p2 is an instance of Add, Sub, Mul or Div
        if isinstance(self.p2, (Add, Sub, Mul, Div)):
            return repr(self.p1) + " - (" + repr(self.p2) + ")"
        return repr(self.p1) + " - " + repr(self.p2)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        # Adding parentheses around p1 and p2 if they are instances of Add, Sub, or Mul
        if isinstance(self.p1, (Add, Sub, Mul)):
            p1_repr = "( " + repr(self.p1) + " )"
        else:
            p1_repr = repr(self.p1)

        if isinstance(self.p2, (Add, Sub, Mul)):
            p2_repr = "( " + repr(self.p2) + " )"
        else:
            p2_repr = repr(self.p2)

        return p1_repr + " / " + p2_repr

# Testing the new classes with various polynomial expressions
poly1 = Sub(Div(X(), Int(2)), Add(X(), Int(3)))
poly2 = Div(Add(X(), Mul(Int(2), X())), Int(5))
poly3 = Mul(Sub(X(), Int(4)), Div(Int(3), Add(X(), Int(1))))

print(poly1)
print(poly2)
print(poly3)