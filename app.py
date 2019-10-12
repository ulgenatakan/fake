# General Modules
import time
from datetime import datetime

# Created Modules
import src.modules as m

# Database Migrations
import src.migration.database as d

# Creted Classes
import src.classes as c


all_devices = m.generate()  # initial device list


while(1):
    d.db_clear()

    # for i in reversed(range(1, 11)):  # CRON JOB EVERY 10 SECONDS
    #    time.sleep(1)

    # current_devices = m.get_devices(all_devices)  # 1 - GET FAKED DEVICE LIST
    # m.print_devices(current_devices)

    # 2 - PUT CURRENT_DEVICES INTO LOCAL DB.CURRENT_LOCAL_DEVICES DB.INSERT
    # d.cld_add_list(current_devices)

    a = d.cld_get_devices()
    # 3 - CREATE A DATA OBJECT (tool_number, current_devices, time , place)
    # COLLECT OTHER DEVICE DATAS -> Database GET  # [TO DO]
    # data_object_0 = c.Data(0, current_devices, datetime.now().strftime(
    #    "%H:%M:%S"), "Speciality Coffee")
    # data_object_1 = c.Data(1, m.get_devices(all_devices), datetime.now().strftime(
    #    "%H:%M:%S"), "Speciality Coffee")
    # data_object_2 = c.Data(2, m.get_devices(all_devices), datetime.now().strftime(
    #    "%H:%M:%S"), "Speciality Coffee")
#
    # collected_data = [data_object_0, data_object_1, data_object_2]  # ROW DATA
#
    # Create merged row data that contains all records.
    # m.create_row_data(collected_data)
#
    #print("Su an databasede ", len(d.db_get_all()), 'kadar kayit var.')
#
    # filtered_data = m.eliminate()  # ELIMINATE DUPLICATE DATA
#
    #print("Su an burada ", len(filtered_data), 'kadar device var.')
