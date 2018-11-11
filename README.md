# RuleEngine
A simple rule engine implementation for an incoming stream of data.
It runs on python 3.5 and uses django rest framework for exposing APIs and results.

## Getting Started

Clone the repo using the below URL.

`git clone https://github.com/gauttham/RuleEngine.git
`

The clone command would also have pulled in a local copy of sqlite DB so that you don't have to be concerned about setting up the migration scripts and validating them.

###Prerequisites

Since this is a python app, you will need to run a python virtual environment if you don't want to mess around with the default set up of your app.

Please follow this link to set up a virtual environment on your mac or linux instance:
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/

Once the environment is activated (please be very sure of this step), please install the dependencies that are present in the requirements.txt file.

`pip install -r requirements.txt
`

###Installation

The installation of a django app is simple. Once the dependencies installation is completed, please navigate to the directory where the file `manage.py` is loated and run the following command.

`python manage.py runserver`

This will start the app on you local instance. Please be very sure that the dependencies in the file requirements.txt are all installed successfully.
Please be rest assured that the set up is completed once you see a response something like this:
![Alt text](images/runserver.jpg?raw=true)

### Testing the App



