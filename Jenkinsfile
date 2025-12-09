pipeline {
    agent any

    environment {
        DOCKERHUB_CREDENTIALS = credentials('dockerhub-creds')
    }

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/wassimhajji13/jenkins-test.git'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                    docker build -t wassimhajji11/jenkins-test-image:latest .
                '''
            }
        }

        stage('Docker Login') {
            steps {
                sh '''
                    echo "$DOCKERHUB_CREDENTIALS_PSW" | docker login -u "$DOCKERHUB_CREDENTIALS_USR" --password-stdin
                '''
            }
        }

        stage('Push Docker Image') {
            steps {
                sh '''
                    docker push wassimhajji11/jenkins-test-image:latest
                '''
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                    docker stop myapp || true
                    docker rm myapp || true
                    docker pull wassimhajji11/jenkins-test-image:latest
                    docker run -d --name myapp -p 8081:80 wassimhajji11/jenkins-test-image:latest
                '''
            }
        }
    }

    post {
        success {
            echo "🎉 Deployment complete!"
        }
    }
}
