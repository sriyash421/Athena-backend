# Athena
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/) [![ForTheBadge built-with-love](http://ForTheBadge.com/images/badges/built-with-love.svg)](https://GitHub.com/Naereen/)

Athena: Common backend for the Course Management System
Created as part of Software Engineering Lab (CS29006) during my 4th semester (Spring 2020)

```shell
.
├── app
│   ├── config.py
│   ├── controller
│   │   ├── chat_controller.py
│   │   ├── __init__.py
│   │   ├── notice_controller.py
│   │   ├── rec_controller.py
│   │   ├── search_controller.py
│   │   └── table_controller.py
│   ├── __init__.py
│   ├── models
│   │   ├── course_data.py
│   │   ├── course.py
│   │   └── slots.py
│   ├── README.md
│   └── site.db
├── __init__.py
├── requirements.txt
├── run.py
├── sanity.sh
```
- `controller` contains the various endpoints to fetch data, and run the utility functions
- `models` contains the SQLLite models for the app

