pipeline {
    agent any

    environment {
        VENV_DIR = 'venv'
    }

    stages {
        stage('Setup Python Env') {
            steps {
                bat 'python -m venv %VENV_DIR%'
                bat "venv\\Scripts\\python.exe -m pip install --upgrade pip"
                bat '%VENV_DIR%\\Scripts\\pip install -r requirements.txt'
            }
        }

        stage('Run App') {
            steps {
                bat '%VENV_DIR%\\Scripts\\python app.py'
                call venv\\Scripts\\activate
                pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu
                python app.py
            }
        }
    }
}
