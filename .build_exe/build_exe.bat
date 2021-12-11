REM --distpath changes the distribution directory so we have a
REM directory read to be copied somewhere with all the associated files
REM --workpath changes the build directory to avoid leaving artificacts in the main repo
REM %SOURCE_FILE_PATH% is the environment variable for the source file to be compiled
pyinstaller pyinstaller_test2\%SOURCE_PYTHON_FILE_PATH% ^
            --distpath .\.build_exe\dist ^
            --workpath .\.build_exe\build ^
            --specpath .\.build_exe\dist

REM Custom steps for this project
REM copying files meant for the users to see
REM PYINST_EXE_NAME is the environment variable used for the name of the compiled executable
copy config.ini .\.build_exe\dist\%PYINST_EXE_NAME%

REM Copy ntc templates
python .\.build_exe\write_ntc_templates_dir_to_file.py
set /p NTC_TEMPLATES_DIR= < .\.build_exe\ntc_templates_dir.txt

xcopy %NTC_TEMPLATES_DIR% .\.build_exe\dist\%PYINST_EXE_NAME%\templates\ /s /e
