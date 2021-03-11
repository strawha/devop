from devop import *

def test_square_root():
    assert square_root(4) == 2.0
    assert square_root(70.5) == 8.396427811873332
    assert square_root(0) == 0.0

def test_factorial():
    assert factorial(4) == 24
    assert factorial(0) == 1
    assert factorial(1) == 1

def test_natural_log():
    assert natural_log(10) == 2.302585092994046
    assert natural_log(2.2) == 0.7884573603642703
    assert natural_log(1) == 0.0

def test_power():
    assert power(2,3) == 8.0
    assert power(100,-2) == 0.0001
    assert power(3,0) == 1.0
    assert power(0,4) == 0.0
    assert power(-2,3) == -8.0
