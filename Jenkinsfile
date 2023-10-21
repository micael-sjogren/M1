pipeline {
    agent any

    stages {
        stage('Set up enviroment') {
            steps {
               bat '''
                    @echo off
                    REM set Python virtual environment 
                    
                    echo Updating PLC firmware
                    REM python.exe %SCRIPTS_DIR%\\_Execute_M1.py %SVN_REVISION% %SVN_URL% %JENKINS_HOME% %BUILD_NUMBER% %JOB_NAME% %PLC_IP% %APPLICATION_NAME% %SVN_TAG%
                '''
            }
        }
        
        stage('Checkout Code') {
            steps {
               bat '''
                    @echo off
                    echo Environment variables:
                    set
                    echo Python version:
                    python --version
                    echo Checkout Code
                    REM C:\\Users\\agent\\AppData\\Local\\Programs\\Python\\Python312\\python.exe %SCRIPTS_DIR%\\_Execute_checkout_project.py %SVN_URL% %APPLICATION_NAME% 
                '''

            }
        }
        

        
        stage('Unit Test') {
            steps {
               bat '''
                    @echo off
                    echo Unit Test     
                '''

            }
        }
        
         stage('Deployment to RnD') {
            steps {
               bat '''
                    @echo off
                    echo Deployment to Rnd
                '''

            }
        }
        
       
        stage('Documentation') {
            steps {
               bat '''
                    @echo off
                    echo Create documentation
                '''

            }
        }
        
        
        stage('Archiving') {
            steps {
               bat '''
                    @echo off
                    echo Archive project for future use
                '''

            }
        }
        
        
        stage('Notification') {
            steps {
               bat '''
                    @echo off
                    echo Notification
                '''

            }
        }
        
        
    }
}
