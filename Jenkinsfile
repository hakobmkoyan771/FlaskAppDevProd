pipeline {
  agent any 
  environment {
    RELEASE = ''
    GIT_USERNAME = ''
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
      steps {
        //${env.RELEASE} = sh returnStdout: true, script: "curl  https://api.github.com/${GIT_USERNAME}/${GIT_REPO}/releases/latest"
        withCredentials([usernamePassword(credentialsId: 'git-id', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
          $GIT_USERNAME = $USERNAME
        }          
        sh "echo user $GIT_USERNAME"
      }
    }
  }
}
