import tweepy, time, os
from os import environ

def main():

    CONSUMER_KEY = environ.get("CONSUMER_KEY")
    CONSUMER_SECRET = environ.get("CONSUMER_SECRET")
    ACCESS_KEY = environ.get("ACCESS_KEY")
    ACCESS_SECRET = environ.get("ACCESS_SECRET")

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    interval = 60 * 60 * 24
    days_gone = 2 * 365

    while True:

        txt = create_string(days_gone)
        api.update_status(txt)
        days_gone += 1
        print("Days gone: {}".format(days_gone))
        time.sleep(interval)

def create_string(num):

    tags = "#bringboernenehjem @statsmin @DanishMFA"
    years = int(num / 365)
    days = int(num % 365)

    if days == 0:

        txt = "De danske børn har nu siddet mindst {} år i lejrene i Syrien. {}".format(years, tags)

    elif days == 1:

        txt = "De danske børn har nu siddet mindst {} år og 1 dag i lejrene i Syrien. {}".format(years, tags)

    else:

        txt = "De danske børn har nu siddet mindst {} år og {} dage i lejrene i Syrien. {}".format(years, days, tags)

    return txt

if __name__ == '__main__':
    main()