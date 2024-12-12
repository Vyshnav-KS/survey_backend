# FastAPI Survey Application Documentation

## Overview

This FastAPI application allows users to create surveys, add responses, and retrieve responses. The application uses an SQLite database to store survey data.

## Features

- **Create Survey**: Allows users to create a survey with multiple questions.
- **Add Response**: Allows users to submit responses to surveys.
- **Get Responses**: Allows users to retrieve the responses to a specific survey.

## Setup

### 1. Create a Virtual Environment

To create and activate a virtual environment, run the following commands:

```bash
python -m venv venv
```
Activate the virtual environment:

Windows:
```bash
venv\Scripts\activate
```
Mac/Linux:
```bash
source venv/bin/activate
```
### 2. Install Dependencies
Once the virtual environment is activated, install the required dependencies using:

```bash
pip install -r requirements.txt
```
### 3. Configure Database URL
In the root directory of the project, create a .env file (or directly modify the database file for testing) and add the following line to configure the SQLite database:

env
```
DB_URL=sqlite:///./survey.db
```
Alternatively, you can directly modify the database URL in the application code for testing purposes.

### 4. Start the Server
Run the following command to start the FastAPI server:

```bash
uvicorn survey.main:app --reload
```
The server will start running on http://127.0.0.1:8000/.

Swagger: http://127.0.0.1:8000/docs

### 5. Test the API
You can test the API using Swagger documentation by navigating to:

```url
http://127.0.0.1:8000/docs
```
Swagger UI will provide interactive documentation where you can test creating surveys, adding responses, and retrieving responses