# Problem 3

def sum_digits(s):
    """ assumes s a string
        Returns an int that is the sum of all of the digits in s.
          If there are no digits in s it raises a ValueError exception. """
    # Your code here
    digits = "0123456789"
    error = 0
    total = 0
    for letter in s:
        if letter in digits:
            total += int(letter)
        else:
            error += 1
    if error == len(s):
        raise ValueError
    return total

# print (sum_digits("a;35d4"))

# Problem 4

def max_val(t):
    """ t, tuple or list
        Each element of t is either an int, a tuple, or a list
        No tuple or list is empty
        Returns the maximum int in t or (recursively) in an element of t """
    # Your code here
    maxOne = 0
    # print t
    for i in t:
        if isinstance(i, int):
            if i > maxOne:
                maxOne = i
        else:
            x = max_val(i)
            if x > maxOne:
                maxOne = x

    return maxOne

# print max_val((5, (1,2), [[1],[2]]))
# print max_val((5, (1,2), [[1],[9]]))

# Problem 5

def cipher(map_from, map_to, code):
    """ map_from, map_to: strings where each contain 
                          N unique lowercase letters. 
        code: string (assume it only contains letters also in map_from)
        Returns a tuple of (key_code, decoded).
        key_code is a dictionary with N keys mapping str to str where 
        each key is a letter in map_from at index i and the corresponding 
        value is the letter in map_to at index i. 
        decoded is a string that contains the decoded version 
        of code using the key_code mapping. """
    # Your code here
    key_code = dict()
    for i in range(len(map_from)):
        key_code[map_from[i]] = map_to[i]
    decoded = ''
    for letter in code:
        decoded += key_code[letter]
    return (key_code, decoded)

# print cipher("abcd", "dcba", "dab")
# returns (order of entries in dictionary may not be the same) ({'a':'d', 'b': 'c', 'd': 'a', 'c': 'b'}, 'adc')

# Problem 6

# Problem 6-1

class Container(object):
    """ Holds hashable objects. Objects may occur 0 or more times """

    def __init__(self):
        """ Creates a new container with no objects in it. I.e., any object 
            occurs 0 times in self. """
        self.vals = {}

    def insert(self, e):
        """ assumes e is hashable
            Increases the number times e occurs in self by 1. """
        try:
            self.vals[e] += 1
        except:
            self.vals[e] = 1

    def __str__(self):
        s = ""
        for i in sorted(self.vals.keys()):
            if self.vals[i] != 0:
                s += str(i) + ":" + str(self.vals[i]) + "\n"
        return s

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # write code here
        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        if e in self.vals:
            return self.vals[e]
        else:
            return 0

# d1 = Bag()
# d1.insert(4)
# d1.insert(4)
# d1.insert(4)
# print(d1.count(2))
# print(d1.count(4))
#
# d2 = Bag()
# d2.insert(4)
# d2.insert(4)
# print(d2)
# d2.remove(2)
# print(d2)

# Problem 6-2

class Bag(Container):
    def remove(self, e):
        """ assumes e is hashable
            If e occurs in self, reduces the number of 
            times it occurs in self by 1. Otherwise does nothing. """
        # write code here
        if e in self.vals:
            self.vals[e] -= 1

    def count(self, e):
        """ assumes e is hashable
            Returns the number of times e occurs in self. """
        # write code here
        if e in self.vals:
            return self.vals[e]
        else:
            return 0

    def __add__(self, other):
        union = Bag()
        union.vals = self.vals
        for e in other.vals:
            if e in union.vals:
                union.vals[e] += other.count(e)
            else:
                union.insert(e)
        return union

# a = Bag()
# a.insert(4)
# a.insert(3)
# b = Bag()
# b.insert(4)
# print(a+b)

# Problem 6-3

class ASet(Container):
    def remove(self, e):
        """assumes e is hashable
           removes e from self"""
        # write code here
        if e in self.vals:
            self.vals.pop(e, None)

    def is_in(self, e):
        """assumes e is hashable
           returns True if e has been inserted in self and
           not subsequently removed, and False otherwise."""
        # write code here
        if e in self.vals:
            return True
        else:
            return False

# d1 = ASet()
# d1.insert(4)
# d1.insert(4)
# d1.remove(2)
# print(d1)
# d1.remove(4)
# print(d1)

# d1 = ASet()
# d1.insert(4)
# print(d1.is_in(4))
# d1.insert(5)
# print(d1.is_in(5))
# d1.remove(5)
# print(d1.is_in(5))

# Problem 7

### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self):
        return self.x

    def getY(self):
        return self.y

    def dist_from(self, other):
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):
    def __init__(self, center_loc):
        self.center_loc = center_loc

    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """

    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects 
        Initializes a new Campus centered at location center_loc 
        with a tent at location tent_loc """
        # Your code here
        Campus.__init__(self, center_loc)
        self.tents = []
        self.add_tent(tent_loc)

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance 
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        # Your code here
        for tent in self.tents:
            if tent.dist_from(new_tent_loc) < 0.5:
                return False
        self.tents.append(new_tent_loc)
        return True

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus. 
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        # Your code here
        if tent_loc in self.tents:
            self.tents.remove(tent_loc)
        else:
            raise ValueError

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain 
        the string representation of the Location of a tent. The list should 
        be sorted by the x coordinate of the location. """
        # Your code here
        tents = []
        def getX(loc):
            return loc.getX()
        new = sorted(self.tents, key=getX)
        for tent in new:
            tents.append(tent.__str__())
        return tents

# c = MITCampus(Location(1,2))
# print(c.add_tent(Location(1,2)))
# print(c.add_tent(Location(0,0)))
# print(c.add_tent(Location(2,3)))
# print(c.add_tent(Location(2,3)))
# print(sorted(c.get_tents()))

# c = MITCampus(Location(1,2), Location(0,1))
# c.add_tent(Location(-1,2))
# c.add_tent(Location(1,-10))
# c.add_tent(Location(1,10))
# c.add_tent(Location(1,20))
# c.add_tent(Location(1,40))
# print(sorted(c.get_tents()))
# print(check_if_x_sorted(c.get_tents()))