node {
    docker.image('ghcr.io/shr-jplf/pipeline-factory:main').inside{} 
    load "../${JOB_BASE_NAME}/resolved.groovy"
}



withCredentials([usernamePassword(credentialsId:'docker-login', passwordVariable: 'GH_TOKEN', usernameVariable: 'Username')]) {
    sh 'env'
    docker.image('ghcr.io/shr-jplf/pipeline-factory:main').inside{} 
    load "../${JOB_BASE_NAME}/resolved.groovy"
}