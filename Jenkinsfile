pipeline {
  agent any 
  stages {
    stage("Build Server image") {
      steps {
        sh 'docker build -f ./server/Dockerfile -t jenkins-server'
      }
    }
    stage("Build Dev image") {
      steps {
        sh 'docker build -f ./agents/dev-ag-1/Dockerfile -t jenkins-agent-1'
      }
    }
    stage("Build Prod image") {
      steps {
        sh 'docker build -f ./agents/prod-ag-2/Dockerfile -t jenkins-agent-2'
      }
    }
  }
}
