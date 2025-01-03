import purestorage
import urllib3

# Connect to the Pure Storage FlashArray
array = purestorage.FlashArray('<IP/HOSTNAME>', api_token='<API-TOKEN>')

# Specify the volume name
volume_name = "<VOLUME-NAME>"

# Fetch volume details
try:
    volume_details = array.get_volume(volume_name)
    print(f"Volume Details for '{volume_name}':")
    print(f"  Name: {volume_details['name']}")
    print(f"  Size: {volume_details['size']} bytes")
    print(f"  Created: {volume_details['created']}")
    print(f"  Source: {volume_details['source']}")
except purestorage.PureError as e:
    print(f"Error fetching volume details: {e}")
    exit(1)

# List Connected Host Groups
try:
    connections = array.list_volume_private_connections(volume_name)
    if connections:
        print(f"\nHost Groups Connected to Volume '{volume_name}':")
        for connection in connections:
            print(f"  Host Group: {connection['host_group']}, LUN: {connection['lun']}")
    else:
        print(f"No host groups are connected to the volume '{volume_name}'.")
except purestorage.PureError as e:
    print(f"Error fetching connected host groups: {e}")
    exit(1)


# Logout from the array
array.invalidate_cookie()
