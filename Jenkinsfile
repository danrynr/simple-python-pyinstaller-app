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
    withDockerContainer(image: 'cdrx/pyinstaller-linux:python2'){
        stage('Deliver') {
            sh "docker run --rm -v $(pwd)/sources:/src cdrx/pyinstaller-linux:python2 'pyinstaller -F sources/add2vals.py'"
            archiveArtifacts{
                pattern('dist/add2vals')
            }
        }
    }
}