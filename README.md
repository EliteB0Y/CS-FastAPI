# CS-FastAPI

This is a simple FastAPI application that utilizes the Ultralytics YOLO model to solve captchas from images provided through URLs.

## Prerequisites

- Python 3.7 or later
- Install dependencies using `pip install -r requirements.txt`

## Getting Started

1. To run the application:

    ```bash
    python main.py
    ```

    The API will be accessible at http://127.0.0.1:8000.

## API Endpoints

### 1. Health Check

- **Endpoint**: `/`
- **Method**: `GET`
- **Description**: Returns the status of the API.
- **Example**: `http://127.0.0.1:8000/`

### 2. Solve Captcha

- **Endpoint**: `/solve/{url:path}`
- **Method**: `GET`
- **Parameters**:
  - `url`: The URL of the image containing the captcha.
- **Description**: Solves the captcha in the provided image and returns the result.
- **Example**: `http://127.0.0.1:8000/solve/https://example.com/captcha.png`

## Error Handling

If there is an issue with the captcha solving process or any other error, the API will return a JSON response with an error message.

```json
{
  "answer": "Error: Unsupported image type."
}
