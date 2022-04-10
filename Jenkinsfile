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
        RELEASE = sh returnStdout: true, script: "curl  https://api.github.com/${env.GIT_USERNAME}/${env.GIT_REPO}/releases/latest"
        sh "echo user ${env.GIT_USERNAME}"
      }
    }
  }
}
