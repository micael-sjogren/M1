pipeline {
    agent {
        label 'windows_agent'
    }

    environment {
        SCRIPTS_DIR = 'C:\\Scripts\\M1\\create_stick'
        SVN_URL = 'https://se-svne-01.packsize.local/svn/nextgen/branch/M1/PLC/Target_1.27.0.0'
        SVN_REVISION = '10074'
        SVN_CREDENTIALS_ID = 'b528ade6-13be-411f-891f-22047a5b3aeb'
        JENKINS_HOME = 'C:\\ProgramData\\Jenkins\\.jenkins'
        BUILD_NUMBER = '23'
        JOB_NAME = 'M1'
        PLC_IP = '10.9.9.57'
        APPLICATION_NAME = 'Prod_Version2'
        SVN_TAG = 'Target_1.27.0.0'
    }

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
                    C:\\Users\\agent\\AppData\\Local\\Programs\\Python\\Python312\\python.exe %SCRIPTS_DIR%\\_Execute_checkout_project.py %SVN_URL% %APPLICATION_NAME% 
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
