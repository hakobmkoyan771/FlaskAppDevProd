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
          RELEASE = sh(script: "curl https://api.github.com/repos/hakobmkoyan771/TestRepo/releases/latest | grep 'prerelease' | awk '{print ${2}}'", returnStdout: true).trim()
          echo $RELEASE
        }
        //echo $RELEASE
      }
    }
  }
}
