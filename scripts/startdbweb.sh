DATABASE_PATH="/home/ubuntu/dev_work/db.sqlite3.db"

# Iniciar o sqlite-web na porta 9080 e salvar a saída em um arquivo de log
nohup sqlite_web $DATABASE_PATH -p 3000 > sqlite_web.log 2>&1 &

