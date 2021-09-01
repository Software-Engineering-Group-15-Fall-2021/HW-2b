import sys
sys.path.append("../code")
import hw_program as p

def test_odd_even():
    assert p.even_odd(7) == "number is odd", "Should be odd"
    assert p.even_odd(0) == "number is even", "Should be even"
    

if __name__ == "__main__":
    test_odd_even()
    print("2/2 test cases passed")
