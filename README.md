## COE332 Final Project

* worked alone


The data for this app contains all stray cats and dogs that are currently listed in the Austin Animal Center's database in the past week.  The data used is from 29 April 2021 to 5 May 2021.  The data that can be accessed includes the intake date, pet type (dog or cat), the breed it looks like, the pet's coloring, and the pet's age.

The data can be accessed with the following link:
https://data.austintexas.gov/Health-and-Community-Services/Austin-Animal-Center-Found-Pets-Map/hye6-gvq2





Current tree:

```bash
.
├── Makefile
├── README.md
├── config
│   ├── dump.rdb
│   └── redis.conf
├── deploy
│   ├── api
│   │   ├── api-deployment.yml
│   │   └── api-service.yml
│   ├── db
│   │   ├── db-deployment.yml
│   │   ├── db-pvc.yml
│   │   └── db-service.yml
│   └── worker
│       └── worker-deployment.yml
├── deployment_docs.md
├── docker
│   ├── Dockerfile.api
│   ├── Dockerfile.db
│   ├── Dockerfile.wrk
│   └── docker-compose.yml
├── requirements.txt
├── source
│   ├── api.py
│   ├── job.py
│   ├── pet_data.json
│   └── worker.py
└── user_docs.md
```