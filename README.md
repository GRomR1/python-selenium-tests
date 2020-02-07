## Getting started with Selenium and Selenoid in Python

This project include a basis of [Selenoid Grid](https://aerokube.com/selenoid/latest/).
The environment defined in  [docker-compose.yml](./docker-compose.yml) file create an environment to
launch automated web tests in parallel with Docker. 

![selenoid-ui](selenoid-ui.png)

### Start the services

Run next in the current directory where `docker-compose.yml` file is present.
```sh
docker-compose up -d
```

Install dependencies and run a simple example to tests them - [main.py](./main.py)
```
pip install -r requirements.txt
python main.py
```

To view runned session open browser and follow to the link [http://localhost:8080](http://localhost:8080)

### Details

Read a detailed article about [Selenium in Docker]() that I explain details of the Selenoid.

> Also read to official materials about [Selenoid](https://aerokube.com/selenoid/latest)
