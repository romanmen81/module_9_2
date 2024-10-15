first_strings = ['Elon', 'Musk', 'Programmer', 'Monitors', 'Variable']
second_strings = ['Task', 'Git', 'Comprehension', 'Java', 'Computer', 'Assembler']

# 1. Список длин строк из first_strings с длиной не менее 5 символов.
first_result = [len(s) for s in first_strings if len(s) >= 5]

# 2. Список кортежей из пар слов одинаковой длины.
second_result = [(f, s) for f in first_strings for s in second_strings if len(f) == len(s)]

# 3. Словарь строк из объединенных списков с четной длиной.
combined_strings = first_strings + second_strings
third_result = {s: len(s) for s in combined_strings if len(s) % 2 == 0}

# Выводим результаты
print(first_result)
print(second_result)
print(third_result)
