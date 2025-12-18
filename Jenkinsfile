pipeline {
    agent any

    stages {
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
