# Flask API with MongoDB

This repository contains a Flask API that serves as a backend service for interacting with MongoDB. It provides various routes for performing CRUD operations on MongoDB collections.

## React App for this project
https://github.com/M-Itrych/Mi-Ka_Frontend

## Setup

1. Clone the repository:

    ```bash
   git clone https://github.com/M-Itrych/databaseApi-mika
   ```

2. Install dependencies:

    ```bash
   pip install -r requirements.txt
   ```

3. Run the Flask application:

    ```bash
   python app.py
   ```
   
The API will be running by default at `http://localhost:5000`

# Endpoints

## News

### 1. Get News

- **URL**: `/api/news`
- **Method**: `GET`
- **Description**: This endpoint retrieves news articles from the database. It supports pagination through query parameters `i` (items per page) and `p` (page number).
- **Query Parameters**:
  - `i` (Optional): Number of items to retrieve.
  - `p` (Optional): Page number for pagination.
- **Response**:
  - `200`: The news articles are successfully retrieved, a JSON response containing the news data is returned.
  - `500`: Internal Server Error.

### 2. Get News by ID

- **URL**: `/api/news/<string:id>`
- **Method**: `GET`
- **Description**: This endpoint retrieves a single news article from the database based on its unique identifier `id`.
- **Path Parameter**
  - `id`: The unique identifier of the news article to retrieve.
- **Response**:
  - `200`: The news article is found, a JSON response containing the news data is returned.
  - `404`: The specified news article is not found in the database.
  - `500`: Internal Server Error.

## Offers

### 1. Get Offers

- **URL**: `/api/offers`
- **Method**: `GET`
- **Description**: Retrieve offers data from the MongoDB `offers` collection.
- **Response**: 
  - `200`: The offers are successfully retrieved, a JSON response containing the offer data is returned.
  - `500`: Internal Server Error.

### 2. Get Offer by ID

- **URL**: `/api/offers/<id>`
- **Method**: `GET`
- **Description**: This endpoint retrieves a single offer from the database based on its unique identifier `id`.
- **Path Parameter**
  - `id`: The unique identifier of the offer to retrieve.
- **Response**: 
  - `200`: The offer is found, a JSON response containing the offer data is returned.
  - `404`: The specified offer is not found in the database.
  - `500`: Internal Server Error.

## Admin Dashborad

### 1. Login to dashboard

- **URL**: `/api/authenticate`
- **Method**: `POST`
- **Description**: This endpoint is used for user authentication. It checks if the provided authentication credentials are valid.
- **Request**: 
  - Authorization credentials should be provided in the request header.
- **Response**:
    - **Status Codes**:
        - `200`: Authentication is successful.
        - `401`: Authentication credentials are missing or invalid.
        - `500`: Internal Server Error.

### 2. Add news to database

- **URL**: `/api/add/news`
- **Method**: `POST`
- **Description**: This endpoint is used to add a new news article to the database. It requires authentication, and only users with the roles 'superadmin' or 'admin' are authorized to access it.
- **Request**:
  - Authorization credentials should be provided in the request header.
  - JSON payload containing the details of the news article to be added:
    - `title`: The title of the news article
    - `desctiption`: A brief description of the news article.
    - `url`: URL of the news article image.
    - `alt`: Alt text for the news article image.
    - `text`: The main text content of the news article.
- **Response**:
  - `200`: The news article is successfully added.
  - `400`: Provided news article data is invalid or incomplete.
  - `401`: Authentication credentials are missing or invalid.
  - `500`: Internal Server Error.
  

### 3. Remove news from database

- **URL**: `/api/add/news`
- **Method**: `POST`
- **Description**: This endpoint is designed to delete news articles from the database. It requires authentication, and only users with the role of 'superadmin' are authorized to access it.
- **Request**:
  - Authorization credentials should be provided in the request header.
  - JSON payload containing the ID of the news article to be deleted:
    - `id`: The unique identifier of the news article to be deleted.
- **Response**:
  - `200`: The news article is successfully deleted.
  - `401`: Authentication credentials are missing or invalid.
  - `500`: Internal Server Error.

### 4. Update news in database

- **URL**: `/api/update/news`
- **Method**: `POST`
- **Description**: This endpoint is used to update existing news articles in the database. Authentication is required, and only users with the roles 'superadmin' or 'admin' are authorized to access it.
- **Request Parameters**: 
  - `id`: The unique identifier of the news article to be updated.
  - `title` (optional): The updated title of the news article.
  - `description` (optional): The updated description of the news article.
  - `url` (optional): The updated URL of the news article image. 
  - `alt` (optional): The updated alt text for the news article image. 
  - `text` (optional): The updated text content of the news article.
- **Response**:
  - `200`: The news entry is successfully deleted.
  - `400`: The news ID is not provided in the request or any required fields are missing or invalid.
  - `401`: Authentication credentials are missing or invalid.
  - `404`: The specified news article is not found in the database.
  - `500`: Internal Server Error.

## Contact Form

### 1. Send Email from Form

- **Endpoint**: `/api/send/email`
- **HTTP Method**: `POST`
- **Description**: This endpoint is used for sending emails, typically for contact form submissions.
- **Request**:
  - JSON payload containing the following fields:
    - `email`: The email address of the sender. 
    - `phone`: The phone number of the sender. 
    - `text`: The message content.
- **Response**:
  - `200`: The email is successfully sent.
  - `400`: The request payload is incomplete or contains invalid data.
  - `500`: Internal Server Error.

## Utils

- **connect_to_mongodb()**: Connects to a MongoDB database hosted on localhost at port 27017 and returns the client and the database object. 
- **close_mongodb_connection(client)**: Closes the MongoDB client connection. 
- **serialize_id(data)**: Converts the ObjectId of MongoDB documents to string format for easier serialization, either for a single document or for a list of documents. 
- **get_date_string()**: Retrieves the current date and time formatted in Polish locale, typically for use in adding timestamps to data. 
- **validate_news(data)**: Validates the fields of a news article. It checks for required fields (title, desc, img, text) and validates the image URL format if provided. 
- **validate_email(email)**: Validates the format of an email address using a regular expression. 
- **validate_phone(phone)**: Validates the format of a phone number, ensuring it consists of exactly 9 digits.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.