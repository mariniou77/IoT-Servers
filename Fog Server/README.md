## API Endpoints

### POST /data/

Stores sensor data.

- **URL:** `/data/`
- **Method:** `POST`
- **Request Body:**

  ```json
  {
    "light_level": 150.75,
    "latitude": 37.7749,
    "longitude": -122.4194
  }
- **Response:**
  ```json
  {
    "message": "Data received successfully",
    "data": {
      "light_level": 150.75,
      "latitude": 37.7749,
      "longitude": -122.4194
    }
  }

### GET /data/

Retrieves all stored sensor data.

- **URL:** `/data/`
- **Method:** `GET`
- **Response:**

  ```json
  [
    {
      "id": 1,
      "light_level": 150.75,
      "latitude": 37.7749,
      "longitude": -122.4194
    }
  ]