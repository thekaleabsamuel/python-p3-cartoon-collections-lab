def roll_call_dwarves(dwarves):
    num = 1
    for dwarf in dwarves:
        print(f"{num}. {dwarf}")
        num += 1


def summon_captain_planet(calls):
    return [call.capitalize() + "!" for call in calls]

def long_planeteer_calls(calls):
    for call in calls:
        if len(call) > 4:
            return True
    return False

def find_the_cheese(food):
    cheese = ["cheddar", "gouda", "camembert"]
    for ingredient in food:
        if ingredient in cheese:
            return ingredient
    return None
