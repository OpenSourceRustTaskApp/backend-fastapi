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