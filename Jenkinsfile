pipeline {
    agent any

    parameters {
        choice(name: 'CONFIG', choices: ['35184', '35164'], description: 'Select the configuration')
    }

    environment {
        apiUrl = 'http://10.9.11.51:8888/execute_script'
        repo = 'https://se-svne-01.packsize.local/svn/nextgen/tag/M1/PLC/'
    }

    stages {
        stage('Initial Setup') {
            steps {
                script {
                    def now = new Date()
                    env.timestamp = now.format("yyyyMMdd_HHmm", TimeZone.getTimeZone('UTC'))
                    env.working_folder = "C:\\JenkinsNode\\Scripts\\M1\\pipeline_scripts\\${env.timestamp}_WORKING_FOLDER"
                }
            }
        }
    
    

        stage('Set up environment') {
            steps {
                script {
                    def CONFIGURATIONS = [
                        '35184': [
                            'CODESYS_PATH': '"C:\\Program Files\\CODESYS 3.5.18.40\\CODESYS\\Common\\CODESYS.exe"',
                            'PROFILE': '"CODESYS V3.5 SP18 Patch 4"',
                            'ADDITIONAL_FOLDER': '"C:\\Program Files\\CODESYS 3.5.18.40\\CODESYS\\AdditionalFolders\\M1"'
                        ],
                        '35164': [
                            'CODESYS_PATH': '"C:\\Program Files\\CODESYS 3.5.16.40\\CODESYS\\Common\\CODESYS.exe" --noUI',
                            'PROFILE': '"CODESYS V3.5 SP16 Patch 4"',
                            'ADDITIONAL_FOLDER': '"C:\\Program Files\\CODESYS 3.5.16.40\\CODESYS\\AdditionalFolders\\M1"'
                        ]
                    ]
                    def selectedConfig = CONFIGURATIONS[params.CONFIG]
                    env.codesysBaseCommand = "${selectedConfig.CODESYS_PATH} --Profile=${selectedConfig.PROFILE} --AdditionalFolder=${selectedConfig.ADDITIONAL_FOLDER}"
                }
            }
        }
        
        
        stage('Checkout project from SVN') {
            steps {
                script {
                    def arg1 = "${env.repo}${SVN_TAG}"
                    def arg2 = "${env.working_folder}"
                    def arg3 = 'M1'

                    def runScriptPath = 'C:\\JenkinsNode\\Scripts\\M1\\pipeline_scripts\\checkout_project.py'
                    def scriptArgs = "${arg1} ${arg2} ${arg3}"
                  
                    
                    env.codesysCommand = "${env.codesysBaseCommand} --runscript=\"${runScriptPath}\" --scriptargs:\"${scriptArgs}\""

                    
                    def escapedCodesysCommand = env.codesysCommand.replaceAll('\\\\', '\\\\\\\\').replaceAll('"', '\\\\"')
                    
                    def payload = "{\"scriptPath\":\"${escapedCodesysCommand}\"}"
                    
                    def response = httpRequest httpMode: 'POST', url: env.apiUrl, contentType: 'APPLICATION_JSON', requestBody: payload
                    if (response.status != 200) {
                        error "API call failed with status ${response.status}"
                    }
                }
            }
        }
    }
}
