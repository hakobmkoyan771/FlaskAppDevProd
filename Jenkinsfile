pipeline {
  agent any 
  environment {
    DEBUG = false
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
          if(RELEASE == "true,") {
            DEBUG = true
          }
          else if(RELEASE == "false,") {
            DEBUG = false
          }
          else {
            error("Broken link")
          }
        }
      }
    }
    stage("Start application on prod") {
      when {
        DEBUG == false
      }
      agent {
        label 'Slave-2' 
      }
      steps {
        sh "docker cp jenkins:/bitnami/jenkins/home/workspace/${env.JOB_NAME}/app/app.py /app/app.py"
        sh "python3 /app/app.py"
      }
    }
    stage("Start application on dev") {
      when {
        DEBUG == true 
      }
      agent {
        label 'Slave-1' 
      }
      steps {
        sh "docker cp jenkins:/bitnami/jenkins/home/workspace/${env.JOB_NAME}/app/app.py /app/app.py"
        sh "python3 /app/app.py"
      }
    }
  }
}
