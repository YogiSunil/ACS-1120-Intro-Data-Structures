import random

quotes = (
    "It's just a flesh wound.",
    "He's not the Messiah. He's a very naughty boy!",
    "THIS IS AN EX-PARROT!!",
    "Nobody expects the Spanish Inquisition!",
    "We are the knights who say... Ni!",
    "Your mother was a hamster and your father smelt of elderberries!",
    "What is the airspeed velocity of an unladen swallow?",
    "Strange women lying in ponds distributing swords is no basis for a system of government!",
    "I fart in your general direction!",
    "Bring out your dead!",
    "I'm not dead yet!",
    "Help! Help! I'm being repressed!",
    "The Holy Hand Grenade of Antioch!",
    "We are now no longer the Knights who say Ni!",
    "Tis but a scratch!"
)

def random_python_quote():
    return random.choice(quotes)

if __name__ == '__main__':
    print(random_python_quote())
