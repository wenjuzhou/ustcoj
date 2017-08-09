# USTCOJ (Django)

[![Build Status](https://travis-ci.com/volltin/ustcoj.svg?token=4JibKQrmfuPTR7qe424i&branch=master)](https://travis-ci.com/volltin/ustcoj)

## Environment

### PyCharm setting

First, create a new **Pure Python** project named `ustcoj` with a Virtual Environment named `ustcoj` based on **Python 3.6**.

Then, open the empty project, pull files from GitHub. (`Terminal` tab in PyCharm)

```
(ustcoj) git init
(ustcoj) git remote add origin git@github.com:volltin/ustcoj.git
(ustcoj) git pull origin master
```

(`ustcoj` is the name of your Virtual Environment)

Now, all files are in your project dir.

Finally, set up the framework support to get better experience:

`Preferences > Languages & Frameworks > Django > enable Django Support`

Django project root: `your_project_root`

Settings: `your_project_root`/ustcoj/setting.py

Manage script: `your_project_root`/manage.py

### Development Environment

#### Install Packages

``` sh
(ustcoj) pip install -r requirements.txt
```

#### Init local database

```sh
python manage.py migrate
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


#### Use Django Admin Panel

```sh
(ustcoj) python manager.py createsuperuser
```

Open http://127.0.0.1:8000/admin

## Tests

### Unittest

Use `unittest` to test the application.

Run the commands in the VirtualEnv. (`Terminal` tab in PyCharm)

```sh
(ustcoj) python manage.py test
```