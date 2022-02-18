if [ -z "$1" ]
then
    TEMP_DIR=".build_exe"
else
    TEMP_DIR=$1
fi
echo "Temp directory is  $TEMP_DIR"

# Argument one is the path to the source file
# Argument two is the name of the final executable
# --onefile builds a bundle
# --add-data includes files in the bundle
# these files will not be in the temporary directory and
# not visible to the user
# --distpath changes the distribution directory so we have a
# directory read to be copied somewhere with all the associated files
# --workpath changes the build directory to avoid leaving artificacts in the main repo

# create bundles directory if it doesn't exist
mkdir -p $TEMP_DIR/dist/bundles

# Finds ntc_templates directory
NTC_TEMPLATES_DIR=$(python scripts/windows/get_ntc_templates_dir.py)
echo "$NTC_TEMPLATES_DIR"

pyinstaller pyinstaller_test2/show_inventory.py \
	--onefile \
	-n show_version \
	--distpath  $TEMP_DIR/dist/bundles/show_inventory \
	--workpath  $TEMP_DIR/build \
	--specpath  $TEMP_DIR/dist \
	--add-data $NTC_TEMPLATES_DIR:ntc_templates


