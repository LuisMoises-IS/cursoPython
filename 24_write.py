with open('./text.txt', 'r+') as file:
    for line in file:
        print(line)

    file.write('Nuevas cosas en este archivo\n')
    file.write('otra linea\n')
    file.write('mas lineas\n')


