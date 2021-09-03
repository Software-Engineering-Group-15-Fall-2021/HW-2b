def even_odd(num):
	print(num)
	if num%2==0:
		return "number is even"
	else:
		return "number is odd"

def test_odd_even():
    assert even_odd(7) == "number is odd", "Should be odd"
    assert even_odd(0) == "number is even", "Should be even"
    

if __name__ == "__main__":
    test_odd_even()
    print("2/2 test cases passed")
