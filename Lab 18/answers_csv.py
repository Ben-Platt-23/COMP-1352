"""
    Description of program
    Filename: answers_csv.py
    Author: Ben Platt
    Date: 3/18/24
    Course: COMP-1352
    Assignment: Lab 18
    Collaborators: N/A
    Internet Source: W3Schools
"""

import csv

def read_csv(filename):
    """
    Function to read the CSV file and return a list of dictionaries where each dictionary represents a row.
    
    Parameters:
    filename (str): The name of the CSV file to read.
    
    Returns:
    list of dict: A list where each element is a dictionary representing a row of the CSV file.
    """
    data = []
    with open(filename, 'r', newline='') as file:
        reader = csv.DictReader(file)
        for row in reader:
            data.append(row)
    return data

def total_deaths_positive_for_both_fentanyl_and_cocaine(data):
    """
    Function to calculate the total number of deaths positive for both Fentanyl and Cocaine.
    
    Parameters:
    data (list of dict): A list where each element is a dictionary representing a row of the CSV file.
    
    Returns:
    int: The total number of deaths positive for both Fentanyl and Cocaine.
    """
    count = 0
    for row in data:
        if row['Fentanyl'] == 'Positive' and row['Cocaine'] == 'Positive':
            count += 1
    return count

def cities_with_male_deaths_positive_for_specific_drugs(data, drugs):
    """
    Function to find the city names for all cities that had Male deaths listed positive for specified drugs.
    
    Parameters:
    data (list of dict): A list where each element is a dictionary representing a row of the CSV file.
    drugs (list of str): A list of drug names to check for positivity.
    
    Returns:
    set of str: A set containing the names of cities where Male deaths were positive for specified drugs.
    """
    cities = set()
    for row in data:
        if row['Sex'] == 'Male' and all(row[drug] == 'Positive' for drug in drugs):
            cities.add(row['DeathCity'])
    return cities

def person_id_for_specific_death(data, criteria):
    """
    Function to find the PersonID for a specific death based on given criteria.
    
    Parameters:
    data (list of dict): A list where each element is a dictionary representing a row of the CSV file.
    criteria (dict): A dictionary containing criteria to match against for finding the specific death.
    
    Returns:
    str or None: The PersonID for the specific death if found, otherwise None.
    """
    for row in data:
        if all(row[key] == value for key, value in criteria.items()):
            return row['PersonID']
    return None

def main():
    filename = 'accidental_drug_deaths.csv'
    data = read_csv("Accidental_Drug_Related_Deaths_2012-2018.csv")

    # Question 1
    total_deaths = total_deaths_positive_for_both_fentanyl_and_cocaine(data)
    print("Total number of deaths positive for both Fentanyl and Cocaine:", total_deaths)

    # Question 2
    drugs = ['Fentanyl', 'Oxycodone', 'Amphet']
    cities = cities_with_male_deaths_positive_for_specific_drugs(data, drugs)
    print("City names for Male deaths positive for Fentanyl, Oxycodone, and Amphetamines:", cities)

    # Question 3
    criteria = {'Sex': 'Male', 'Age': '34', 'Fentanyl': 'Positive', 'Cocaine': 'Positive',
                'Methadone': 'Positive', 'Heroin': 'Positive', 'Benzodiazepine': 'Positive'}
    person_id = person_id_for_specific_death(data, criteria)
    print("PersonID for the specific death:", person_id)

if __name__ == "__main__":
    main()
