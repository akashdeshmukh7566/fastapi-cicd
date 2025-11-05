pipeline {
    agent any

    stages {
        stage('Checkout Code') {
            steps {
                echo ' Cloning repository...'
                checkout scm
            }
        }

        stage('Build Docker Image') {
            steps {
                echo 'Building Docker image...'
                sh 'docker build -t fastapi_app_image .'
            }
        }

        stage('Run Docker Compose') {
            steps {
                echo ' Starting services...'
                sh '''
                echo " cleaning up old containers.."
                docker stop fastapi_app my_postgres || true
                docker rm fastapi_app my_postgres || true
                docker compose down || true
                docker compose up -d
                '''
            }
        }

        stage('Run Tests') {
            steps {
                echo ' Running tests...'
                // Run your pytest or FastAPI tests here if you have any
                sh 'echo "No tests defined yet"'
            }
        }

        stage('Cleanup') {
            steps {
                echo ' Cleaning up...'
                sh 'docker system prune -f'
            }
        }
    }
}































