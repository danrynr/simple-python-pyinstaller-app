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
    // Deploy stage, and wait 1 minute after deploy before end the pipeline
    // withDockerContainer(image: 'cdrx/pyinstaller-linux') {
        // stage('Deploy') {
        //     sh 'docker pyinstaller --onefile --clean --distpath dist --workpath build sources/add2vals.py'
        //     sleep 60
        // }
        stage('Deploy') {
            sh 'echo "Deploy"'
        }
    // }
    







    // withDockerContainer(image: 'cdrx/pyinstaller-linux:python2') {
    //     stage('Deploy') {
    //         sh 'pyinstaller --onefile sources/add2vals.py'
    //         archiveArtifacts 'dist/add2vals'
    //     }
    // }
}