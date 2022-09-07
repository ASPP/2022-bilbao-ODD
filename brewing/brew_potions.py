from brewing import potion_class, containers, cooking, inspection,ingredients


def make_example_potion(student_name):
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


def make_python_expert_potion(student_name):
    my_potion = potion_class.Potion(student_name=student_name)
    my_potion.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    my_potion.add_ingredients(ingredients=[ingredients.fish_eyes, ingredients.unicorn_hair, ingredients.tea_leaves])
    cooking.simmer(my_potion, duration=2)

    print("I am a Python Expert")
    # todo: write this function!
    
    inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')
    return


if __name__ == "__main__":
    my_name = 'ASPP student'
    my_potion = make_example_potion(student_name=my_name)
    print(make_python_expert_potion(student_name = my_name))
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')



# et Professor Snape to inspect your potion as shown for the example potion. Calling `` should never give you an error, so you will have to read what Snape does and says to find out what went wrong.

# This is supposed to be easy and fun, so run the inspection often and make mistakes with the potion.

# Use your git skills to commit the changes you made to a new branch, and create a pull request on Github.
