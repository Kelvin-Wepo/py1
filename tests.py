from shop import donut_costs


if __name__ == '__main__':
    # Test 1: num_donuts is 6 and customer is a member
    assert donut_costs(6, True) == 450
    
    # Test 2: num_donuts is 9 and customer is not a member
    assert donut_costs(9, False) == 720
    
    # Test 3: num_donuts is 1 and customer is a member
    assert donut_costs(1, True) == 85
    
    # Test  4: num_donuts is 2 and customer is not a member
    assert donut_costs(2, False) == 160
    
    # Test 5: num_donuts is 10 and customer is a member
    print(donut_costs(10, True)) # add this line
    
    # Test  6: num_donuts is 10 and customer is not a member
    assert donut_costs(10, False) == 700



