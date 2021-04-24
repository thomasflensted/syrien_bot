import tweepy, time, os
from credentials import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_KEY, ACCESS_SECRET

def main():

    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
    api = tweepy.API(auth)

    interval = 5
    days_gone = 2 * 365

    while True:

        txt = create_string(days_gone)
        api.update_status(txt)
        days_gone += 1
        time.sleep(interval)

def create_string(num):

    tag_ministries = "#bringboernenehjem @statsmin @DanishMFA"
    years = int(num / 365)
    days = int(num % 365)

    if days == 0:

        txt = "De danske børn har nu siddet mindst {} år i lejrene i Syrien. {}".format(years, tag_ministries)

    elif days == 1:

        txt = "De danske børn har nu siddet mindst {} år og 1 dag i lejrene i Syrien. {}".format(years, tag_ministries)

    else:

        txt = "De danske børn har nu siddet mindst {} år og {} dage i lejrene i Syrien. {}".format(years, days, tag_ministries)

    return txt

if __name__ == '__main__':
    main()