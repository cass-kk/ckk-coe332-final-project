## Instructions for building a REST API interface to a json data set.

Included:

1. Makefile Instructions
2. Flask API Interaction
3. More about the Redis Database
4. More about the Worker

### Makefile

A Makefile is included to easily launch the app or for quick commands to generate portions of the app individually. The following will list command lines that can be used with and without a Makefile shortcut.

At the top of the Makefile, certain variables are declared for their later use within the Makefile commands.  Before using the Makefile and any of its commands, change the values of certain variables.  For example, change the namespace, redis port (RPORT), flask port (FPORT), user ID, and group ID values.

Github and Docker are connected for this app so that everytime a change is made to the app, all of the Docker containers (api, rd/db, and worker) will all be tagged with the same release.  Edit the version (VER) at the top of the Makefile and then please do the following to tag a release:

```bash
[]$ git add <files_with_new_code> 
[]$ git commit -m "<update_message>"
[]$ git branch -M main
[]$ git push -u origin main
login
[]$ git tag a <tag> -m '<description>'
git push origin <tag>
```

### Interacting with the API

The flask api is mapped to port 5000 on ISP from 5015.

The following routes are included in the flask api:

```bash
/pets			# get all the pets in the data set
/pets/<type_p>		# takes a user requested type of pet, specified by <type_p>, and gets all pets of that type (i.e. either cat or dog)
/pets/breed		# get a list of all of the breeds (only breeds)
/pets/color		# takes a user requested color and gets all of the pets with that color
/pets/find		# takes a user requested pet type (i.e. cat or dog) and a user requested age to get pets that match the type and age
/pets/date		# takes a user requested date and gets all pets taken in on that date
/download/<jobuuid>	# takes a user requested job UUID and downloads the image associated with the job UUID
/jobs			# submits a job with a generated job UUID
/delete/<jobid>		# takes a user requested job UUID and deletes it
```

And can be accessed by:

```bash
[]$ curl localhost:5000/<add_in_the_rest_of_route>
```

The /jobs submits jobs with the POST method as follows:

```bash
[]$ curl -X POST -H "key=dog" -d localhost:5000/jobs 
```


### Redis Database

The Redis Database maps to the default Redis port 6379 on ISP from port 6395.  The configuration for Redis is in the redis.conf file under the config directory.  The database will dump and update into the dump.rdb file, also in the config directory, and also access the most recently updated database.

To remove and clean the database, the redis container must be stopped before the dump.rdb file can be deleted.  After the file is deleted, start a new container and a new dump.rdb will be created.

### Worker

The worker receives messages about new jobs and performs the analysis steps in the execute_job function.  This worker will receive user input of a date range and do the following:

1. Check each data subset to see if it's date at key[12] falls in the date range given.
2. It also checks that the animal for that subset is a dog (i.e. at key[13]).
3. If so, it will then take that subset and append the breed (i.e. at key[14]) to an array/dictionary called results.
4. The worker will then plot the results in a historgram graph.  The x-axis being the Breed Types and the y-axis being the Number of Dogs in order to sort the data between the date range to see how many dogs are of a certain breed.