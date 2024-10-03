pipeline {
    agent any

    stages {
        stage('Check Python Installation') {
            steps {
                // This runs a command in the Windows command prompt (cmd)
                bat 'python --version'  // Check if Python is installed
                bat 'pip --version'     // Check if pip is installed
            }
        }
    }
}
