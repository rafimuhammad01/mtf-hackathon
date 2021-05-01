# USER
**POST api/v1/auth/register/**
----
  Register User
* **URL Params**  
  None
* **Data Params**  
  ```
    {
      "username" : "test",
      "password" : "test123456",
      "password2" : "test123456",
      "email" : "test@gmail.com",
      "first_name" : "test",
      "last_name" : "test"
    }
  ```
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "username": "test1",
    "email": "tes1t@gmail.com",
    "first_name": "test",
    "last_name": "test"
}
```

**POST api/v1/auth/login/**
----
  Login User
* **URL Params**  
  None
* **Data Params**  
  ```
    {
      "username" : "test",
      "password" : "test123456"
    }
  ```
* **Headers**  
  Content-Type: application/json
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
  {
      "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTI0NzAxNywianRpIjoiMDE4Yzk0M2UwZjMyNDRjM2FkYTllNmM3MmI3YjllYmEiLCJ1c2VyX2lkIjoyfQ.PVi8_eE8QxocXAXe5CDgtAgvBylqcmQ2WrAxUaTz5jI",
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5MTYwOTE3LCJqdGkiOiI1YmY5YTdiYzlhZjE0MzZiOWQxZWVmYWJjZjZhNDZiNiIsInVzZXJfaWQiOjJ9.LWsT9Z0CUYJtZze1DDbFwtJqNlyVUEsBbX-eGtZ3UAA"
  }
```

**POST api/v1/auth/refresh/**
----
  Get user refresh token
* **URL Params**  
  None
* **Data Params**  
  ```
    {
      "refresh" : "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxOTI0Njg3NywianRpIjoiNmQ3ZmE5OWFjMTZlNGI0MzkxMDMzOGVkMzYyMzdkOTYiLCJ1c2VyX2lkIjoyfQ.NhnGG-yFjAP9lB0NA0OblesO1tVyM9_qAE0NRv1Fb3I"
    }
  ```
* **Headers**  
  Content-Type: application/json
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
  {
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5MTYwOTE3LCJqdGkiOiI1YmY5YTdiYzlhZjE0MzZiOWQxZWVmYWJjZjZhNDZiNiIsInVzZXJfaWQiOjJ9.LWsT9Z0CUYJtZze1DDbFwtJqNlyVUEsBbX-eGtZ3UAA"
  }
```

**POST api/v1/auth/user/**
----
  Get user data
* **URL Params**  
  None
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
  {
      "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE5MTYwOTE3LCJqdGkiOiI1YmY5YTdiYzlhZjE0MzZiOWQxZWVmYWJjZjZhNDZiNiIsInVzZXJfaWQiOjJ9.LWsT9Z0CUYJtZze1DDbFwtJqNlyVUEsBbX-eGtZ3UAA"
  }
```





# DILAN

**GET api/v1/article?category=**
----
  Returns all article related to category.
* **URL Params**  
  *Required:* `category=[string]`
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 200,
    "message" : "success",
    "data" : {
        "section" : [
            {
                "id" : "string",
                "title" : "string",
                "article" : [
                    {
                        "id" : "string",
                        "title" : "string",
                        "content" : "HTML"
                    }
                ]
            }
        ],
        count : "int"
    }
}
```

**GET api/v1/article?search=**
----
  Returns all article related to search.
* **URL Params**  
  *Required:* `search=[string]`
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 200,
    "message" : "success",
    "data" : {
        "articles" : [
            {
                "id" : "string",
                "title" : "string",
                "content" : "HTML"
            }
        ],
        count : "int"
    }
}
```

**GET api/v1/article/:ID**
----
  Returns article detail by ID.
* **URL Params**  
  *Required:* `ID=[string]`
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 200,
    "message" : "success",
    "data" : {
        "id" : "string",
        "title" : "string",
        "content" : "HTML"
    }
}
```

**GET api/v1/forum?category=&sort=**
----
  Returns all forums related to category.
* **URL Params**  
  *Required:* `category=[string]`
  *Required:* `sort=[string]`
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 200,
    "message" : "success",
    "data" : {
        "forum" : [
            {   
                "id" : "string",
                "username": "string",
                "title" : "string",
                "question" : "string",
                "upvote" : "int"
                "total_answer" : "int",
                "created_at" : "string",
                "is_upvote" : "boolean"
            }
        ],
        "count" : "int"
    }
}
```

**GET api/v1/forum?search=**
----
  Returns all forums related to search.
* **URL Params**  
  *Required:* `search=[string]`
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 200,
    "message" : "success",
    "data" : {
        "forum" : [
            {   
                "id" : "string",
                "username": "string",
                "title" : "string",
                "question" : "string",
                "upvote" : "int"
                "total_answer" : "int",
                "created_at" : "string",
                "is_upvote" : "boolean"
            }
        ],
        "count" : "int",
        
    }
}
```

**GET api/v1/forum/:ID**
----
  Returns detail forum by ID.
* **URL Params**  
  *Required:* `ID=[string]`
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 200,
    "message" : "success",
    "data" : {
        "id" : "string"
        "username" : "string",
        "title" : "string",
        "question" : "string",
        "upvote" : "int",
        "answer" : [
            {
                "id" : "string",
                "username" : "string",
                "answer" : "answer",
                "upvote" : "int",
                "is_upvote" : "boolean",
                "created_at": "date"
            }
        ],
        "is_upvote" : "boolean",
        "created_at": "date"
    }
}
```


**POST api/v1/forum/**
----
  Create Forum.
* **URL Params**  
  *Required:* `ID=[string]`
* **Data Params**  
  ```
  {
    "title" : "string",
    "question" : "string",
    "topic" : ["string"]
  }
  ```
* **Headers**  
  Content-Type: application/json
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 201,
    "message" : "success",
    "data" : {
        "id" : "string"
        "username" : "string",
        "title" : "string",
        "question" : "string",
        "upvote" : "int",
        "answer" : [],
        "is_upvote" : "boolean",
        "created_at": "date"
    }
}
```



**POST api/v1/forum/:ID**
----
  Create answer of forum.
* **URL Params**  
  *Required:* `ID=[string]`
* **Data Params**  
  ```
  {
    "answer" : "string"
  }
  ```
* **Headers**  
  Content-Type: application/json
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 201,
    "message" : "success",
    "data" : {
        "id" : "string",
        "username" : "string"
        "answer" : "string",
        "upvote" : "int",
        "is_upvote" : "boolean",
        "created_at": "date"
    }
}
```



**POST api/v1/forum/:ID/vote**
----
  increase or decrease vote of forum.
* **URL Params**  
  *Required:* `ID=[string]`
* **Data Params**  
  ```
  {
      "is_increase" : "true"
  }
  ```
* **Headers**  
  Content-Type: application/json
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 201,
    "message" : "success",
    "data" : {
        "id" : "string"
        "username" : "string",
        "title" : "string",
        "question" : "string",
        "upvote" : "int",
        "is_upvote" : "boolean",
        "created_at": "date"
    }
}
```

**POST api/v1/forum/answer/:ID/vote**
----
  increase or decrease upvote of answer.
* **URL Params**  
  *Required:* `ID=[string]`
* **Data Params**  
  ```
  {
      "is_increase" : "true"
  }
  ```
* **Headers**  
  Content-Type: application/json
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : 201,
    "message" : "success",
    "data" : {
        "id" : "string",
        "username" : "string",
        "answer" : "answer",
        "upvote" : "int",
        "is_upvote" : "boolean",
        "created_at": "date"
    }
}
```
# PUSAT KURSUS
**GET api/v1/course**
----
  get all course
* **URL Params** \
  *optional:* `search=[string]`
* **Data Params** \
  None
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status" : "200",
    "message" : "berhasil",
    "data" : {
        "my_course" : {
            "list" : [
                {
                    "id" : "string",
                    "name" : "string",
                    "topic" : [],
                    "last_progress" : {
                        "id": 3,
                        "title": "Testing Course 1 Section 1 Lesson 1",
                        "type": "lesson",
                        "step": {
                            "id": 4,
                            "title": "Testing Course 1 Section 1 Lesson 1 Step 2"
                        },
                    "progress" : "float",
                    "img" : "string"
                }
            ],
            "count" :"int"
        },
        "course": {
            "list": [
                {
                    "id": "string",
                    "name": "string",
                    "description": "string",
                    "topic": [],
                    "img": "string",
                    "price": 0.0,
                    "reward": 0.0
                }
            ],
            "count": "int"
        }
    }
}
```

**GET api/v1/course/:ID**
----
  get all course
* **URL Params** \
  *required:* `ID=[string]`
* **Data Params** \
  None
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**
  
is_owned=False
```
{
    "status": 200,
    "message": "success",
    "data": {
        "id": 2,
        "is_owned": false,
        "name": "test",
        "about": "<p>awdawd</p>",
        "learning_point": "<p>awdaw</p>",
        "rating": 0.0,
        "total_rating": 0,
        "total_participant": 0,
        "estimate_time": "06:00:00",
        "img": "http://res.cloudinary.com/dr5j1qjsv/image/upload/v1619610821/ipxiy4eokh5kp6hv8oah.jpg",
        "price": 0.0,
        "topic": [
            "Testing"
        ],
        "section": [
            {
                "lesson": [
                    {
                        "id": 1,
                        "title": "Lesson 1"
                    }
                ],
                "quiz_section": {
                    "id": 1,
                    "title": "Coba1",
                    "description": "Coba1",
                    "quiz": [
                        {
                            "id": 3
                        },
                        {
                            "id": 4
                        }
                    ]
                }
            }
        ]
    }
}
```
is_owned = True
```
{
    "status": 200,
    "message": "success",
    "data": {
        "id": 1,
        "is_owned": true,
        "name": "Test Course",
        "about": "<p>awdawdawdawdawdawd</p>",
        "learning_point": "<p>adawdawdawdawdawdawd</p>",
        "section": [
            {
                "lesson": [
                    {
                        "id": 1,
                        "title": "Lesson 1"
                    }
                ],
                "quiz_section": {
                    "id": 1,
                    "title": "Coba1",
                    "description": "Coba1",
                    "quiz": [
                        {
                            "id": 3
                        },
                        {
                            "id": 4
                        }
                    ]
                }
            }
        ],
        "total_score": 0.0
        "last_progress": {
            "id": 3,
            "name": "Testing Course 1 Section 1 Lesson 1",
            "type": 0,
            "step": {
                "id": 4,
                "title": "Testing Course 1 Section 1 Lesson 1 Step 2"
            }
        }
    }
}
```
**POST api/v1/course/:ID/**
----
  user buy course
* **URL Params** \
  *required:* `ID=[string]`
* **Data Params** \
  None
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 201,
    "message": "success",
}
```

**GET api/v1/course/lesson/:ID/**
----
  get lesson by ID
* **URL Params** \
  *required:* `ID=[string]`
* **Data Params** \
  None
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 200,
    "message": "success",
    "data": {
        "steps": [
            {
                "id": 1,
                "title": "Coba1",
                "type": 0,
                "is_complete": true
            },
            {
                "id": 2,
                "title": "cob2",
                "type": 1,
                "is_complete": true
            }
        ]
    }
}
```

**POST api/v1/course/lesson/:ID/**
----
  Update lesson is_complete status
* **URL Params** \
  *required:* `ID=[string]`
* **Data Params** \
  None
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 200,
    "message": "success",
    "data": {
        "id": 3,
        "is_complete": true
    }
}
```

**GET api/v1/course/step/:ID/**
----
  get step by ID
* **URL Params** \
  *required:* `ID=[string]`
* **Data Params** \
  None
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 200,
    "message": "success",
    "data": {
        "id": 1,
        "title": "Coba1",
        "type": 0,
        "content_text": "<p>Tesuebtste<strong>awdawdawad<u>awdawdawd</u></strong><u>awdawdaw</u></p>",
        "content_video": "",
        "transcript": "",
        "is_complete": true,
        "time_consume": "00:20:11"
    }
}
```

**POST api/v1/course/step/:ID/**
----
  edit is_complete status by timestamps
* **URL Params** \
  *required:* `ID=[string]`
* **Data Params** \
  ```
    {
      "timestamp" : "00:21:00"
    }
  ```
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 200,
    "message": "success",
    "data": {
        "id": 2,
        "time_consume": "00:21:00",
        "is_complete": true
    }
}
```


**GET api/v1/course/quiz/:ID/**
----
  edit is_complete status by timestamps
* **URL Params** \
  *required:* `ID=[string]`
* **Data Params** \
  None
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 200,
    "message": "success",
    "data": {
        "quiz_section": [
            {
                "id": 3,
                "question": "Bla Bla Bla",
                "choice_1": {
                    "id": 1,
                    "choice": "a",
                    "is_right": false
                },
                "choice_2": {
                    "id": 2,
                    "choice": "b",
                    "is_right": false
                },
                "choice_3": {
                    "id": 3,
                    "choice": "c",
                    "is_right": true
                },
                "choice_4": {
                    "id": 4,
                    "choice": "d",
                    "is_right": false
                },
                "point": 10.0
            }
        ],
        "attempt": 2
    }
}
```

**POST api/v1/course/quiz/:ID/**
----
  edit is_complete status by timestamps
* **URL Params** \
  *required:* `ID=[string]`
* **Data Params** \
  ```
    {
        "answer" : [
            {
                "id" : 3,
                "answer" : {
                    "id" : 3
                }
            },
            {
                "id" : 4,
                "answer" : {
                    "id" : 3
                }
            }
        ]
    }
  ```
* **Headers**  
  Content-Type: application/json \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 200,
    "message": "success",
    "data": {
        "id": 1,
        "is_complete": true,
        "quiz_result": 20.0,
        "is_passed": true,
        "attempt": 2
    }
}
```


# MULAN
**POST api/v1/training**
----
  Register User
* **URL Params**  
  None
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 200,
    "message": "success",
    "data": [
        {
            "date": "2021-05-01",
            "training": [
                {
                    "id": 4,
                    "name": "test 2",
                    "img": "",
                    "start_time": "2021-05-01T09:40:08Z",
                    "end_time": "2021-05-01T18:00:00Z",
                    "location": "adaw"
                }
            ]
        },
        {
            "date": "2021-05-02",
            "training": [
                {
                    "id": 5,
                    "name": "test 2",
                    "img": "",
                    "start_time": "2021-05-02T06:00:00Z",
                    "end_time": "2021-05-02T07:00:00Z",
                    "linkUrl": "http://zoom.us"
                },
                {
                    "id": 1,
                    "name": "test",
                    "img": "",
                    "start_time": "2021-05-02T09:30:26Z",
                    "end_time": "2021-05-02T18:00:00Z"
                },
                {
                    "id": 2,
                    "name": "test",
                    "img": "",
                    "start_time": "2021-05-02T18:00:00Z",
                    "end_time": "2021-05-02T19:00:00Z"
                }
            ]
        },
        {
            "date": "2021-05-03",
            "training": [
                {
                    "id": 3,
                    "name": "test",
                    "img": "",
                    "start_time": "2021-05-03T18:00:00Z",
                    "end_time": "2021-05-03T19:00:00Z",
                    "linkUrl": "http://zoom.us"
                }
            ]
        }
    ]
}
```

**POST api/v1/training?date=**
----
  Register User
* **URL Params**  
  *required:* `date=[string, YYYY-MM-DD]` 
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 200,
    "message": "success",
    "data": [
        {
            "id": 1,
            "name": "test",
            "img": "",
            "method": null,
            "start_time": "2021-05-02T09:30:26Z",
            "end_time": "2021-05-02T18:00:00Z"
        },
        {
            "id": 2,
            "name": "test",
            "img": "",
            "method": null,
            "start_time": "2021-05-02T18:00:00Z",
            "end_time": "2021-05-02T19:00:00Z"
        },
        {
            "id": 5,
            "name": "test 2",
            "img": "",
            "method": 0,
            "start_time": "2021-05-02T06:00:00Z",
            "end_time": "2021-05-02T07:00:00Z",
            "linkUrl": "http://zoom.us"
        }
    ]
}
```

**POST api/v1/training/:ID**
----
  Register User
* **URL Params**  
   *required:* `ID=[string]`
* **Data Params**  
  None
* **Headers**  
  Content-Type: application/json  \
  Authorization : Bearer `XXX`
* **Success Response:**  
* **Code:** 200  
  **Content:**  
```
{
    "status": 200,
    "message": "success",
    "data": {
        "id": 5,
        "name": "test 2",
        "img": "",
        "organizer": "MTF",
        "about": "",
        "date": "2021-05-02",
        "start_time": "06:00:00",
        "end_time": "07:00:00",
        "method": 0,
        "linkUrl": "http://zoom.us"
    }
}
```



