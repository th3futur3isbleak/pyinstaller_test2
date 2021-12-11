import os
import shutil
import site


def main():
    # So the output in the github action will be easily identified.
    output_prefix = 'PYTHON: copy_ntc_templates.py '

    # Distribution parent directory where the compiled EXEs will be written to
    distribution_parent_dir = os.path.join('.build_exe', 'dist')

    # Bundles parent directory name
    bundle_parent_dir = 'bundles'
    os.path.abspath('.')
    print(output_prefix + f'Working path {os.path.abspath(".")}')
    # One of these entries will contain the parent directory for the installed packages
    site_packages_directories = site.getsitepackages()

    for site_package_directory in site_packages_directories:
        # while it is possible for there to be multiple site-packages, we are assuming only one
        if 'site-packages' in site_package_directory:
            # This directory has the templates used by textfsm to parse Cisco CLI output
            ntc_templates_dir = os.path.join(site_package_directory, "ntc_templates", "templates")
            print(output_prefix + f"Setting ntc_templates directory to {ntc_templates_dir}")
            # This env variable is set in the github action pyinstaller step
            exe_name = os.environ['PYINST_EXE_NAME']

            # unbundled directory does not use the --onefile pyinstaller argument
            unbundled_dir_templates_dist_path = os.path.join(distribution_parent_dir, exe_name, "templates")
            print(output_prefix + f"Unbundled directory templates path: {unbundled_dir_templates_dist_path}")
            print(output_prefix + 'Copying templates to unbundled distribution directory.')
            shutil.copytree(ntc_templates_dir, unbundled_dir_templates_dist_path)

            # unbundled directory does not use the --onefile pyinstaller argument
            bundled_dir_templates_dist_path = os.path.join(distribution_parent_dir, bundle_parent_dir, exe_name, "templates")
            print(output_prefix + f"Bundled directory templates path: {bundled_dir_templates_dist_path}")
            print(output_prefix + 'Copying templates to bundled distribution directory.')
            # shutil.copytree(ntc_templates_dir, bundled_dir_templates_dist_path)
            with open('ntc_templates_dir.txt', 'w') as output_file:
                output_file.write(f"{ntc_templates_dir}\n")


if __name__ == '__main__':
    main()
