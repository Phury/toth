
To configure a eve application to run on heroku you will need to following:

* create a virtual python environement for packaging the application correctly
* install your required dependencies
* create a requirements.txt file
* create a procfile to configure app as web dyno
* create your eve app
* pass the Heroku env parameters to your app

Create a virtual environment

> python -m venv ./
This will create a virtual environment in your project, you can now activate it by:
>  source ./Scripts/activate

It's time to install your local dependencies:

> pip install eve

Finally you can generate your requirements with the `-l` flag (local):

> pip freeze -l > requirements.txt