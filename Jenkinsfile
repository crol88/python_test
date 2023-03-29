pipeline {
  agent any
  stages {
     stage("Build image") {
        steps {
            catchError {
               script {
                      docker.build("python-web-tests", "-f Dockerfile .")
               }
            }
        }
     }
     stage('Pull browser') {
        steps {
           catchError {
              script {
                      docker.image('selenium/standalone-chrome:4.8.1-20230306')
      	      }
      	   }
        }
     }
  }
}
