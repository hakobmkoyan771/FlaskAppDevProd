pipeline {
	agent any
	stages {
		stage("First-Initial") {
			agent {
				docker {
					image 'ubuntu'
					args '-u 0'
				}
			}
			steps {
				sh 'ls | grep workspace'
			}
		}
	}
}
