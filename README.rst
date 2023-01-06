=========
Passwords
=========

Passwords is console based script/application to generate, store and manage your passwords

=============
Documentation
=============

Installation
============

Current development of the binaries and scripts can downloaded via this repo zip version, in release tabs together along
previous releases or using git clone command in terminal as follows

.. code-block:: bash

    git clone https://github.com/TodoLodo/Passwords.git

Usage
=====

Initiation
----------

To use the functions either the scripts or the binary file must be executed via a terminal

To execute the root dir script (``__main__.py``) either of the following 2 methods can be followed

* Method 1 (while in the root dir)

.. code-block:: bash

    py .

* Method 2 (while out of the root dir but is accessible in the current location and assuming root dir is "Passwords")

.. code-block:: bash

    py Passwords

If you wish to execute the ``Passwords.py`` located in scripts dir under root dir use the following command

.. code-block:: bash

    py path\to\Passwords.py

To execute the binary file (Passwords.exe) available under the root dir use the following command

.. code-block:: bash

    path\to\Passwords.exe

(Optionally) to avoid typing the relative path to the binary file or having change working dir to the root dir the root
dir can be added into environmental variable paths

Functionalities
---------------

The Passwords script/application can either generate passwords with least amount of repetition for any given amount
password length among 95 characters, store generated password or manually entered password with a reference and a
username, modify saved passwords, delete save passwords and search up passwords using a keyword

All available options will be listed on terminal upon initiation of the script/application

Other than the listed functionalities, available functions are

* clearing all password records which simply can be achieved by typing "ca" or "clearall" when selecting options

===========================
Other Important Information
===========================

* The shown example bash commands are mainly focused on windows terminal but the scripts do run other os environments where python can run on

* The available binary file is an exe file hence can be only can run on windows os

* The intention of the project is to aid our users to store passwords at there ease with least complicated functions as possible meaning that the database is simply based in the data dir where the user is accountable of safeguarding their own database with the policy that by using our project binaries/scripts will not share any data of what you decide to store

* This project is under consistent development meaning some point above such simple functionalities maybe made complex but still achieving to provide an easy to use liable source of binaries/scripts to save your password

* Any issues please direct it to our repo issue page and any with the skill can make pull requests to help this project improve

* If new release is available or just by deciding to reclone to the same location as your previous location installed/ cloned make sure to backup the database file available under the data dir in the root dir

* Donation links are available for you to donate on your freewill and it would not affect you using our project if you did donate or did not
