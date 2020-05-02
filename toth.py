from eve import Eve
import os

APP_PORT = int(os.environ['PORT'])

settings = {
    'MONGO_HOST': os.environ['MONGO_HOST'],
    'MONGO_PORT': os.environ['MONGO_PORT'],
    'MONGO_USERNAME': os.environ['MONGO_USERNAME'],
    'MONGO_PASSWORD': os.environ['MONGO_PASSWORD'],
    'MONGO_DBNAME': os.environ['MONGO_DBNAME'],
    'DOMAIN': {
    	'decks': {},
    	'collection': {}
	}
}


app = Eve(settings=settings)


if __name__ == '__main__':
   app.run(port=APP_PORT)