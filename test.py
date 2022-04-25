class Letter:
    def __init__(self, name = "A"):
        self.m_name =  name


dict = {"key": [Letter("A"), Letter("B"), Letter("C")]}

print(len(dict["key"]))
