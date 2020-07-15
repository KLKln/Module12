import csv


class IowaCounties:
    def __init__(self, pci, mhi, mfi, pop, noh):
        self.per_capit_income = pci
        self.median_household_income = mhi
        self.median_family_income = mfi
        self.population = pop
        self.num_of_households = noh


with open('Iowa 2010 Census Data Population Income.csv') as csv_file:
    csv_reader = csv.reader(csv_file, delimiter=",")
    line_count = 0
    county = {}
    for row in csv_reader:
        if line_count == 0:
            line_count += 1
            continue
        county[str(row[1])] = IowaCounties(row[2],row[3],row[4],row[5], row[6])


def pop_per_household_dallas_county():
    dal_co_pop = county['Dallas'].population.replace(',','')
    dal_co_hh = county['Dallas'].num_of_households.replace(',','')
    pphdc = int(dal_co_pop)/int(dal_co_hh)
    print('Population per household of Dallas County:', pphdc)


def total_pop_iowa():
    pop_sum = 0
    for key in county:
        if key == "United States":
            pop_sum += 1
            continue
        if key == "Iowa State":
            pop_sum += 1
            continue
        pop_sum += int(county[key].population.replace(',',''))
    print('Total population of Iowa:', pop_sum)


if __name__ == '__main__':
    print(county)
    pop_per_household_dallas_county()
    total_pop_iowa()
