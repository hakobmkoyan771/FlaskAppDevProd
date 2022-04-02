pipeline {
    agent none
    options {
        timeout(time: 4, unit: 'MINUTES')   
    }
    stages {
        stage("Build images") {
            agent any
            steps {
                script {
                    try {                     
                        sh 'cd ./FlaskJenkins/; docker build -t jenkins-server .'
                    }
                    catch (Exception e) {
                            echo "Quitting job due to error in build image"
                            error('Failed to build')
                    }
                    try {                     
                        sh 'cd ./FlaskJenkins/; docker build -f Dockerfile_agent_1 -t jenkins-agent-1 .'
                    }
                    catch (Exception e) {
                            echo "Quitting job due to error in build image"
                            error('Failed to build')
                    }
                }
            }
        }   
    }
}
