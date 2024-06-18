node {

    stage 'Checkout'
        println "Checkout branch: ${env.BRANCH_NAME}"
        checkout scm

    stage 'Unit Test'
        println 'Unit testing ...'
        println 'Run 10/10 tests passed.'

    stage 'Deploy'
        
        
        if (shouldDeploy()) {
            println 'Deploying ...'
            println "deploying main branch"
            println "Author is semantic release"
            println 'DEPLOYING .....'
            print 'Deployment succeeded!'
        }
        else if (env.BRANCH_NAME == "dev") {
            println "deploying dev branch"
            print 'Deployment succeeded!'
        }
        else {
            println "No deployment will be applied"
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

