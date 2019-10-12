import psycopg2


def cld_add_item(device):
    """ insert a new device into the currrent_local_devices table """
    sql = """INSERT INTO current_local_devices(mac_number)
             VALUES(%s) RETURNING id;"""
    try:
        conn = psycopg2.connect(host="localhost", database="countdb",
                                user="postgres", password="postgres")
        cur = conn.cursor()
        # execute the INSERT statement
        cur.execute(sql, (device.mac_number,))
        # get the generated id back
        device_id = cur.fetchone()[0]
        # commit the changes to the database
        conn.commit()
        # close communication with the database
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()
    return device_id


def cld_add_list(devices):
    sql = "INSERT INTO current_local_devices(mac_number) VALUES(%s)"
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="countdb",
                                user="postgres", password="postgres")
        cur = conn.cursor()
        mac_adresses = list(
            map(lambda x: getattr(x, 'mac_number'), devices))
        mac_adresses = list(map(lambda x: (x,), mac_adresses))
        cur.executemany(sql, mac_adresses)
        conn.commit()
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def cld_get_devices():
    """ query data from the vendors table """
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="countdb",
                                user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute("SELECT mac_number FROM current_local_devices")
        print("The number of parts: ", cur.rowcount)
        row = cur.fetchone()
        a = []
        while row is not None:
            print(row)
            a.append(row[0])
            row = cur.fetchone()
        return a
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


row_database = []


def db_add_item(item):  # Add an item to database
    row_database.append(item)


def db_del_item(item):  # Del an item to database
    row_database.remove(item)


def db_get_all():  # Get all item
    return row_database


def db_clear():   # Clear all items from database
    row_database.clear()
