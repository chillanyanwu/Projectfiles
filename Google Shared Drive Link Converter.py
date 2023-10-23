#import resources needed

import re
import subprocess
import platform

# Get the input URL from the user
input_url = input("Enter/paste the Google Drive file URL: ")

# Use regular expression to extract the file ID
match = re.search(r'/d/([^/]+)', input_url)

if match:
    file_id = match.group(1)
    new_url = "https://drive.google.com/uc?id=" + file_id
    print("New URL:", new_url)

    # Copy the new URL to the clipboard using platform-specific code
    if platform.system() == "Darwin":  # macOS
        subprocess.run(["pbcopy"], text=True, input=new_url)
        print("New URL copied to clipboard!")
    elif platform.system() == "Linux":
        subprocess.run(["xclip", "-selection", "c"], text=True, input=new_url)
        print("New URL copied to clipboard!")
    elif platform.system() == "Windows":
        subprocess.run(["clip"], text=True, input=new_url)
        print("New URL copied to clipboard!")
    else:
        print("Clipboard copying is not supported on this platform.")
else:
    print("Unable to convert Google Drive link. Please check link and try again")


