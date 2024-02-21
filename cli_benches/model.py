def do_numbers(numbers: list[int]):
    assert all(isinstance(n, int) for n in nubers)
    return numbers

def do_strings(strings: list[str]):
    assert all(isinstance(s, str) for s in strings)
    return strings

def run(numbers: list[int], strings: list[str]):
    print("dem numbers: ", numbers)
    print("dem strings: ", strings)
