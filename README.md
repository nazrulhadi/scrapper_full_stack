# 


# scrapper_full_stack

scrape the data from zus website and check the intersection with outlet

## Getting Started

These instructions will help you set up and run the project on your local machine.

### Prerequisites

- Docker installed on your local machine.
- Visual Studio Code with the DevContainer extension.

### Running the Code

1. Clone the repository to your local machine.
2. Open the project in Visual Studio Code.
3. Run the DevContainer using the shortcut `Ctrl + Shift + P` and choose "Build without cache."
4. run comman ` docker ps`  to check the docker up an running example:
```
CONTAINER ID   IMAGE                                          COMMAND                  CREATED         STATUS         PORTS                                                                                            NAMES
fece37b7f6af   scraper_full_stack_devcontainer-devcontainer   "/bin/sh -c 'echo Co…"   8 minutes ago   Up 8 minutes   0.0.0.0:7071->7071/tcp, :::7071->7071/tcp                                                        scraper_full_stack_devcontainer-devcontainer-1
06849eef6310   neo4j:enterprise                               "tini -g -- /startup…"   8 minutes ago   Up 8 minutes   0.0.0.0:7474->7474/tcp, :::7474->7474/tcp, 7473/tcp, 0.0.0.0:7687->7687/tcp, :::7687->7687/tcp   scraper_full_stack_devcontainer-neo4j-1

```

### Copy file to docker
run this command to copy file to docker
` docker cp outlets_with_coordinates.csv <container_id>:/var/lib/neo4j/import/ `

### Database Configuration

After the Docker container is up and running, obtain the Docker IP for the database:

``` bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id_or_name>
```

Paste the obtained Docker IP into the uri variable in server.py.
Paste the obtained Docker IP into the uri variable in ingest_data.py.

### Ingest Data in database
run this command

`python ingest_data.py`

### Set Up Flask

Run the following export command to set up Flask:

`export FLASK_APP=server.py`

### Run Flask Application

Now, run the Flask application with debugging:

`flask run --debug`

Upon running Flask, you will land on the dashboard page.

### Navigate to Maps

Click on "Maps" to navigate to the maps page.

### Search for Outlets

Upon landing on the maps page, enter the outlet name and the distance. For example:


`ZUS Coffee – MITC Melaka, 5`

Click "Search" to proceed.