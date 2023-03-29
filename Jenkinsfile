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
                      docker.image('selenoid/chrome:110.0')
      	      }
      	   }
        }
     }
  }
}
