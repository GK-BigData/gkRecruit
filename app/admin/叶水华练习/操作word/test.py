import os
filepath='./need'
for i,j,k in os.walk(filepath):
    for name in k:
        houzhui=name.split('.')[-1]
        if houzhui=='png':
            print('插入图片',name)
        if houzhui=='txt':
            print('插入txt',name)
        else:
            pass

