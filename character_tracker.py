import sys
from argparse import ArgumentParser


class CharacterTracker(object):
    def __init__(self, hit_points, expendable_slots):
        self.hit_points = hit_points
        self.experience = 0
        self.inspiration = False
        self.expendable_slots = expendable_slots
        self.expendable_slots_max = expendable_slots

    def update_hit_points(self, point_change):
        self.hit_points += point_change

    def add_experience(self, xp_gained):
        self.experience += xp_gained

    def spend_expendable_slot(self):
        self.expendable_slots -= 1

    def reset_expendable_slot(self):
        self.expendable_slots = self.expendable_slots_max


class BardTracker(CharacterTracker):
    def __init__(self, hit_points, expendable_slots):
        super().__init__(hit_points, expendable_slots)
        self.expendable_resource_name = 'Bardic Inspiration'


class WarlockTracker(CharacterTracker):
    def __init__(self, hit_points, expendable_slots):
        super().__init__(hit_points, expendable_slots)
        self.expendable_resource_name = 'Pact'


if __name__ == '__main__':
    arg_parser = ArgumentParser(description='Test CharacterTracker classes')
    arg_parser.add_argument('--character-class', '-c', required=True, help='Class name')
    args = arg_parser.parse_args()

    character_class = args.character_class.lower()

    class_mapping = {'bard': BardTracker,
                     'warlock': WarlockTracker}

    if character_class not in class_mapping.keys():
        print('Character class \'{}\' not supported.'.format(character_class))
        sys.exit(1)

    tracker = class_mapping[character_class](hit_points=20, expendable_slots=3)

    print('Character takes 3 damage!')
    tracker.update_hit_points(-3)
    print('Character has {} hit points remaining.'.format(tracker.hit_points))

    print('Character grants {}!'.format(tracker.expendable_resource_name))
    tracker.spend_expendable_slot()
    print('Character has {}/{} {} left.'.format(tracker.expendable_slots,
                                                tracker.expendable_slots_max,
                                                tracker.expendable_resource_name))
