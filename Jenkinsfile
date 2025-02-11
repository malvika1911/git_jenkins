pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }
    stages {
        stage('Test') {
            steps {
              echo 'hello sfsf'
              bat 'python3 pull.py'
            }
        }
    }
}
