# USTCOJ (Django)

## Environment

### PyCharm setting

First, create a new **Pure Python** project named `ustcoj` with a Virtual Environment named `ustcoj` based on **Python 3.6**.

Then, open the empty project, pull files from GitHub. (`Terminal` tab in PyCharm)

```
(ustcoj) git init
(ustcoj) git remote add origin git@github.com:volltin/ustcoj.git
(ustcoj) git pull origin master
```

(`ustcoj` is.the name of your Virtual Environment)

Now, all files are in your project dir.

Finally, set up the framework support to get better experience:

`Preferences > Languages & Frameworks > Django > enable Django Support`

Django project root: `your_project_root`

Settings: `your_project_root`/ustcoj/setting.py

Manage script: `your_project_root`/manage.py

### Development Environment

#### Install new Packages

Use `pip install package_name` to install a new python package. Then freeze the package list.

``` sh
(ustcoj) pip freeze > requirements/requirements.txt
```

#### Run in Debug Mode

##### IDE method

Click `Run` (Ctrl + R) in PyCharm.

##### Manual method

Run the commands in the VirtualEnv. (`Terminal` tab in PyCharm)

```sh
(ustcoj) python manager.py runserver
```

Now it is running on http://127.0.0.1:8000/

## Tests

### Unittest

Use `unittest` to test the application.

Run the commands in the VirtualEnv. (`Terminal` tab in PyCharm)

```sh
(ustcoj) python -m unittest discover -v
```