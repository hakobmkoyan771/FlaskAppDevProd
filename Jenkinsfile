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
      steps {
        //def RELEASE = sh(script: "curl  https://api.github.com/${env.GIT_USERNAME}/${env.GIT_REPO}/releases/latest", returnStdout: true)
        sh "echo user ${GIT_USERNAME}"
      }
    }
  }
}
