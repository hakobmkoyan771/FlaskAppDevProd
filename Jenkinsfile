pipeline {
  agent any 
  environment {
    GIT_USERNAME = 'hakobmkoyan771'
    GIT_REPO = 'TestRepo'
  }
  options {
    timeout(time: 5, unit: 'MINUTES') 
  }

  stages {
    stage("Request Git Release API") {
      agent {
        label 'Master'
      }
      //steps {
        //sh "echo user ${GIT_USERNAME}"
      //}
      steps {
        script {
          RELEASE = sh returnStdout: true, script: '''rel=$(curl https://api.github.com/repos/hakobmkoyan771/TestRepo/releases/latest | grep 'prerelease'); echo $rel'''
          echo RELEASE
        }
        //echo $RELEASE
      }
    }
  }
}
