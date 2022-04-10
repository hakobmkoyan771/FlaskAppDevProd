pipeline {
  agent any 
  environment {
    RELEASE = ''
    GIT_USERNAME = 'hakobmkoyan771'
    GIT_REPO = 'TestRepo'
  }
  options {
    timeout(time: 5, unit: 'MINUTES') 
  }
  withCredentials([usernamePassword(credentialsId: 'git-id', usernameVariable: 'USERNAME', passwordVariable: 'PASSWORD')]) {
    sh "echo pass $PASSWORD"
    sh "echo user $USERNAME"
  }
  stages {
    stage("Request Git Release API") {
      agent {
        label 'Master'
      }
      steps {
        //${env.RELEASE} = sh returnStdout: true, script: "curl  https://api.github.com/${GIT_USERNAME}/${GIT_REPO}/releases/latest"
        sh "echo ${USERNAME}"
      }
    }
  }
}
