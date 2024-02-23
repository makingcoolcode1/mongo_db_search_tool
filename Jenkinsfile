pipeline{
    agent any

    stages{
        stage("SCM"){
            steps{
                checkout scm
            }
        }

        stage("SonarQube Analysis"){
            steps{
                script{
                    def scannerHome = tool 'sonar_scanner_1';
                    withSonarQubeEnv() {
                        sh "${scannerHome}/bin/sonar-scanner"
                }

                }
            }
        }
    }
}