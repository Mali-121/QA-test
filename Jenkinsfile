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
        success {
            emailext(
                to: 'ali@smartwalkietalkie.com',
                subject: "Build Successful: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                body: "The build was successful.\nJob Name: ${env.JOB_NAME}\nBuild Number: ${env.BUILD_NUMBER}\nBuild URL: ${env.BUILD_URL}",
                attachLog: true
            )
        }
        failure {
            emailext(
                to: 'ali@smartwalkietalkie.com',
                subject: "Build Failed: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                body: "The build has failed.\nJob Name: ${env.JOB_NAME}\nBuild Number: ${env.BUILD_NUMBER}\nBuild URL: ${env.BUILD_URL}",
                attachLog: true
            )
        }
        always {
            emailext(
                to: 'ali@smartwalkietalkie.com',
                subject: "Build Completed: ${env.JOB_NAME} [${env.BUILD_NUMBER}]",
                body: "The build has completed with result: ${currentBuild.result}.\nJob Name: ${env.JOB_NAME}\nBuild Number: ${env.BUILD_NUMBER}\nBuild URL: ${env.BUILD_URL}",
                attachLog: true
            )
        }
    }
}
