from dice import *


def getstatus(barbarian, mage):
    status = ''
    status += barbarian.get_status()
    status += '\n'
    status += mage.get_status()
    status += '\n'
    return status


def one_round(barbarian, mage):
    status = ''
    who_starts = roll_custom(2)
    if who_starts == 1:
        status += barbarian.act(mage)
        status += mage.act(barbarian)
    else:
        status += mage.act(barbarian)
        status += barbarian.act(mage)

    return status


def get_hp(barbarian, mage):
    return "%s: %d HP left." % (barbarian.name, barbarian.health_point)
    return "%s: %d HP left.\n" % (mage.name, mage.health_point)
