import requests # For using API to check number of password hacks for a given password
import hashlib # built-in python module with hash functions
import sys # for command-line arguments

# We should send a hashed password to the API endpoint in the query of the GET request for a successful response
# Furthermore, to maintain K-anonymity (K-anonymity is a property of a dataset that indicates the 
# re-identifiability of its records. A dataset is k-anonymous if quasi-identifiers for each person in the dataset 
# are identical to at least k – 1 other people also in the dataset), only the first 5 characters of the hashed 
# password string is sent with the API. The API then matches all password strings in its database that have the 
# same first 5 hash characters and returns results for all these password strings. 
# This way, our exact password hash (and thereby, the password string itself) is not exposed to the API and 
# someone cannot decrypt password by guessing its hash using a hash-function generator for password-strings.


# HASH FUNCTIONS are functions that generate a fixed length value for an input. This fixed length value is very
# specific to the input ... even a single character change in the input will completely change the HASH FUNCTION
# output, however, the same input will generate the same hash value out of the hash function (This property is
# called Indempotency). In most cases, there is no way to get the original input from the hash value recieved 
# from the hash function. Hash Functions are used widely in data integrity and data security.
# Memory Addresses for data structures like Hash Tables (Dictionaries) are also based on hash functions. The data
# in a hash table is stored in a memory address that is mapped to the output of the hash function 
# applied to the data. This allows quick data access typical of Hash Tables (Dictionaries). Hash Functions slow 
# down the process of storing data in memory for Hash Tables and hence, an optimal hash function for quickly 
# developing an address to the data are neccessary.
# url = 'https://api.pwnedpasswords.com/range/' + 'cbfda' # API endpoint + the first 5 characters of our
# password's hash (SHA1 of 'password123' = 'cbfdac6008f9cab4083784cbd1874f76618d2a97')
# res = requests.get(url) # Get the number of times this password was hacked using a GET request
# We want a response of 200 for successfull API request-response call
# This API uses hashing to encrypt the password sent in the API call. The call will return a success HTTPS 
# reponse (status: 200) only when a hashed password string is given as the query in the GET request
# print("API response : ", res) # response 400 means unauthorized access / API hosting server errors


# Function to retrieve the number of times the related passwords have been hacked given the first five 
# characters of the hash of our password of interest, from the API
def request_api_data(query_char):
    url = 'https://api.pwnedpasswords.com/range/' + query_char
    res = requests.get(url)
    if res.status_code != 200:
        raise RuntimeError(f'Error fetching: {res.status_code}, check the API call and try again!')
    else:
        return res

# check if our password of interest exists in the API response
def pwned_api_check(password):
    # use .encode() on the unicode string to convert it into a byte string like b'cdfa'. Use .hexdigest() on the object
    # returned by haslib.sha1() to get a string object of double length containing only hexadecimal digits that 
    # can be use safely. Use .upper() to convert string to upper-case.
    sha1password = hashlib.sha1(password.encode('utf-8')).hexdigest().upper()
    first5_char, tail = sha1password[:5], sha1password[5:] # first 5 characters in the hash and the remaining characters
    # print("First 5 characters of password hash : ", first5_char)
    # print("Remaining characters of password hash : ", tail)
    response = request_api_data(first5_char)
    # print("Response : ", response)
    return get_password_leaks_count(response, tail)

# Function to read through the response from the API and print the response object in text format
# The API gives the REMAINING CHARACTERS of hashes that match the first 5 characters that we gave in the 
# API request and the number of hacks for their corresponding passwords
def read_res(response):
    print(response.text) # print the text data from the response

# Function that takes the response object and the TAIL HASH of our password and matches them, to get the count of
# the hacks for our password. The TAIL HASH is the remaining characters of our password's hash apart from the first
# 5 characters that were given in the API request.
def get_password_leaks_count(hashes, hash_to_check):
    # generator object of (hash, count) tuple created for each line in the response text
    hashes = (line.split(':') for line in hashes.text.splitlines())
    for h, count in hashes:
        if h == hash_to_check: # If the hash from a particular line in the response text matches the tail hash of our password
            return count # return each hash in the response text and its corresponding count
        return 0


# API Error Status Check
# pwned_api_check('123') 


def main(args):
    for password in args:
        count = pwned_api_check(password)
        if count: # If a count exists, ie, count is not None
            print(f"'{password}' was found {count} times... you should probably change your password!")
        else:
            print(f"'{password}' was NOT found. Carry on!")
    return 'done'

if __name__ == '__main__': # only run the code if this file is run directly and not imported anywhere.
    sys.exit(main(sys.argv[1:])) # sys.exit() to make sure the script exists after running the main() call
    # the main() call returns 'done' which is returned by sys.exit() as it exits the script


