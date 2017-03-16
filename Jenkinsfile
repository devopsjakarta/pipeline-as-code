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
            test1: { runTests(10,'staging') },
            test2: { runTests(20,'staging') }
        )
    }

    stage('Production') {
        input "Does staging looks good?"
        deploy('production')
    }
    
    stage("Production Test") {
        parallel(
            test1: { runTests(10,'production') },
            test2: { runTests(20,'production') }
        )
    }
}

def runTests(duration, environment) {
    if (environment == "staging"){
        test = 'test1'
    }
    else if (environment == "production"){
        test = 'test2'
    }
    sh """
        nosetests src/${test}.py
        sleep ${duration}
    """
}

def deploy(id) {
    if (id == "staging"){
        port = '8989'
    }
    else if (id == "production"){
        port = '8000'
    }
    sh "cd src && ./server.py ${port} > output.log 2>&1 &"
    sh "echo 'Deployed to ${id}'"
}
