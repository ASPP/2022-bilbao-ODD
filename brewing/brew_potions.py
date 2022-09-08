import brewing.potion_class as potion_class
import brewing.containers as containers
import brewing.cooking as cooking
import brewing.inspection as inspection
from brewing.ingredients import fish_eyes, unicorn_hair, tea_leaves

def make_example_potion(student_name):
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


def make_python_expert_potion(student_name='Harry'):
    """Make an expert potion.
    
    Makes a potion in a pewter cauldron container over fire.
    Adds fish eyes, unicorn hair and tea leaves.
    Cooks for 2 hours.

    Parameters
    ----------
    student_name : str, default='Harry'
    
    Returns
    -------
    python_expert : potion_class.Potion
        Potion class instance for expert_potion
    """
    print("I am a Python Expert")
    python_expert = potion_class.Potion(student_name=student_name)
    python_expert.setup(container=containers.pewter_cauldron, heat_source=cooking.fire)
    python_expert.add_ingredients([fish_eyes, unicorn_hair, tea_leaves])
    cooking.simmer(python_expert, duration=2)
    print("You have successfully run make_python_expert_potion, well done :).")
    return python_expert


if __name__ == "__main__":
    my_name = 'ASPP student'
    python_expert = make_python_expert_potion(student_name=my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=python_expert, target_potion='python_expert')
