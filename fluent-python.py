import collections
import math
from random import choice

Card = collections.namedtuple('Card', ['rank', 'suite'])

class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suites = 'spades diamonds clubs heards'.split()

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suites for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

my_deck = FrenchDeck()

# print(len(my_deck))
# print('the random card ===>>>', choice(my_deck))
# print(Card('A', 'spades') in my_deck)

# for card in reversed(my_deck[:9]):
#     print(card)

# magic_numbers = dict(FOO=1, BAR=2, BAZ=3)
# print(magic_numbers['FOO'])
# print(magic_numbers['BAR'])
# print(magic_numbers['BAZ'])

class Vector:
    def __init__(self, x , y):
        self.x = x
        self.y = y
    def __repr__(self):
        return f'Vector({self.x}, {self.y})'
    def __add__(self, other):
        result = Vector(self.x + other.x, self.y + other.y)
        return result
    def __abs__(self):
        return math.hypot(self.x, self.y)
    def __bool__(self):
        return bool(abs(self))

my_vector_a = Vector(2, 3)
my_vector_b = Vector(1, 7)
print(my_vector_a)
print(my_vector_b)
print(my_vector_a + my_vector_b)
print(abs(Vector(4, 3)))

if not Vector(0, 0):
    print("ese veztor es una kk")
else:
    print(f"er veztorcico {Vector(1 - 1, 2 - 2)} mola matho")

#test
