pipeline {
    agent {
        docker {
            image 'python:3'
        }
    }
    stages {
        stage('Test') {
            steps {
                bat 'python --version'
                bat 'ls -l'  // Debugging step to check if pyg1.py exists
                bat 'python pyg1.py'  // Ensure this script exists in the workspace
            }
        }
    }
}
