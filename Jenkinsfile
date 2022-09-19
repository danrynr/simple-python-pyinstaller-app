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
    
    stage('Deploy') {
        // sh "docker run --rm -v \$(pwd)/sources:/src cdrx/pyinstaller-linux:python2 'pyinstaller -F /sources/add2vals.py'"
        // sh "docker run --rm -v \$(pwd):/src/ cdrx/pyinstaller-linux:python2"
        sh "docker pull cdrx/pyinstaller-linux:python2"
        sh "docker run --rm -v \$(pwd):/src/ cdrx/pyinstaller-linux:python2 'pyinstaller -F /src/sources/add2vals.py'"
        // sh 'pyinstaller -F /src/add2vals.py'
        archiveArtifacts 'dist/add2vals'
    }
}