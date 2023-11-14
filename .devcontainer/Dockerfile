# Use an official Python runtime as a parent image
ARG VARIANT=bullseye
FROM --platform=amd64 mcr.microsoft.com/devcontainers/python:0-${VARIANT}

# Set the working directory to /app
WORKDIR /workspace

# Copy the current directory contents into the container at /app
COPY . /workspace

# Install any needed packages specified in requirements.txt
RUN pip install -r requirements.txt

#Install Azure CLI
RUN curl -fsSL https://aka.ms/install-azd.sh | bash \
    && curl https://packages.microsoft.com/keys/microsoft.asc | gpg --dearmor > microsoft.gpg \
    && mv microsoft.gpg /etc/apt/trusted.gpg.d/microsoft.gpg \
    && sh -c 'echo "deb [arch=amd64] https://packages.microsoft.com/debian/$(lsb_release -rs | cut -d'.' -f 1)/prod $(lsb_release -cs) main" > /etc/apt/sources.list.d/dotnetdev.list' \
    && apt-get update && apt-get install -y azure-functions-core-tools-4 \
    && apt update && apt-get install -y xdg-utils
# Install Node.js and npm
RUN apt-get update && apt-get install -y nodejs npm

# Install cypher shell
ADD https://dist.neo4j.org/cypher-shell/cypher-shell_4.4.19_all.deb /root/

RUN apt install /root/cypher-shell* -y --no-install-recommends

RUN pip install reflex

# Install Azurite using npm
RUN npm install -g azurite

# Expose the ports for FastAPI, Neo4j, and Azurite (modify the ports if necessary)
# EXPOSE 8000 7474 7687 10000

# Start FastAPI application
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
