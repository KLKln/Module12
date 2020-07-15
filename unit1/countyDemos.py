import csv


class CountyDemos:
    def __init__(self, population, num_households):
        self.population = population
        self.num_households = num_households

with open('ExampleCSV.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    county = {}
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        county[str(row[0])] = CountyDemos(row[1],row[2])



if __name__ == '__main__':
    print(county)
    print(county['Polk'].population)
    pop_sum = 0
    for key in county:
        pop_sum += int(county[key].population.replace(',',''))
    print(pop_sum)
