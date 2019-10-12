from randmac import RandMac
import random


class Device:   # Device Object
    def __init__(self, mac_number, device_id):
        self.mac_number = mac_number
        self.device_id = device_id


# Generate Random Mac Numbers and create device object.
def generate_devices(n, arr):
    for i in range(n):
        arr.append(Device(RandMac("00:00:00:00:00:00"), i))


def select_devices(n, arr):  # Select Random Devices
    tmp_arr = arr[:]
    devices = []
    for i in range(n):
        selected = random.choice(tmp_arr)
        devices.append(selected)
        tmp_arr.remove(selected)
    return devices


def print_devices(arr):  # Print Devices
    for device in arr:
        print("DEVICE", device.device_id, "- MAC:", device.mac_number)


def generate():  # Generate Devices
    # Device Array
    devices_list = []

    # Initialize Device Array
    generate_devices(50, devices_list)
    return devices_list


def get_devices(arr):  # Select Random Devices
    n = random.randrange(10)
    selected_devices = select_devices(n, arr)
    print("selected_devices", len(selected_devices))
    return selected_devices
