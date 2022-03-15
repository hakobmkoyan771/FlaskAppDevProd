pipeline {
	agent any
	stages {
		stage("First-Initial") {
			agent {
				docker {
					image 'ubuntu'
					
					reuseNode true
				}
			}
			steps {
				sh 'ls /* | grep workspace'
			}
		}
	}
}
