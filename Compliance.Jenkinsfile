node {
    withCredentials([usernamePassword(credentialsId:'docker-login', passwordVariable: 'GH_TOKEN', usernameVariable: 'Username')]) {
        docker.image('ghcr.io/shr-jplf/pipeline-factory:main').inside{
            sh "python /app/factory.py"
        } 
        load "../${JOB_BASE_NAME}/resolved.groovy"
    }
}