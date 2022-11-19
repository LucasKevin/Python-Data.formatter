while True:
 format = input('O que você quer formatar?\n '
 '1 - CPF\n '
 '2 - CNPJ\n'
 '3 - MEC \n '
 '>>')

 if format == '1':
     s = input("CPF: ")
     test = ''.join(filter(lambda i: i if i.isdigit() else None, s))
     cpf = test[:3] + "." + test[3:6] + "." + test[6:9] + "-" + test[9:]
     print(cpf)
     break
 elif format == '2':
     s = input("CNPJ: ")
     test = ''.join(filter(lambda i: i if i.isdigit() else None, s))
     cnpj = test[:2] + "." + test[2:5] + "." + test[5:8] + "/" + test[8:12] + "-" + test[12:14]
     print(cnpj)
     break
 elif format == '3':
     s = input('Digite o MEC: ')
     s = s.replace(':', '')
     test = ''.join(s[i:i + 2] for i in range(0, 12, 2))
     cnpj = test[:4] + "-" + test[4:8] + "-" + test[8:12]
     print(cnpj)
     break
 else:
     print('Opção Inválida!')
     continue










