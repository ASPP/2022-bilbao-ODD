## Exercise 5: Virtual Environments

#### Goal

Create a virtual environment + (editable) install your package + see that your dependencies are automatically installed

#### Tasks

We will use `venv` as our environment manager - it is a basic one, but all the principles will apply to all other package managers as well.

1. Check which Python you are currently using, and which packages are installed. Uninstall the brewing package and check that it is not there anymore.
2. Navigate to the folder which contains the brewing package
3. Create and activate a new environment
4. Check again which Python you are using and which packages are installed - Are they different?
5. Editable install the *brewing* package and check that the code still works

#### Commands in case you get stuck (not in correct order):

```bash
> which python
> pip freeze
> pip uninstall brewing
> pip install -e <path-to-folder-containing-brewing>


% create an environment option 1
> cd <path-to-project_folder>
> python3 -m venv .
> source ./bin/activate

% create an environment option 2
> python3 -m venv <path-to-project_folder>
> source <path-to-project_folder>/bin/activate


% fyi: deactivate a venv environment
> deactivate
```
