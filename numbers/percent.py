def calc(total=None, part=None, percent=None):
    """
     %     part
    ---- = ----
    100    total
    """
    if percent and total:
        return total * (percent / 100)
    elif part and percent:
        return 100 / percent * part
    return part / total * 100