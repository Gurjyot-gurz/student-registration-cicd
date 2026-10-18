# Student Registration System — CI/CD on AWS EC2

A containerized **two-tier web application** built with Python Flask and MySQL, deployed on AWS EC2 using Docker, Docker Compose, Jenkins, and Docker Hub.

This project demonstrates the end-to-end workflow of developing a web application, managing source code with Git and GitHub, running automated tests, building a Docker image, publishing it to Docker Hub, and deploying the application to an AWS EC2 instance.

## 📌 Project Overview

The Student Registration System allows users to register students and view student records stored in a MySQL database.

The application was first developed and tested locally, then containerized and integrated with a Jenkins pipeline. The Docker image was published to Docker Hub and deployed on an Ubuntu EC2 instance. Database connectivity and student record retrieval were subsequently verified on the deployed application.

## ✨ Features

- Student registration through a Flask web interface
- Student records stored in a MySQL database
- Database connectivity through a dedicated Python database module
- Input validation and duplicate-email handling
- Dockerized Flask application
- MySQL container with persistent storage
- Multi-container configuration using Docker Compose
- Automated application tests using Pytest
- Jenkins pipeline for build and test workflows
- Docker image published to Docker Hub
- Deployment of the containerized application on AWS EC2

## 🛠️ Technology Stack

| Category | Technologies |
|---|---|
| Frontend | HTML, CSS, Jinja templates |
| Backend | Python, Flask |
| Database | MySQL 8.4 |
| Testing | Pytest |
| Containerization | Docker, Docker Compose |
| CI/CD | Jenkins, Jenkinsfile |
| Version Control | Git, GitHub |
| Container Registry | Docker Hub |
| Cloud Platform | AWS EC2 |
| Operating System | Ubuntu Linux |

## 🏗️ Architecture

```mermaid
flowchart TD
    A[User Browser] -->|HTTP Port 80| B[AWS EC2 Instance]
    B --> C[Flask Web Container]
    C -->|SQL Queries| D[MySQL Database Container]
    D --> E[Persistent Docker Volume]

    F[Developer / VS Code] --> G[GitHub Repository]
    G --> H[Jenkins Pipeline]
    H --> I[Automated Tests and Docker Build]
    I --> J[Docker Hub]
    J -. Image Pull and Deployment .-> B
```

### Two application tiers

**Tier 1 — Web Tier**
- Flask application served by Gunicorn.
- Accepts HTTP requests from the browser.
- Handles student registration and retrieval of student records.

**Tier 2 — Data Tier**
- MySQL database running in a separate Docker container.
- Stores student information in the `students` table.
- Uses a Docker named volume for persistent database storage.

Both application tiers run on the same EC2 instance. Jenkins, GitHub, and Docker Hub support the delivery workflow; they are not additional application tiers.

## 📂 Project Structure

```text
student-registration-cicd/
├── app/
│   ├── templates/
│   │   └── index.html
│   ├── app.py
│   ├── db.py
│   ├── requirements.txt
│   └── schema.sql
├── screenshots/
├── tests/
│   └── test_app.py
├── scripts/
├── docs/
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── Jenkinsfile
└── README.md
```

*This is a representative project structure. Some supporting files and folders may differ in the repository.*

## 🔄 Development and CI/CD Workflow

1. Developed the Flask application and MySQL schema in VS Code.
2. Tested the application locally at `http://localhost:5000`.
3. Managed source code using Git and GitHub.
4. Created a Dockerfile and Docker Compose configuration.
5. Created a Jenkinsfile and configured the Jenkins pipeline.
6. Ran the configured pipeline tests.
7. Built the Docker image and published it to Docker Hub.
8. Launched an Ubuntu EC2 instance and installed Docker.
9. Pulled and ran the application image on EC2.
10. Troubleshot MySQL database initialization, schema creation, user permissions, and application database connectivity.
11. Verified that the deployed webpage could retrieve student data from MySQL.

**Docker Hub repository:** [gk740/student-registration](https://hub.docker.com/r/gk740/student-registration)

Image tag used: `latest`

> The pipeline's build, test, and image-publishing workflow was configured and exercised. Fully automatic deployment following every new GitHub commit should be considered verified only after confirming that the Jenkins pipeline deploys the updated image to EC2 without a separate manual deployment step.

## 🖼️ Project Screenshots

The screenshots below document the project's development and deployment in chronological order.

### 1. Repository Setup and Git

![Git ignore configuration](screenshots/.gitignore_content.png)

![Git file creation workflow](screenshots/files_creations.png)

![Automated test run](screenshots/automated_test_run.png)

### 2. Docker Configuration and Local Application

![Dockerfile creation](screenshots/dockerfile_created.png)

![Docker Compose file creation](screenshots/docker_compose_file_created.png)

![Docker Compose build started](screenshots/docker_compose_build_started.png)

![Student website running locally](screenshots/student_website_started.png)

![Student registration interface](screenshots/student_registration.png)

![Updated requirements and Docker configuration](screenshots/requirements_dockerfile_updated.png)

![Git status and push workflow](screenshots/adding_new_files_git_status_push.png)

### 3. Secrets Management and Docker Compose

![Secrets and files ignored by Git](screenshots/SECRETS_FILES_IGNORED.png)

![Docker Compose configuration](screenshots/New_Docker_Compose.png)

### 4. Jenkins Configuration and Pipeline

![Jenkins credentials configuration](screenshots/jenkins_credentials_making.png)

![Docker Hub personal access token configuration](screenshots/docker_hub_PAT.png)

![Docker Hub credentials in Jenkins](screenshots/dockerhub_credentials_jenkins.png)

![Jenkins pipeline creation](screenshots/jenkins_pipeline_creation.png)

![Pipeline configuration added](screenshots/pipeline_added.png)

![Jenkins pipeline run](screenshots/pipeline_run.png)

![Docker Hub repository created](screenshots/dockerhub_repo_created.png)

![Jenkins connected to Docker Engine](screenshots/jenkins_connected_to_dockerengine.png)

![Jenkinsfile added to project](screenshots/project_jenkinsfile_added.png)

![Successful Jenkins pipeline and Docker Hub push](screenshots/jenkins_pipeline_success_dockerhub_push.png)

### 5. AWS EC2 Deployment

![EC2 instance network settings](screenshots/EC2_Instance_Network_Settings.png)

![EC2 instance launched](screenshots/EC2_Instance_Launched.png)

![Docker installed and service configured on EC2](screenshots/EC2_Instance_docker_installed_service_st...)

![Docker service running](screenshots/Docker_service_running.png)

![Docker image pulled from Docker Hub](screenshots/image_pulled_from_dockerhub.png)

![EC2 environment configuration](screenshots/EC2_Instance_envFile.png)

![EC2 Docker Compose configuration](screenshots/EC2_Instance_compose_file.png)

![Updated EC2 Compose configuration](screenshots/updated_EC2_compose.yaml.png)

![EC2 database schema configuration](screenshots/EC2_schema.sqlfile.png)

### 6. Troubleshooting and Database Verification

![Files prepared for deployment](screenshots/all_files_ready.png)

![Deployed webpage showing SQL error](screenshots/website_deployed_with_sqlError.png)

![Database table creation and fix](screenshots/missing_sql_table_created_fixed.png)

![Web-side SQL login error](screenshots/sql_login_error_web_side.png)

![EC2 webpage after SQL fix](screenshots/ec2_instance_webpage_sql_fixed.png)

![Registered student displayed on webpage](screenshots/ec2_webpage_data_registered.png)

![Student data verified in SQL](screenshots/ec2_wbpage_data_verified_in_sql.png)

![Updating Git ignore configuration](screenshots/updating_gitignore.png)

*If a screenshot filename differs in the repository, update the corresponding path above. GitHub image paths are case-sensitive.*

## 🧪 Testing and Validation

The following checks have been performed or are part of the final validation workflow:

- Local application startup and access
- Automated test execution through the configured test workflow
- Docker image build and publication to Docker Hub
- EC2 deployment of the application container
- MySQL database and `students` table availability
- MySQL application-user login and permissions
- Web application database connectivity
- Retrieval and display of student records from MySQL

### Recommended final end-to-end checks

- Submit a new student through the deployed webpage and query MySQL to verify the inserted record.
- Restart the web container and confirm that student records remain available.
- Push a harmless application change and confirm that Jenkins builds and publishes a new image.
- Verify that the new image is automatically deployed to EC2 by the configured pipeline.

## 🚀 Running the Project Locally

### Prerequisites

- Python
- Docker Engine or Docker Desktop
- Docker Compose
- Git

### Steps

**1. Clone the repository**

```bash
git clone https://github.com/Gurjyot-gurz/student-registration-cicd.git
cd student-registration-cicd
```

**2. Configure environment variables**

Create a local `.env` file containing the variables required by your Compose configuration. Use secure, private values. Do not commit `.env` to GitHub.

**3. Start the application**

```bash
docker compose up -d --build
```

**4. Open the local application**

```text
http://localhost:5000
```

**5. Check the running containers**

```bash
docker compose ps
```

**6. Inspect application logs**

```bash
docker compose logs -f web
```

Use the service names and ports defined in your current Compose configuration if they differ from these examples.

## ☁️ AWS EC2 Deployment

The application is deployed on an Ubuntu EC2 instance.

- The Flask/Gunicorn application listens on container port `5000`.
- Host port `80` forwards HTTP requests to the web container.
- MySQL runs in a separate container.
- Docker Compose manages the application services.
- A named Docker volume stores MySQL data persistently.

Access the application using the current public IPv4 address of the EC2 instance:

```text
http://YOUR-EC2-PUBLIC-IP
```

Replace the placeholder with the instance's current public IP. The instance must be running, and its security group must permit HTTP traffic on port `80`.

## 🔐 Security Practices

- Keep `.env` files out of Git.
- Never commit SSH private keys (`.pem`), access tokens, passwords, or other credentials.
- Restrict SSH access to trusted IP addresses.
- Do not expose MySQL port `3306` publicly unless explicitly required and securely controlled.
- Rotate credentials that have been exposed.
- Use HTTPS and appropriate secrets management for production deployments.

## 🎯 Learning Outcomes

This project provided practical experience with:

- Developing a Python Flask application.
- Connecting a web application to MySQL.
- Containerizing services with Docker.
- Managing multi-container applications using Docker Compose.
- Writing and executing a Jenkins pipeline.
- Running automated tests.
- Publishing Docker images to Docker Hub.
- Deploying containerized applications to AWS EC2.
- Troubleshooting database initialization, authentication, and connectivity issues.
- Documenting infrastructure and deployment steps.

## 🔮 Future Improvements

- Verify and complete automatic EC2 deployment through Jenkins.
- Configure HTTPS with a domain and TLS certificate.
- Add application monitoring and centralized logging.
- Implement automated database backups and recovery.
- Improve CI/CD security and secrets management.
- Expand application and integration test coverage.

## 👨‍💻 Author

**Gurjyot Singh**

- GitHub: [Gurjyot-gurz](https://github.com/Gurjyot-gurz)
- Repository: [student-registration-cicd](https://github.com/Gurjyot-gurz/student-registration-cicd)
- Docker Hub: [gk740/student-registration](https://hub.docker.com/r/gk740/student-registration)

---

*An educational DevOps project demonstrating a two-tier web application, containerization, CI/CD tooling, and cloud deployment on AWS EC2.*
