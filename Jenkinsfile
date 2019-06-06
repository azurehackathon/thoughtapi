pipeline {
    agent any
    stages {
        stage('Build') {
            agent {
              label "docker_slave"
            }
            steps {
                sh 'sudo docker build -t euwmgmt030cdoacr.azurecr.io/thought-api .'
            }
        }
    }
}
