HEAD_TAG=$(git tag --points-at HEAD)
if [ -z "$HEAD_TAG" ]
then
      # $HEAD_TAG is empty, use current version and abbrev commit for release suffix
      CURRENT_VERSION=$(python -c "import pyinstaller_test2;print(pyinstaller_test2.__version__)")
      ABBREV_COMMIT=$( git log -1 --pretty=format:%h)
      echo "$CURRENT_VERSION-$ABBREV_COMMIT"
else
      # HEAD is tagged, use that for release suffix
      echo "$HEAD_TAG"
fi
