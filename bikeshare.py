### Python Udacity Eirik Stoe.le Hanssen

import time
import pandas as pd
import numpy as np

# See what pd version is running.
# print(pd.__version__)

# If not version 2.0.3, run the following and restart the query.
# !pip install pandas==2.0.3

# See pwd and what is in it
# pwd
# ls

# Change wd if necessary
# cd

CITY_DATA = { 'chicago': 'chicago.csv',
              'new york city': 'new_york_city.csv',
              'washington': 'washington.csv' }

def user_input (start_message, question_message, correct_input, wrong_message):
    '''
    Ask user to specify a value from a defined list and output this value.

    Args:
        (str) start_message - what user should be told first
        (str) question_message - what is the question being asked
        (list) correct_input - correct input that the user can input
        (str) wrong_message - what message should be if user inputs wrong
    Returns:
        variable - one of outputs defined in correct_input
    '''

    print(start_message)
    while True:
        variable = (input(question_message)).lower()
        try:
            if variable in correct_input:
                print('You entered {}, a valid input.'.format(variable.title()))
                break
            else:
                print(wrong_message)
        except ValueError:
            print('Wrong input')
    return variable



def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')
    # TO DO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    city = user_input(
        'You can choose between 3 cities: Chicago, New York City and Washington',
        'Please enter the city you want to take a look at: ',
        ['chicago', 'new york city', 'washington'],
        'Wrong input. Please enter one of the following city names: Chicago, New York City or Washington'
        )
    # TO DO: get user input for month (all, january, february, ... , june)
    print('You can choose between all months in the sample or a specific month between January and June')
    while True:
        month = str(input('Please enter the month you want to take a look at. For no filtering, please enter: "all".')).lower()
        try:
            if month in ['january','february','march', 'april', 'may', 'june', 'all']:
                print('You entered {}, a valid input.'.format(month.title()))
                break
            else:
                print('Wrong input. Please enter one of the following: January, February, March, April, May, June or all.')
        except ValueError:
            print('Wrong input')    
    # TO DO: get user input for day of week (all, monday, tuesday, ... sunday)
    print('Which day do you want to take a look at?')
    while True:
        day = str(input('Please enter the day you want to look at. For no filtering, please enter: "all".')).lower()
        try:
            if day in ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday', 'all']:
                print('You entered {}, a valid input.'.format(day.title()))
                break
            else:
                print('Wrong input. Please enter one of the following: Monday, Tuesday, Wednesday, Thursday, Friday, Saturday, Sunday or all.')
        except ValueError:
            print('Wrong input')

    print('-'*40)
    return city, month, day


def load_data(city, month, day):
    """
    Loads data for the specified city and filters by month and day if applicable.

    Args:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    Returns:
        df - Pandas DataFrame containing city data filtered by month and day
    """
    # load data file into a dataframe
    df = pd.read_csv(CITY_DATA[city])
    
    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])
    df['End Time'] = pd.to_datetime(df['End Time'])
    
    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    df['day_of_week'] = df['Start Time'].dt.weekday
    df['day_of_week2'] = df['Start Time'].dt.day_name()
    
    # filter by month if applicable
    if month != 'all':
        # use the index of the months list to get the corresponding int
        months = ['january', 'february', 'march', 'april', 'may', 'june']
        month = months.index(month) + 1
    
        # filter by month to create the new dataframe
        df = df[df['month'] == month]
    
    # filter by day of week if applicable
    if day != 'all':
        # use the index of the months list to get the corresponding int
        days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
        day = days.index(day)
        
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day]
        
        #df = df[df['day_of_week2'] == day.title()]
    
    return (df)


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""

    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TO DO: display the most common month
    months = ['january', 'february', 'march', 'april', 'may', 'june']
    popular_month = months[df['month'].mode()[0] - 1].title()
    print('The most popular start month is: {}'.format(popular_month))
    
    # TO DO: display the most common day of week
    days = ['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    popular_day = days[df['day_of_week'].mode()[0] - 1].title()
    print('The most popular start day is: {}'.format(popular_day))

    # TO DO: display the most common start hour
    df['hour'] = df['Start Time'].dt.hour
    popular_hour = df['hour'].mode()[0]
    if popular_hour <= 11:
        print('The most popular start hour is: {} am'.format(popular_hour))
    elif popular_hour <= 23:
        print('The most popular start hour is: {} pm'.format(popular_hour))
    else:
        print('The most popular start hour is: {} am'.format(popular_hour))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    input("Press Enter to continue...")


# In[387]:


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""

    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TO DO: display most commonly used start station
    popular_start_station = df['Start Station'].mode()[0]
    print('The most popular start station is: {}'.format(popular_start_station))
    
    # TO DO: display most commonly used end station
    popular_end_station = df['End Station'].mode()[0]
    print('The most popular end station is: {}'.format(popular_end_station))

    # TO DO: display most frequent combination of start station and end station trip
    df['Trip'] = df['Start Station']+' to '+df['End Station']
    popular_trip = df['Trip'].mode()[0]
    print('The most popular trip is: {}'.format(popular_trip))
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)

    input("Press Enter to continue...")


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""

    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TO DO: display total travel time
    df['Travel Time'] = df['End Time'] - df['Start Time']
    total_travel_time = df['Travel Time'].sum()
    print('Total travel time is {}.'.format(total_travel_time))
    
    # TO DO: display mean travel time
    mean_travel_time = df['Travel Time'].mean()
    print('Average time of travel is {}.'.format(mean_travel_time))
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    input("Press Enter to continue...")


def user_stats(df):
    """Displays statistics on bikeshare users."""

    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TO DO: Display counts of user types
    user_types = df['User Type'].value_counts(dropna = False, ascending = True)
    print('Statistic about user types:')
    for i in range(len(user_types.index)):
        print('There are {} {} in the sample.'.format(user_types[i],user_types.index[i]))
    print('-'*40+'\n')
        
    # TO DO: Display counts of gender
    print('Statistics about gender:')
    if 'Gender' in df.columns:
        gender_types = df['Gender'].value_counts(dropna = False, ascending = True)
        for i in range(len(gender_types.index)):
            print('There are {} {} in the sample.'.format(gender_types[i],gender_types.index[i]))      
    else:
        print('There are no information about gender in Washington')
    print('-'*40+'\n')

    # TO DO: Display earliest, most recent, and most common year of birth
    print('Statistics about birth year:')
    if 'Birth Year' in df.columns:
        age_oldest = df['Birth Year'].min()
        print('The oldest person in the sample was born in {}.'.format(int(age_oldest)))
        age_youngest = df['Birth Year'].max()
        print('The youngest person in the sample was born in {}.'.format(int(age_youngest)))
        age_mode = df['Birth Year'].mode()[0]
        print('The most people were born in {}.'.format(int(age_mode)))
    else:
        print('There are no information about birth year in Washington')
    
    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)
    
    input("Press Enter to continue...")


def display_raw_data(df):
    """Displays raw data output."""

    counter = 0
    
    input_value = input('Please enter "yes" if you want to see the raw data: ').lower()
    if input_value == 'yes':
        print('You entered {}, here are the first {} rows of the raw data.'.format(input_value,len(df) - counter))
        print(df[counter:counter+5])
        counter += 5
    
    while True:
        try:
            input_value = (input('Do you want to see the next five rows of raw data? If so, enter "yes" ')).lower()
            if input_value == 'yes':
                if len(df) - counter <= 0:
                    print('You\'ve got no more rows to display.')
                    break
                elif len(df) - counter <= 5:
                    print('Here are the last {} rows of data.'.format(len(df) - counter))
                    print(df[counter:len(df)])
                    break
                else:
                    print('You entered {}, here is the next five rows of raw data.'.format(input_value))
                    print(df[counter:counter+5])
                    counter += 5
            else:
                break
        except ValueError:
            print('Wrong input')


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        display_raw_data(df)

        restart = input('\nWould you like to restart? Enter yes or no.\n')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
	main()

