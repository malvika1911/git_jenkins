pipeline {
    agent any {
    stages {
        stage('Test') {
            steps {
                bat 'python --version'
                bat 'python pyg1.py'  // Ensure this script exists in the workspace
            }
        }
    }
}
}
