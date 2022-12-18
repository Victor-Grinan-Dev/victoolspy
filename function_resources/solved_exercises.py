# We want to make a row of bricks that is goal inches long. We have a number of small bricks (1 inch each) and big
# bricks (5 inches each). Return True if it is possible to make the goal by choosing from the given bricks.
# This is a little harder than it looks and can be done without any loops. See also: Introduction to MakeBricks

def make_bricks(small, big, goal):
    b_bricks = []
    s_bricks = []
    for _ in range(small):
        s_bricks.append(1)
    for _ in range(big):
        b_bricks.append(5)
    print(s_bricks, b_bricks)

    while goal > 0:
        if goal >= 5 and b_bricks:
            goal -= 5
            b_bricks.pop()
            if goal == 0:
                return True
        elif s_bricks:
            for _ in s_bricks:
                goal -= 1
                s_bricks.pop()
                if goal == 0:
                    return True
        else:
            return False


def make_bricks1(small, big, goal):
    """works fine, not in the page"""
    leftover = goal
    big_value = 5
    for brick in range(big):
        if leftover - big_value >= 0:
            leftover -= big_value

    if small >= leftover >= 0:
        return True

    return False
