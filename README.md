# Flask API with MongoDB

This repository contains a Flask API that serves as a backend service for interacting with MongoDB. It provides various routes for performing CRUD operations on MongoDB collections.

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

### 1. Get News

- **URL**: `/api/news`
- **Method**: `GET`
- **Description**: Retrieve news data from the MongoDB `news` collection.
- **Query Parameters**:
  - `i` (Optional): Number of items to retrieve.
  - `p` (Optional): Page number for pagination.
- **Response**: JSON array of news items.

### 2. Get News by ID

- **URL**: `/api/news/<id>`
- **Method**: `GET`
- **Description**: Retrieve a specific news item by its ID from the MongoDB `news` collection.
- **Response**: JSON object representing the news item content.

### 3. Get Offers

- **URL**: `/api/offers`
- **Method**: `GET`
- **Description**: Retrieve offers data from the MongoDB `offers` collection.
- **Response**: JSON array of offers items.

### 4. Get Offer by ID

- **URL**: `/api/offers/<id>`
- **Method**: `GET`
- **Description**: Retrieve a specific offer item by its ID from the MongoDB `offers` collection.
- **Response**: JSON object representing the offer item content.

### 5. Login to dashboard

- **URL**: `/api/authenticate`
- **Method**: `POST`
- **Description**: Verifies if the provided `authKey` exists in the MongoDB `users` collection and returns the appropriate status.
- **Response**: JSON object containing an error message and additional status code to indicate the user's permission to access the page.

    - **Status Codes**:
        - `200`: Access granted.
        - `401`: Access denied.
        - `500`: Internal Server Error.

### 6. Add news to database

- **URL**: `/api/add/news`
- **Method**: `POST`
- **Description**: Validates the provided authentication key `authKey` against entries in the MongoDB `users` collection. If the key matches an entry with a `superadmin` or `admin` role, it proceeds with validating and adding news data. Otherwise, it returns an authentication failure error message.
- **Response**: JSON object containing an error message and status code.
    - **Status Codes**:
    - `200`: Operation Successful.
    - `400`: Validation not passed.
    - `401`: Access denied.
    - `500`: Internal Server Error.


## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.