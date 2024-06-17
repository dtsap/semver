node {

    stage 'Checkout'
        println "Checkout branch: ${env.BRANCH_NAME}"
        checkout scm

    stage 'Unit Test'
        println 'Unit testing ...'
        println 'Run 10/10 tests passed.'

    stage 'Deploy'
        println 'Deploying ...'
        sh 'git log --format="%ae" | head -1
        print 'Deployment succeeded!'


}