pipeline {
    agent any

    stages {
        stage('version') {
            steps {
                sh'python --version'
                sh'pwd'
            }
        }

        stage('Installing requirements') {
            steps {
                sh'pip install -r requirements.txt'
            }
        }

        stage('testing the app') {
            steps {
                sh'python -m unittest'
            }
        }

        stage('build a Docker image and test container') {
            steps {
                sh'docker build -t flask_api .'
                sh'docker run -d -p 5000:5000 flask_api'
            }
        }
        
        stage('Deploy') {
            steps {
                echo 'Hello World'
            }
        }
    }
}
