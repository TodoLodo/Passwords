@echo off

echo Adding "%cd%" to PATH

setx /M PATH "%PATH%;%cd%"

echo.

echo Creating Passwords.bat

(
    echo echo off
    echo py %cd%
) > Passwords.bat

echo Successful!
echo.

pause