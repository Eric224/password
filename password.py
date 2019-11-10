password = 'a123456'
numb = 3
while numb > 0 :
	numb = numb - 1
	pwd = input('請輸入密碼： ')
	if pwd == password :
		print('密碼正確！')
		break
	else :
		if numb > 0 :
			print('密碼錯誤！')
			print( '你還有', numb, '次機會！')
		else :
			print('密碼錯誤！')

