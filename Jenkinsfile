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
      script {
        env.RELEASE = env.GIT_USERNAME
      }
      //steps {
        //  //sh returnStdout: true, script: "curl  https://api.github.com/${GIT_USERNAME}/${GIT_REPO}/releases/latest"
        //sh "echo user ${env.RELEASE}"
//      }
    }
  }
}
