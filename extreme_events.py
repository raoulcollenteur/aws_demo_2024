""" Method to check if an event is extreme.
"""


def check_extreme_event(value):
    """check_extreme_event

    Parameters
    ----------
    value : float
        value of the precipitation event.

    """
    if value > 100:
        print(
            "This is an extreme event, precipitation is greater than 100mm. Prepare for a flood."
        )
    elif value < 10:
        print(
            "This is not an extreme event, precipitation is less than 10mm. But it might get dry."
        )
    else:
        print(
            "This is not an extreme event, precipitation is less than 100mm. No need to worry."
        )

check_extreme_event(101)
check_extreme_event(1)