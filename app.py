from flask import Flask, redirect, render_template, request, url_for
import os

items = []

def normalize_item(item):
    """Normalize an item by stripping whitespace and title-casing."""
    return item.strip().title() if item else ""

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def index():
        return render_template('index.html', items=items)

    @app.route('/health')
    def health():
        return {"status": "ok"}

    @app.route('/add', methods=['POST'])
    def add_item():
        item = request.form.get('item')
        if item:
            items.append(normalize_item(item))
        return redirect(url_for('index'))

    @app.route('/delete/<int:index>')
    def delete_item(index):
        if index < len(items):
            items.pop(index)
        return redirect(url_for('index'))

    @app.route('/update/<int:index>', methods=['POST'])
    def update_item(index):
        if index < len(items):
            items[index] = normalize_item(request.form.get('new_item'))
        return redirect(url_for('index'))

    return app

app = create_app()

if __name__ == '__main__':
    app.run(debug=True)
