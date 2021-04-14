import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import csv

# Y = np.random.rand(100, 10)

website1 = 0.0
website2 = 0.1


websites_to_values = []
data = []

websites = []

with open('immigration_incognito.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')

    # Extracts columns out of the rows
    for row in spamreader:
        transformed_row = row[0].split(',')
        websites.append(transformed_row[0])
        # second.append(transformed_row[1])
        # third.append(transformed_row[2])
        # fourth.append(transformed_row[3])
        # fifth.append(transformed_row[4])
        # sixth.append(transformed_row[5])
        # seventh.append(transformed_row[6])
        # eigth.append(transformed_row[7])
        # ninth.append(transformed_row[8])
        # tenth.append(transformed_row[9])

        # print(row, '||||')
websites.pop(0)

num = 0
for website in websites:
    websites_to_values.append(num)
    num += 0.1

data.append(websites_to_values)
graph = plt.pcolor(data )
plt.title('Graph')
plt.ylabel("Search Results")
plt.xlabel('Participants')

plt.show()

