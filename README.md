# RuleEngine
A simple rule engine implementation for an incoming stream of data.
It runs on python 3.5 and uses django rest framework for exposing APIs and results.

## Getting Started

Clone the repo using the below URL.

`git clone https://github.com/gauttham/RuleEngine.git
`

The clone command would also have pulled in a local copy of sqlite DB so that you don't have to be concerned about setting up the migration scripts and validating them.

### Prerequisites

Since this is a python app, you will need to run a python virtual environment if you don't want to mess around with the default set up of your app.

Please follow this link to set up a virtual environment on your mac or linux instance:
https://uoa-eresearch.github.io/eresearch-cookbook/recipe/2014/11/26/python-virtual-env/

Once the environment is activated (please be very sure of this step), please install the dependencies that are present in the requirements.txt file.

`pip install -r requirements.txt
`

### Installation

The installation of a django app is simple. Once the dependencies installation is completed, please navigate to the directory where the file `manage.py` is loated and run the following command.

`python manage.py runserver`

This will start the app on you local instance. Please be very sure that the dependencies in the file requirements.txt are all installed successfully.
Please be rest assured that the set up is completed once you see a response something like this:
![image](src/images/runserver.jpg?raw=true)
The above response means that the app is running on the port 8000 on your localhost.

You can visit the admin console by going to:

````angular2html
http://localhost:8000/admin
username: appuser
password: appuser
````
This will also give you direct access to the tables and add or create rules of your own.


### Testing the App

#### Loading Bulk raw_signal.json 

API:
`http://localhost:8000/v1/load/`

A **POST** Call to the above endpoint would load all the records in the raw_signal.json file and emit the rows that violated along with the rules that were violated for each row.
Sample response below:
![image](src/images/bulksignalloader.jpg?raw=true)




#### Creating a Rule

Rule creation has been built in a way that would make it easy to convert it into a Domain Specific Language (DSL) in the future.
The Rules are as verbose as possible.
For Eg one of the rules is as below:

`ATL1 Datetime Should Be > 2018-11-11 00:00:00`

The format in which new rules are accepted right now is shown below:
 
`<signal value> <value Type> <should/should not be> <greater than/lass than/equal to> <a value>`

The reason this design was chosen was with an intention of making rule creation as verbose as possible.

Creating a rule with an API:

EndPoint:

`http://localhost:8000/v1/rule/`

A GET Call to this API lists all the existing rules:

Eg:

````
[
    {
        "id": 3,
        "appliesOn": "ATL2",
        "valueType": "Datetime",
        "ruleType": "Should Not Be",
        "operator": "<",
        "value": "2018-11-11 00:00:00"
    },
    {
        "id": 4,
        "appliesOn": "ATL1",
        "valueType": "Datetime",
        "ruleType": "Should Be",
        "operator": ">",
        "value": "2018-11-11 00:00:00"
    },
    {
        "id": 5,
        "appliesOn": "ATL1",
        "valueType": "Integer",
        "ruleType": "Should Be",
        "operator": ">",
        "value": "56.679"
    }
]
````
However, following is a sample POST call that would create a new rule:

POST:

`data = {"appliesOn": "ATL2", "valueType": "Datetime", "ruleType": "Should Not Be", "operator": "<", "value": "2018-11-11 00:00:00"}`


#### Testing on Individual Signal Data 

A POST call with the signal data to the endpoint, returns the list of rules that a particular row violates.

Eg:
````angular2html
EndPoint: http://localhost:8000/v1/signal/

data: {
        "signal": "ATL1",
        "value": "3.3",
        "value_type": "Integer"
    }

Response:
{
    "violatedRules": [
        "ATL1 Integer Should Be > 56.679"
    ],
    "isViolated": true,
    "signal": "ATL1",
    "value": "3.3",
    "value_type": "Integer"
}

````


### Approach, Thoughts and Further Improvements

Please follow this page for further updates as information in thsi page is limited to setup, configuration and testing.
[Design Approach, thoughts and further improvements](APPROACH.md)









