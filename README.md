# Backend FastAPI プロジェクト

概要を記述

## プロジェクト構造

```
.
├── app/
│   ├── api/
│   │   └── v1/
│   │       └── endpoints/
│   ├── core/
│   ├── db/
│   ├── models/
│   ├── repositories/
│   ├── schemas/
│   ├── services/
│   └── main.py
├── docker-entrypoint-initdb.d/
├── Dockerfile
├── docker-compose.yml
├── requirements.txt
└── README.md
```

## ディレクトリの説明

- `app/`: メインアプリケーションパッケージ
  - `api/`: API関連のコード
    - `v1/`: APIのバージョン1
      - `endpoints/`: 個別のAPIエンドポイント
  - `core/`: アプリケーションのコア機能（設定など）
  - `db/`: データベース関連のコード（接続処理など）
  - `models/`: SQLAlchemy ORMモデル
  - `repositories/`: データアクセス層（データベース操作を担当）
  - `schemas/`: リクエスト/レスポンス用のPydanticモデル
  - `services/`: ビジネスロジック層
  - `main.py`: FastAPIアプリケーションのメインインスタンスと設定

- `docker-entrypoint-initdb.d/`: データベース初期化用のSQLスクリプト
- `Dockerfile`: アプリケーションのDockerイメージビルド用の指示書
- `docker-compose.yml`: ローカル開発用のDocker Compose設定
- `requirements.txt`: Pythonパッケージの依存関係

## セットアップと実行方法

1. DockerとDocker Composeがインストールされていることを確認してください。
2. このリポジトリをクローンします。
3. プロジェクトディレクトリに移動します。
4. `docker-compose up --build` を実行して、アプリケーションとデータベースを起動します。
5. APIは `http://localhost:8080` で利用可能になります。

## APIドキュメント

アプリケーションが起動したら、以下のURLで自動生成されたAPIドキュメントにアクセスできます：

- Swagger UI: `http://localhost:8080/docs`
- ReDoc: `http://localhost:8080/redoc`

## データベースマイグレーション

このプロジェクトではAlembicを使用してデータベースマイグレーションを管理しています。以下のコマンドを使用してマイグレーションを実行できます：

- 新しいマイグレーションの作成:
  ```
  make migrate-revision message="変更の説明"
  ```

- マイグレーションの適用:
  ```
  make migrate-upgrade
  ```

- 直前のリビジョンへのダウングレード:
  ```
  make migrate-downgrade
  ```

- マイグレーション履歴の表示:
  ```
  make migrate-history
  ```

- 現在のリビジョンの表示:
  ```
  make migrate-current
  ```

## 開発

新機能の追加や既存機能の修正を行う場合：

1. `app/api/v1/endpoints/` にエンドポイントを作成または修正します。
2. `app/models/` にデータモデルを定義します。
3. `app/schemas/` にPydanticスキーマを作成します。
4. `app/repositories/` にデータアクセスロジックを実装します。
5. `app/services/` にビジネスロジックを追加します。
6. 必要に応じて `app/main.py` を更新し、新しいルーターを追加します。

## マイグレーションの開発フロー

1. モデル（`app/models/`）を変更または新規作成します。
2. 新しいマイグレーションを生成します: `make migrate-revision message="変更の説明"`
3. 生成されたマイグレーションファイル（`alembic/versions/`内）を確認し、必要に応じて編集します。
4. マイグレーションを適用します: `make migrate-upgrade`
5. アプリケーションを再起動し、変更が正しく反映されていることを確認します。

## テスト

（テストを実装した後、テストの実行方法に関する情報を追加してください）

## コントリビューション

（プロジェクトへの貢献に関するガイドラインを追加してください）

## ライセンス

このプロジェクトは、リポジトリに含まれるLICENSEファイルの条件に基づいてライセンスされています。