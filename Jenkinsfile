pipeline {
    agent any
    environment {
        DOCKER_IMAGE_NAME = 'calculator'
	DOCKER_TEST_IMAGE_NAME = 'selenium-webdriver'
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
                    image = docker.build("${DOCKER_IMAGE_NAME}", '.')
                }                
            }
        }
	stage('Run') {
            steps {
		script{
		container = image.run("-d -p 8090:80")
		}
            }
        }
	stage('Test') {
	   steps {
		script{
		       dir('testing')
		       {
		      	 //def output = sh(returnStdout: true, script: 'pwd')
			//echo "Output: ${output}"
			       sh 'pwd'
			       test_image = docker.build("${DOCKER_TEST_IMAGE_NAME}",'.')
			       test_container = test_image.run("-d")
		       }
		}
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
    stage('Terminate') {
            steps {
		script{
		container.stop()
		test_container.stop()
		}
            }
        }
    }
}
