## Instructions for building a REST API interface to a json data set.

### Makefile

A Makefile is included to easily launch the app or for quick commands to generate portions of the app individually. The following will list command lines that can be used with and without a Makefile shortcut.

At the tpo ????????????????????????????????????????????????????
AND IMAGE TAGGING ?????????????????????????????????????????????



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

### Redis Database

The Redis Database maps to the default Redis port 6379 on ISP from port 6395.  The configuration for Redis is in the redis.conf file under the config directory.  The database will dump and update into the dump.rdb file, also in the config directory, and also access the most recently updated database.

To remove and clean the database, the redis container must be stopped before the dump.rdb file can be deleted.  After the file is deleted, start a new container and a new dump.rdb will be created.

### Worker

The worker receives messages about new jobs and performs the analysis steps in the execute_job function.  This worker will receive user input of a date range and do the following:
1.) Check each data subset to see if it's date at key[12] falls in the date range given.
2.) It also checks that the animal for that subset is a dog (i.e. at key[13]).
3.) If so, it will then take that subset and append the breed (i.e. at key[14]) to an array/dictionary called results.
4.) The worker will then plot the results in a historgram graph.  The x-axis being the Breed Types and the y-axis being the Number of Dogs in order to sort the data between the date range to see how many dogs are of a certain breed.

### Docker/Docker-Compose

Individual docker files have been set up for the api, rd/db, and worker files.

Using commands from the Makefile, build these docker containers individually,

```bash
[]$ make build-db
[]$ make build-api
[]$ make build-worker
```

Or build them together

```bash
[]$ make build-all
```

Later, remove the containers with

```bash
[]$ make clean-db
[]$ make clean-api
[]$ make clean-worker
```

Or remove them together
```bash
[]$ make clean-all
```

A Docker-Compose file has also been created in order to launch multiple containers at once.  Use the commands set from the Makefile to build all of the containers at once

```bash
[]$ make compose-up
```

And to remove them all together

```bash
[]$ make compose-down
```


### Kubernetes

This app supports the Kubernetes environment with deployment, pvc, and service .yml files.  However, changes will need to be made, including: image tags, IP_addresses, and possibly ports.

The following commands will then be useful to launch the deployments, pvc, and service files from the deploy folder.

To create an individual deployment in the command line:

```bash
[]$ kubectl apply -f <deployment_name>.yml
```

Or, to launch all of the .yml files in the deploy folder use the commands found in the Makefile:

```bash
[]$ make k
```

To delete an individual deployment in the command line:

```bash
[]$ kubectl delete deployment <deployment_name>.yml
```

Or, using the command in the Makefile to delete all of the deployments running from .yml files in the deploy folder:

```bash
[]$ make k-del
```

Note: Pods connected to deployments can only be deleted by deleting the deployments.  Just deleting the pod will not do anything as kubernetes will launch another pod immediately.


To see more information for the deployments (i.e. name, status, age, IP_address, node):

```bash
[]$ kubectl get deployment -o wide
```