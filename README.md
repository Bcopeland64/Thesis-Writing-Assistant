# ThesisAI - Research Assistant Web Application

## Overview

ThesisAI is a web application designed to assist users in their research and thesis writing process. This initial version focuses on providing core functionalities such as user authentication and literature management, including searching for academic papers and summarizing them using the Groq AI services. The goal is to streamline the research workflow and provide intelligent assistance to academic users.

## Project Structure

The project is organized into two main directories:

*   `backend/`: Contains the FastAPI application that serves as the API for the project. It handles business logic, database interactions, and communication with external AI services.
*   `frontend/`: Contains the React (TypeScript) single-page application that provides the user interface.

## Prerequisites

Before you begin, ensure you have the following installed:

*   **Python:** Version 3.8 or higher.
*   **Node.js and npm:** Node.js version 16.x or higher, npm version 8.x or higher.
    *   *Note:* While the project might run on other versions, these are recommended. The environment has shown some warnings with Node v18 and react-router-dom v7.6.1 which expects Node >=20.0.0.
*   **Database:**
    *   The backend defaults to using **SQLite**. No separate database server installation is required for the default setup.
    *   **PostgreSQL** can be configured as an alternative (see Backend Setup).

## Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create and activate a virtual environment:**
    *   On macOS and Linux:
        ```bash
        python3 -m venv venv
        source venv/bin/activate
        ```
    *   On Windows:
        ```bash
        python -m venv venv
        venv\\Scripts\\activate
        ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

4.  **Environment Variables:**
    *   The backend requires certain environment variables to function correctly. These are managed using a `.env` file in the `backend` directory.
    *   A sample configuration is provided in `backend/.env.example`. Copy this file to `.env` and update it with your specific values:
        ```bash
        cp .env.example .env
        ```
    *   **Key variables to configure in `.env`:**
        *   `GROQ_API_KEY`: Your API key for Groq services. This is essential for literature search and summarization features.
        *   `SECRET_KEY`: A secret key for JWT token generation. The example file provides a default, but it's recommended to change this to a strong, unique key.
        *   `SQLALCHEMY_DATABASE_URL`:
            *   Defaults to `sqlite:///./test.db` for SQLite, which will create a `test.db` file in the `backend` directory.
            *   To use PostgreSQL, you would change this to a PostgreSQL connection string, e.g., `postgresql://user:password@host:port/database_name`. Ensure `psycopg2-binary` (already in `requirements.txt`) is used.

5.  **Running the backend:**
    *   From within the `backend` directory (with the virtual environment activated):
        ```bash
        uvicorn app.main:app --reload --port 8000
        ```
    *   The API server will typically be available at `http://localhost:8000`.

## Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install dependencies:**
    *   If you encounter issues with `npm install` related to `node_modules/.bin` or `npx` not finding executables (as observed during development of this project), ensure your Node.js and npm installation is correct and that your `PATH` is configured properly.
    ```bash
    npm install
    ```

3.  **Running the frontend:**
    ```bash
    npm start
    ```
    *   This command usually starts the React development server on `http://localhost:3000`.
    *   The frontend application is configured to proxy API requests to the backend server (running at `http://localhost:8000` by default) to avoid CORS issues during development. This is set up in `frontend/package.json`.

## Running Tests

*   **Backend Tests:**
    *   Ensure you are in the `backend` directory and your virtual environment is activated.
    *   The tests use a separate SQLite database (`test.db`) that is created and destroyed during the test session.
    ```bash
    pytest
    ```

*   **Frontend Tests:**
    *   Ensure you are in the `frontend` directory.
    ```bash
    npm test
    ```

## API Access

*   The backend API is versioned and accessible under the `/api/v1` prefix (e.g., `/api/v1/auth/login`).
*   Most API endpoints, particularly those related to literature services, require JWT authentication. The token must be included in the `Authorization` header as a Bearer token.

## Next Steps / Future Work

This project provides a foundational implementation of an AI-assisted research tool. Future enhancements could include:
*   Expanding the range of AI-powered assistance features (e.g., writing assistance, reference management).
*   Support for more data sources and AI models.
*   User interface improvements and more detailed user feedback.
*   Full PostgreSQL integration and production deployment configurations.
*   More comprehensive error handling and logging.

---
*This README was generated based on the project state as of the last update.*
