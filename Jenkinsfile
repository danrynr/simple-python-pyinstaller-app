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
        sh "docker run --rm -v cdrx/pyinstaller-linux:python2 'pyinstaller -F /sources/add2vals.py'"
        archiveArtifacts 'dist/add2vals'
    }
    // \$(pwd)/sources:/src
    







    // withDockerContainer(image: 'cdrx/pyinstaller-linux:python2') {
    //     stage('Deploy') {
    //         sh 'pyinstaller --onefile sources/add2vals.py'
    //         archiveArtifacts 'dist/add2vals'
    //     }
    // }
}