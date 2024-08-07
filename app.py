from flask import Flask, render_template, request, jsonify
import sqlite3

app = Flask(__name__)

# إعداد قاعدة البيانات SQLite
def init_db():
    with sqlite3.connect('donations.db') as conn:
        cursor = conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS donations (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                email TEXT NOT NULL,
                amount REAL NOT NULL
            )
        ''')
        conn.commit()

# الصفحة الرئيسية
@app.route('/')
def index():
    return render_template('index.html')

# صفحة تبرع
@app.route('/donate', methods=['POST'])
def donate():
    data = request.form
    name = data['name']
    email = data['email']
    amount = float(data['amount'])  # تحويل المبلغ إلى عدد عشري

    # إضافة التبرع إلى قاعدة البيانات
    with sqlite3.connect('donations.db') as conn:
        cursor = conn.cursor()
        cursor.execute('INSERT INTO donations (name, email, amount) VALUES (?, ?, ?)', (name, email, amount))
        conn.commit()

    return jsonify({'message': 'تم التبرع بنجاح!'})

if __name__ == '__main__':
    init_db()
    app.run(debug=True)
