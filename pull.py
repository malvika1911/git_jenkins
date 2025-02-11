pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }
    stages {
        stage('Test') {
            steps {
                sh 'python --version'
                sh 'ls -l'  // Debugging step to check if pyg1.py exists
                sh 'python pyg1.py'  // Ensure this script exists in the workspace
            }
        }
    }
}
