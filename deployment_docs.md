## Instructions for deploying the app on a Kubernetes cluster

Included:

1. Makefile Instructions
2. Docker/Docker-Compose
3. Kubernetes

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