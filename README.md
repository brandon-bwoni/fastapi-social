![fast-social](https://github.com/user-attachments/assets/559b921b-a209-48a3-8276-b099bbf1ec84)
# Social App API Documentation

## 1. Project Overview

### Title
Social App API

### Description
This API, built using FastAPI, provides a backend solution for social applications with full CRUD (Create, Read, Update, Delete) functionality. It is designed to handle user accounts, posts, comments, likes, and other common features found in social media platforms. The API is fully tested, adheres to modern development practices, and is designed with scalability and maintainability in mind. It is ready for deployment on platforms like Heroku, Docker, and can integrate with CI/CD pipelines using Git.

---

## 2. Features

### Core Features
1. **User Management**
   - User registration and authentication (JWT-based authentication).
   - Profile management (update profile details).

2. **Post Management**
   - Create, read, update, and delete posts.
   - Retrieve posts by user or globally.

3. **Comments**
   - Add, read, edit, and delete comments on posts.

4. **Likes**
   - Like and unlike posts and comments.
   - Retrieve the number of likes for a post or comment.

5. **Search**
   - Search functionality for users and posts.

6. **Testing**
   - Fully tested with unit and integration tests using `pytest`.

---

## 3. Technologies Used

### Backend
- **FastAPI**: Framework for building APIs.
- **SQLAlchemy**: ORM for database interactions.
- **SQLite** (development) / **PostgreSQL** (production): Database for storing data.
- **Pytest**: For testing.

### Deployment
- **Docker**: For containerization.
- **Heroku**: For hosting the API.
- **Git Pipelines**: For setting up CI/CD pipelines.

### Other Tools
- **JWT (JSON Web Tokens)**: For secure user authentication.
- **Pydantic**: For data validation and serialization.

---

## 4. Installation and Setup

### Prerequisites
- Python 3.9+
- Docker (if containerizing the app)
- Git
- Heroku CLI (for Heroku deployment)

### Steps to Set Up Locally

1. **Clone the Repository:**
   ```bash
   git clone <repository-url>
   cd social-app-api
   ```

2. **Create a Virtual Environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Windows: venv\Scripts\activate
   ```

3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set Up Environment Variables:**
   Create a `.env` file in the root directory and define the following:
   ```env
   DATABASE_URL=<database-connection-string>
   SECRET_KEY=<your-secret-key>
   ```

5. **Run Database Migrations:**
   ```bash
   alembic upgrade head
   ```

6. **Run the Application:**
   ```bash
   uvicorn main:app --reload
   ```
   The API will be accessible at `http://127.0.0.1:8000`.

### Running Tests
```bash
pytest
```

---

## 5. Deployment

### Heroku Deployment
1. **Login to Heroku CLI:**
   ```bash
   heroku login
   ```

2. **Create a Heroku App:**
   ```bash
   heroku create <app-name>
   ```

3. **Set Up Heroku Postgres Add-on:**
   ```bash
   heroku addons:create heroku-postgresql:hobby-dev
   ```

4. **Push the Code to Heroku:**
   ```bash
   git push heroku main
   ```

5. **Run Migrations on Heroku:**
   ```bash
   heroku run alembic upgrade head
   ```

### Docker Deployment
1. **Build Docker Image:**
   ```bash
   docker build -t social-app-api .
   ```

2. **Run Docker Container:**
   ```bash
   docker run -p 8000:8000 social-app-api
   ```

### CI/CD with Git Pipelines
1. **Set Up GitHub Actions Workflow:**
   Create a `.github/workflows/ci-cd.yml` file with the following:
   ```yaml
   name: CI/CD Pipeline

   on:
     push:
       branches:
         - main

   jobs:
     build-and-test:
       runs-on: ubuntu-latest

       steps:
         - name: Checkout code
           uses: actions/checkout@v3

         - name: Set up Python
           uses: actions/setup-python@v4
           with:
             python-version: '3.9'

         - name: Install dependencies
           run: |
             python -m pip install --upgrade pip
             pip install -r requirements.txt

         - name: Run tests
           run: pytest

     deploy:
       needs: build-and-test
       runs-on: ubuntu-latest

       steps:
         - name: Deploy to Heroku
           run: |
             heroku container:login
             heroku container:push web --app <your-app-name>
             heroku container:release web --app <your-app-name>
   ```

---

## 6. API Endpoints

### Authentication
- **POST /auth/register**: Register a new user.
- **POST /auth/login**: Authenticate and obtain a JWT token.

### Users
- **GET /users/{id}**: Get user details.
- **PUT /users/{id}**: Update user profile.
- **DELETE /users/{id}**: Delete a user account.

### Posts
- **POST /posts/**: Create a new post.
- **GET /posts/**: Retrieve all posts.
- **GET /posts/{id}**: Get a specific post.
- **PUT /posts/{id}**: Update a post.
- **DELETE /posts/{id}**: Delete a post.

### Comments
- **POST /comments/**: Add a comment to a post.
- **GET /comments/{post_id}**: Retrieve all comments for a post.
- **PUT /comments/{id}**: Update a comment.
- **DELETE /comments/{id}**: Delete a comment.

### Likes
- **POST /likes/**: Like a post or comment.
- **DELETE /likes/{id}**: Remove a like.

---

## 7. Challenges and Learnings

### Challenges
- Ensuring robust JWT authentication.
- Writing comprehensive test cases for all endpoints.
- Optimizing database queries for scalability.

### Learnings
- Gained expertise in FastAPI’s capabilities.
- Learned to containerize apps using Docker for consistent deployment.
- Strengthened understanding of CI/CD pipelines.

---

## 8. Future Enhancements
1. **Real-time Notifications:**
   - Integrate WebSockets for real-time updates.

2. **Social Features:**
   - Add friend requests and messaging functionality.

3. **Analytics Dashboard:**
   - Provide admin insights into user engagement and activity.

4. **Enhanced Security:**
   - Add rate-limiting and IP-based restrictions.

---

## 9. References
- [FastAPI Documentation](https://fastapi.tiangolo.com/)
- [Docker Documentation](https://docs.docker.com/)
- [Heroku Documentation](https://devcenter.heroku.com/)
- [GitHub Actions](https://docs.github.com/en/actions)

---

## 10. Conclusion
The Social App API is a robust and scalable backend solution tailored for modern social applications. Its flexibility, coupled with its deployment-ready configuration, ensures developers can focus on building engaging user experiences while the API handles the backend seamlessly.

