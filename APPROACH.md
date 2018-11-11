## Design Doc for the Rule Engine

###Model Design

#####Model - SignalData:

- signal: Signal name (ALT1 .. ALT N)
- value: Charfield ( A literal value)
- valueType: Charfield (Integer, Datetime, String)
- isViolated: Boolean

#####Model - Rule

The rule model stores the rules persistently in the database. The following are the attributes of the Rule model.

- appliesOn : Char Field (Applies on what signal value? ALT1, ALT N etc)
- valueType: Char Field (Type of field on which the rule applies)
- ruleType: Char Field (Should something happen or should something not happen)
- operator: Char Field (The current supported operators are '<', '>', '=')
- value: Char Field (The value against which a rule has to be checked)

####Trade Offs:

Since we are using the database driven rules engine, we will at some point of time reach a place where the any new updates to the engine or a rule will regress to the rest of the app and we would never know when what would break with what change.

We should also think of how best to break this into async tasks by using an async worker framework such as celery.

Right now, we are using the database to store the rules persistently, which means we will have to keep reading from database for every new signal. This is currently adding a lot to the network traffic is the database resides in a remote server.


#### Runtime performance, Complexity and Bottlenecks

The runtime performance is pretty good as of now since the number of records that we tested were around 200 in number.
The complexity with respect to time continues to be `O(n)` since the data is being parsed once at a time.

I see bottlenecks to be around the synchronous nature of the app's functioning. We will have to implement celery workers to make the processing of the data async and also bring in a caching layer like redis which would reduce the number of hits to the DB and read from the app's cache.

#### Further improvements - with more time

Further, the first thing that needs to be done is to convert the whole processing from being a synchronous process into parallely executing async implementation.
This will reduce the time drastically while dealing with a huge amount of incoming stream of data.

The next would be the caching implementation by introducing a redis layer in between the app and the DB, to avoid as many hits to the DB as possible for the same combination of signal and value type.

Provide flexibility to create new rules like verbose commands or DSLs.
For eg: `ALT1 Integer should be < 100`
Parse the text and create rule by understanding the text. This would be a major breakthrogh in building real time rules engine using natural language.
 
 
