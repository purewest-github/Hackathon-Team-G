import pymysql
from util.DB import DB

class dbConnect:
    # ユーザーを作成
    def createUser(user):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入
        「usersテーブルの(uid,user_name,email,password)列へそれぞれ値を挿入」
        execute文にsqlと挿入する値(userのインスタンス変数)を渡して実行
        commitで変更を確定
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'INSERT INTO users (uid, user_name, email, password) VALUES (%s, %s, %s, %s);'
            cur.execute(sql, (user.uid, user.name, user.email, user.password))
            conn.commit()

        # 例外処理
        except Exception as e:
            print(e, 'が発生しています')
            return None

        #最終処理 カーソルを閉じる
        finally:
            cur.close()

    # 指定したemailに該当するユーザーを取得
    def getUser(email):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入
        「usersテーブルから指定したemailに該当する行の全カラムを取得」
        execute文にsqlとemailを渡して実行
        fetchoneでemailが一致する1行のみデータを取得→userに代入
        userを返す
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'SELECT * FROM users WHERE email=%s;'
            cur.execute(sql, (email))
            user = cur.fetchone()
            return user

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        #最終処理 カーソルを閉じる
        finally:
            cur.close()


    #チャンネル一覧取得機能
    def getChannelAll():
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:「channelsテーブルの全カラムの値を取得する」
        execute文でsqlを実行
        実行結果を全て取り出し変数channelsに代入
        channelsを返す
        """

        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'SELECT * FROM channels;'
            cur.execute(sql)
            channels = cur.fetchall()
            return channels

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理:カーソルを閉じる
        finally:
            cur.close()

    # チャンネル名取得
    def getChannelByName(channel_name):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        * カーソルとは - 検索結果からデータを１件ずつ取得する仕組みまたその目印のこと
        channelsテーブルから該当のテーブル名を取得する処理そのもの→sqlへ代入
        channelsテーブルから引数で渡ってきたchannel_nameという値を検索し、抜き取る
        * executeとは - SQL文を渡すと実行してくれる関数
        fetchoneでchannel名が一致する1行のみデータを取得→channelに代入
        channelを返す
        """

        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'SELECT * FROM channels WHERE name=%s;'
            cur.execute(sql, (channel_name))
            channel = cur.fetchone()
            return channel

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理:カーソルを閉じる
        finally:
            cur.close()

    # チャンネル追加(ユーザーID, チャンネル名, チャンネル概要, タグID)
    def addChannel(uid, newChannelName, newChannelDescription):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入
        execute文でsqlを実行(channelテーブルにユーザーID,チャンネル名,チャンネル概要を追加,タグID)
        commitで変更を確定
        * commitとは - トランザクションの結果を確定する(変更を確定する)
        """

        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'INSERT INTO channels (uid, name, abstract) VALUES (%s, %s, %s);'
            cur.execute(sql, (uid, newChannelName, newChannelDescription))
            conn.commit()

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理:カーソルを閉じる
        finally:
            cur.close()

    # 引数で渡したチャンネルIDに該当するチャンネルを取得
    def getChannelById(cid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        channelsテーブルから該当のcidのチャンネルを取得するSQL文→sqlへ代入
        channelsテーブルから引数で渡ってきたcidの値を検索し、抜き取る
        fetchoneでcidが一致する1行のみデータを取得→channelに代入
        channelを返す
        """

        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT * FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            channel = cur.fetchone()
            return channel

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理:カーソルを閉じる
        finally:
            cur.close()

    # チャンネル更新(ユーザーID, チャンネル名, チャンネル概要、タグID)
    def updateChannel(uid, newChannelName, newChannelDescription, cid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        channelsテーブルで該当するcidの（ユーザーID,チャンネル名,チャンネル概要,タグID）を更新するSQL文→sqlへ代入
        execute文にsqlと更新する値の入った各変数を渡して実行
        commitで変更を確定
        カーソルを閉じる
        """
        conn = DB.getConnection()
        cur = conn.cursor()
        sql = "UPDATE channels SET uid=%s, name=%s, abstract=%s WHERE id=%s;"
        cur.execute(sql, (uid, newChannelName, newChannelDescription, cid))
        conn.commit()
        cur.close()

    # チャンネル削除
    def deleteChannel(cid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        channelsテーブルから該当するcidのチャンネルデータを削除するSQL文→sqlへ代入
        execute文にsqlと削除するチャンネルのcidを渡して実行
        commitで変更を確定
        """

        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "DELETE FROM channels WHERE id=%s;"
            cur.execute(sql, (cid))
            conn.commit()

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理：カーソルを閉じる
        finally:
            cur.close()

    # メッセージ作成(ユーザーID, チャンネルID, メッセージ)
    def createMessage(uid, cid, message):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入
        * 「INSERT INTO テーブル名(列名1,列名2,...)VALUES(値1,値2,...);」
        execute文でsqlを実行(messagesテーブル(ユーザーID, チャンネルID, メッセージ)列にそれぞれ登録)
        commitで変更を確定
        """

        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'INSERT INTO messages(uid, cid, message) VALUES(%s, %s, %s)'
            cur.execute(sql, (uid, cid, message))
            conn.commit()

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理：カーソルを閉じる
        finally:
            cur.close()

    # メッセージ全取得(チャンネルID)
    def getMessageAll(cid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:「uid列を軸としてmessagesテーブルとusersテーブルを結合させる。
        その上で、該当するcidの行から(メッセージID、ユーザーID、ユーザー名、メッセージ)を取得する」
        * 内部結合の構文(
            SELECT <カラム名>
            FROM <結合元テーブル名> AS 略称
            INNER JOIN <結合先テーブル名> AS 略称
            ON <結合元テーブルのカラム名> = <結合先テーブルのカラム名>
            WHERE 条件;
            )
        cidを指定してexecute文でsqlを実行
        取得したデータを全て取り出す→messagesに代入
        messagesを返す
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = "SELECT m.id, u.uid, u.user_name, m.message FROM messages AS m INNER JOIN users AS u ON m.uid = u.uid WHERE cid = %s;"
            cur.execute(sql, (cid))
            messages = cur.fetchall()
            return messages

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理：カーソルを閉じる
        finally:
            cur.close()

    # メッセージ削除(メッセージID)
    def deleteMessage(message_id):
        """
        DBクラスに定義した接続用メソッドを使用してDBに接続→connへ代入
        カーソルを作成→curへ代入
        sqlにSQL文を代入
        execute関数でsql文を実行(messagesテーブルからメッセージのidが一致するデータを削除)
        commitで変更を確定
        """

        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'DELETE FROM messages WHERE id=%s'
            cur.execute(sql, (message_id))
            conn.commit()

        # 例外処理
        except Exception as e:
            print(e + '発生しています')
            return None

        # 最終処理:カーソルを閉じる
        finally:
            cur.close()

    # タグ一覧取得機能
    def getTagsAll():
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:
        「タグIDをもとにtagsテーブルとchannels_tagsテーブルを左外部結合させて、
        タグIDごとにグループ化する。そして、タグID、タグ名、タグIDごとにcid列の数を集計した結果（列名はcountとする）を取得する。」
        * 外部結合とはテーブル結合時に基準となる列を指定し、その基準となるテーブルにデータがあれば、
        もう一方のテーブルにデータがなくても取り出す方式。今回はtagsテーブルのid列を基準とする。
        * GROUP BY:同じ値同士のデータをグループ化する。
        execute文でsqlを実行
        実行結果を全て取り出し変数tagsに代入
        tagsを返す
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = '''
            SELECT tags.id, tags.name, COUNT(cid) AS count FROM tags LEFT OUTER JOIN channels_tags
            ON tags.id=channels_tags.tid GROUP BY tags.id;
            '''
            cur.execute(sql)
            tags = cur.fetchall()
            return tags

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理:カーソルを閉じる
        finally:
            cur.close()

    # タグ一覧取得機能(channels_tagsテーブルと結合させたバージョン)
    def getTagsAllByTagId():
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:「タグIDをもとにtagsテーブルとchannels_tagsテーブルを結合させて全カラムの値を取得する」
        execute文でsqlを実行
        実行結果を全て取り出し変数tagsに代入
        tagsを返す
        """

        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'SELECT * FROM tags join channels_tags on tags.id=channels_tags.tid;'
            cur.execute(sql)
            tags_join = cur.fetchall()
            return tags_join

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理:カーソルを閉じる
        finally:
            cur.close()

    # 指定されたタグIDに一致するタグの取得
    def getTagById(tid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:「tagsテーブルから指定したtidに該当するタグを取得する」
        execute文でsqlを実行
        実行結果(指定したtidに該当するタグ1つ)を取り出す→tagに代入
-       tagを返す
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'SELECT * FROM tags WHERE id=%s;'
            cur.execute(sql, (tid))
            tag = cur.fetchone()
            return tag

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理:カーソルを閉じる
        finally:
            cur.close()

    # タグIDからタグに紐づいているチャンネルの取得
    def getChannelsByTagId(tid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:
-      「チャンネルIDをもとにchannels_tagsテーブルとchannelsテーブルを結合させて、
-       指定したタグIDに一致する行を全て取得する」
        execute文でsqlを実行
        実行結果(指定したタグIDに一致するチャンネル全て)を取り出す→tag_channelsに代入
        tagを返す
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'SELECT * FROM channels_tags JOIN channels ON channels_tags.cid=channels.id WHERE channels_tags.tid=%s;'
            cur.execute(sql, (tid))
            tag_channels = cur.fetchall()
            return tag_channels

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理:カーソルを閉じる
        finally:
            cur.close()


    # 入力されたタグ名からデータを取得(タグ名)
    def getTagByName(tag_name):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:「tagsテーブルからタグ名(name)が同じものを取得」
        execute文でsqlを実行
        実行結果(指定したタグ名と一致する)データを取り出す→tagに代入
        tagを返す
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'SELECT * FROM tags WHERE name=%s;'
            cur.execute(sql, (tag_name))
            tag = cur.fetchone()
            return tag
        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None
        # 最終処理:カーソルを閉じる
        finally:
            cur.close()

    # タグ追加(タグ名)
    def addTag(tag_name):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:tagsテーブルにタグを追加
        execute文でsqlを実行
        commitで変更を確定
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'INSERT INTO tags (name) VALUES (%s);'
            cur.execute(sql, (tag_name))
            conn.commit()
        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None
        # 最終処理
        finally:
            cur.close()

    # チャンネルとタグを紐付け
    def linkChannelTag(cid, tid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:channels_tagsテーブルにチャンネルIDとタグIDの組み合わせを登録
        execute文でsqlを実行
        commitで変更を確定
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'INSERT INTO channels_tags(cid, tid) VALUES(%s, %s);'
            cur.execute(sql, (cid, tid))
            conn.commit()
        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None
        # 最終処理
        finally:
            cur.close()

    # チャンネルIDからチャンネルに紐付いているタグを取得
    def getTagsByChannelId(cid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:チャンネルに紐付いているタグIDのタグをtagsテーブルから取得
        execute文でsqlを実行
        取得したデータをchannel_tagsへ代入
        channel_tagsを返す
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'SELECT * FROM tags JOIN channels_tags ON tags.id = channels_tags.tid WHERE channels_tags.cid = %s;'
            cur.execute(sql, (cid))
            channel_tags = cur.fetchall()
            return channel_tags
        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None
        # 最終処理
        finally:
            cur.close()

    # 既に紐付いているチャンネルIDとタグIDの数を取得
    def countExistData(cid, tid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        sqlにSQL文を代入:受け取ったcidとtidと同じ組み合わせのデータをchannels_tagsテーブルから取得
        execute文でsqlを実行
        実行結果→countに代入
        countを返す
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'SELECT COUNT(*) FROM channels_tags WHERE cid=%s AND tid=%s;'
            cur.execute(sql, (cid, tid))
            count = cur.fetchone()
            return count
        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None
        # 最終処理
        finally:
            cur.close()

    # チャンネルとタグの紐付けを削除(チャンネルID, タグID)
    def deleteTagLink(cid, tid):
        """
        MySQLにDBクラスで定義した接続用メソッドを使用して接続
        カーソルを作成→curへ代入
        channels_tagsテーブルから渡ってきたチャンネルIDとタグIDと同じ組み合わせを削除
        execute文でsqlを実行
        commitで変更を確定
        """
        try:
            conn = DB.getConnection()
            cur = conn.cursor()
            sql = 'DELETE FROM channels_tags WHERE cid=%s AND tid=%s;'
            cur.execute(sql,(cid, tid))
            conn.commit()

        # 例外処理
        except Exception as e:
            print(e + 'が発生しています')
            return None

        # 最終処理：カーソルを閉じる
        finally:
            cur.close()