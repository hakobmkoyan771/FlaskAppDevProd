pipeline {
  agent any 
  stages {
    stage("Build Server image") {
      steps {
        sh 'cd ./server; docker build -t jenkins-server .'
      }
    }
    stage("Build Dev image") {
      steps {
        sh 'cd ./agents/dev-ag-1/; docker build -t jenkins-agent-1 .'
      }
    }
    stage("Build Prod image") {
      steps {
        sh 'cd ./agents/prod-ag-2/; docker build -t jenkins-agent-2 .'
      }
    }
  }
}
