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

### Database Configuration

After the Docker container is up and running, obtain the Docker IP for the database:

```bash
docker inspect -f '{{range .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container_id_or_name>```
