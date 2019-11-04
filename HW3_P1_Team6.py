"""
@author: Johnny and Thanh
"""
import time
start = time.time()

# Main Program asks user for input and prints all the data for the tweet.
def main():
    example_input='Tesla software V10 is lookin real good! \
Releasing to early access list soon …'
    text=example_input
#text = input('Please enter your tweet: ')
    word_counter(text)
    print(average_number_of_letters(text))
    print(upper_case_letters(text))
    print(lower_case_letters(text))
    print(reverse(text))
    string_stats(text)
    
# Function counts number of words in tweet.
def word_counter(tweet):
    word_count = tweet.split()
    print(str(len(word_count)) + ' words.')

# Functions counts the number of letters in tweet and divides by number of
# words.
def average_number_of_letters(tweet):
    num_of_words = len(tweet.split())
    letter_count = len(tweet.replace(' ' , ''))
    return letter_count / num_of_words
# Function counts the number of uppercase letters in tweet.
def upper_case_letters(tweet):
    upper_count = 0
    for letter in tweet:
        if letter.isupper():
            upper_count += 1
    return upper_count
# Function counts the number of lowercase letters in tweet
def lower_case_letters(tweet):
    lower_count = 0
    for letter in tweet:
        if letter.islower():
            lower_count += 1
    return lower_count
# Function makes a copy of tweet, reverses, and returns it
def reverse(tweet):
    tweet_reversed = tweet[::-1]
    return tweet_reversed
# Function shows tweets components(letters, numbers, and special characters)
def string_stats(tweet):
    alphabet_count = 0
    digit_count = 0
    special_count = 0
    x = tweet.replace(' ', '')
    for letter in x:
        if letter.isalpha():
            alphabet_count += 1
        elif letter.isdigit():
            digit_count += 1
        else:
            special_count += 1
    print('Alphabet count: ' + str(alphabet_count))
    print('Digit count: ' + str(digit_count))
    print('Special Character count: ' + str(special_count))

# Main Program
main()

end = time.time()

print(end - start)