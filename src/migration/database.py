row_database = []


def db_add_item(item):  # Add an item to database
    row_database.append(item)


def db_del_item(item):  # Del an item to database
    row_database.remove(item)


def db_get_all():  # Get all item
    return row_database


def db_clear():   # Clear all items from database
    row_database.clear()
