import os
import re

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct the full path to original_urls.txt
original_urls_path = os.path.join(script_dir, "original_urls.txt")

# Check if original_urls.txt exists in the same directory
if not os.path.isfile(original_urls_path):
    print("original_urls.txt not found in the script's directory.")
else:
    # Read the list of URLs from original_urls.txt
    with open(original_urls_path, "r") as file:
        original_urls = file.readlines()

    # Initialize an empty list to store the new URLs
    new_urls = []

    # Process each URL and extract the file ID
    for input_url in original_urls:
        input_url = input_url.strip()  # Remove random spaces to keep formatting clean
        match = re.search(r'/d/([^/]+)', input_url)
        if match:
            file_id = match.group(1)
            new_url = "https://drive.google.com/uc?id=" + file_id
            new_urls.append(new_url)
        else:
            print("Unable to extract the file ID from the input URL:", input_url)

    # Write the converted URLs to new_urls.txt in the script's directory
    new_urls_path = os.path.join(script_dir, "new_urls.txt")
    with open(new_urls_path, "w") as file:
        file.writelines([url + "\n" for url in new_urls])

    print("Converted URLs saved to new_urls.txt")
