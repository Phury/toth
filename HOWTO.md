
To configure a eve application to run on heroku you will need to following:

* create a requirements.txt file
* create a procfile to configure app as web dyno
* create your eve app
* pass the Heroku env parameters to your app

Generate a requirements file with pip
> pip freeze > requirements.txt.