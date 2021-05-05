## COE332 Final Project

* worked alone

Current tree:

```bash
.
├── README.md
├── config
│   ├── dump.rdb
|   └── redis.conf
├── deploy
│   ├── api
│   │   ├── api-deployment.yml
│   │   └── api-service.yml
│   ├── db
│   │   ├── db-deployment.yml
│   │   ├── db-pvc.yml
│   |   └── db-service.yml
│   └── worker
│       └── worker-deployment.yml
├── docker
│   ├── Dockerfile.api
│   ├── Dockerfile.db
│   ├── Dockerfile.wrk
│   ├── docker-compose.yml
│   └── requirements.txt
└── source
    ├── api.py
    ├── job.py
    ├── pet_data.json
    └── worker.py
```