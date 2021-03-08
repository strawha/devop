pipeline {
    environment {
        registry = "vikrant1strawha/devop"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    agent any
    stages {
       stage('Build') {
            steps{
                script {
                    dockerImage = docker.build registry + ":latest"
                }
            }
        }
        stage('test'){
            steps {
                sh 'pip3 install pytest'
                sh 'pytest'
            }
        }
        stage('Archive'){
            steps{
                script {
                    docker.withRegistry( '', registryCredential ) {
                    dockerImage.push()
                    }
                }
            }
        }
        stage('Deploy'){
            steps{
                 ansiblePlaybook becomeUser: null, colorized: true, disableHostKeyChecking:true, installation: 'Ansible', inventory: 'inventory', playbook: 'deploy.yml', sudoUser:null
            }
        }
    }
}
