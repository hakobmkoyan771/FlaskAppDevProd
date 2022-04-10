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
  parameters {
    string(name: '') 
  }
  stages {
    stage("Request Git Release API") {
      agent {
        label 'Master'
      }
      steps {
        RELEASE = sh returnStdout: true, script: "curl  https://api.github.com/${GIT_USERNAME}/${GIT_REPO}/releases/latest"
        echo ${RELEASE}
      }
    }
  }
}
