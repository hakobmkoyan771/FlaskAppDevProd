pipeline {
  agent any 
  stages {
    stage("Build Images") {
      parallel {
        stage("Build Server image") {
          steps {
            step([$class: 'DockerBuilderPublisher', cleanImages: false, cleanupWithJenkinsJobDelete: false, cloud: '', dockerFileDirectory: './server/', fromRegistry: [], noCache: true, pushCredentialsId: '', pushOnSuccess: false, tagsString: ''])
          }
        }
        stage("Build Dev image") {
          steps {
            step([$class: 'DockerBuilderPublisher', cleanImages: false, cleanupWithJenkinsJobDelete: false, cloud: '', dockerFileDirectory: './agents/dev-ag-1', fromRegistry: [], noCache: true, pushCredentialsId: '', pushOnSuccess: false, tagsString: ''])
          }
        }
        stage("Build Prod image") {
          steps {
            step([$class: 'DockerBuilderPublisher', cleanImages: false, cleanupWithJenkinsJobDelete: false, cloud: '', dockerFileDirectory: './agents/prod-ag-2', fromRegistry: [], noCache: true, pushCredentialsId: '', pushOnSuccess: false, tagsString: ''])
          }
        }
      }
    }
  }
}
