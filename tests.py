from functions.get_file_content import get_file_content

def test():
    print("Test 1: get_file_content('calculator', 'main.py')")
    result = get_file_content("calculator", "main.py")
    print(result)
    print()

    print("Test 2: get_file_content('calculator', 'pkg/calculator.py')")
    result = get_file_content("calculator", "pkg/calculator.py")
    print(result)
    print()

    print("Test 3: get_file_content('calculator', '/bin/cat') (should error)")
    result = get_file_content("calculator", "/bin/cat")
    print(result)
    print()

if __name__ == "__main__":
    test()
