-- 初期化処理
DROP DATABASE chatapp;
DROP USER 'testuser'@'localhost';

-- ユーザーの作成 ユーザー名:testuser パスワード:testuser
CREATE USER 'testuser'@'localhost' IDENTIFIED BY 'testuser';
-- データベースの作成
CREATE DATABASE chatapp;

-- testuserにchatappデータベースの全テーブルへの権限を付与
USE chatapp;
GRANT ALL PRIVILEGES ON chatapp.* TO 'testuser'@'localhost';

-- usersテーブルの作成
--   [uid]ユーザーID:主キー、255字以内
--   [user_name]ユーザー名:255字以内、重複不可、空データ不可
--   [email]メールアドレス:255字以内、重複不可、空データ不可
--   [password]パスワード:255字以内、空データ不可
CREATE TABLE users (
    uid varchar(255) PRIMARY KEY,
    user_name varchar(255) UNIQUE NOT NULL,
    email varchar(255) UNIQUE NOT NULL,
    password varchar(255) NOT NULL
);

-- channnelsテーブルの作成
--   [id]チャンネルID:主キー、serial型はオートインクリメントの重複しない整数
--   [uid]ユーザーID:255字以内、userテーブルより参照
--   [name]チャンネル名:255字以内、重複不可、空データ不可
--   [abstract]チャンネル概要:255字以内
  -- [tid]タグID: 整数 tagsテーブルより参照
CREATE TABLE channels (
    id serial PRIMARY KEY,
    uid varchar(255) REFERENCES users(uid),
    name varchar(255) UNIQUE NOT NULL,
    abstract varchar(255)
);

-- messagesテーブルの作成
--   [id]メッセージID:主キー, serial型はオートインクリメントの重複しない整数
--   [uid]ユーザーID:255字以内, usersテーブルより参照
--   [cid]チャンネルID:整数型, channelsテーブルより参照, 親テーブルを削除するときに子テーブルも一緒に削除
--   [message]メッセージ: テキスト型
--   [created_at] timestamp型, 空データ不可, デフォルト:現在日時
CREATE TABLE messages (
  id serial PRIMARY KEY,
  uid varchar(255) REFERENCES users(uid),
  cid integer REFERENCES channels(id) ON DELETE CASCADE,
  message text,
  created_at timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP
);

-- tagsテーブルの作成
--   [id]タグID:主キー, serial型はオートインクリメントの重複しない整数
--   [name]タグ名:255文字以内, 重複不可, 空データ不可
CREATE TABLE tags (
  id serial PRIMARY KEY,
  name varchar(255) UNIQUE NOT NULL
);

CREATE TABLE channels_tags (
  cid integer REFERENCES channels(id),
  tid integer REFERENCES tags(id),
  UNIQUE(cid, tid)
);

-- 動作確認用データの挿入
-- テスト1とテスト2のuidとpasswordは最後の1文字だけ変えています。
INSERT INTO users(uid, user_name, email, password) VALUES('970af84c-dd40-47ff-af23-282b72b7cca8','テスト1','test1@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da578');
INSERT INTO channels(id, uid, name, abstract) VALUES(1, '970af84c-dd40-47ff-af23-282b72b7cca8','ブラジル注目選手','最近の注目選手について語ろう');

INSERT INTO users(uid, user_name, email, password)VALUES('970af84c-dd40-47ff-af23-282b72b7cca9','テスト2','test2@gmail.com','37268335dd6931045bdcdf92623ff819a64244b53d0e746d438797349d4da579');
INSERT INTO channels(id, uid, name, abstract)VALUES(2, '970af84c-dd40-47ff-af23-282b72b7cca9','アルゼンチンWC神プレーまとめ','アルゼンチン代表選手のワールドカップ神プレーをまとめるチャンネルです');

-- 動作確認用tagsデータの登録
INSERT INTO tags (id, name) VALUES
  (1, 'ブラジル'),
  (2, 'アルゼンチン'),
  (3, 'フランス'),
  (4, 'イングランド'),
  (5, 'クロアチア'),
  (6, 'スペイン'),
  (7, '日本代表'),
  (8, 'メッシ'),
  (9, '三苫薫'),
  (10, '久保健英'),
  (11, 'ブラボー'),
  (12, '本田圭佑'),
  (13, '長友佑都'),
  (14, 'ネイマール');

-- 動作確認用channels_tagsへデータの登録
INSERT INTO channels_tags (cid, tid) VALUES
  (1, 1),
  (1, 20),
  (1, 17),
  (2, 2),
  (2, 14);
