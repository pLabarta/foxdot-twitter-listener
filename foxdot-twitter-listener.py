### Imports
import threading
import time
from xml.sax.saxutils import unescape
#
from twython import Twython
TWITTER_APP_KEY = ' ' #supply the appropriate value
TWITTER_APP_KEY_SECRET = ' ' 
TWITTER_ACCESS_TOKEN = ' '
TWITTER_ACCESS_TOKEN_SECRET = ' '
t = Twython(app_key=TWITTER_APP_KEY, 
            app_secret=TWITTER_APP_KEY_SECRET, 
            oauth_token=TWITTER_ACCESS_TOKEN, 
            oauth_token_secret=TWITTER_ACCESS_TOKEN_SECRET)
### Funcion traer tuits
#usa twython para traer una cantidad definida de los ultimos tuits en un hashtag
def traer_tweets(hashtag, cantidad):
    search = t.search(q=hashtag, count=cantidad)
    tweets = search['statuses']
    return tweets
### Funcion traer constantemente
# crea un thread que cada 10 segundos revisa cual es el ultimo tuit en el hashtag y actualiza el player c1 con el texto del tuit unscapeado
def traer_constantemente():
    while(boton_de_encendido):
        tweet = traer_tweets(hashtag, cantidad_de_tweets)[0]
        text = tweet['text']        
        user = tweet['user']['screen_name']
        tweet_sonando = unescape(text[0:text.find(hashtag)-1]) #Tomo el tweet hasta el hashtag sin incluir el espacio
        c1 >> play(tweet_sonando)
        print('Esta sonando: \"'+ tweet_sonando +'\" por @'+user)
        time.sleep(10)
#Config
hashtag = '#algosuperespecifico'
cantidad_de_tweets = 1
tweets = traer_tweets(hashtag, cantidad_de_tweets)
#Test
if len(tweets) > 0:
    print('Todo OK, papa!')
    print(f'Escuchando hashtag {hashtag}')

## Dale gas
#si le das False al boton se apaga
boton_de_encendido = True
threading.Thread(target=traer_constantemente).start()


tweet = traer_tweets(hashtag, cantidad_de_tweets)[0]
text = tweet['text']
user = tweet['user']['screen_name']

print(text)
print(user)

print('\"')
