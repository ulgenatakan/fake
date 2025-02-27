from .database import db_add_item, db_get_all


def create_row_data(row_data):  # Merge Devices from Tools
    for data in row_data:
        for device in data.devices:
            db_add_item({
                "tool_id": data.tool_id,
                "device_id": device.device_id,
                "mac_number": device.mac_number,
                "time": data.time,
                "place": data.place,
            })


def filter_dicts(target, key):  # Filter and Remove Duplicate Elements
    seen = set()  # a temporary set to store already visited values
    return [d for d in target if d[key] not in seen and not seen.add(d[key])]


def eliminate():  # Elimination of Duplicate Devices by Mac Number
    data = db_get_all()
    return filter_dicts(data, "mac_number")
