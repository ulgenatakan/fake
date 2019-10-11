# General Modules
import time
from datetime import datetime

# Created Modules
import modules as m

# Creted Classes
import classes as c


all_devices = m.generate()  # initial device list
current_devices = m.get_devices(all_devices)  # current device list


while(1):
    m.db_clear()

    # CRON JOB EVERY 10 SECONDS
    for i in reversed(range(1, 11)):
        time.sleep(1)

    # 1 - GET FAKED DEVICE LIST
    current_devices = m.get_devices(all_devices)

    # 2 - PUT CURRENT_DEVICES INTO LOCAL DB.CURRENT_LOCAL_DEVICES DB.INSERT

    # 3 - CREATE A DATA OBJECT (tool_number, current_devices, time , place)
    #     COLLECT OTHER DEVICE DATAS -> Database GET  # [TO DO]
    data_object_0 = c.Data(0, current_devices, datetime.now().strftime(
        "%H:%M:%S"), "Speciality Coffee")
    data_object_1 = c.Data(1, m.get_devices(all_devices), datetime.now().strftime(
        "%H:%M:%S"), "Speciality Coffee")
    data_object_2 = c.Data(2, m.get_devices(all_devices), datetime.now().strftime(
        "%H:%M:%S"), "Speciality Coffee")

    # CREATE ROW DATA
    # Collected Data = A list objects that contains data_objects from tools
    collected_data = [data_object_0, data_object_1, data_object_2]
    # Create merged row data that contains all records.
    m.create_row_data(collected_data)

    # ELIMINATE DUPLICATE DATA
    # Display all records
    print("Su an databasede ", len(m.db_get_all()), 'kadar kayit var.')
    # Elimination of duplicate records.
    filtered_data = m.eliminate()
    # Display filtered data
    print("Su an burada ", len(filtered_data), 'kadar device var.')
