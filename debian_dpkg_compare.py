import re
import subprocess
import sys


def main():
    """Get information about the Debian packages in an older system and the current system or another system."""

    if len(sys.argv) > 2:
        new_file_info = read_in_dpkg_listing_output_file(sys.argv[2])
        new_pkgs = parse_package_listing(new_file_info)
    else:
        packager_output, _ = gather_dpkg_package_listing()
        new_pkgs = parse_package_listing(packager_output.splitlines())

    old_file_info = read_in_dpkg_listing_output_file(sys.argv[1])
    old_pkgs = parse_package_listing(old_file_info)

    # Cause dicts are great, but never are they sorted
    old_pkg_names = old_pkgs.keys()
    old_pkg_names.sort()

    print("Old packages not in new system...")
    for pkg in old_pkg_names:
        if pkg not in new_pkgs:
            print("{}\n\t\t\t\t{}".format(pkg, old_pkgs[pkg]))


def parse_package_listing(listing):
    """Parse the package listing from the given list."""
    pkg = {}
    counter = 0
    for pkg_info_line in listing:
        counter += 1
        if counter > 5:
            pkg_info = pkg_info_line.split()
            pkg_name = pkg_info[1]
            pkg_version = pkg_info[2]
            pkg[pkg_name] = pkg_version
    return pkg


def gather_dpkg_package_listing():
    """Run dpkg -l and gather in input."""
    list_pkgs_process = subprocess.Popen(["dpkg", "-l"], stdout=subprocess.PIPE)
    return list_pkgs_process.communicate()


def read_in_dpkg_listing_output_file(filename):
    """Reads in a text file with output from dpkg -l."""
    with open(filename, "r") as input_file:
            file_contents = input_file.readlines()
    return file_contents


if __name__ == '__main__':
    main()
