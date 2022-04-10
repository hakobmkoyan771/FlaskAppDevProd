pipeline {
  agent any 
  environment {
    DEBUG = 'false'
    GIT_USERNAME = 'hakobmkoyan771'
    GIT_REPO = 'TestRepo'
  }
  stages {
    stage("Request Git Release API") {
      agent {
        label 'Master'
      }
      steps {
        script {
          RELEASE = sh returnStdout: true, script: '''rel=$(curl https://api.github.com/repos/hakobmkoyan771/TestRepo/releases | grep 'prerelease' | awk '{print $2}' | awk 'FNR == 1 {print}'); echo $rel'''
          for(el in RELEASE) {
            if(el == "t") { // if RELEASE variable is true and the first char is 't'
              DEBUG = 'true'
              break;
            }
            else if(el == "f") { // if RELEASE variable is false and the first char is 'f'
              DEBUG = 'false'
              break;
            }
            else {
              error("Broken link")
              break;
            }
          }
        }
      }
    }
    stage("Copying application on dev") {
      when {
        environment(name: "DEBUG", value: 'true')
      }
      agent {
        label 'Slave-1' 
      }
      steps {
        sh 'ls'
        sh "python3 /home/jenkins/agent-1/workspace/${env.JOB_NAME}/app/app.py"
      }
    }
    stage("Copying application on prod") {
      when {
        environment(name: "DEBUG", value: 'false')
      }
      agent {
        label 'Slave-2' 
      }
      steps {
        sh 'ls'
        sh "python3 /home/jenkins/agent-1/workspace/${env.JOB_NAME}/app/app.py"
      }
    }
  }
}
