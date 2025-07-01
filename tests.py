from functions.write_file import write_file

def test():
    print('Test 1: write_file("calculator", "lorem.txt", "wait, this is not lorem ipsum")')
    result = write_file("calculator", "lorem.txt", "wait, this isn't lorem ipsum")
    print(result)
    print()

    print('Test 2: write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")')
    result = write_file("calculator", "pkg/morelorem.txt", "lorem ipsum dolor sit amet")
    print(result)
    print()

    print('Test 3: get_file_content("calculator", "/bin/cat") (should error)')
    result = write_file("calculator", "/tmp/temp.txt", "this should not be allowed")
    print(result)
    print()

if __name__ == "__main__":
    test()
