import sys
import subprocess
import pkg_resources
from main import main

installed_packages = pkg_resources.working_set
installed_packages_list = sorted(["%s==%s" % (i.key, i.version)
                                  for i in installed_packages])

package_list = []
found_auth, found_client = False, False

for package in range(len(installed_packages_list)):
    package_list.append(installed_packages_list[package].split("=="))

    if "google-auth-oauthlib" in package_list[len(package_list)-1][0]:
        found_auth = True

    if "google-api-python-client" in package_list[len(package_list)-1][0]:
        found_client = True

    if found_client and found_auth is True:
        print("Required packages found...")
        main()

if found_auth or found_client is False:
    if found_auth is False:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'google-auth-oauthlib'])
    if found_client is False:
        subprocess.check_call([sys.executable, '-m', 'pip', 'install', 'google-api-python-client'])

input("Press enter once installation has been completed.")
main()
