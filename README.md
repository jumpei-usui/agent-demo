# タスク管理Webアプリ (ToDoリスト)

PythonのFlaskフレームワークを使用したシンプルなタスク管理Webアプリケーションです。

## 機能

- タスクの新規追加（タイトル＋完了フラグ）
- タスクの一覧表示（現在登録されているタスクを表示）
- タスクの完了フラグの切り替え
- メモリ上でのタスク管理（Pythonリスト使用）

## 使用方法

### 1. 依存関係のインストール

```bash
pip install -r requirements.txt
```

### 2. アプリケーションの起動

```bash
python app.py
```

### 3. ブラウザでアクセス

ブラウザで `http://localhost:5000` にアクセスしてください。

## ルート構成

- `/` : タスク一覧と追加フォームを表示
- `/add` : タスク追加 (POST)
- `/toggle` : タスクの完了フラグを切り替え (POST)

## ファイル構成

```
├── app.py                 # メインのFlaskアプリケーション
├── templates/
│   └── index.html        # HTMLテンプレート
├── requirements.txt      # Python依存関係
└── README.md            # このファイル
```