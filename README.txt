------------------------------------------------------------
SR Environment Manager Rough Demo
------------------------------------------------------------
PRODUCT   :     Environment Manager Demo
VERSION   :     0.0.6
AUTHOR    :     THATWHICHIS MEDIA
SUPPORT   :     thatwhichis@gmail.com	
PUBLISHER :     THATWHICHIS MEDIA 
PERMISSION:     FOR DEMONSTRATION PURPOSES ONLY
COPYRIGHT :     (C)2019 THATWHICHIS MEDIA, LLC
------------------------------------------------------------

CODE SAMPLE: SR_EnvironmentManager.py
This is the requested Python source sample. It is written in 
Python 3.8. It has only been tested in Windows 10 
environments.

EXECUTABLE FILE: dist\SR_EnvironmentManager.exe
This file is the PyInstallar packaged executable version of 
SR_EnvironmentManager.py.

XML DEPENDENCY: SR_EMConfig.xml
This file contains XML formatted environment variables to be 
set. NOTE: This file must be placed in the same base 
directory as the SR_EnvironmentManager.py file or the 
'dist' subdirectory with the SR_EnvironmentManager.exe file.

BUILD FILE: SR_EMBuild.bat
This file, when run, packages SR_EnvironmentManager.py as an 
executable in the 'dist' subdirectory using PyInstaller and 
copies the current version of the SR_EMConfig.xml file into 
the 'dist' subdirectory.

DESIGN CHOICES:
This file was built to the rough spcifications discussed at 
our interview on Wednesday, 10/23/2019 at ~3:00 PM.

Choice 1: 
Export to single executable for ease of use. Generated 
SR_EMBuild.bat.

Choice 2: 
Will not currently worry about code-signing anything for 
this sample.

Choice 3: 
Import environment variable names and values from external 
file for ease of update without having to alter core program. 
Use XML for external file based entirely on personal 
familiarity. Generated SR_EMConfig.xml.

Choice 4: 
Ensure project names are easily recognizable and 
identifiable.

Choice 5: 
Generate dummy Environment Variable names and values 
to minimize potential damage to testing system.

Choice 6: 
Use 'setx' rather than 'set' for ease of visibility in 
Windows 10 Environment Variables GUI under the 'User 
variables' subsection upon execution.

Choice 7: 
Attempt to provide reasonable user feedback to trouble-
shoot without assistance.

Choice 8: 
Create file(s) with additional information 
and timestamps to assist Pipeline in troubleshooting should 
issues prove more complex. Generated 
SR_EnvironmentManager.log.