# Banking Backend API (Python, Flask-Restful, SQLAlchemy)

tags: `Flask` `RESTful` `SQLAlchemy` `Connexion` `Swagger`

A pseudo banking Backend API.

The tool consists of RESTful API's for given the Transaction details of a particular bank account [https://s3-ap-southeast-1.amazonaws.com/he-public-data/bankAccountdde24ad.json](https://s3-ap-southeast-1.amazonaws.com/he-public-data/bankAccountdde24ad.json).

Active APIs are

- [X] A GET request on /transactions/Date

  must return all transactions that occurred on that specific date

  Example - /transactions/29-06-17
- [X] A GET request on /details/:ID

  must return all the transaction details of that particular ID
- [X] A POST request on /add

  must allow the users to add additional transaction data with appropriate fields and proper error handling.

Not active APIs:

- [] A GET request on /balance/Date

  must return the balance amount remaining at the end of a day

  (Reason: Unable to understand the requirements for this API.)

## :gear: Features Implemented
- [X] Error Handling
- [X] Heroku Deployed

### :pushpin: Initialize The Database
This application currently uses SQLiteDB.
```console=1
$ python3 db_initializer.py
```

### Finally Run Application

Run the application which will be listening on port `5000`.

```console
$ python3 app.py
```

## API Endpoints

After the app is running and the end points can be accessed using the `Swagger2.0` API documentation at:

```
http://localhost:5000/api/ui
```


