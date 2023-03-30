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
          	     docker.image('selenium/standalone-chrome:4.8.1-20230306').withRun('-d -p 4444:4444 --shm-size="2g"',
            	'-timeout 600s -limit 2') { c ->
              	docker.image('python-web-tests') {
                    	sh "pytest -n 2 --reruns 1 ${CMD_PARAMS}"
                	    }
                   }
        	     }
      	   }
        }
     }
  }
}
