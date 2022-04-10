pipeline {
  agent any 
  stages {
    stage("Build Server image") {
      steps {
        sh 'docker build -t jenkins-server -f ./server/Dockerfile'
      }
    }
    stage("Build Dev image") {
      steps {
        sh 'docker build -t jenkins-agent-1 -f ./agents/dev-ag-1/Dockerfile'
      }
    }
    stage("Build Prod image") {
      steps {
        sh 'docker build -t jenkins-agent-2 -f ./agents/prod-ag-2/Dockerfile'
      }
    }
  }
}
