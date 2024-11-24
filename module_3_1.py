
calls = 0

def count_calls():
    global calls
    calls += 1

def string_info(string: str):
    count_calls()
    return len(string), string.upper(), string.lower()

def is_contains(string: str, list_to_search: list):
    count_calls()
    return string.lower() in (item.lower() for item in list_to_search)


result1 = string_info("Hello, World!")
print(result1)

result2 = string_info("Armageddon")
print(result2)

result3 = is_contains('Urban', ['ban', 'BaNaN', 'urBAN'])
print(result3)

result4 = is_contains('cycle', ['recycling', 'cyclic'])
print(result4)


print(calls)
