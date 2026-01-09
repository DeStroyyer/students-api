pipeline {
    agent any

environment {
        DOCKERFILE_CREDS_ID_123 = 'dockerhub-id'
        DOCKER_IMAGE = 'destroyyer/students-api'
    }

    stages {
        stage('Clone repository') {
            steps {
                git branch: 'main', url: 'https://github.com/DeStroyyer/students-api.git'
            }
        }
        stage('BUILD Docker Image') {
            steps {
                script {
                    docker.build(DOCKER_IMAGE)
                }
            }
        }
        stage('Test Docker Image') {
            steps {
                script {
                    sh "echo 'Running tests...'"
                }
            }
        }
        stage('Push Docker Image') {
            steps {
                script {
                    docker.withRegistry('', DOCKERFILE_CREDS_ID_123) {
                        docker.image(DOCKER_IMAGE).push()
                    }
                }
            }
        }

        stage('DEPLOYMENT to stage') {
            steps {
                script {

                    sh "docker pull ${DOCKER_IMAGE}:latest"
                    sh "echo 'Deploying to staging environment...'"
                    sh "docker run -d -p 8000:8000 ${DOCKER_IMAGE}:latest"
                }
            }
        }
         stage('DEPLOYMENT to PROD') {
            steps {
                script {
                    input message: 'Approve deployment?', ok: 'Deploy'
                    sh "echo 'Deploying application...'"
                }
            }
        }
    }
}