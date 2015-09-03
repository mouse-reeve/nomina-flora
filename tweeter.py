''' tweets out fake facts '''
from NominaFlora import NominaFlora

import settings
import tweepy
from tweepy.error import TweepError

def get_flower():
    ''' pops a fact off the fact list '''
    namer = NominaFlora()
    flower = '%s (%s) #generative #flowers' % (namer.get_common_name(), namer.get_scientific_name())

    return flower

if __name__ == '__main__':

    auth = tweepy.OAuthHandler(settings.API_KEY, settings.API_SECRET)
    auth.set_access_token(settings.ACCESS_TOKEN, settings.ACCESS_SECRET)
    api = tweepy.API(auth)

    try:
        api.verify_credentials()
    except TweepError:
        pass
    else:
        for _ in range(0, 4):
            content = get_flower()
            try:
                api.update_status(status=content)
                break
            except TweepError as e:
                print 'Failed to tweet: "%s"' % content
                print 'error: %s' % e
