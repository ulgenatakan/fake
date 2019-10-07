import time
from datetime import datetime
import database
from elimination import create_row_data, eliminate
from random_mac_generator import generate, get_devices, print_devices

all_devices = generate()  # initial device list
current_devices = get_devices(all_devices)  # current device list


class Data:   # Device Object
    def __init__(self, tool_id, devices, time, place):
        self.tool_id = tool_id
        self.devices = devices
        self.time = time
        self.place = place


while(1):
    database.clear()

    # CRON JOB EVERY 10 SECONDS
    for i in reversed(range(1, 11)):
        time.sleep(1)

    # 1 - GET FAKED DEVICE LIST
    current_devices = get_devices(all_devices)

    # 2 - PUT CURRENT_DEVICES INTO LOCAL DB.CURRENT_LOCAL_DEVICES DB.INSERT

    # 3 - CREATE A DATA OBJECT (tool_number, current_devices, time , place)
    #     COLLECT OTHER DEVICE DATAS -> Database GET  # [TO DO]
    data_object_0 = Data(0, current_devices, datetime.now().strftime(
        "%H:%M:%S"), "Speciality Coffee")
    data_object_1 = Data(1, get_devices(all_devices), datetime.now().strftime(
        "%H:%M:%S"), "Speciality Coffee")
    data_object_2 = Data(2, get_devices(all_devices), datetime.now().strftime(
        "%H:%M:%S"), "Speciality Coffee")

    # CREATE ROW DATA
    # Collected Data = A list objects that contains data_objects from tools
    collected_data = [data_object_0, data_object_1, data_object_2]
    # Create merged row data that contains all records.
    create_row_data(collected_data)

    # ELIMINATE DUPLICATE DATA
    # Display all records
    print("Su an databasede ", len(database.get_all()), 'kadar kayit var.')
    # Elimination of duplicate records.
    filtered_data = eliminate()
    # Display filtered data
    print("Su an burada ", len(filtered_data), 'kadar device var.')
