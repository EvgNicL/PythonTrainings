calls = 0

def count_calls():
    global calls
    calls += 1
    return calls

def string_info (string):
    count_calls()
    if isinstance(string, str):
        tuple_ = (len(string), string.upper(), string.lower())
        return tuple_
    else: return "Error"

def is_contains(string, list_to_search):
    count_calls()
    for el in list_to_search:
        el.lower()
    if string.lower() in list_to_search:
        return True
    else: return False

# ЗДРАВСТВУЙТЕ, ПОДСКАЖИТЕ, ПОЧЕМУ У МЕНЯ ВАРИАНТ НИЖЕ НЕ СРАБОТАЛ?
    # for el in list_to_search:
    #     if el.lower() == string.lower():
    #         return True
    #     else: return False

print(is_contains("kk", ["hfhfh", 'hhh']))
print(is_contains("kk", ["hfhfh", 'hhh', "kk"]))
print(is_contains("kk", ["hfhfh", 'hhh']))

print(string_info("hghgh"))
print(string_info(12))

print(calls)
