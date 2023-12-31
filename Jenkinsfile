pipeline {
    agent any

    parameters {
        choice(name: 'CONFIG', choices: ['35184_NoUI', '35184'], description: 'Select the configuration')
    }

    environment {
        apiUrl = 'http://10.9.11.51:8888/execute_script'
        repo = 'https://se-svne-01.packsize.local/svn/nextgen/tag/M1/PLC/'
        scriptpath = 'C:\\JenkinsNode\\Scripts\\M1\\pipeline_scripts\\'
    }

    stages {
        stage('Set up environment') {
            steps {
                script {
                    def CONFIGURATIONS = [
                        '35184_NoUI': [
                            'CODESYS_PATH': '"C:\\Program Files\\CODESYS 3.5.18.40\\CODESYS\\Common\\CODESYS.exe"',
                            'PROFILE': '"CODESYS V3.5 SP18 Patch 4"',
                            'ADDITIONAL_FOLDER': '"C:\\Program Files\\CODESYS 3.5.18.40\\CODESYS\\AdditionalFolders\\M1" --noUI'
                        ],
                        '35184': [
                            'CODESYS_PATH': '"C:\\Program Files\\CODESYS 3.5.18.40\\CODESYS\\Common\\CODESYS.exe"',
                            'PROFILE': '"CODESYS V3.5 SP18 Patch 4"',
                            'ADDITIONAL_FOLDER': '"C:\\Program Files\\CODESYS 3.5.18.40\\CODESYS\\AdditionalFolders\\M1"'
                        ]
                    ]
                    def selectedConfig = CONFIGURATIONS[params.CONFIG]
                    env.codesysBaseCommand = "${selectedConfig.CODESYS_PATH} --Profile=${selectedConfig.PROFILE} --AdditionalFolder=${selectedConfig.ADDITIONAL_FOLDER}"
                }
            }
        }

        stage('Pipeline Execution') {
            steps {
                script {
                    def versions = ['Prod_Version2', 'Prod_Version1']
                    versions.each { version ->
                        def now = new Date()
                        env.timestamp = now.format("yyyyMMdd_HHmm", TimeZone.getTimeZone('UTC'))
                        env.working_folder = "${env.scriptpath}${env.timestamp}_${SVN_TAG}_M1_${version}"

                        def arg1 = "${env.working_folder}"
                        echo "arg1: ${env.working_folder}" 
                        def arg2 = version 
                        echo "arg2: ${version}" 
                        def arg3 = "${env.repo}${SVN_TAG}"
                        echo "arg3: ${env.repo}${SVN_TAG}" 
                        def runScriptPath = "${scriptpath}generate_application.py"
                        def scriptArgs = "${arg1} ${arg2} ${arg3}"
                        env.codesysCommand = "${env.codesysBaseCommand} --runscript=\"${runScriptPath}\" --scriptargs:\"${scriptArgs}\""

                        withCredentials([usernamePassword(credentialsId: 'api-credentials', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
                            def escapedCodesysCommand = env.codesysCommand.replaceAll('\\\\', '\\\\\\\\').replaceAll('"', '\\\\"')
                            def payload = "{\"scriptPath\":\"${escapedCodesysCommand}\"}"
                            echo "Payload: ${payload}" 
                            def response = httpRequest httpMode: 'POST',
                                                       url: env.apiUrl,
                                                       contentType: 'APPLICATION_JSON',
                                                       requestBody: payload,
                                                       authentication: 'api-credentials'
                            if (response.status != 200) {
                                error "API call failed with status ${response.status}"
                            }
                        }

                        def workspaceArg = "--workspace \"${scriptpath}\\tmp\""
                        def extractPathArg = "--extract_path \"${scriptpath}\\source\\usbupdate-mx6.zip\""
                        def updateAppPathArg = "--update_app_path \"${env.working_folder}\""
                        def composePathArg = "--compose_path \"${working_folder}\\${version}\\usbupdate-mx6.zip\""
                        def pythonCommand = "python ${scriptpath}create_usb_stick_files.py ${workspaceArg} ${extractPathArg} ${updateAppPathArg} ${composePathArg}"
                        def escapedCodesysCommand = pythonCommand.replaceAll('\\\\', '\\\\\\\\').replaceAll('"', '\\\\"')
                        def payload = "{\"scriptPath\":\"${escapedCodesysCommand}\"}"
                        echo "Payload: ${payload}" 
                        def response = httpRequest httpMode: 'POST',
                                                       url: env.apiUrl,
                                                       contentType: 'APPLICATION_JSON',
                                                       requestBody: payload,
                                                       authentication: 'api-credentials'
                        if (response.status != 200) {
                            error "API call failed with status ${response.status}"
                        }
                    }
                }
            }
        }

        stage('Run Unit Tests') {
            steps {
                echo "Unit test logic will go here"
            }
        }
    }

    post {
        success {
            echo "Build was successful."
        }
        failure {
            echo "Build failed."
        }
    }
}
