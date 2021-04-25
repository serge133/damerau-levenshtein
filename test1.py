import matplotlib.pyplot as plt
import numpy as np
from matplotlib.colors import LogNorm
import csv

# Y = np.random.rand(100, 10)

website1 = 0.0
website2 = 0.1


websites_to_values = []

websites = []

graph_data = []

with open('immigration_incognito.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=' ', quotechar='|')
    # Extracts columns out of the rows
    for row in spamreader:
        transformed_row = row[0].split(',')
        print(transformed_row)
        websites.append(transformed_row[0])
        graph_data_row = []
        transformed_row.pop(0)

        for num in transformed_row:
            graph_data_row.append(float(num) / 10)

        graph_data.append(graph_data_row)
        # print(row, '||||')
websites.pop(0)


num = 0
for website in websites:
    websites_to_values.append(num)
    num += 0.1

print(websites, websites_to_values)
graph = plt.pcolor(graph_data)
plt.title('Graph')
plt.ylabel("Search Results")
plt.xlabel('Participants')

plt.show()

