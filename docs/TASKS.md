# Athena: A Course Management System

## Tasks Completed
The following are the tasks completed :

### Backend
- Created endpoints to 
    - run a `search` for courses, given a set of keywords
    - `filter` the search results, based on users choices
    - `get course information` such as credits, professor names and keywords

- Created endpoints to 
    - `generate recommended courses` for the user, given a set of keywords

- Created endpoints to 
    - `fetch the slots` for various courses
    - `add and delete courses` to and from the timetable

- Created endpoints to
    - `search notice boards` of different courses
    - `fetch, create, delete and downvote` notices

- Created endpoints to
    - `search chat rooms` of different courses
    - fetch `chat history`
    - send `messages`

- Created a pipeline to implement real time message conversation using `websockets and networking`

- Create database models to
    - store `course information`
    - store `course slots`
    - store `notices`
    - store `messages`
    - store `user information(ip_address, downvotes etc.)`

- Created an `elastic search instance` to get search and recommend results
- `Scraped the internet` to get information about the course
- `Populated the database` with the scraped data

### Frontend

- Created a `landing page` for the users
- Created a `search page` with `multi-keyword input`, `filter checkboxes` and `hyperlinks`
- Created a `recommendation page` with `multi-keyword input`, `graphical output` and `hyperlinks`
- Created a `page to add courses` to the timetable with `autocomplete search bar`, `graphical output` option to `download the timtable` and `warnings`, in case of clashes
- Created a page to `search for notice boards`
- Created a page to `see, add, delete and downvote your notices`
- Created a page to `search for chat rooms`
- Created a page to `see the chat history and send messages`


#### All functionalities are implemented with the users identity being anonymous.