"""
    Description of program
    Filename: platt_project_5.py
    Author: Ben Platt
    Date: 3/11/24
    Course: COMP-1352
    Assignment: Project 5
    Collaborators: N/A
    Internet Source: W3Schools
"""

class Election:
    def __init__(self, district_number, dem_votes, rep_votes):
        """
        Initialize an Election object with district number, Democratic votes, and Republican votes.

        Parameters:
        - district_number: The district number for the election.
        - dem_votes: The number of votes for the Democratic candidate.
        - rep_votes: The number of votes for the Republican candidate.
        """
        self.district_number = district_number
        self.dem_votes = dem_votes
        self.rep_votes = rep_votes


def read_election_data(filename):
    """
    Read the election data from a file and store it in a nested dictionary.

    Parameters:
    - filename: The name of the file containing election data.

    Returns:
    - A nested dictionary containing election data by year and state.
    """
    election_results = {}
    with open(filename, 'r') as file:
        for line in file:
            # Split the line by commas to extract data
            data = line.strip().split(',')
            # Extract year and state from the first two elements
            year = data[0]
            state = data[1]
            districts = []
            # Iterate over remaining elements in sets of three to extract district info
            for i in range(2, len(data), 3):
                district_number = data[i]
                dem_votes = float(data[i+1])
                rep_votes = float(data[i+2])
                district = Election(district_number, dem_votes, rep_votes)
                districts.append(district)
            # Store district data for each state in the corresponding year
            if year not in election_results:
                election_results[year] = {}
            election_results[year][state] = districts
    return election_results


def calculate_wasted_votes(districts):
    """
    Calculate wasted votes for Democratic and Republican candidates.

    Parameters:
    - districts: A list of Election objects representing districts.

    Returns:
    - Wasted Democratic votes and wasted Republican votes.
    """
    dem_wasted = rep_wasted = 0
    for district in districts:
        # Wasted votes are the excess of votes for a candidate beyond the threshold to win
        dem_wasted += max(0, district.dem_votes - (district.dem_votes + district.rep_votes) / 2)
        rep_wasted += max(0, district.rep_votes - (district.dem_votes + district.rep_votes) / 2)
    return dem_wasted, rep_wasted


def calculate_efficiency_gap(dem_wasted, rep_wasted):
    """
    Calculate the efficiency gap and which party it favors.

    Parameters:
    - dem_wasted: Total wasted votes for the Democratic candidate.
    - rep_wasted: Total wasted votes for the Republican candidate.

    Returns:
    - Efficiency gap percentage and the favored party.
    """
    total_votes = dem_wasted + rep_wasted
    gap = abs(dem_wasted - rep_wasted) / total_votes * 100
    favor = "Democrats" if dem_wasted < rep_wasted else "Republicans"
    return gap, favor


def main():
    """
    Main function to run the program.
    """
    print("This program evaluates districting fairness for US House elections from 1976-2020.")
    election_results = read_election_data("election_data.txt")
    while True:
        year = input("What election year would you like to evaluate? ")
        if year not in election_results:
            print("Sorry, valid election years are even years from 1976-2020.")
            continue
        state = input("What state would you like to evaluate? ").upper()
        if state not in election_results[year]:
            print(f"{state} is not a valid state")
            continue

        districts = election_results[year][state]
        if len(districts) == 1:
            print("Efficiency gap cannot be computed for states with only one district.")
        else:
            dem_wasted, rep_wasted = calculate_wasted_votes(districts)
            gap, favor = calculate_efficiency_gap(dem_wasted, rep_wasted)
            print(f"Wasted Democratic votes: {dem_wasted}")
            print(f"Wasted Republican votes: {rep_wasted}")
            print(f"Efficiency gap: {gap:.1f}%, in favor of {favor}.")

        cont = input("Would you like to continue? (yes/no) ").lower()
        if cont != "yes":
            break


if __name__ == "__main__":
    main()
