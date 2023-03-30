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
          	     docker.image('selenium/standalone-chrome:4.8.1-20230306').withRun('-p 4444:4444 --shm-size="2g"') { c ->
              	docker.image('python-web-tests') {
                    	sh "pytest -n 2 ${CMD_PARAMS}"
                	    }
                   }
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
}
