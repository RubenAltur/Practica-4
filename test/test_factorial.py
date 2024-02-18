import pytest
from src.factorial import factorial


def test_factorialInt():
    with pytest.raises(TypeError):
        factorial("r")==0

def test_factorial_major0():
   with pytest.raises(ValueError):
     factorial(-5)==-5

def test_factorial_de_1():
    assert factorial(1)==1

def test_factorial_de_5():
    assert factorial(5)==120