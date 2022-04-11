pipeline {
  agent any 
  environment {
    //DEBUG = 'false'
    GIT_USERNAME = 'hakobmkoyan771'
    GIT_REPO = 'TestRepo'
    DOCKERHUB_CREDENTIALS = credentials('docker-repo')
  }
  stages {
    stage("Build application image") {
      agent {
        label 'Master' 
      }
      steps {
        script {
          sh "cd ./app/; docker build -t hakobmkoyan771/flaskapp ."
        }
      }
    }
    stage("Deploy application image") {
      agent {
        label 'Master' 
      }
      steps {
        script {
          sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin --password-stdin'
          sh "docker image push ${DOCKERHUB_CREDENTIALS_USR}/flaskapp:latest"
        }
      }       //ERRORMESSAGE: Error saving credentials: error storing credentials - err: exit status 1, out: `Cannot autolaunch D-Bus without X11 $DISPLAY`
    }
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
              error()
              script {
                LOCAL_ERR = 'true'
              }
              break;
            }
          }
        }
      }
    }
    stage("Running application on dev") {
      when {
        expression {
          DEBUG == "true" 
        }
      }
      agent {
        label 'Slave-1' 
      }
      steps {
        //sh "python3 ./app/app.py"
        //sh 'docker run -d -p 5040:5000 hakobmkoyan771/flaskapp'
        sh 'docker images'
      }
    }
    stage("Running application on prod") {
      when {
        expression {
          DEBUG == "false" 
        }
      }
      agent {
        label 'Slave-2' 
      }
      steps {
        //sh "python3 ./app/app.py"
        //sh 'docker run -d -p 5050:5000 hakobmkoyan771/flaskapp'
        sh 'docker images'
      }
    }
  }
}
