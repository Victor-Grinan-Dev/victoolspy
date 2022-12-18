def set_in_same_order(some_list):
    unique_items = []

    for item in some_list:
        if item not in unique_items:
            unique_items.append(item)

    return unique_items