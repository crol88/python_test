pipeline {
  agent any
  stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
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
  }
}
