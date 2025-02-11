pipeline {
    agent any 
    stages {
        stage('Test') {
            steps {
                bat 'python --version'
                bat 'dir'  // Debugging step to check if pyg1.py exists
                bat 'python pyg1.py'  // Ensure this script exists in the workspace
            }
        }
    }
}

