pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Python Env') {
            steps {
                sh 'python -m venv $VENV_DIR'
                sh './$VENV_DIR/Scripts/pip install --upgrade pip'
                sh "./$VENV_DIR/Scripts/pip install -r requirements.txt"
            }
        }

        stage('Run App') {
            steps {
                sh "./$VENV_DIR/Scripts/python app.py"
            }
        }
    }
}
