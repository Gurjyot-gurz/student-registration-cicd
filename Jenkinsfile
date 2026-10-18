
pipeline {
    agent any

    environment {
        DOCKER = 'C:\\Users\\sgurj\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe'
        DOCKER_IMAGE = 'gk740/student-registration:latest'
    }

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code checked out by Jenkins from SCM.'
            }
        }

        stage('Check Environment') {
            steps {
                bat '''
                    python --version
                    git --version
                    "%DOCKER%" --version
                '''
            }
        }

        stage('Install Dependencies') {
            steps {
                bat '''
                    python -m venv .venv
                    .venv\\Scripts\\python.exe -m pip install -r app\\requirements.txt
                '''
            }
        }

        stage('Run Tests') {
            steps {
                bat '.venv\\Scripts\\python.exe -m pytest tests\\ -v'
            }
        }

        stage('Build Docker Image') {
            steps {
                bat '''
                    "%DOCKER%" build --tag "%DOCKER_IMAGE%" .
                    if errorlevel 1 exit /b 1
                '''
            }
        }

        stage('Push to Docker Hub') {
            steps {
                withCredentials([usernamePassword(
                    credentialsId: 'dockerhub-credentials',
                    usernameVariable: 'DOCKER_USER',
                    passwordVariable: 'DOCKER_TOKEN'
                )]) {
                    script {
                        try {
                            bat '''
                                @echo off
                                echo Logging in to Docker Hub...
                                echo %DOCKER_TOKEN%| "%DOCKER%" login --username "%DOCKER_USER%" --password-stdin
                                if errorlevel 1 exit /b 1

                                "%DOCKER%" push "%DOCKER_IMAGE%"
                                if errorlevel 1 exit /b 1
                            '''
                        } finally {
                            bat '''
                                @echo off
                                "%DOCKER%" logout
                            '''
                        }
                    }
                }
            }
        }
    }

    post {
        success {
            echo 'SUCCESS: Tests passed, Docker image built and pushed.'
        }
        failure {
            echo 'FAILED: Check Console Output for the failing stage.'
        }
    }
}
