Links
=====

Doxygen documentation:
    http://turulomio.users.sourceforge.net/doxygen/caloriestracker/

Pypi web page:
    https://pypi.org/project/caloriestracker/

Install in Linux
================
If you use Gentoo, you can find the ebuild in https://github.com/turulomio/myportage/tree/master/app-office/caloriestracker

If you use another distribution, you nee to install PyQtChart and PyQtWebEngine manually. They aren't in Linux setup.py dependencies due to PyQt5 doesn't use standard setup tools. So for compatibility reasons with distributions like Gentoo, we use this additional step.

`pip install PyQtChart`

`pip install PyQtWebEngine`

`pip install caloriestracker`

Install in Windows
==================

You just download caloriestracker-X.X.X.exe and caloriestracker_console-X.X.X.exe and execute them. They are portable apps so they took a little more time to start.

Install in Windows with Python
==============================
Install python from https://www.python.org/downloads/ and don't forget to add python to the path during installation.

Open a CMD console

`pip install caloriestracker`

If you want to create a Desktop shortcut you can write in console

`caloriestracker_shortcuts`

How to launch caloriestracker
========================
caloriestracker uses PostgreSQL database as its backend. So you need to create a database and load its schema. Just type:

`caloriestracker_console`

Once database has been created, just log into caloriestracker after typing:

`caloriestracker`

Warning: Remember caloriestracker it's still in beta status

Dependencies
============
* https://www.python.org/, as the main programming language.
* https://pypi.org/project/colorama/, to give console colors.
* http://initd.org/psycopg/, to access PostgreSQL database.
* https://pypi.org/project/PyQt5/, as the main library.
* https://pypi.org/project/pytz/, to work with timezones.
* https://pypi.org/project/officegenerator/, to work with LibreOffice and Microsoft Office documents.
* https://pypi.org/project/PyQtChart/, to work with charts.
* https://pypi.org/project/colorama/, to work with colors in console.

How to colaborate with Calories Tracker
=======================================

Products database is updated automatically each version in an unattended way.

In Calories tracker you can add your own products and you can share them with us, if you wish


Changelog
=========
0.1.0
  * First version