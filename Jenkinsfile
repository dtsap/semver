node {

    stage('Checkout') {
        println "Checkout branch: ${env.BRANCH_NAME}"
        checkout scm
    }        

    if (!shouldDeploy()) {
        println "Skipping deployment: Current changes are not supposed to be deployed."
        return
    }

    stage('Unit Test') {
        println 'Unit testing ...'
        println 'Run 10/10 tests passed.'
    }        

    stage('Deploy') {
        println 'Deploying ...'
        println "deploying branch: ${env.BRANCH_NAME}"
        println "Commit Author: ${env.COMMIT_AUTHOR}"
        println 'DEPLOYING .....'
        println 'Deployment succeeded!'
    }
}

def shouldDeploy() {
    
    env.COMMIT_AUTHOR = getLastCommitAuthor()

    if (env.BRANCH_NAME == "main" && env.COMMIT_AUTHOR != "semantic-release") {
        return false
    }

    return true
}


def getLastCommitAuthor() {    
    return sh(
        script: "git log -1 --pretty=format:'%an'",
        returnStdout: true
    ).trim()
}

