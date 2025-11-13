pipeline {
    agent any
    
    stages {
        stage('Copy Environment File') {
            steps {
                script {
                    sh 'cp /env/notesdiffer/.env .env'
                }
            }
        }
        
        stage('Run Docker') {
            steps {
                script {
                    sh 'docker-compose up -d --build'
                }
            }
        }
    }
}
