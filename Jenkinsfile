pipeline {
    agent none
    environment {
        ENV = "dev"
    }
    parameters {
         string(defaultValue: "DEV", description: 'Environment to deploy to?', name: 'ENV')
    }
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
