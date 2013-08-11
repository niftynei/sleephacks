sleephacks
==========

To install dependencies with pip, run 
`pip install -r pip_startup.txt`

Using the API requires two environment variables to be set.
Run the following before running the django server.

- `export UP_API_CLIENT=  (Key from email)`
- `export UP_API_SECRET=  (Key from email)`

Requires setting up a database on mysql called sleephackers, and adding a user, sleephacker.  Password: sleepers.  These configurations are set in settings.py.

- `CREATE DATABASE sleephackers;`

