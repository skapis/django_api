# Django API

This repository contains simple API in Django REST Framework. To use API, follow instructions in API Documentation below. You can also use postman collection, where are all request to this project.

# API Documentation
In project are two models, Users and Purchases. Each User can have zero or more purchases. Each Purchase must have at least one user. 

**Flow**
1. Create or Get User information
2. Create new Purchase for selected User
3. Get User detail (including all his purchases)

## Users
**API KEY**<br>
You can create authorization token for each user by 
```
./manage.py drf_create_token <username>
```
or you can use existing one 
```
d10aee56408b1ef49c399be3e9cb180296637670
```


