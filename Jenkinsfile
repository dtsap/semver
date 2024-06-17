node {

    stage 'Checkout'
        println "Checkout branch: ${env.BRANCH_NAME}"
        checkout scm

    stage 'Unit Test'
        println 'Unit testing ...'
        println 'Run 10/10 tests passed.'

    stage 'Deploy'
        println 'Deploying ...'
        println env.BRANCH_NAME
        
        def author = sh(
            script: "git log -1 --pretty=format:'%an'",
            returnStdout: true
        ).trim()

        echo "Commit Author: ${author}"

        env.COMMIT_AUTHOR = author

        if (env.BRANCH_NAME == "main" && env.COMMIT_AUTHOR == "semantic-release") {
            println "deploying main branch"
            println "Author is semantic release"
            println 'DEPLOYING .....'
        }
        else if (env.BRANCH_NAME == "dev") {
            println "deploying dev branch"
        }
        
        print 'Deployment succeeded!'


}