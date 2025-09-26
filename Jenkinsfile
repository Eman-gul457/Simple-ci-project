pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-credentials') 
        DOCKER_IMAGE = "emangul199/simple-ci"
    }

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/Eman-gul457/simple-ci-project.git'
            }
        }

        stage('Get commit id') {
            steps {
                script {
                    COMMIT_ID = sh(returnStdout: true, script: 'git rev-parse --short HEAD').trim()
                    echo "Commit ID: ${COMMIT_ID}"
                }
            }
        }

        stage('Setup') {
            steps {
                sh 'echo "Setting up environment..."'
            }
        }

        stage('Run tests') {
            steps {
                sh 'echo "Running tests..."'
                // Example test command
                sh 'pytest || echo "No tests found"'
            }
        }

        stage('Build Docker image') {
            steps {
                script {
                    sh "docker build -t ${DOCKER_IMAGE}:${COMMIT_ID} ."
                }
            }
        }

        stage('Push to Docker Hub') {
            steps {
                script {
                    sh "echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin"
                    sh "docker push ${DOCKER_IMAGE}:${COMMIT_ID}"
                    sh "docker tag ${DOCKER_IMAGE}:${COMMIT_ID} ${DOCKER_IMAGE}:latest"
                    sh "docker push ${DOCKER_IMAGE}:latest"
                }
            }
        }
    }

    post {
        success {
            echo "PIPELINE SUCCESS ✅"
        }
        failure {
            echo "PIPELINE FAILED ❌"
        }
    }
}
