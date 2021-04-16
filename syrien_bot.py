import tweepy, time, os

CONSUMER_KEY = os.environ.get('CONSUMER_KEY')
CONSUMER_SECRET = os.environ.get('CONSUMER_SECRET')
ACCESS_KEY = os.environ.get('ACCESS_KEY')
ACCESS_SECRET = os.environ.get('ACCESS_SECRET')

auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
auth.set_access_token(ACCESS_KEY, ACCESS_SECRET)
api = tweepy.API(auth)

def main():

    seconds_pr_min = 1
    mins_pr_hour = 1
    hours_pr_day = 5
    one_day = seconds_pr_min * mins_pr_hour * hours_pr_day

    days_gone = 2 * 365

    while True:

        txt = create_string(days_gone)
        api.update_status(txt)
        days_gone += 1
        time.sleep(one_day)

def create_string(num):

    if num % 365 == 0:

        txt = "De danske børn har nu siddet mindst {} år i Syrien og de er stadig ikke på vej hjem. #bringboernenehjem".format(int(num / 365))

    elif num % 365 == 1:

        txt = "De danske børn har nu siddet mindst {} år og 1 dag i Syrien og de er stadig ikke på vej hjem. #bringboernenehjem".format(int(num / 365))

    else:

        txt = "De danske børn har nu siddet mindst {years} år og {days} dage i Syrien og de er stadig ikke på vej hjem. #bringboernenehjem".format(years =  int(num / 365), days = num % 365)

    return txt

if __name__ == '__main__':
    main()