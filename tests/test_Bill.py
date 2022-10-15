import pytest

from Bill import Bill

def name_test():
    mohammad=Bill("mohammad",250)
    actual=str(mohammad)
    expected="welcome mohammad to the elictrical bill program"
    assert actual == expected
