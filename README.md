# タスク管理Webアプリ (ToDoリスト)

PythonのFlaskフレームワークを使用したシンプルなタスク管理Webアプリケーションです。

## 機能

- タスクの新規追加（タイトル＋完了フラグ）
- タスクの一覧表示（現在登録されているタスクを表示）
- タスクの完了フラグの切り替え
- タスクの削除
- SQLiteデータベースでのタスク管理（データ永続化）

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

## データベース

アプリケーションはSQLiteデータベース（`tasks.db`）を使用してタスクデータを永続化します。データベースファイルは初回起動時に自動的に作成され、以下のテーブル構造を持ちます：

```sql
CREATE TABLE tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    title TEXT NOT NULL,
    completed INTEGER DEFAULT 0
);
```

データベースファイルはアプリケーション再起動後もデータを保持します。

## ルート構成

- `/` : タスク一覧と追加フォームを表示
- `/add` : タスク追加 (POST)
- `/toggle` : タスクの完了フラグを切り替え (POST)
- `/delete` : タスクの削除 (POST)

## ファイル構成

```
├── app.py                 # メインのFlaskアプリケーション
├── templates/
│   └── index.html        # HTMLテンプレート
├── requirements.txt      # Python依存関係
├── tasks.db              # SQLiteデータベース（実行時に自動作成）
└── README.md            # このファイル
```