pipeline {
    agent any

environment {
        DOCKERFILE_CREDS_ID = 'dockerhub-id'
        DEPLOY_IMAGE = 'destroyyer/students-api'
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
                    docker.build(DEPLOY_IMAGE)
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
                    docker.withRegistry('', DOCKERFILE_CREDS_ID) {
                        docker.image(DEPLOY_IMAGE).push()
                    }
                }
            }
        }
    }
}