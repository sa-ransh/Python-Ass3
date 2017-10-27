import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import Tasks
import os


def fairness_df(list_mean_values):
    '''data frame for list of mean face values to prove fairness'''
    df = pd.DataFrame(list_mean_values, index=[x+1 for x in range(len(list_mean_values))], columns=['Probability of drawing a card'])
    return df


def fairness_plot_bar(list_mean_values):
    '''bar chart of mean face values'''
    y=list_mean_values
    x=[x+1 for x in range(len(list_mean_values))]
    plt.bar(x,y, color='b')
    plt.xlabel('Attempt number')
    plt.ylabel('Probability of card drawn')
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))
    plt.yticks(np.arange(1, max(y)+2, 1.0))
    plt.title('Mean value of cards drawn\n')
    plt.show()


def fairness_plot_hist(list_mean_values):
    '''histogram chart of mean face values'''
    y=list_mean_values
    face_nos = [x+1 for x in range (13)]
    plt.hist(y, face_nos, histtype='bar', rwidth=0.8)
    plt.xlabel('Mean value of drawn card')
    plt.ylabel('Number of occurences')
    plt.xticks(np.arange(min(face_nos)+0.5, max(face_nos), 1))
    plt.yticks(np.arange(1, max(y)+5, 1.0))
    plt.title('Histogram of drawn card mean values collected\n')
    plt.show()


def chance_royal_flush_df(list_attempts):
    '''data frame for attempts required to obtain a Royal Flush hand'''
    df = pd.DataFrame(list_attempts,index=[x+1 for x in range(len(list_attempts))], columns=['Attempts to achieve a Royal Flush'])
    return df


def royal_flush_plot_bar(list_attempts):
    '''Bar chart of attempts required to land a Royal Flush hand'''
    y=list_attempts
    x=[x+1 for x in range(len(list_attempts))]
    plt.bar(x,y, color='b')
    plt.xlabel('Attempt number')
    plt.ylabel('Number of chances')
    plt.xticks(np.arange(min(x), max(x)+1, 1.0))
    plt.yticks(np.arange(0, max(y), 500000))
    plt.title('Chances to land 1 Royal Flush hand\n')
    plt.show()


def royal_flush_plot_hist(list_attempts):
    '''Histogram chart of attempts required to land a Royal Flush hand'''
    y=list_attempts
    bins=[x*500000 for x in range(15)]
    plt.hist(y, bins, histtype='bar', rwidth=0.8)
    plt.xlabel('Number of Chances')
    plt.ylabel('Number of Occurrences')
    plt.xticks(np.arange(min(bins),max(bins), 500000), rotation=90)
    plt.title('Histogram of chances to land Royal Flush\n')
    plt.show()


def change_in_chance_df(counters):
    '''Data frame for lists of attempts for landing a Royal flush hand in decks with an increasing suit size'''
    df=pd.DataFrame(counters,index=[x+1 for x in range(10)], columns=[y+1 for y in range(5)])
    return df


def change_plot_scatter(counters):
    '''Scatter plot for attempts of landing Royal Flush hand in decks with an increasing suit size'''
    x=[x+1 for x in range(10)]
    y=mean(counters)

    plt.scatter(x,y,color='k',marker='.')
    plt.plot(x,y,color='k')
    plt.grid(True)
    plt.xlabel('Number of Suits')
    plt.ylabel('Number of Chances')
    plt.title('Chances required to land a royal flush\n')
    plt.show()


def mean(counters):
    '''To calculate mean value from the trial attempts collected'''
    sum = 0
    mean_list=[]
    for suit in range(10):
        for attempt in range(5):
            sum = sum + counters[suit][attempt]
        mean_calc = sum/5
        mean_list.append(mean_calc)
    return mean_list


def main():
    i=0
    while i < 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print('1. Fairness\n2.Chance of Royal Flush\n3.Change in chance for Royal Flush')
        user_input=input('Enter 1 or 2 or 3 to continue, Press Q to quit')
        if user_input.upper() == 'Q':
            input("Thank you for using the service. Press enter to exit")
            i = 1
        if user_input == '1':
            j=0
            f = Tasks.fairness()
            while j < 1:
                os.system('cls' if os.name == 'nt' else 'clear')

                print('1. Data Frame of mean face values\n2. Bar Chart of mean face values\n3. Histogram Chart of mean face values')
                user_input1=input('Enter 1 or 2 or 3 to continue')
                if user_input1 == '1':
                    data_frame = fairness_df(f)
                    print('The data frame is :\n',data_frame)
                    input('Press Enter to continue')
                    j=1
                elif user_input1 == '2':
                    print('Bar chart can be depicted as follows: \n')
                    fairness_plot_bar(f)
                    input('Press Enter to continue')
                    j=1
                elif user_input1 == '3':
                    print('Histogram chart can be depicted as follows: \n')
                    fairness_plot_hist(f)
                    input('Press Enter to continue')
                    j=1
                else:
                    input('Incorrect Choice! Press Enter to continue')
                    j=1
        if user_input == '2':
            k=0
            ch = Tasks.chance_of_hand()
            while k < 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('1. Data Frame of obtaining a Royal Flush\n2. Bar Chart of obtaining a Royal Flush\n3. Histogram Chart of obtaining a Royal Flush')
                user_input2 = input('Enter 1 or 2 or 3 to continue')

                if(user_input2 == '1'):
                    data_frame=chance_royal_flush_df(ch)
                    print('The data frame is :\n',data_frame)
                    input('Press Enter to continue')
                    k=1
                elif(user_input2 == '2'):
                    print('Bar chart can be depicted as follows: \n')
                    royal_flush_plot_bar(ch)
                    input('Press Enter to continue')
                    k=1
                elif(user_input2 == '3'):
                    print('Histogram chart can be depicted as follows: \n')
                    royal_flush_plot_hist(ch)
                    input('Press Enter to continue')
                    k=1
                else:
                    print('Incorrect input! Press Enter to continue')
                    k=1
        if user_input == '3':
            l=0
            cc = Tasks.change_of_chance()
            while l < 1:
                os.system('cls' if os.name == 'nt' else 'clear')
                print('1. Data Frame of obtaining a Royal Flush\n2. Bar Chart of obtaining a Royal Flush\n3. Histogram Chart of obtaining a Royal Flush')
                user_input3 = input('Enter 1 or 2 or 3 to continue')

                if (user_input3 == '1'):
                    data_frame = change_in_chance_df(cc)
                    print('The data frame is :\n', data_frame)
                    input('Press Enter to continue')
                    l = 1
                elif (user_input3 == '2'):
                    print('Bar chart can be depicted as follows: \n')
                    royal_flush_plot_bar(cc)
                    input('Press Enter to continue')
                    l = 1
                elif (user_input2 == '3'):
                    print('Histogram chart can be depicted as follows: \n')
                    royal_flush_plot_hist(cc)
                    input('Press Enter to continue')
                    l = 1
                else:
                    print('Incorrect input! Press Enter to continue')
                    l = 1


if __name__ == '__main__':
    main()