# Author Name: James Lee
# Date: 6/5/2022
# Program Name: Lee_Population.py
# Purpose: Given starting number, average daily increase, and number of days of growth,
#          display a table showing ~size of population for each day.

def main():

    # Get starting number of organisms
    num_init_organisms = float(input('\nStarting number of organisms: '))

    # Make sure starting number of organisms is greater than 0
    while num_init_organisms <= 0:
        print('ERROR: The starting number of organisms must be greater than 0.')
        num_init_organisms = float(input('Starting number of organisms: '))

    # Get average daily increase as a percent
    ave_daily_increase = float(input('Average daily increase (percent): '))

    # Get number of days to multiply
    duration = int(input('Number of days to multiply: '))

    # Make sure the number of days is greater than 0
    while duration <= 0:
        print('ERROR: The number of days to multiply must be greater than 0.')
        duration = int(input('Number of days to multiply: '))

    # Initialize the total population count
    total = num_init_organisms
    print("Day\t\tPopulation")

    # Calculate the population growth for each day
    for day in range(1, duration+1, 1):

        # Day 1 is just the starting number of initial organisms
        if day == 1:
            print("1\t\t" + format(num_init_organisms, '.1f'))
        else:

            # Population growth for Day 2 and on...
            total = total + total * ave_daily_increase * .01

            # Trim leading and trailing zeros from result before printing
            tempStr = str(day) + '\t\t' + format(total, '.5f').strip("0")
            print(tempStr)


# Call the main function.
main()
