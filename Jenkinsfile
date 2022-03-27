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
                            currentBuild.result = 'FAILURE'
                            sh 'echo "Quitting job due to error in build image"'
                            return
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
                        sh 'cd ./FlaskJenkins/slave; docker-compose down || true'
                    }
                    finally {
                        sh 'cd ./FlaskJenkins/slave; docker-compose up -d'
                    }
                }
            }
        }
        stage("Start App") {
            agent {
                label 'Agent_1'  
            }
            steps {
                sh "cd /home/jenkins/agent/workspace/${env.JOB_NAME}; python3 app.py"
            }
        }
    }
}
