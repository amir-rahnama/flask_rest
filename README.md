### Flask RESTful API

The reason for this repo is to show an example of how you can work with flask both front-end and backend. I know that flaskr example from the repo is actually pretty good but it lacks the followings:

* More thorough project structure such as the separation of adapters from blueprints themselves
* The usage of static files per blueprints
* Exception handling
* Unit tests and integration tests
* Building the image with Docker

I have tried to improve my solution with aforementioned points, basically.

#### Installation

Clone the repo: 

```
git clone git@github.com:ambodi/flask_rest.git
```

Go to the directory of the project:

```
cd flask_rest
```

Run the following command:

```
export FLASK_APP=mini/app.py
```

After that, initialize the database with: 

```
flask initdb
```

And then, run the server with: 

```
flask run
```

You can now go to `localhost:5000/users`. 


### Run the tests
