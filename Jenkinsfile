pipeline {
    agent any
    parameters {
        string(name: 'DISTANCIA', description: 'Limiar de distancia de busca.')
        string(name: 'PERGUNTA', description: 'Pergunta a ser feita')
    }
    stages {
        stage('Preparação do Ambiente') {
            steps {
                
                echo 'ja instalado'
            }
        }

        stage('Execução do Teste Levenshtein') {
            steps {
                sh 'python3 levenshtein_teste.py'
            }
        }

        stage('Verificação do Arquivo de Perguntas') {
            steps {
                script {
                    if (fileExists('perguntas.txt')) {
                        echo 'Arquivo perguntas.txt encontrado!'
                    } else {
                        error('Arquivo perguntas.txt não encontrado. Interrompendo o pipeline.')
                    }
                }
            }
        }

        stage('Execução do Chatbot') {
            steps {
                sh 'python3 chat_bot.py "${DISTANCIA}" "${PERGUNTA}"'
            }
        }
    }
    post {
        always {
            mail body: 'Build de pergunta executado', cc: '', subject: 'Executado Build', to: 'hfraia@yahoo.com.br'
        }
    }
}
