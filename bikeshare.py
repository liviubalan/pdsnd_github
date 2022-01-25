import os
import pandas as pd
import sys
import time

ALL = 'all'


def get_filters():
    """
    Asks user to specify a city, month, and day to analyze.

    Returns:
        (str) city - name of the city to analyze
        (str) month - name of the month to filter by, or "all" to apply no month filter
        (str) day - name of the day of week to filter by, or "all" to apply no day filter
    """
    print('Hello! Let\'s explore some US bikeshare data!')

    # TODO: get user input for city (chicago, new york city, washington). HINT: Use a while loop to handle invalid inputs
    cities = ['chicago', 'new york city', 'washington']
    message = 'City name: (Allowed {}): '.format(', '.join(cities))
    city = liviu_read(message, cities)

    # TODO: get user input for month (all, january, february, ... , june)
    months = [ALL, 'january', 'february', 'march', 'april', 'may', 'june']
    message = 'Month (Allowed {}): '.format(', '.join(months))
    month = liviu_read(message, months)
    # use the index of the months list to get the corresponding int
    if month != ALL:
        month = months.index(month)

    # TODO: get user input for day of week (all, monday, tuesday, ... sunday)
    days = [ALL, 'monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday']
    message = 'Day of week (Allowed {}): '.format(', '.join(days))
    day = liviu_read(message, days)

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
    # check CSV file based on city name
    file = './' + city + '.csv'
    if not os.path.exists(file):
        liviu_halt('File "{}" not found. Enter another city name.'.format(file))

    # read CSV into DataFrame
    df = pd.read_csv(file)

    # convert the Start Time column to datetime
    df['Start Time'] = pd.to_datetime(df['Start Time'])

    # extract month and day of week from Start Time to create new columns
    df['month'] = df['Start Time'].dt.month
    # in order for this to work on Udacity environment use this line
    # df['day_of_week'] = df['Start Time'].dt.weekday_name
    df['day_of_week'] = df['Start Time'].dt.day_name()

    # extract hour
    df['hour'] = df['Start Time'].dt.hour

    # filter by month if applicable
    if month != ALL:
        # filter by month to create the new dataframe
        df = df[df['month'] == month]

    # filter by day of week if applicable
    if day != ALL:
        # filter by day of week to create the new dataframe
        df = df[df['day_of_week'] == day.title()]

    return df


def time_stats(df):
    """Displays statistics on the most frequent times of travel."""
    print('\nCalculating The Most Frequent Times of Travel...\n')
    start_time = time.time()

    # TODO: display the most common month
    value = df['month'].mode()[0]
    print('Most common month: {}'.format(value))

    # TODO: display the most common day of week
    value = df['day_of_week'].mode()[0]
    print('Most common day of week: {}'.format(value))

    # TODO: display the most common start hour
    value = df['hour'].mode()[0]
    print('Most common hour: {}'.format(value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def station_stats(df):
    """Displays statistics on the most popular stations and trip."""
    print('\nCalculating The Most Popular Stations and Trip...\n')
    start_time = time.time()

    # TODO: display most commonly used start station
    value = df['Start Station'].mode()[0]
    print('Most commonly used start station: {}'.format(value))

    # TODO: display most commonly used end station
    value = df['End Station'].mode()[0]
    print('Most commonly used end station: {}'.format(value))

    # TODO: display most frequent combination of start station and end station trip
    value = (df['Start Station'] + ' to ' + df['End Station']).mode()[0]
    print('Most frequent combination of start station and end station trip: {}'.format(value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def trip_duration_stats(df):
    """Displays statistics on the total and average trip duration."""
    print('\nCalculating Trip Duration...\n')
    start_time = time.time()

    # TODO: display total travel time
    value = df['Trip Duration'].sum()
    print('Total travel time: {}'.format(value))

    # TODO: display mean travel time
    value = df['Trip Duration'].mean()
    print('Mean travel time: {}'.format(value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def user_stats(df):
    """Displays statistics on bikeshare users."""
    print('\nCalculating User Stats...\n')
    start_time = time.time()

    # TODO: Display counts of user types
    value = df['User Type'].value_counts()
    print('Counts of user types:\n{}'.format(value))

    if 'Gender' in df.columns:
        # TODO: Display counts of gender
        value = df['Gender'].value_counts()
        print('Counts of gender:\n{}'.format(value))

    if 'Birth Year' in df.columns:
        # TODO: Display earliest, most recent, and most common year of birth
        value = df['Birth Year'].min()
        print('Earliest year of birth: {}'.format(value))
        value = df['Birth Year'].max()
        print('Most recent year of birth: {}'.format(value))
        value = df['Birth Year'].mode()[0]
        print('Most common year of birth: {}'.format(value))

    print("\nThis took %s seconds." % (time.time() - start_time))
    print('-'*40)


def liviu_read(message, white_list):
    """Read a value until is one in the white list."""
    while True:
        value = input(message).lower()
        if value in white_list:
            break
        else:
            print('Invalid value. Please enter one of the following: {}.'.format(', '.join(white_list)))

    return value


def liviu_halt(message, exit_status=os.EX_DATAERR):
    """Display the error and exit with a status code."""
    print(message)
    sys.exit(exit_status)


def liviu_display_dataframe(df):
    """Display DataFrame raw data."""
    i = 0
    n = df.shape[0]
    step = 5
    while True:
        view_data = input('\nWould you like to see the raw data? Type "yes" or "no": ').lower()
        if view_data == 'yes' and i <= n:
            print(df.iloc[i:i+step])
            i += step
        else:
            break


def main():
    while True:
        city, month, day = get_filters()
        df = load_data(city, month, day)

        time_stats(df)
        station_stats(df)
        trip_duration_stats(df)
        user_stats(df)
        liviu_display_dataframe(df)

        restart = input('\nWould you like to restart? Enter "yes" or "no": ')
        if restart.lower() != 'yes':
            break


if __name__ == "__main__":
    main()
