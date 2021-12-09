'''c = str(input('Em que cidade você nasceu?: ')).lower().strip()
print('santo' in c')'''
cid = str(input('Que cidade você nasceu?: ')).title().strip()
print(cid[:5]=='Santo')