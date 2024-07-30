# Flask REST API with JWT Authentication and Docker Support

This repository contains a Flask application that provides REST APIs for managing lists and users. It includes features for creating, retrieving, updating, and deleting lists, as well as creating, retrieving, and deleting users. JWT authentication is implemented to secure the list APIs.

## Features

- **Lists API**:
  - Create a new list
  - Retrieve all lists
  - Retrieve a specific list by ID
  - Update a list by ID
  - Delete a list by ID
  - All list APIs require JWT validation

- **Users API**:
  - Create a new user
  - Retrieve all users
  - Retrieve a specific user by ID
  - Delete a user by ID

- **Authentication**:
  - User login
  - User logout
  - JWT authentication for securing APIs

## Setup Instructions

### Prerequisites

- Docker
- Docker Compose

### Running the Application

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/rrvermaa/first-app
   cd first-app

2. **Build and Run the Docker Container:**
    sh
    Copy code
    docker-compose up --build

3. **Access the Application:**
    The application will be accessible at `http://localhost:5000`.
    Swagger UI is available at `http://localhost:5000/swagger-ui`.

4. **Postman API Dashboard**
Below is an image showing the Postman API dashboard:
![Alt text](https://github.com/rrvermaa/first-app/image)
