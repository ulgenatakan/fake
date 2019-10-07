row_database = []


def add_item(item):  # Add an item to database
    row_database.append(item)


def del_item(item):  # Del an item to database
    row_database.remove(item)


def get_all():  # Get all item
    return row_database


def clear():   # Clear all items from database
    row_database.clear()
