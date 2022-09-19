node {
    withDockerContainer(image: 'python:2-alpine') {
        stage('Build') {
            sh 'python -m py_compile sources/add2vals.py sources/calc.py'
        }
    }
    withDockerContainer(image: 'qnib/pytest') {
        stage('Test') {
            sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            junit 'test-reports/results.xml'
        }
    }
    stage('Manual Approval') {
        sh 'echo "Approval"'
        input 'Lanjutkan ke tahap Deploy?'
    }
    
        stage('Deploy') {
            environment {
                VOLUME = '$(pwd)/sources:/sources'
                IMAGE = 'cdrx/pyinstaller-linux'
            }

            sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F /sources/add2vals.py'"
        }
    // }
    







    // withDockerContainer(image: 'cdrx/pyinstaller-linux:python2') {
    //     stage('Deploy') {
    //         sh 'pyinstaller --onefile sources/add2vals.py'
    //         archiveArtifacts 'dist/add2vals'
    //     }
    // }
}