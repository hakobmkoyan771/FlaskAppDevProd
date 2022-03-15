pipeline {
	agent any
	stages {
		stage("First-Initial") {
			agent {
				dockerfile true	
			}
			steps {
				sh 'ls /* | grep workspace'
			}
		}
	}
}
