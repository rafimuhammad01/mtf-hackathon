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
