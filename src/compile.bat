pyinstaller -F Passwords.py --icon Passwords.ico --clean --distpath ..
rmdir /s /q build
del Passwords.spec
pause