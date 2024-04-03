"""
    CS110 Lab
    Dictionary Lab

    Updated By: Carson White

    CSCI 110
    Date: 4/1/24

    Working with Python dictionary (dict) data structure.
"""
import os

# create a mapping of state names to their codes using a dictionary
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI',
    'Colorado': 'CO',
    'Massachusetts': 'MA' ,
    'Nevada': 'NV' ,
    'Illinois': 'IL',
    'Ohio' : 'OH'
    # FIXME- Fixed – add codes for the rest of the states
}

# create a mapping of states to their capital state using a dictionary
capitalCity = {
    'CA': 'Sacramento',
    'MI': 'Lansing',
    'FL': 'Tallahassee'
    
}

# add some more entires to capitalCity dictionary
capitalCity['NY'] = 'Albany'
capitalCity['OR'] = 'Salem'
capitalCity['CO'] = 'Denver'
capitalCity['MA'] = 'Boston'
capitalCity['NV'] = 'Carson City'
capitalCity['IL'] = 'Springfield'
capitalCity['OH'] = 'Columbus'
# FIXME4-Fixed: Add rest of the states’ capital cities to capitalCity dictionary


def menu():
    print("""
            Enter one of the menu options:
            [1] Find US state's code given its name
            [2] Find US state's capital given its code
            [3] Find US state's capital given its name
            [4] Exit the program
        """)


def main():
    while True:
        # clear screen
        ##os.system('clear')
        # print menu
        menu()
        # get menu option
        option = input()
        if option == '4':
            print('SEE YOU AGAIN... GOOD BYE!')
            break

        if option == '1':
            state = input('Enter a US state name: ')
            if state in states:  # check if state is in states dict
                print('Code for {} is {}.'.format(state, states[state]))
            else:
                print("Sorry! The US state name '{}' NOT found!".format(state))
        elif option == '2':
            # FIXME5-Fixed - complete menu option 2
            state_code = input('Enter a U.S. states code: ')
            if state_code in capitalCity:
                print('The capital city for {} is {}.'.format(state_code, capitalCity[state_code]))
            else:
                print("Sorry! The US state code '{} NOT found!".format(state_code))
        elif option == '3':
            state = input('Enter a US state name: ')
            state_code = states[state]
            if state in states:
                print('The capital city for {} is {}.'.format(state, capitalCity[state_code]))
            else:
                print("Sorry! The US state is '{} NOT found!".format(state))
        else:
            print(" Invalid input please try again ")
        # FIXME6-Fixed - complete menu option 3

        # FIXME7-Fixed - handle the case where user enters invalid menu option
        


if __name__ == "__main__":
    main()