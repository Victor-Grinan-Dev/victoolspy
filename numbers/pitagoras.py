def is_close(position1: tuple, position2: tuple, req_distance: int):
    """

    :param position1: x,y coordinates of object 1
    :param position2: x,y coordinates of object 2
    :param req_distance: distance to be considered close
    :return: true or false
    """
    a = position1[0] - position2[0]
    b = position1[1] - position2[1]
    distance = ((a ** 2) + (b ** 2)) ** 0.5

    if distance < req_distance:
        return True
    else:
        return False
