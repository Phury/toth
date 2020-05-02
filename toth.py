from eve import Eve
import os

print(os.environ['PORT'])
print(os.environ['MONGO_HOST'])
print(os.environ['MONGO_PORT'])
print(os.environ['MONGO_USERNAME'])
print(os.environ['MONGO_PASSWORD'])
print(os.environ['MONGO_DBNAME'])

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
   app.run(port=os.environ['PORT'])