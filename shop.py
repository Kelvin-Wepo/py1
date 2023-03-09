def donut_costs(num_donuts, member):
    """
    Calculate the total cost of a donut order in cents.

    Parameters:
    num_donuts (int): Number of donuts the customer is purchasing.
    member (bool): True if the customer is a member, False otherwise.

    Returns:
    int: Total cost of the customer's order in cents.
    """
    if num_donuts == 1:
        cost_per_donut = 90
    elif 2 <= num_donuts <= 9:
        cost_per_donut = 80
    else:
        cost_per_donut = 70

    if member:
        cost_per_donut -= 5

    total_cost = num_donuts * cost_per_donut
    return total_cost
