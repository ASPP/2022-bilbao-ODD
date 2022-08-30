## Exercise 1: Importing

#### Goal

Get comfortable with different ways of importing objects from a package.

#### Tasks

0. [if not done already] fork the repository
   
   https://github.com/ASPP/2022-bilbao-ODD

1. Import the module `brew_potions.py` in the `example_usage_inside_package.py` file that lives inside the `brewing` directory: 
   
   1. import only the `make_example_potion` function and call it
   2. change the import statement so that you can call the `make_example_potion` function like this: `br.make_example_potion`

2. Import the brewing package from the `example_usage_outside_package.py` that lives at the top level of the repo.
   
   1. import only the `make_example_potion` function and call it
   2. does it work? if yes, why? If no, why not?

3. In the `scripts_and_notebooks` folder, there is a file called `example_usage_different_folder.py` that lives in the `scripts` directory. Try to import the `make_example_potion` function from there.
   
   1. import only the `make_example_potion` function and call it
   2. does it work? if yes, why? If no, why not?
