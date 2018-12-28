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
                cursor_this.execute("insert into user(username, password, nickname, user_icon) values ('{}', '{}', '{}', '{}')"
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

    db_all.close()
    db_this.close()


def help_register(username, nickname, password):
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
            cursor_all.execute("insert into user(username, password, nickname) values ('{}', '{}', '{}')"
                                    .format(username, password, nickname))
            cursor_this.execute("insert into user(username, password, nickname) values ('{}', '{}', '{}')"
                                    .format(username, password, nickname))
            # 提交到数据库执行
            db_all.commit()
            db_this.commit()
            return '注册成功'
        except:
            # 如果发生错误则回滚
            db_all.rollback()
            db_this.rollback()
            return '异常'

    db_all.close()
    db_this.close()

def help_compile_pwd(username, password):
    db_all = pymysql.connect("192.168.101.14", "root", "shaoyang", "user")

    cursor_all = db_all.cursor()

    cursor_all.execute("select * from user where username = '{}'".format(username))

    results = cursor_all.fetchall()

    if len(results) == 1:
        try:
            cursor_all.execute("update user set password='{}' where username='{}'"
                               .format(password, username))
            db_all.commit()
            return '修改成功'
        except:
            db_all.rollback()
            return '未知错误'
    else:
        return '未知错误'


def help_compile_nkn(username, nickname):
    db_all = pymysql.connect("192.168.101.14", "root", "shaoyang", "user")

    cursor_all = db_all.cursor()

    cursor_all.execute("select * from user where username = '{}'".format(username))

    results = cursor_all.fetchall()

    if len(results) == 1:
        try:
            cursor_all.execute("update user set nickname='{}' where username='{}'"
                               .format(nickname, username))
            db_all.commit()
            return '修改成功'
        except:
            db_all.rollback()
            return '未知错误'
    else:
        return '未知错误'


def help_compile_uic(username, user_icon):
    db_all = pymysql.connect("192.168.101.14", "root", "shaoyang", "user")

    cursor_all = db_all.cursor()

    cursor_all.execute("select * from user where username = '{}'".format(username))

    results = cursor_all.fetchall()

    if len(results) == 1:
        try:
            cursor_all.execute("update user set user_icon='{}' where username='{}'"
                               .format(user_icon, username))
            db_all.commit()
            return '修改成功'
        except:
            db_all.rollback()
            return '未知错误'
    else:
        return '未知错误'



if __name__ == '__main__':
    print(help_register('18738661138', '默认用户', 'e10adc3949ba59abbe56e057f20f883e'))

