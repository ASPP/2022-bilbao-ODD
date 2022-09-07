import brewing.potion_class as potion_class
import brewing.containers as containers
import brewing.cooking as cooking
import brewing.inspection as inspection


def make_example_potion(student_name):
    my_potion = potion_class.Potion(student_name=student_name)
    # Set up your old kettle and light an eternal flame underneath it.
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


def make_python_expert_potion(student_name='Harry'):
    print("I am a Python Expert")
    # todo: write this function!
    my_potion = potion_class.Potion(student_name=student_name)
    my_potion.setup(container=containers.old_kettle, heat_source=cooking.eternal_flame)
    # Simmer for 5 hours.
    cooking.simmer(my_potion, duration=5)
    print("You have successfully run make_example_potion, well done :).")
    return my_potion


if __name__ == "__main__":
    my_name = 'ASPP student'
    my_potion = make_python_expert_potion(student_name=my_name)
    # Let Snape inspect the potion
    inspection.inspection_by_Snape(potion=my_potion, target_potion='example_potion')
    python_expert = potion_class.Potion(student_name=my_name)
    python_expert.setup(container=containers.pewter_cauldron, heat_source=cooking.eternal_flame)
    inspection.inspection_by_Snape(potion=python_expert, target_potion='python_expert')
