from argparse import ArgumentParser
from random import randint


class Dice(object):

    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        """
        Roll the dice
        :return: integer
        """
        result = randint(1, self.sides)
        return result


if __name__ == '__main__':
    arg_parser = ArgumentParser(description='Roll a die')
    arg_parser.add_argument('--quantity', '-q', required=False, default=1, help='Number of dice')
    arg_parser.add_argument('--sides', '-s', required=True, help='Number of sides')
    args = arg_parser.parse_args()

    quantity = int(args.quantity)
    sides = int(args.sides)

    dice = Dice(sides=sides)

    for roll in range(0, quantity):
        print(dice.roll())
