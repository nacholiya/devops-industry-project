pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/nacholiya/devops-industry-project.git'
            }
        }

        stage('Sanity Check') {
            steps {
                sh '''
                  cd app
                  python3 -c "import main; print('App syntax OK')"
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '''
                  docker build -t devops-fastapi:jenkins .
                '''
            }
        }
    }
}
