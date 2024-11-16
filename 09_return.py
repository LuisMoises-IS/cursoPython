def find_volume(length = 1, width = 1, depth = 1):
    return length * width * depth, width, 'Hola'

result = find_volume(10, 20)

print(result)
print(result[1])

result_vol, width, text = find_volume(10, 5)
print(result_vol)
print(width)
print(text)