pipeline {
    agent any

    environment {
        DOCKER_IMAGE = "faizuu7/shopflow"
        KUBECONFIG = "C:\\ProgramData\\Jenkins\\.kube\\config"
    }

    stages {

        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Install Dependencies') {
            steps {
                bat 'python -m pip install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'python -m pytest'
            }
        }

        stage('Check Docker') {
            steps {
                bat 'docker --version'
            }
        }

        stage('Check Kubernetes') {
            steps {
                bat 'kubectl config current-context'
                bat 'kubectl get nodes'
            }
        }

        stage('Docker Build') {
            steps {
                bat 'docker build -t %DOCKER_IMAGE%:%BUILD_NUMBER% .'
            }
        }

        stage('Docker Login') {
            steps {
                withCredentials([
                    usernamePassword(
                        credentialsId: 'dockerhub-creds',
                        usernameVariable: 'DOCKER_USERNAME',
                        passwordVariable: 'DOCKER_PASSWORD'
                    )
                ]) {
                    bat 'echo %DOCKER_PASSWORD% | docker login -u "%DOCKER_USERNAME%" --password-stdin'
                }
            }
        }

        stage('Docker Push') {
            steps {
                bat 'docker push %DOCKER_IMAGE%:%BUILD_NUMBER%'
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl set image deployment/shopflow shopflow=%DOCKER_IMAGE%:%BUILD_NUMBER%'
            }
        }

        stage('Kubernetes Rollout') {
            steps {
                bat 'kubectl rollout status deployment/shopflow'
            }
        }

        stage('Verify Deployment') {
            steps {
                bat 'kubectl get deployment shopflow'
                bat 'kubectl get pods'
            }
        }
    }
}