password = 'a123456'
numb = 2
while numb >= 0 :
	pwd = input('請輸入密碼： ')
	if pwd == password :
		print('密碼正確！')
		break
	else :
		if numb != 0 :
			print('密碼錯誤！ 你還有', numb, '次機會！')
			numb = numb - 1
		else :
			print('密碼錯誤！')
			break

