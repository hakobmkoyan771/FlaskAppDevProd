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
            withCredentials([usernamePassword(credentialsId: 'git-id', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
              sh returnStdout: true, script: '''rel=$(curl https://api.github.com/repos/hakobmkoyan771/TestRepo/releases?client_id=${USERNAME}&client_secret=${PASSWORD}; echo $rel)'''
              RELEASE = sh returnStdout: true, script: '''echo $rel | grep 'prerelease' | awk '{print $2}' | awk 'FNR == 1 {print}' '''
              echo RELEASE
            }
          //RELEASE = sh returnStdout: true, script: '''rel=$(curl https://api.github.com/repos/hakobmkoyan771/TestRepo/releases | grep 'prerelease' | awk '{print $2}') | awk 'FNR == 2 {print}'; echo $rel'''
        }
        //echo $RELEASE
      }
    }
  }
}
