pipeline {
    agent any

    stages {
        stage('Check Python Installation') {
            steps {
                bat 'C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe --version'
                bat 'C:/Users/user/AppData/Local/Programs/Python/Python312/Scripts/pip.exe --version'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Use full path to the script on your desktop
                bat 'C:/Users/user/AppData/Local/Programs/Python/Python312/python.exe C:/Users/user/Desktop/python-test/selanium_test.py'
            }
        }
    }

    post {
        always {
            emailext(
                to: 'm.ali149@outlook.com',
                subject: "Test Result: ${currentBuild.result}",
                body: "The build has ${currentBuild.result}. Check details at: ${env.BUILD_URL}"
            )
        }
    }
}
