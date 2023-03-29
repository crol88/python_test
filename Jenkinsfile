pipeline {
  agent any
  stages {
     stage("Initialize") {
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
     }
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
