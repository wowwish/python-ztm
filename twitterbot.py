
import tweepy # module to access twitter API functionalities
import time # Wait for a time duration before sending next API request - Pause the script

# Initialize the Twitter API authentication object (OAuth1 connects to the older version of the API)
# The latest version is Oauth 2.0 which uses OAuth2BearerHandler() and OAuth2AppHandler()
auth = tweepy.OAuth1UserHandler(
   'consumer_key', 'consumer_secret', 'access_token', 'access_token_secret'
)


# Authenticate API using credentials
api = tweepy.API(auth)

# Get tweets from Timeline and print their text to console
print('Tweets from the Timelime : ')
public_tweets = api.home_timeline()
for tweet in public_tweets:
    print(tweet.text)

print()
print()

user = api.verify_credentials() # Get the user object of the current user to whom the credentials belong
# user = api.get_user(screen_name='@<...>') # Get a tweepy object wth info of a Twitter user using their screen name
# example: @twitter
# print("User : ", user)
# print(dir(user))
print("Username : ", user.screen_name)
print("Followers : ", user.followers_count) # Get the follower count of the user

# helper function to limit the API response results (paginate the response)
# This function will extract the data in the API response batch-by-batch according to the ratelimit set in the
# tweepy Cursor (generator)
def limit_handler(cursor):
        while True:
            try:
                yield cursor.next()
            except tweepy.TooManyRequests: # If too many requests sent to the API, beyond its limit
                time.sleep(60) # pause the script for 60 seconds. Ideally should be 15 mins for next set of API requests to open up
            except StopIteration: # When the generator ends (no data left to yield), break out of the while loop
                break

# Tweepy provides a Cursor (generator) to paginate the response from the API to prevent bombardment with Data
# from continuous API calls / spams
# Loop through the followers of the authenticated user and print their screen name
for follower in limit_handler(tweepy.Cursor(api.get_followers).items()):
    # print(dir(follower))
    print(follower.name)
    # Follow every follower of the authenticated user
    follower.follow()
    
# user.follow_user(target_user_id='') # Make the owner of the API credentials follow a patricular follower who follows them


# Code template to favourite tweets from past 30 days containing a specific query string
# Here, we limit the number of tweets favourited to 2.
search_string = 'python'
numberOfTweets = 2

for tweet in tweepy.Cursor(api.search_30_day, query=search_string).items(numberOfTweets):
    try:
        tweet.favourite() # Like a Tweet
        # tweet.retweet() # Retweet the tweet
        print('I liked that Tweet!')
    except tweepy.HTTPException as e:
        print(e.api_errors)
    except StopIteration:
        break 