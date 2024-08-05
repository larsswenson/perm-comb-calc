import math

def permutations(n, r):
    return math.factorial(n) // math.factorial(n - r)

def combinations(n, r):
    return math.factorial(n) // (math.factorial(r) * math.factorial(n - r))

def main():
    n = int(input("Please enter the total number of items (n): "))
    r = int(input("Please enter the number of items to be chosen or arranged (r): "))
    
    if n < 0 or r < 0 or r > n:
        print("Sorry, invalid input. Please ensure that 0 <= r <= n and n, r are non-negative integers.")
        return
    
    print(f"The number of permutations P({n}, {r}) is: {permutations(n, r)}")
    print(f"The number of combinations C({n}, {r}) is: {combinations(n, r)}")

# Test cases
def run_tests():
    test_cases = [
        (10, 3, (720, 120)),
        (5, 2, (20, 10)),
        (7, 5, (2520, 21)),
        
        # Edge cases
        (0, 0, (1, 1)),  # n = 0, r = 0
        (6, 0, (1, 1)),  # r = 0
        (6, 6, (720, 1)),  # r = n
    ]

    for i, (n, r, expected) in enumerate(test_cases, 1):
        perm_result = permutations(n, r)
        comb_result = combinations(n, r)
        assert (perm_result, comb_result) == expected, f"Test case {i} failed. Got {(perm_result, comb_result)}, expected {expected}."
        print(f"Test case {i} passed!")

if __name__ == "__main__":
    run_tests()
    main()
