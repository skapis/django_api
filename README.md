# Django API

This repository contains simple API in Django REST Framework. To use API, follow the instructions in API Documentation below. You can also use the postman collection, where are all requests for this project.

# API Documentation
In the project are two models, Users and Purchases. Each User can have zero or more purchases. Each Purchase must have at least one user. 

**Authentication**<br>
To use any user endpoint you have to be authenticated. This API uses authentication by token, which belongs to the user. You can create an authorization token for each user by 
```
./manage.py drf_create_token <username>
```
or you can use existing one 
```
Token d10aee56408b1ef49c399be3e9cb180296637670
```

## Users

### User list

To get list of all users

```http
GET /users/list
```
**Response** 
```
{
    "users": {
        "total": 4,
        "items": [
            {
                "id": 1,
                "username": "admin",
                "first_name": "admin",
                "last_name": "admin",
                "email": "testappemail9@gmail.com",
                "is_staff": true,
                "is_superuser": true,
                "date_joined": "2022-10-29T04:34:21Z"
            },
            ....
```
### User detail

```http
GET /users/list?user=1&type=full
```

**Parameters**
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `user` | `int` | **Required**. ID of User|
| `type` | `string` | [**Optional**] If type=full you get user with all his purchases|

**Response**
```
{
    "id": 2,
    "username": "TestUser",
    "first_name": "Test",
    "last_name": "User",
    "email": "testappemail9+1@gmail.com",
    "is_staff": false,
    "is_superuser": false,
    "date_joined": "2022-10-30T05:14:05Z",
    "purchases": [
        {
            "id": 2,
            "purchase_id": "2f60490e-6d76-47f0-9c51-2aebe5b6f6d0",
            "product": "Iphone 13",
            "amount": 2,
            "currency": "CZK",
            "unit_price": 25000,
            "total_price": 50000,
            "purchase_date": "2022-10-29",
            "payment_method": "Cash",
            "shipping_method": "In the store",
            "email": "testappemail9+1@gmail.com",
            "country": "Czech Republic",
            "city": "Velké Svatoňovice",
            "street": null,
            "street_number": "25",
            "zipcode": "54234",
            "user": 2
        },
        {
            "id": 6,
            "purchase_id": "e3b6d14c-c547-4dab-931f-efed89545b0f",
            "product": "Samsung Galaxy",
            "amount": 2,
            "currency": "USD",
            "unit_price": 500,
            "total_price": 1000,
            "purchase_date": "2018-02-02",
            "payment_method": "Cash",
            "shipping_method": "In the store",
            "email": "testappemail9+1@gmail.com",
            "country": "Czech Republic",
            "city": "Brno",
            "street": "Brněnská",
            "street_number": "256",
            "zipcode": "800 00",
            "user": 2
        }
    ]
}
```

### User Purchases
To get all users and their purchases

```http
GET /users/purchases
```

**Response**
```
{
    "users": {
        "total": 4,
        "items": [
            {
                "id": 1,
                "username": "admin",
                "first_name": "admin",
                "last_name": "admin",
                "email": "testappemail9@gmail.com",
                "is_staff": true,
                "is_superuser": true,
                "date_joined": "2022-10-29T04:34:21Z",
                "purchases": [
                    {
                        "id": 1,
                        "purchase_id": "c44838d9-7f31-41ad-8df4-f7770d1fd7d1",
                        "product": "Iphone 12",
                        "amount": 2,
                        "currency": "CZK",
                        "unit_price": 20000,
                        "total_price": 40000,
                        "purchase_date": "2022-10-29",
                        "payment_method": "Credit Card",
                        "shipping_method": "In the store",
                        "email": "testappemail9@gmail.com",
                        "country": "Czech Republic",
                        "city": "Úpice",
                        "street": "Upická",
                        "street_number": "123",
                        "zipcode": "54232",
                        "user": 1
                    },
                    {
                        "id": 3,
                        "purchase_id": "6e001ea3-03b6-490e-806f-bf0b8f6f8fa5",
                        "product": "Iphone 14",
                        "amount": 2,
                        "currency": "CZK",
                        "unit_price": 45000,
                        "total_price": 90000,
                        "purchase_date": "2022-10-29",
                        "payment_method": "Cash",
                        "shipping_method": "In the store",
                        "email": "testappemail9@gmail.com",
                        "country": "Czech Republic",
                        "city": "Broumov",
                        "street": "Broumovská",
                        "street_number": "789",
                        "zipcode": "48978",
                        "user": 1
                    },
                    {
                        "id": 22,
                        "purchase_id": "22fff9a5-3212-4435-b54a-c05688d52f12",
                        "product": "Lenovo Thinkpad",
                        "amount": 1,
                        "currency": "EUR",
                        "unit_price": 1000,
                        "total_price": 1000,
                        "purchase_date": "2022-10-30",
                        "payment_method": "Cash",
                        "shipping_method": "In the store",
                        "email": "testappemail9@gmail.com",
                        "country": "Czechia",
                        "city": "Malé Svatoňovice",
                        "street": null,
                        "street_number": "30",
                        "zipcode": "54232",
                        "user": 1
                    }
                ]
            },
            {
                "id": 2,
                "username": "TestUser",
                "first_name": "Test",
                "last_name": "User",
                "email": "testappemail9+1@gmail.com",
                "is_staff": false,
                "is_superuser": false,
                "date_joined": "2022-10-30T05:14:05Z",
                "purchases": [
                    {
                        "id": 2,
                        "purchase_id": "2f60490e-6d76-47f0-9c51-2aebe5b6f6d0",
                        "product": "Iphone 13",
                        "amount": 2,
                        "currency": "CZK",
                        "unit_price": 25000,
                        "total_price": 50000,
                        "purchase_date": "2022-10-29",
                        "payment_method": "Cash",
                        "shipping_method": "In the store",
                        "email": "testappemail9+1@gmail.com",
                        "country": "Czech Republic",
                        "city": "Velké Svatoňovice",
                        "street": null,
                        "street_number": "25",
                        "zipcode": "54234",
                        "user": 2
                    }
                    .....
```

### Create New User
You can create a new user by post request with user data in body

```http
POST /users/list
```

**Body**

```
{
    "username": "APITest",
    "password": "Django12345",
    "email": "testappemail9+apitest@gmail.com",
    "first_name": "API",
    "last_name": "Test"
}
```

## Purchases

### Purchase list
To get list of all purchases in the database

```http
GET /purchases/list?currency=CZK&from=2022-01-01&to=2022-05-05
```
**Parameters**
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `currency` | `string` | [**Optional**] currency code of purchase|
| `from` | `date` | [**Optional**] Filter only purchase which is greater than or equal date|
| `to` | `date` | [**Optional**] Filter only purchase which is less than or equal date|
| `amount_from` | `int` | [**Optional**] Filter only purchase which is greater than or equal amount|
| `amount_to` | `int` | [**Optional**] Filter only purchase which is less than or equal amount|

Note: parameters `from`, `to` and `amount_from`, `amount_to` must be used together

**Response**
```
{
    "purchases": {
        "total": 3,
        "items": [
            {
                "id": 1,
                "purchase_id": "c44838d9-7f31-41ad-8df4-f7770d1fd7d1",
                "product": "Iphone 12",
                "amount": 2,
                "currency": "CZK",
                "unit_price": 20000,
                "total_price": 40000,
                "purchase_date": "2022-10-29",
                "payment_method": "Credit Card",
                "shipping_method": "In the store",
                "email": "testappemail9@gmail.com",
                "country": "Czech Republic",
                "city": "Úpice",
                "street": "Upická",
                "street_number": "123",
                "zipcode": "54232",
                "user": 1
            },
            {
                "id": 2,
                "purchase_id": "2f60490e-6d76-47f0-9c51-2aebe5b6f6d0",
                "product": "Iphone 13",
                "amount": 2,
                "currency": "CZK",
                "unit_price": 25000,
                "total_price": 50000,
                "purchase_date": "2022-10-29",
                "payment_method": "Cash",
                "shipping_method": "In the store",
                "email": "testappemail9+1@gmail.com",
                "country": "Czech Republic",
                "city": "Velké Svatoňovice",
                "street": null,
                "street_number": "25",
                "zipcode": "54234",
                "user": 2
            },
            {
                "id": 3,
                "purchase_id": "6e001ea3-03b6-490e-806f-bf0b8f6f8fa5",
                "product": "Iphone 14",
                "amount": 2,
                "currency": "CZK",
                "unit_price": 45000,
                "total_price": 90000,
                "purchase_date": "2022-10-29",
                "payment_method": "Cash",
                "shipping_method": "In the store",
                "email": "testappemail9@gmail.com",
                "country": "Czech Republic",
                "city": "Broumov",
                "street": "Broumovská",
                "street_number": "789",
                "zipcode": "48978",
                "user": 1
            }
        ]
    }
}
```

### Purchase detail
To get information of the selected purchase

```http
GET /purchases/detail?purchase=c44838d9-7f31-41ad-8df4-f7770d1fd7d1
```
**Parameters**
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `purchase` | `uuid` | **Required** purchase id|


### Update Purchase
To update or change purchase data

``` http
PUT /purchases/detail?purchase=2f60490e-6d76-47f0-9c51-2aebe5b6f6d0
```

**Parameters**
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `purchase` | `uuid` | **Required** purchase id|


**Body**

```
{
    "purchase_id": "2f60490e-6d76-47f0-9c51-2aebe5b6f6d0",
    "product": "Iphone 13",
    "amount": 2,
    "currency": "CZK",
    "unit_price": 25000,
    "total_price": 50000,
    "purchase_date": "2022-10-29",
    "payment_method": "Cash",
    "shipping_method": "In the store",
    "email": "testappemail9+1@gmail.com",
    "country": "Czech Republic",
    "city": "Velké Svatoňovice",
    "street": null,
    "street_number": "25",
    "zipcode": "54234"
}
```

### Delete Purchase
To delete purchase

``` http
DELETE /purchases/detail?purchase=2f60490e-6d76-47f0-9c51-2aebe5b6f6d0
```

**Parameters**
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `purchase` | `uuid` | **Required** purchase id|


### Create New Purchase
To create new purchase you have to call POST request with user id as a parameter and purchase data in body, because each purchase must be assigned to user

```http
POST /purchases/list?user=3
```

**Parameters**
| Parameter | Type | Description |
| :--- | :--- | :--- |
| `user` | `int` | **Required** user id|

**Body**

```
{
    "product": "Iphone 13",
    "amount": 2,
    "currency": "CZK",
    "unit_price": 25000,
    "total_price": 50000,
    "purchase_date": "2022-10-29",
    "payment_method": "Cash",
    "shipping_method": "In the store",
    "email": "testappemail9+1@gmail.com",
    "country": "Czech Republic",
    "city": "Velké Svatoňovice",
    "street": null,
    "street_number": "25",
    "zipcode": "54234"
}
```



