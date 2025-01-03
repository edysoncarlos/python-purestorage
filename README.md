This repository contains a simple Python script demonstrating basic interaction with a Pure Storage FlashArray using the official Pure Storage Python library.

**Prerequisites:**

Python: Ensure you have Python installed on your system.
Pure Storage Python Library: Install the library using pip:

pip install purestorage

Pure Storage FlashArray Credentials: Obtain the IP address/hostname and API token for your FlashArray.

**How to Use:**

**Replace Placeholders:**

Update <IP/HOSTNAME> with the actual IP address or hostname of your FlashArray.
Replace <API-TOKEN> with your valid API token.
Replace <VOLUME-NAME> with the name of the volume you want to query.
Run the Script: Execute the Python script:

python your_script_name.py

**Script Functionality:**

Connects to FlashArray: Establishes a connection to the specified FlashArray using the provided API token.
Fetches Volume Details: Retrieves information about the specified volume, including its name, size, creation time, and source.
Lists Connected Host Groups: Displays a list of host groups connected to the volume and their respective LUNs.
Logs Out: Invalidates the session cookie to maintain proper security.


Note:
This is a basic example. The Pure Storage Python library offers a wide range of functionalities for interacting with FlashArrays. Refer to the official library documentation for more advanced usage.
