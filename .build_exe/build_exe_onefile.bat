REM create bundles directory if it doesn't exist
mkdir .\.build_exe\dist\bundles
REM --onefile builds a bundle
REM --add-data includes files in the bundle
REM these files will not be in the temporary directory and
REM not visible to the user
REM --distpath changes the distribution directory so we have a
REM directory read to be copied somewhere with all the associated files
REM --workpath changes the build directory to avoid leaving artificacts in the main repo

python .\.build_exe\write_ntc_templates_dir_to_file.py
set /p NTC_TEMPLATES_DIR= < .\.build_exe\ntc_templates_dir.txt

pyinstaller pyinstaller_test2\%SOURCE_PYTHON_FILE_PATH% ^
	--onefile ^
	--distpath .\.build_exe\dist\bundles\%PYINST_EXE_NAME% ^
	--workpath .\.build_exe\build ^
	--specpath .\.build_exe\dist ^
	--add-data "%NTC_TEMPLATES_DIR%;templates"


REM Custom steps for this project
REM copying files meant for the users to see
REM PYINST_EXE_NAME is the environment variable used for the name of the compiled executable
copy config.ini .\.build_exe\dist\bundles\%PYINST_EXE_NAME%
