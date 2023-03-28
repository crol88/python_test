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
     stage('Run tests') {
        steps {
           catchError {
              script {
          	     docker.image('python-web-tests')
        	     }
      	    }
         }
     }
     stage('Reports') {
        steps {
           allure([
      	   includeProperties: false,
      	   jdk: '',
      	   properties: [],
      	   reportBuildPolicy: 'ALWAYS',
      	   results: [[path: 'report']]
    	   ])
  	        }
         }
     }
}