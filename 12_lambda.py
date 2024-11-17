def increment(x):
    return x + 1

result = increment(10)
print(result)

# Funcion Lambda

incremente_v2 = lambda x : x + 1

result_v2 = incremente_v2(20)

print(result_v2)

full_name = lambda name, last_name : f'Full name is {name} {last_name}'

student = full_name ('Luis', 'Hernandez')
print(student)