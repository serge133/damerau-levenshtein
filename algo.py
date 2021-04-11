from pyxdameraulevenshtein import damerau_levenshtein_distance
import csv

_first = []
second = []
third = []
fourth = []
fifth = []
sixth = []
seventh = []
eigth = []
ninth = []
tenth = []

columns = []

total_diff = 0.0
total_avg = 0.0

print("filename:")
file_name = str(input())

with open(file_name + '.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    # Extracts columns out of the rows
    for row in spamreader:
        transformed_row = row[0].split(',')
        # print(transformed_row)
        # first.append(transformed_row[0])
        second.append(transformed_row[1])
        third.append(transformed_row[2])
        fourth.append(transformed_row[3])
        fifth.append(transformed_row[4])
        sixth.append(transformed_row[5])
        seventh.append(transformed_row[6])
        eigth.append(transformed_row[7])
        ninth.append(transformed_row[8])
        tenth.append(transformed_row[9])

        # print(row, '||||')

# print(second)
second.pop(0)
third.pop(0)
fourth.pop(0)
fifth.pop(0)
sixth.pop(0)
seventh.pop(0)
eigth.pop(0)
ninth.pop(0)
tenth.pop(0)


columns.append(','.join(second))
columns.append(','.join(third))
columns.append(','.join(fourth))
columns.append(','.join(fifth))
columns.append(','.join(sixth))
columns.append(','.join(seventh))
columns.append(','.join(eigth))
columns.append(','.join(ninth))
columns.append(','.join(tenth))

# * Compares adjacent Columns
# for column_index in range(8):
#     print(columns[column_index])
#     print(columns[column_index+1])

#     diff_tmp += damerau_levenshtein_distance(columns[column_index].split(','), columns[column_index + 1].split(',')) 

for column_index in range(8):
    # * First Column
    total_diff += damerau_levenshtein_distance(columns[0].split(','), columns[column_index + 1].split(',')) / 8
    # * Second Column
    if column_index < 7:
        total_diff += damerau_levenshtein_distance(columns[1].split(','), columns[column_index + 2].split(',')) / 7
    # * Third Column
    if column_index < 6:
        total_diff += damerau_levenshtein_distance(columns[2].split(','), columns[column_index + 3].split(',')) /6
    # * Fourth Column
    if column_index < 5:
        total_diff += damerau_levenshtein_distance(columns[3].split(','), columns[column_index + 4].split(',')) /5
    # * Fifth Column
    if column_index < 4:
        total_diff += damerau_levenshtein_distance(columns[4].split(','), columns[column_index + 5].split(',')) /4
    # * Sixth Column
    if column_index < 3:
        total_diff += damerau_levenshtein_distance(columns[5].split(','), columns[column_index + 6].split(',')) /3
    # * Seventh Column
    if column_index < 2:
        total_diff += damerau_levenshtein_distance(columns[6].split(','), columns[column_index + 7].split(',')) /2
    # * Eighth Column
    if column_index < 1:
        total_diff += damerau_levenshtein_distance(columns[7].split(','), columns[column_index + 8].split(',')) /1

 


# * Results
total_avg += (total_diff / 8)

print('Total Difference: ', total_diff)
print('Average Difference', total_avg)

# print(damerau_levenshtein_distance([1, 2, 3, 4, 5, 6], [7, 8, 9, 7, 10, 11, 4]))