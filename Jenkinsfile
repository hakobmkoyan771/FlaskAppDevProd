pipeline {
	agent any
	stages {
		stage("First-Initial") {
			agent {
				docker {
					image 'ubuntu:alpine'
					
					reuseNode true
				}
			}
			steps {
				sh 'ls /*'
			}
		}
	}
}
