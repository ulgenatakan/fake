import psycopg2
import requests


def cld_add_item(mac_number):
    url = "http://127.0.0.1:8000/current-local/"
    response = requests.post(url, data={"mac_number": mac_number})
    print(response.text, response.status_code)


def cld_add_list(devices):
    for device in devices:
        cld_add_item(device.mac_number)


def cld_get_devices():
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="countdb",
                                user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute(
            "SELECT row_to_json(current_local_devices) FROM current_local_devices")
        row = cur.fetchone()

        a = []
        while row is not None:
            a.append(row[0]["mac_number"][1:-1])
            row = cur.fetchone()
        return a
        cur.close()
    except (Exception, psycopg2.DatabaseError) as error:
        print(error)
    finally:
        if conn is not None:
            conn.close()


def cld_clear():
    conn = None
    try:
        conn = psycopg2.connect(host="localhost", database="countdb",
                                user="postgres", password="postgres")
        cur = conn.cursor()
        cur.execute("DELETE FROM current_local_devices")
        conn.commit()
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
