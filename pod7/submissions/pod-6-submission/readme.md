# Pod 6 Submission

## Summary
This submission contains a frontend and a backend that can be hosted in Docker 
containers. The frontend and backend are defined with separate Dockerfiles that
can be ran simultaneously using the included docker-compose file.

## Instructions
1. Run docker-compose up in root directory (directory where docker-compose.yaml
exists)
2. Open the frontend in a browser by heading to localhost:3000.
3. Witness that frontend is speaking to backend. There should be a message that
says "Received data from server: Hello from the backend" (backend can be communicated
with through localhost:3001)
4. If frontend Docker container is ran without backend then the message will read
"An error occurred while fetching data."

## Alternate Instructions 
To illustrate running containers separately you can follow these instructions
1. Build both of the containers by heading into their respective directories
(/frontend & /backend) and using the commands "docker build -t frontend ." and 
"docker build -t backend ." respectively
2. Run the frontend Docker container by using the command "docker run -d -p 3000:80
frontend"
3. Once that Docker container is running head to localhost:3000 in a browser to 
see frontend. It should display a message saying: "An error occurred while 
fetching data.", since the backend is not up yet.
4. Run the backend Docker container by using the command "docker run -d -p 3001:3001
backend".
5. Refresh the frontend webpage and now it should display a message saying:
"Received data from server: Hello from the backend"

