"""Restaurant rating lister."""


# put your code here

import sys

def make_restaurant_ratings_dict(input_file):
    ratings_dict = {}

    file = open(input_file)
    for line in file:
        restaurant_name, rating = line.rstrip().split(":")
        ratings_dict[restaurant_name]= rating
    
    return ratings_dict

    # new_restaurant = input("What is your restaurant name?: ").title()
    # new_rating = input("What do you rate your restaurant on a scale of 1 to 5?: ")

    # ratings_dict[new_restaurant] = new_rating

    # sorted_restaurants_list = sorted(ratings_dict)

    # for restaurant in sorted_restaurants_list:
    #     rating = ratings_dict[restaurant]
    #     print("{} is rated at {}.".format(restaurant, rating))


def add_new_restaurant(ratings_dict):
    new_restaurant = input("What is your restaurant name?: ").title()

    # Throw away value to enter loop - immediately overwritten
    new_rating = 100

    while new_rating < 0 or new_rating > 5:
        try:
            new_rating = int(input("What do you rate your restaurant on a scale of 1 to 5?: "))
        except ValueError:
            print("Try again, this time with an integer.")
            new_rating = int(input("What do you rate your restaurant on a scale of 1 to 5?: "))

    ratings_dict[new_restaurant] = new_rating
    return ratings_dict


def sort_and_print_restaurants(ratings_dict):

    for restaurant in sorted(ratings_dict):
        rating = ratings_dict[restaurant]
        print("{} is rated at {}.".format(restaurant, rating))


def rating_restaurants(input_file):

    ratings_dictionary = make_restaurant_ratings_dict(input_file)
    while True:
        print("\n[S]ee all the ratings")
        print("[A]dd restaurant")
        print("[Q]uit")

        choice= input("\nWhat would you like to do? \n").upper()

        if choice == "A":
            ratings_dictionary = add_new_restaurant(ratings_dictionary)
        elif choice == "S":
            sort_and_print_restaurants(ratings_dictionary)
        elif choice == "Q":
            return False
        else:
            print("Please choose from the available options")

rating_restaurants(sys.argv[1])
