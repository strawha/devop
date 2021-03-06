pipeline {
    environment {
        registry = "vikrant1strawha/devop"
        registryCredential = 'dockerhub'
        dockerImage = ''
    }
    aagent any
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
    }
}
