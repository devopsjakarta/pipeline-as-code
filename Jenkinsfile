node{
    stage('Dev') {
        checkout scm
        sh "echo 'Running test...'"
    }

    stage('Staging') {
        deploy('staging')
    }

    stage("QA") {
        parallel(
            test1: { runTests(10) },
            test2: { runTests(20) }
        )
    }
    
    stage('Production') {
        input "Does staging looks good?"
        deploy('production')
    }
}

def runTests(duration) {
    node {
        sh """
          nosetests src/test.py
          sleep ${duration}
        """
    }
}

def deploy(id) {
    if (id == "staging"){
        port = '8989'
    }
    else if (id == "production"){
        port = '8000'
    }
    sh "./server.py ${port} > output.log 2>&1 &"
    sh "echo 'Deployed to ${id}'"
}
