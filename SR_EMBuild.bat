@ECHO OFF

SET pyfile=src\SR_EnvironmentManager.py
SET configfile=SR_EMConfig.xml

REM package steamroller.py as an executable in the distributable subdirectory
pyinstaller --onefile %pyfile%

REM copy the required configuration file into the distributable subdirectory
copy "%cd%\src\%configfile%" "%cd%\dist\%configfile%"