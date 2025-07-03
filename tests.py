import os

from functions.run_python import run_python_file

def test():
    print("Test 1: run_python_file('calculator', 'main.py')")
    result = run_python_file("calculator", "main.py")
    print(result)
    print()

    print("Test 2: run_python_file('calculator', 'tests.py')")
    result = run_python_file("calculator", "tests.py")
    print(result)
    print()

    print("Test 3: run_python_file('calculator', '../main.py') (should error)")
    result = run_python_file("calculator", "../main.py")
    print(result)
    print()

    print("Test 4: run_python_file('calculator', 'nonexistent.py') (should error)")
    result = run_python_file("calculator", "nonexistent.py")
    print(result)
    print()

if __name__ == "__main__":
    test()
