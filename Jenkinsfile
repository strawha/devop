pipeline {
    environment {
        registry = "vikrant1strawha/devop"
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
        stage('Build') {
            steps{
                script {
                     dockerImage = docker.build registry + ":$BUILD_NUMBER"
        }
      }
    }
    stage('Deploy Image') {
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
