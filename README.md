# USTCOJ (Django)

## Environment

### Development Environment

To keep the environment clean, please use Virtual Environment.

In PyCharm, you can create and apply the VirtualEnv in `Preferences > Project : proj_name > Project Interpreter > ... > create VirtualEnv`.

(Assume the name of VirtualEnv is  `ustcoj`)

Note that our project is based on Python 3.6.

#### Initialize the VirtualEnv

Run the commands in the VirtualEnv. (`Terminal` tab in PyCharm)

```sh
(ustcoj) pip install -r requirements.txt
```

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