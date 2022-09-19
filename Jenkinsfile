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
        input 'Lanjutkan ke tahap Deploy?'
    }
    
    // stage('Deploy') {
    //     sh "docker run --rm -v \$(pwd)/sources:/src cdrx/pyinstaller-linux:python2 'pyinstaller -F /sources/add2vals.py'"
    //     archiveArtifacts 'dist/add2vals'
    // }
    

    withDockerContainer(image: 'cdrx/pyinstaller-linux:python2') {
        stage('Deploy') {
            //wait until pyinstaller is installed
            sh 'sleep 10'

            sh 'pyinstaller --onefile sources/add2vals.py'
            archiveArtifacts 'dist/add2vals'
        }
    }
}