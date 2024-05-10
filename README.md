# Flask API with MongoDB

This repository contains a Flask API that serves as a backend service for interacting with MongoDB. It provides various routes for performing CRUD operations on MongoDB collections.

## React App for this project
Find the corresponding React frontend app [here](https://github.com/M-Itrych/Mi-Ka_Frontend).

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

## Endpoints

### News

#### 1. Get News

- **URL**: `/api/news`
- **Method**: `GET`
- **Description**: Retrieve news articles from the database with support for pagination through query parameters `i` (items per page) and `p` (page number).
- **Query Parameters**:
  - `i` (Optional): Number of items to retrieve.
  - `p` (Optional): Page number for pagination.
- **Response**:
  - `200`: Successful retrieval of news articles.
  - `500`: Internal Server Error.

#### 2. Get News by ID

- **URL**: `/api/news/<string:id>`
- **Method**: `GET`
- **Description**: Retrieve a single news article from the database based on its unique identifier `id`.
- **Path Parameter**:
  - `id`: Unique identifier of the news article to retrieve.
- **Response**:
  - `200`: Successful retrieval of the news article.
  - `404`: News article not found.
  - `500`: Internal Server Error.

#### 3. Get News Count

- **URL**: `/api/news_count`
- **Method**: `GET`
- **Description**: Retrieve the count of news articles from the MongoDB `news` collection.
- **Response**:
  - `200`: Successful retrieval of the count of news articles.
  - `500`: Internal Server Error.

### Offers

#### 1. Get Offers

- **URL**: `/api/offers`
- **Method**: `GET`
- **Description**: Retrieve offers data from the MongoDB `offers` collection.
- **Response**: 
  - `200`: Successful retrieval of offers.
  - `500`: Internal Server Error.

#### 2. Get Offer by ID

- **URL**: `/api/offers/<id>`
- **Method**: `GET`
- **Description**: Retrieve a single offer from the database based on its unique identifier `id`.
- **Path Parameter**:
  - `id`: Unique identifier of the offer to retrieve.
- **Response**: 
  - `200`: Successful retrieval of the offer.
  - `404`: Offer not found.
  - `500`: Internal Server Error.

### Admin Dashboard

#### 1. Login to Dashboard

- **URL**: `/api/authenticate`
- **Method**: `POST`
- **Description**: Endpoint for user authentication.
- **Request**: 
  - Authorization credentials in the request header.
- **Response**:
    - **Status Codes**:
        - `200`: Authentication successful.
        - `401`: Authentication credentials missing or invalid.
        - `500`: Internal Server Error.

#### 2. Add News to Database

- **URL**: `/api/add/news`
- **Method**: `POST`
- **Description**: Add a new news article to the database. Requires authentication.
- **Request**:
  - Authorization credentials in the request header.
  - JSON payload containing news article details (`title`, `description`, `url`, `alt`, `text`).
- **Response**:
  - `200`: News article successfully added.
  - `400`: Invalid or incomplete news article data.
  - `401`: Authentication credentials missing or invalid.
  - `500`: Internal Server Error.

#### 3. Remove News from Database

- **URL**: `/api/delete/news`
- **Method**: `POST`
- **Description**: Delete news articles from the database. Requires authentication.
- **Request**:
  - Authorization credentials in the request header.
  - JSON payload containing the ID of the news article to be deleted.
- **Response**:
  - `200`: News article successfully deleted.
  - `401`: Authentication credentials missing or invalid.
  - `500`: Internal Server Error.

#### 4. Update News in Database

- **URL**: `/api/update/news`
- **Method**: `POST`
- **Description**: Update existing news articles in the database. Requires authentication.
- **Request Parameters**: 
  - `id`: Unique identifier of the news article to be updated.
  - `title` (optional): Updated title of the news article.
  - `description` (optional): Updated description of the news article.
  - `url` (optional): Updated URL of the news article image. 
  - `alt` (optional): Updated alt text for the news article image. 
  - `text` (optional): Updated text content of the news article.
- **Response**:
  - `200`: News article successfully updated.
  - `400`: Missing or invalid request parameters.
  - `401`: Authentication credentials missing or invalid.
  - `404`: News article not found.
  - `500`: Internal Server Error.

### Contact Form

#### 1. Send Email from Form

- **Endpoint**: `/api/send/email`
- **HTTP Method**: `POST`
- **Description**: Send emails, typically for contact form submissions.
- **Request**:
  - JSON payload containing fields: `email`, `phone`, `text`.
- **Response**:
  - `200`: Email successfully sent.
  - `400`: Incomplete or invalid request payload.
  - `500`: Internal Server Error.

## Utils

- **connect_to_mongodb()**: Connects to a MongoDB database hosted on localhost at port 27017 and returns the client and the database object. 
- **close_mongodb_connection(client)**: Closes the MongoDB client connection. 
- **serialize_id(data)**: Converts the ObjectId of MongoDB documents to string format for easier serialization, either for a single document or for a list of documents. 
- **get_date_string()**: Retrieves the current date and time formatted in Polish locale, typically for use in adding timestamps to data. 
- **validate_news(data)**: Validates the fields of a news article. It checks for required fields (`title`, `desc`, `img`, `text`) and validates the image URL format if provided. 
- **validate_email(email)**: Validates the format of an email address using a regular expression. 
- **validate_phone(phone)**: Validates the format of a phone number, ensuring it consists of exactly 9 digits.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
