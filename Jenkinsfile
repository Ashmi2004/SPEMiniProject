pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'calculator'
        GITHUB_REPO_URL = 'https://github.com/Ashmi2004/SPEMiniProject.git'
	DOKCERHUB_CREDENTIALS = credentials('DockerHubCred')
    }
    stages {
        stage('Checkout') {
            steps {
                script {
                    // Checkout the code from the GitHub repository
                    git branch: 'main', url: "${GITHUB_REPO_URL}"
                }
            }
        }
        stage('Build Docker Image') {
            steps {
               script {
                    // Build Docker image
                    docker.build("${DOCKER_IMAGE_NAME}", '.')
                }                
            }
        }
	stage('Test') {
	    steps {
		sh '''
	 	cd /app
                python testing/test.py
		'''
		}
	}
        stage('Push Docker Images') {
            steps {
                script{
                    docker.withRegistry('', 'DockerHubCred') {
                    sh 'docker tag calculator asmita963/calculator:latest'
                    sh 'docker push asmita963/calculator'
                    }
                 }
            }
        }
   stage('Run Ansible Playbook') {
            steps {
                script {
                    ansiblePlaybook(
                        playbook: 'deploy.yml',
                        inventory: 'inventory'
                     )
                }
            }
        }
    }
}
