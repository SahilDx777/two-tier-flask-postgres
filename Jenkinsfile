pipeline {
    agent any

    stages {
        stage('Deploy') {
            steps {
                sh '''
                cd /opt/two-tier-flask-postgres
                docker-compose down
                docker-compose up -d --build
                '''
            }
        }
    }
}
