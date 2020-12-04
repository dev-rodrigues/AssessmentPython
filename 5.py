file_a = open('a.txt', 'r')
file_b = open('b.txt', 'r')

line_a = str(file_a.read())
columns_a = line_a.split(' ')
len_columns_a = len(columns_a)

line_b = str(file_b.read())
columns_b = line_b.split(' ')
len_columns_b = len(columns_b)

def add_zero(vet, max_len):
    len_aux = len(vet)

    for v in vet:
        if len_aux < max_len:
            vet.append(0)
            len_aux = len(vet)
        else:
            break
    return vet


if len_columns_a < len_columns_b:
    columns_a = add_zero(columns_a, len_columns_b)
elif len_columns_b < len_columns_a:
    columns_b = add_zero(columns_b, len_columns_a)


sums = []

max = len(columns_a)

for n in range(0, max):
    position_a = int(columns_a[n])
    position_b = int(columns_b[n])

    sum = position_a + position_b
    sums.append(sum)

print(sums)





