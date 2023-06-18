# import tweepy


# api_k = 'SXgBQ9FQ2QuBlSyyfb3nsI6Kf'
# api_ks = 'IeCy1wt3qjG4HMXMgA82wobVCHqqkUdkzk4sNa2zQkHuUGSXr7'

# at = '1668830207552409603-FsLghuyntFwvE3Btte7EiiMKVj8aWt'
# ats = '1F2oplauhiuPHxo5xsjpjFRJGwVi7FU1fWkcgQtEhnKy4'

# def OAuth():
#     try:
#         auth = tweepy.OAuthHandler(api_k, api_ks)
#         auth.set_access_token(at, ats)
#         return auth

#     except Exception:
#         return None

# OAuth = OAuth()
# apicall = tweepy.API(OAuth)

# apicall.update_status('Here is a sample tweet from Bevin Levin himself')
# print('Tweet tweeted')

import tweepy

consumer_key = "K3GHMEkGoYJQQaywJsvouYN2S"
consumer_secret = "2RHnRIP3SdJoZedvPfRYOfeih4fL8C3eCFgGn02bKU7b7H1XxL"

access_token = "1668830207552409603-vfSXOOdTX69XI8MF0e0grQvWaFERvm"
access_token_secret = "ciKmz2d0W6poM9ShqnQ6vgEHfCXvLmdFYs471IRA3IWIp"

client = tweepy.Client(
    consumer_key=consumer_key,
    consumer_secret=consumer_secret,
    access_token=access_token,
    access_token_secret=access_token_secret,
)

# The app and the corresponding credentials must have the Write permission
# Check the App permissions section of the Settings tab of your app, under the
# Twitter Developer Portal Projects & Apps page at
# https://developer.twitter.com/en/portal/projects-and-apps

# Make sure to reauthorize your app / regenerate your access token and secret
# after setting the Write permission

response = client.create_tweet(text="Jack Simoes is an interesting guy for sure")
print(f"https://twitter.com/user/status/{response.data['id']}")
