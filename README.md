# Social Networking Application

A social networking application using Django Rest Framework.

## Features

- User Login/Signup (JWT Authentication)
- API to send/accept/reject friend requests
- API to list friends (list of users who have accepted friend requests)
- List pending friend requests (received friend requests)
- Users can not send more than 3 friend requests within a minute

## Installation

Follow the steps below to set up the application:

1. Install Docker on your system. You can find installation instructions [here](https://docs.docker.com/compose/install/).

2. Navigate to the `social_networking_app` directory.

3. Run the following command to start the application:
   ```bash
   docker-compose up

4. Check the running containers:
   ```bash
    docker ps

5. Access the application container:
   ```bash
    docker exec -it <container_id> bash

6. Apply database migrations:
   ```bash
    python manage.py migrate

7. Create a superuser for admin access:
   ```bash
    python manage.py createsuperuser

Now, your application is running at http://localhost:8000.
