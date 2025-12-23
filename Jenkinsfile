pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                git branch: 'main', url: 'https://github.com/nacholiya/devops-industry-project.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
                  cd app
                  pip install -r requirements.txt
                '''
            }
        }

        stage('Test') {
            steps {
                sh '''
                  cd app
                  python -c "import main; print('App loaded')"
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
