import pymysql

def login(userid, password):
    db_all = pymysql.connect("192.168.101.14", "root", "shaoyang", "user")
    db_this = pymysql.connect("192.168.101.14", "root", "shaoyang", "aitoubiao")

    cursor_all = db_all.cursor()
    cursor_this = db_this.cursor()

    cursor_all.execute("select * from user where userid = '{}'".format(userid))

    results = cursor_all.fetchall()

    if len(results) == 0:
        return '没有此用户'
    elif len(results) == 1:
        result = results[0]
        if result[3] == password:
            print(result[3])
            try:
                # 执行sql语句
                cursor_this.execute("insert into user(userid, username, password, user_icon) values ('{}', '{}', '{}', '{}')"
                                    .format(result[1], result[2], result[3], result[4]))
                # 提交到数据库执行
                db_this.commit()
                return '登录成功'
            except:
                # 如果发生错误则回滚
                db_this.rollback()
                return '未知错误'
        else:
            return '密码错误'
    else:
        #查询到多条数据
        return '错误'

def test():
    return 'asasas'

if __name__ == '__main__':
    login('a', '1')

