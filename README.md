# Collab Editor

This is a collaborative editor application that allows multiple users on a local network to edit files together in real-time. The application uses Docker and Docker Compose for easy setup and deployment.

[![Video Title](https://img.youtube.com/vi/eolc7DF0PTo/0.jpg)](https://www.youtube.com/watch?v=eolc7DF0PTo)

## Features

- Real-Time Editing: Collaborate on documents in real-time, with changes visible to all users instantly.
- Caret position continuity: Even when collaborators are writing up a storm, your caret stays in context.
- User-Friendly Interface: Simple interface for team members to join in.
- Contained in Docker and Restricted to "Files" Directory: Collaborators can only modify files located within the designated "files" directory. This restriction ensures that collaborators can only access and edit the files intended by the host.

## Use Cases

- Software development teams can leverage the Collab Editor for pair programming and code reviews. Multiple developers can simultaneously work on the same piece of code, spotting errors and providing feedback in real-time.
- Authors, content creators, and journalists can collaborate seamlessly on articles, reports, and documents. The editor allows them to co-write, edit, and refine content together, ensuring consistency and accuracy throughout the writing process.
- Teams can engage in brainstorming sessions using the editor and collectively generate ideas and organize them.

## Installation Steps

Before you begin, make sure you have Docker and Docker Compose installed on your system.

### 1. Install Docker and Docker Compose

- [Install Docker](https://docs.docker.com/get-docker/)
- [Install Docker Compose](https://docs.docker.com/compose/install/)

### 2. Build the Docker Containers

Navigate to the root directory of the collaborative editor project and execute the following command to build the Docker containers:

```sh
docker-compose build
```

## First Run Steps

Follow these steps to set up and run the collaborative editor application.

### 1. Place Files to Edit

Put the files you want to collaborate on in the `files` directory within the project's root directory.

### 2. Start the Application

Run the following command to start the collaborative editor application:

```sh
docker-compose up
```

This command will start the container and automatically launch the Flask server.

### 3. Access the Application

- To access the collaborative editor from your host computer, open a web browser and go to `http://localhost:8000`.
- To access the application from other computers on the same local network, use the IP address of the host computer. For example, if the IP address of the host computer is `192.168.1.100`, you can access the editor from another device by entering `http://192.168.1.100:8000` in a web browser.

## Usage

- Upon accessing the collaborative editor, you can select one of the files available for editing in the `files` directory.
- Click on edit button to open it for editing.
- Changes made by one user will be instantly reflected for all other users viewing the same file.
- Click on save button to commit the changes to the file in `files` folder. 

## Technologies Used

- 

