
def test_calculator():
    test_cases = [
        ("2+3", "5.0"),
        ("10-4", "6.0"),
        ("7*6", "42.0"),
        ("8/2", "4.0"),
        ("2+3*4", "14.0"),
        ("2*(3+4)", "14.0"),  
        ("5/0", "Infinity"),
        ("-2+3", "1.0"),
        ("2.5+3.1", "5.6"),
        ("2++3", "ERROR")
    ]
    
    for expression, expected in test_cases:
        result = Calculator.run(expression)
        print(f"Expression: {expression} | Expected: {expected} | Result: {result} | {'Pass' if result == expected else 'Fail'}")

test_calculator()
