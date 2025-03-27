import timeit

d = ['1', '2', '3', '4']

string = '    '

# Форматирование через .format()
format_time = timeit.timeit('"".join(d[i] + c if i % 2 == 1 else c for i, c in enumerate(d,1))', number=10**6)
dsad = timeit.timeit('string.replace(" ", "s", 2)', number=10**6)


print("Join", format_time)
print("Replace", dsad)