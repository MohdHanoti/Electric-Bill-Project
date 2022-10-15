import pytest

from Bill import bill

def test_set_name_str():
    """Test str and set name functions"""
    bill.set_name("mohammad")
    mohammad=bill
    actual=str(mohammad)
    expected="welcome mohammad to the elictrical bill program"
    assert actual == expected
#***********************************************************************
"""Test if uodate function updates the taxes object correctlly"""
def test_update_Taxes_1():
    
    bill.set_KW(550)
    bill.update_Taxes()
    actual=bill.Taxes["Trash tax"]
    expected=3.41
    assert actual == expected

def test_update_Taxes_2():
    bill.set_KW(550)
    bill.update_Taxes()
    actual=bill.Taxes["other taxes"]
    expected=0.550
    assert actual == expected
#**********************************************************************
"""Test if get elictric price function will give correct return for differunt cases"""
def test_get_elictric_price_1():
    bill.set_KW(550)
    actual=bill.get_elictric_price()
    expected=38.260000000000005
    assert actual== expected

def test_get_elictric_price_2():
    bill.set_KW(50)
    actual=bill.get_elictric_price()
    expected=1.6500000000000001
    assert actual== expected

def test_get_elictric_price_3():
    bill.set_KW(850.5)
    actual=bill.get_elictric_price()
    expected=86.554
    assert actual== expected

def test_get_elictric_price_4():
    bill.set_KW(-50)
    actual=bill.get_elictric_price()
    expected="Please enter a positive power consumbtion in KW"
    assert actual== expected
#**********************************************************************
""" Test the final output """

def test_get_final_price_1():
     bill.set_KW(500)
     bill.update_Taxes()
     actual=bill.get_final_price()
     expected= 37.42
     assert actual==expected

def test_get_final_price_2():
     bill.set_KW(1030.80)
     bill.update_Taxes()
     actual=bill.get_final_price()
     expected= 130.86679999999998
     assert actual==expected

def test_get_data():
    bill.set_KW(500)
    bill.set_name("mohammad")
    bill.update_Taxes()
    actual=bill.get_data()
    expected= f"""
        welcome mohammad to the elictrical bill program
        Your elictrical consumbtion is 500 KW
        and your elictrical consumbtion price is 32.56 JD
        taxes :{bill.Taxes}

        and your total price is 37.42 JD

        """
    assert actual==expected    