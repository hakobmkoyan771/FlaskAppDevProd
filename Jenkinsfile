pipeline {
  agent any 
  stages {
    stage("Build Dev image") {
      steps {
        step([$class: 'DockerBuilderPublisher', cleanImages: false, cleanupWithJenkinsJobDelete: false, cloud: '', dockerFileDirectory: 'server/', fromRegistry: [], noCache: true, pushCredentialsId: '', pushOnSuccess: false, tagsString: ''])
      }
    }
  }
}
