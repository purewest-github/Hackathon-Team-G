import pymysql

class DB:
    #MySQLと接続するためのメソッドを定義。
    #models.pyの各メソッド毎にいちいち接続処理を書くのは面倒なのでここで定義している。
    def getConnection():
        try:
            #接続の関数connect()を実行。接続に必要な各情報を引数で渡す。
            conn = pymysql.connect(
            host = 'localhost',
            db = 'chatapp',
            user = 'testuser',
            password = 'testuser',
            charset = 'utf8',
            cursorclass = pymysql.cursors.DictCursor
        )
            #コネクションオブジェクトを返す
            return conn
        #例外処理
        except(ConnectionError):
            print('コネクションエラーです')
            conn.close
