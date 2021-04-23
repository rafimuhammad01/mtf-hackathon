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
        "article_section" : [
            {
                "id" : "string",
                "title" : "string",
                "article" : [
                    {
                        "id" : "string",
                        "title" : "string",
                        "description" : "string"
                    }
                ]
            }
        ]
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
                "description" : "string"
            }
        ]
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
        "judul" : "string",
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
                "created_at" : "string"
            }
        ],
        "count" : "int"
        "is_upvote" : "boolean"
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
            }
        ],
        "count" : "int",
        "is_upvote" : "boolean"
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
                "is_upvote" : "boolean"
            }
        ],
        "is_upvote" : "boolean"
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
        "is_upvote" : "boolean"
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
        "is_upvote" : "boolean"
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
        "is_upvote" : "boolean"
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
        "is_upvote" : "boolean"
    }
}
```
