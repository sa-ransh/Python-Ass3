from card import Card
from deck import Deck
import os


def fairness(count = 1000, attempts = 20):
    '''proves the fairness(equal chance of drawing each card_value) of the deck if mean value is between 6.5 and 7.5'''
    no_of_attempts = attempts
    list_mean_values = []
    while no_of_attempts > 0:
        test_deck = Deck(1,13,4)
        face_value_sum = 0
        count_attempts = count
#for each card, its face value is obtained and added to sum variable which is later divided by the count to obtain the mean value.
        while count_attempts > 0:
            test_card = test_deck.drawCard()
            test_face = test_card.getFace()
            face_value_sum += test_face
            test_deck.placeCardTop(test_card)
            test_deck.shuffle()
            count_attempts = count_attempts-1
        mean_value = face_value_sum/count
        list_mean_values.append(mean_value)
        no_of_attempts = no_of_attempts - 1
    return list_mean_values


def chance_of_hand(deck=Deck(1,13,4), trials=20):
    '''chance of obtaining royal flush for a standard 52-card deck'''
    test_deck = deck
    nbr_of_trials=trials
    list_count_attempts=[]
    count_attempts = 0
    condition = 0
    while nbr_of_trials > 0:
        while condition == 0:
            test_deck.shuffle()
            cards = []
            test_success = 0
            for i in range(0,5):
                cards.append(test_deck.drawCard())

            for i in range(0,5):
                if cards[i].getSuit() == 0:
                    if cards[i].getFace() in (1, 10, 11, 12, 13):
                        test_success = test_success + 1
                test_deck.placeCardTop(cards[i])
            if test_success == 5:
                condition = 1
            count_attempts = count_attempts + 1
        list_count_attempts.append(count_attempts)
        nbr_of_trials=nbr_of_trials-1
    return list_count_attempts


def change_in_chance(size=10, trials=5):
    '''Chance of obtaining a Royal Flush for increasing number of suits'''
    counters = []
    suit_size = size
    for suit in range(1, suit_size+1):
        counter_suit = chance_of_hand(Deck(1,13,suit),trials)
        counters.append(counter_suit)
    return counters



def main():
    i=0
    while i < 1:
        os.system('cls' if os.name == 'nt' else 'clear')
        print("1. Proving fairness of a deck\n2. Calculating Probability of obtaining Royal Flush\n3. Calculating change in chance for Royal Flush")

        user_input = input("Enter 1 or 2 or 3 to continue, Press Q to quit")
        if(isinstance(user_input, str)):
            if(user_input.upper()=='Q'):
                input("Thank you for using the service. Press enter to exit")
                i=1

            elif(user_input == '1'):
                print("Proving fairness of a 52-card deck")
                j=0
                while j<1:
                    try:
                        count_input = int(input("Enter the desired count size or press 0 to use default settings:"))

                    except(ValueError):
                        print('Oops, please enter an integer')
                        j=1
                    try:
                        attempt_input = int(input("Enter the desired number of attempts or press 0 to use default settings:"))
                    except(ValueError):
                        print('Oops, please enter an integer')
                        j=1

                    if count_input == 0 and attempt_input == 0:
                        f = fairness()
                        print('List of calculated mean face values are : ',f)
                        input('Press Enter to continue')
                        j=1
                    elif count_input == 0 and attempt_input != 0:
                        f = fairness(attempts=attempt_input)
                        print('List of calculated mean face values are : ', f)
                        input('Press Enter to continue')
                        j=1
                    elif count_input >= 1000 and attempt_input == 0:
                        f = fairness(count=count_input)
                        print('List of calculated mean face values are : ',f)
                        input('Press enter to continue')
                        j=1
                    elif count_input >= 1000 and attempt_input != 0:
                        f = fairness(count=count_input, attempts=attempt_input)
                        print('List of calculated mean face values are : ',f)
                        input('Press Enter to continue')
                        j=1
                    else:
                        input('Count size is insufficient. Press enter to continue')
                        j=1

            elif(user_input == '2'):
                print('Calculating probability of drawing Royal Flush for standard 52-card deck')
                k=0
                while k<1:
                    try:
                        trial_input = int(input('Enter the number of trials or press 0 to use default settings: '))
                    except(ValueError):
                        input("Oops please enter an integer! Press enter to continue")
                        k=1
                    if trial_input == 0:
                        c = chance_of_hand()
                        print('List of calculated attempts to achieve a Royal Flush hand for standard 52-card deck are:',c)
                        input('Press Enter to continue')
                        k=1
                    else:
                        c = chance_of_hand(trials=trial_input)
                        print('List of calculated attempts to achieve a Royal Flush hand for standard 52-card deck are:', c)
                        input('Press Enter to continue')
                        k = 1

            elif(user_input == '3'):
                print('Calculating probability of drawing Royal Flush for suit sizes 1 to 10')
                l=0
                while l<1:
                    try:
                        trial_input = int(input('Enter the number of trials or press 0 to use default settings: '))
                    except(ValueError):
                        input("Oops please enter an integer! Press enter to continue")
                        l = 1
                    if(trial_input==0):
                        ch=change_in_chance()
                        print('List of calculated attempts to achieve a Royal Flush hand for decks of increasing number of suit size are: ', ch)
                        input('Press Enter to continue')
                        l=1
                    elif(trial_input!=0):
                        ch = change_in_chance(trials=trial_input)
                        print('List of calculated attempts to achieve a Royal Flush hand for decks of increasing number of suit size are: ',ch)
                        input('Press Enter to continue')
                        l = 1

            elif user_input != '1' or user_input != '2' or user_input != '3':
                input('Incorrect Choice! Press enter to return to Main menu')




if __name__ == '__main__':
    main()





    # f = fairness()
    # print(f)
    # c = chance_of_hand()
    # print(c)
    # ch=change_in_chance()
    # print(ch)





# [4215, 31534, 409330, 2339281, 6200134, 21030828, 54005407, 20831460, 128559242, 240740080]
# [382, 29719, 254441, 1205690, 6648147, 112644556, 31262111, 29816890, 119734850, 341734741]

# 786741,     1043792,     6292352,       4111301,      4151753,      4793342,      1286568,     3228082,     7771889,    1026063