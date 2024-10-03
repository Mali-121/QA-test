pipeline {
    agent any

    environment {
        CHROME_DRIVER_PATH = 'C:/Users/user/Downloads/chromedriver-win64/chromedriver.exe'  // Update this path as needed
    }

    stages {
        stage('Checkout Code') {
            steps {
                git branch: 'main', url: 'https://github.com/Mali-121/QA-test.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                // Install dependencies (ensure Python and Selenium are installed)
                sh 'pip install selenium'  // On Windows, you can use 'bat' instead of 'sh' for batch commands
            }
        }

        stage('Run Selenium Tests') {
            steps {
                // Run your Selenium test script (use 'bat' for Windows)
                bat 'python python-test/selanium_test.py'  // Change 'sh' to 'bat' for Windows
            }
        }
    }

    post {
        always {
            // If you are not generating JUnit reports, you can remove this step
            junit '**/test-reports/*.xml'  // Remove this if you are not generating JUnit reports

            // Optional: Send an email notification
            emailext(
                subject: "Test Result: ${currentBuild.result}",
                body: "The build has ${currentBuild.result}. Check details at: ${env.BUILD_URL}",
                recipientProviders: [[$class: 'DevelopersRecipientProvider']]
            )
        }
    }
}
