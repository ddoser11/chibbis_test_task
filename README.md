# chibbis_test_task 🐦🐦🐦
Тестовое задание в компанию Chibbis на позицию Data Engineer


## Запуск скрипта - все необходимые команды

```powershell
git clone https://github.com/ddoser11/chibbis_test_task.git
cd chibbis_test_task
python -m venv .venv
.\.venv\Scripts\Activate.ps1
pip install -r requirements.txt
python .\main.py
```

После запуска создается файл базы данных `jsonplaceholder.db`.

## Небольшое описание того, что сделано 

- скрипт загружает данные из jsonplaceholder.typicode.com (users, posts, comments)
- сохраняет их в SQLite
- при повторном запуске записывает данные без дублирования путем upsert



