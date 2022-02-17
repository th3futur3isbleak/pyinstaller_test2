"""Used to add discover the location of site-packages.  This is used to either copy the
ntc-templates directory into a distribution folder or add it to the PyInstaller
bundle by including it with the --add-data argument.

The full path of ntc-templates is written to stdout."""
from pathlib import Path
import site


def main():
    # One of these entries will contain the parent directory for the installed packages
    site_packages_directories = site.getsitepackages()

    for site_package_directory in site_packages_directories:
        # while it is possible for there to be multiple site-packages, we are assuming only one
        if 'site-packages' in site_package_directory:
            # This directory has the templates used by TextFSM to parse Cisco CLI output
            print(Path(site_package_directory) / "ntc_templates")


if __name__ == '__main__':
    main()
