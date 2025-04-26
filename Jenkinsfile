pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Clone Repo') {
            steps {
                git 'https://github.com/NaquiyaJuzar/Farm_Intrusion_Detection_System.git'
            }
        }

        stage('Setup Python Env') {
            steps {
                sh 'python3 -m venv $VENV_DIR'
                sh './$VENV_DIR/bin/pip install --upgrade pip'
                sh "./$VENV_DIR/bin/pip install -r requirements.txt"
            }
        }

        stage('Run App') {
            steps {
                sh "./$VENV_DIR/bin/python app.py"
            }
        }
    }
}
