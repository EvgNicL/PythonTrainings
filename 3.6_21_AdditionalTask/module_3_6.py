
data_structure = [
  [1, 2, 3],
  {'a': 4, 'b': 5},
  (6, {'cube': 7, 'drum': 8}),
  "Hello",
  ((), [{(2, 'Urban', ('Urban2', 35))}])
]

def calculate_structure_sum(*data):
    summ = 0
    if len(data) == 0:
        return summ

    for i in data:
        if isinstance(i, str):
            summ += len(i)
        elif isinstance(i, int):
            summ += i
        elif isinstance(i, dict):
            list_ = []
            for key, value in i.items():
                list_.extend([key, value])
            summ += calculate_structure_sum(list_)
        else:
            summ += calculate_structure_sum(*i)
    return summ



result = calculate_structure_sum(data_structure)
print(result)

