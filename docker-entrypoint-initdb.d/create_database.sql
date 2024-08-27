-- データベースが存在しない場合は作成
CREATE DATABASE IF NOT EXISTS ta1;

-- データベースを選択
USE ta1;

-- データベースのデフォルト文字セットと照合順序を設定 (既存のデータベースにも適用可能)
ALTER DATABASE ta1 CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci;

-- ユーザーが存在しない場合は作成し、パスワードを設定
CREATE USER IF NOT EXISTS 'app_user' @'%' IDENTIFIED BY 'sgL2XM5abQsc';

-- ユーザー 'app_user' にデータベース 'ta1' への全ての権限を付与
GRANT ALL PRIVILEGES ON ta1.* TO 'app_user' @'%';

-- 権限の変更を反映
FLUSH PRIVILEGES;

-- m_users テーブルの作成
CREATE TABLE IF NOT EXISTS m_users (
  id bigint AUTO_INCREMENT PRIMARY KEY,
  username varchar(20) NOT NULL,
  created_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP,
  updated_at datetime NOT NULL DEFAULT CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP,
  updated_by bigint NOT NULL,
  is_deleted tinyint NOT NULL DEFAULT 0
) ENGINE = InnoDB DEFAULT CHARSET = utf8mb4 COLLATE = utf8mb4_general_ci;

-- インデックスの追加（必要に応じて）
CREATE INDEX idx_username ON m_users(username);

CREATE INDEX idx_is_deleted ON m_users(is_deleted);