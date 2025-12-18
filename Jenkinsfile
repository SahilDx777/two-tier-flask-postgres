pipeline {
    agent any

    stages {
        stage('Checkout') {
            steps {
                git branch: 'main',
                    url: 'https://github.com/<your-username>/two-tier-flask-postgres.git'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                cd /opt/two-tier-flask-postgres
                docker-compose up -d --build
                '''
            }
        }
    }
}

