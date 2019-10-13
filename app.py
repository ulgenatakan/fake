#########################
#       IMPORTS         #
#########################
# General Modules
import time
from datetime import datetime

# Created Modules
import src.modules as m

# Database Migrations
import src.migration.database as d

# Creted Classes
import src.classes as c


#########################
#  GENERATING DEVICES   #
#########################

# initial device list FAKED
all_devices = m.generate()


while(1):
    d.db_clear()

    #########################
    #       CRON JOB        #
    #########################
    for i in reversed(range(1, 11)):
        print(10-i, end=" - ")
        time.sleep(1)

    #########################
    #   SNIFFING DEVICES    #
    #########################
    current_devices = m.get_devices(all_devices)
    m.print_devices(current_devices)

    ############################
    # INSERTING INTO CLD TABLE #
    ############################
    d.cld_add_list(current_devices)

    ###########################################
    # CREATING DATA OBJECT AND COLLECTED DATA #
    ###########################################
    # 3 - Create a data object (tool_number, current_devices, time , place)
    tmp = d.cld_get_devices()
    devices_0 = list(map(lambda x: c.Device(x), tmp))
    data_object_0 = c.Data(0, devices_0, datetime.now().strftime(
        "%H:%M:%S"), "Speciality Coffee")
    data_object_1 = c.Data(1, m.get_devices(all_devices), datetime.now().strftime(
        "%H:%M:%S"), "Speciality Coffee")
    data_object_2 = c.Data(2, m.get_devices(all_devices), datetime.now().strftime(
        "%H:%M:%S"), "Speciality Coffee")
    collected_data = [data_object_0, data_object_1, data_object_2]  # ROW DATA

    ##########################################
    # INSERTING COLLECTED DATA INTO CD TABLE #
    ##########################################
    # m.create_row_data(collected_data)
#
    # print("Su an databasede ", len(d.db_get_all()), 'kadar kayit var.')
#
    # filtered_data = m.eliminate()  # ELIMINATE DUPLICATE DATA
#
    # print("Su an burada ", len(filtered_data), 'kadar device var.')
