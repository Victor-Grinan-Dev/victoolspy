class Mother:

    def __init__(self, cooking="rice", dancing="salsa"):
        self.cooking = cooking
        self.dancing = dancing


class Father:

    def __init__(self, playing="board games", be_useless="doing nothing"):
        self.playing = playing
        self.be_useless = be_useless


class Child(Father, Mother):

    def __init__(self, cooking="rice", dancing="salsa", playing="board games", be_useless="doing nothing"):
        Father.__init__(self, playing, be_useless)
        Mother.__init__(self, cooking, dancing)


alma = Child()

print(alma.cooking)
print(alma.playing)

alma.dancing = "Hip Hop"
alma.be_useless = False

print(alma.dancing)
print(alma.be_useless)