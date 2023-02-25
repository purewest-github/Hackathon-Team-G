# ユーザークラスの定義
class User:

    # インスタンス生成時に実行される初期化メソッド
    def __init__(self, uid, name, email, password):
        """
        (ユーザーID、ユーザーネーム、メールアドレス、パスワード)をインスタンス変数に代入
        """

        self.uid = uid
        self.name = name
        self.email = email
        self.password = password

    # インスタンス変数nameを取得するメソッド
    def getUserName(self):
        return self.name

    # インスタンス変数emailを取得するメソッド
    def getUserEmail(self):
        return self.email

    # インスタンス変数passwordを取得するメソッド
    def getUserPassword(self):
        return self.password