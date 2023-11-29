password = 'a123456'
chance = 3
while True:
    input_password = input('請輸入密碼：')
    if input_password == password:
        print('登入成功！')
        break
    else:
        chance = chance - 1
        print('密碼錯誤！還有', chance, '次機會')
        if chance == 0:
            break