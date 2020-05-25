# Athena: A Course Management System

## Implementational Details

### TechStack: 
- Backend
    - Flask
    - Flask Admin
    - Flask Cors
    - Flask SQLAlchemy
    - Flask SocketIO
    - SQLLite
    - Elastic Search
    - JavaScript Objects
    - requests
    - BeautifulSoup4

- Frontend
    - ReactJS
    - axios
    - react-bootstrap
    - react socket.io
    - HTML
    - CSS
    - JavaScript Objects

### Frontend Interface
- ReactJS is used as a framework for its implementation.
- CSS and some react libraries are used to beautify the pages.
- Used CSS animation to create the landing page
- Used HTMLtoPng to download the timetable
- Used socketio.client to get real time messaging
- Used axios to fetch data from server and ip_adress
- Used JavaScript obejcts to pass data

### Backend
- Used flask request to send data from the client(i.e the frontend) to the server.
- Used flask response to send back response to client
- Used Elastic Search to generate the search and recommendation results
- Used SQLLite as database and SQLAlchemy as ORM
- Used JavaScript obejcts to pass data
- Used Websockets to enable real time data transfer between the clients and thus, implement the chat room.
- Used requests and BeautifulSoup4 to scrape the internet to get data about course information and slots.

#### GUI        : ReactJS
#### Networking : Websockets
#### Database   : SQL   