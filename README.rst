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


