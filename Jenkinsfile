pipeline {
    agent any

    stages {
        stage('Check Python Installation') {
            steps {
                // Use full path to Python executable
                bat 'C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe --version'
                bat 'C:/Users/user/AppData/Local/Programs/Python/Python312/Scripts/pip.exe --version'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Use the full path to Python executable when running the Selenium test
                bat 'C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe python-test/selenium_test.py'
            }
        }
    }

    post {
        always {
            emailext(
                to: 'm.ali149@outlook.com',  // Your email address
                subject: "Test Result: ${currentBuild.result}",
                body: "The build has ${currentBuild.result}. Check details at: ${env.BUILD_URL}"
            )
        }
    }
}
