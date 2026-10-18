
pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                echo 'Source code is checked out by Jenkins from SCM.'
            }
        }

        stage('Check Environment') {
            steps {
                bat '''
                    whoami
                    git --version
                    python --version
                    "C:\\Users\\sgurj\\AppData\\Local\\Programs\\DockerDesktop\\resources\\bin\\docker.exe" --version
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
    }

    post {
        success {
            echo 'Checkout, environment checks and Python tests completed successfully.'
        }
        failure {
            echo 'Pipeline failed. Check Console Output for details.'
        }
    }
}
