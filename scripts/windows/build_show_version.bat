@echo "Temp directory " %1

REM Argument one is the path to the source file
REM Argument two is the name of the final executable
REM --onefile builds a bundle
REM --add-data includes files in the bundle
REM these files will not be in the temporary directory and
REM not visible to the user
REM --distpath changes the distribution directory so we have a
REM directory read to be copied somewhere with all the associated files
REM --workpath changes the build directory to avoid leaving artificacts in the main repo

REM create bundles directory if it doesn't exist
mkdir %1\dist\bundles

REM Forces clean build
rmdir /S /Q %1\dist\bundles\show_version

REM Finds ntc_templates directory
python scripts\windows\get_ntc_templates_dir.py > scripts\windows\ntc_templates_dir.txt
set /p NTC_TEMPLATES_DIR= < scripts\windows\ntc_templates_dir.txt
ECHO "%NTC_TEMPLATES_DIR%"

pyinstaller pyinstaller_test2\show_version.py ^
	--onefile ^
	-n show_version ^
	--distpath  %1\dist\bundles\show_version ^
	--workpath  %1\build ^
	--specpath  %1\dist ^
	--add-data %NTC_TEMPLATES_DIR%;ntc_templates


