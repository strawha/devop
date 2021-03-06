pipeline {
    environment {
        registry = "strawha/devop"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    agent any
    stages {
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
    }
}
