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
                    # IMPORTANT : on force une vraie reconstruction
                    docker build --no-cache -t wassimhajji11/jenkins-test-image:latest .
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

        stage('Deploy on VM') {
            steps {
                sh '''
                    # Arrêter ancien conteneur
                    docker stop myapp || true
                    docker rm myapp || true

                    # Télécharger nouvelle image
                    docker pull wassimhajji11/jenkins-test-image:latest

                    # Relancer nouvelle version
                    docker run -d --name myapp -p 8081:80 --memory="512m" wassimhajji11/jenkins-test-image:latest
                '''
            }
        }
    }

    post {
        success {
            echo "🚀 Nouveau déploiement réussi !"
        }
        failure {
            echo "❌ Le déploiement a échoué"
        }
    }
}
