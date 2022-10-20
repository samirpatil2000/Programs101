# DATABASE : Student

# v1/students [GET] -->  list all the student from the DB -->
{
    "status_code": 200,
    "data": [
        {
            "id": 1,
            "name": ""
        }
    ],
    "message": "Succesfully fetch !"
}


# v1/students [POST] {"name": "sai"} -->  Create Student --> 
{"status_code": 201, "message":"Resource created successful "}


# v1/students/:id [GET] -->  Return student details with that id 

# v1/students/:id [PUT] -->  Update student details with that id 

# v1/students/:id [DELETE] -->  Delete 