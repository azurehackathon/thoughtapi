pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
              label "docker_slave"
            }
            steps {
                container('docker') {
                    sh 'docker build -t euwmgmt030cdoacr.azurecr.io/thought-api .'
                }
            }
        }
    }
}
