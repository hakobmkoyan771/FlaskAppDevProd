pipeline {
    agent none
    options {
        timeout(time: 4, unit: 'MINUTES')   
    }
    stages {
        stage("Build images") {
            agent {
                label 'Master'   
            }
            steps {
                script {
                    try {                     
                        sh 'cd ./FlaskJenkins/; docker build -t jenkins-agent-1 .'
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
        stage("Start Containers")  {
            agent {
                label 'Master'  
            }
            steps {
                script {
                    try {
                        step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StopAllServices'], useCustomDockerComposeFile: false])
                    }
                    catch (Exception e) {
                        echo 'No services to down, trying to up!'
                    }
                    try {
                        step([$class: 'DockerComposeBuilder', dockerComposeFile: 'docker-compose.yml', option: [$class: 'StartAllServices'], useCustomDockerComposeFile: false])
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
