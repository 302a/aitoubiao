import pymysql

def help_login(username, password):
    db_all = pymysql.connect("192.168.101.14", "root", "shaoyang", "user")
    db_this = pymysql.connect("192.168.101.14", "root", "shaoyang", "aitoubiao")

    cursor_all = db_all.cursor()
    cursor_this = db_this.cursor()

    cursor_all.execute("select * from user where username = '{}'".format(username))

    results = cursor_all.fetchall()

    if len(results) == 0:
        return '没有此用户'
    elif len(results) == 1:
        result = results[0]
        if result[2] == password:
            # print(result[2])
            try:
                # 执行sql语句
                cursor_this.execute("insert into user(username, password, nickname) values ('{}', '{}', '{}')"
                                    .format(result[1], result[2], result[3]))
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

    db_all.close()
    db_this.close()


def help_register(username, nickname, password, user_icon):
    db_all = pymysql.connect("192.168.101.14", "root", "shaoyang", "user")
    db_this = pymysql.connect("192.168.101.14", "root", "shaoyang", "aitoubiao")

    cursor_all = db_all.cursor()
    cursor_this = db_this.cursor()

    cursor_all.execute("select * from user where username = '{}'".format(username))

    results = cursor_all.fetchall()

    if len(results) != 0:
        return '用户名已存在'
    else:
        try:
            # 执行sql语句
            cursor_all.execute("insert into user(username, password, nickname, user_icon) values ('{}', '{}', '{}', '{}')"
                                    .format(username, nickname, password, user_icon))
            cursor_this.execute("insert into user(username, password, nickname, user_icon) values ('{}', '{}', '{}', '{}')"
                                    .format(username, nickname, password, user_icon))
            # 提交到数据库执行
            db_all.commit()
            db_this.commit()
            return '注册成功'
        except:
            # 如果发生错误则回滚
            db_all.rollback()
            db_this.rollback()

    db_all.close()
    db_this.close()



if __name__ == '__main__':
    print(help_login('a', '1'))

