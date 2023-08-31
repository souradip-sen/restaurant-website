Please review the following end points:

1. User registration endpoints:

1.1. http://127.0.0.1:8000/auth/users/
METHOD: POST
Authentication required- NO

Usecase- new user gets registered (as a customer)

Required fields in payload (Form URL Encoded):
username
password
email


1.2. http://127.0.0.1:8000/auth/token/login
METHOD: POST
Authentication required- NO

Usecase- registered users can submit their username and password to generate a token to access other endpoints

Required fields in payload (Form URL Encoded):
username
password

1.3. http://127.0.0.1:8000/auth/users/me
METHOD: GET
Authentication required- YES

Usecase- registered users can use their token to access their login credentials

1.4. http://127.0.0.1:8000/api-token-auth
METHOD: POST
Authentication required- YES
Payload:
username
password

Usecase- can use this endpoint to generate a token

2. Menu-categories endpoint:

2.1 http://127.0.0.1:8000/menu-categories
METHOD: GET
Authentication required- NO

Usecase- users can access the category list. 
Note- No POST method allowed for this endpoint. Superuser can add categories from the admin panel


3. Menu Endpoints:

3.1 http://127.0.0.1:8000/menu
METHOD: GET
3.2 http://127.0.0.1:8000/menu
METHOD: POST
Payload:
title
price
category (check the category ids from the endpoint 2.1 above)
description 
inventory

3.3 http://127.0.0.1:8000/menu/<int:pk>
METHOD: GET, PUT, PATCH, DELETE

4. Booking endpoints:

4.1 3.1 http://127.0.0.1:8000/booking
METHOD: GET
Authentication required- YES

Usecase: Users with authentication can view all bookings

3.2 http://127.0.0.1:8000/booking
METHOD: POST
Authentication required- YES

Usecase: Users with authentication can book a table
Payload:
name
guests
reservation_date (in yyyy-mm-dd)
reservation_slot (integer between 0 to 23, corresponding to hour of day)




