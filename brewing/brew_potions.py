from brewing import potion_class
from brewing import containers
from brewing import cooking
from brewing import inspection
from brewing import ingredients


def make_example_potion(student_name):
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


def make_python_expert_potion(student_name):
    print("I am a Python Expert")
    # todo: write this function!
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your pewter cauldron and light a fire underneath it and adds ingredients.
    my_potion.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    my_potion.add_ingredients(ingredients = ["fish_eyes","unicorn_hair","tea_leaves"])
    # Simmer for 2 hours.
    breakpoint()
    cooking.simmer(my_potion, duration=2)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


if __name__ == "__main__":
    my_name = 'jasmine'
    my_potion = make_python_expert_potion(student_name=my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')
