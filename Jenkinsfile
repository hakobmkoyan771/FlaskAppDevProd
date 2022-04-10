pipeline {
  agent any 
  environment {
    RELEASE = ''
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
        echo "${GIT_COMMITTER_NAME}"
        //RELEASE = sh returnStdout: true, script: 'curl  https://api.github.com/repos/octocat/hello-world/releases/latest' 
      }
    }
  }
}
