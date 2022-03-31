pipeline {
    agent none
    options {
        timeout(time: 4, unit: 'MINUTES')   
    }
    stages {
        stage("Image of Agent_1") {
            agent {
                label 'Master'   
            }
            steps {
                script {
                    try {                     
                        sh 'cd ./FlaskJenkins/slave; docker build -t jenkins-agent-1 .'
                    }
                    catch (Exception e) {
                            echo "Quitting job due to error in build image"
                            error('Failed to build')
                    }
                }
            }
        }   
        stage("Start Agent_1")  {
            agent {
                label 'Master'   
            }
            steps {
                script {
                    try {
                        step([$class: 'DockerComposeBuilder', dockerComposeFile: 'FlaskJenkins/slave/docker-compose.yml', option: [$class: 'StopService', service: 'agent-1'], useCustomDockerComposeFile: true])
                    }
                    catch (Exception e) {
                        echo 'No services to down, trying to up!'
                    }
                    try {
                        step([$class: 'DockerComposeBuilder', dockerComposeFile: 'FlaskJenkins/slave/docker-compose.yml', option: [$class: 'StartService', scale: 1, service: 'agent-1'], useCustomDockerComposeFile: true])
                    }
                    catch (Exception e) {
                        echo 'Unable to up service, quitting job'
                        error('Failed to start agent')
                    }
                }
            }
        }
        stage("Start App") {
            agent {
                label 'Agent_1'  
            }
            steps {
                sh "python3 /home/jenkins/agent/workspace/${env.JOB_NAME}/app.py"
            }
        }
    }
}
