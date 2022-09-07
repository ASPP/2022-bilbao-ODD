import brewing.potion_class as potion_class
import brewing.containers as containers
import brewing.cooking as cooking
import brewing.inspection as inspection
import brewing.ingredients as ingredients


def make_example_potion(student_name):
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion

"""
1. Set up a pewter cauldron and light a fire underneath it
2. Add fish eyes, unicorn hair and tea leaves
3. Let simmer for 2 hours
4. Have Snape inspect the potion (use target_potion='python_expert').
"""
def make_python_expert_potion(student_name):
    potion = potion_class.Potion(student_name=student_name)

    #Set up a pewter cauldron and light a fire underneath it
    potion.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)

    #Add fish eyes, unicorn hair and tea leaves
    potion.add_ingredients(ingredients=[ingredients.fish_eyes, ingredients.unicorn_hair, ingredients.tea_leaves])

    #Let simmer for 2 hours
    cooking.simmer(potion, duration=2)
    
    return potion


if __name__ == "__main__":
    my_name = 'GreatStudents'
    my_potion = make_python_expert_potion(student_name=my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='python_expert')
