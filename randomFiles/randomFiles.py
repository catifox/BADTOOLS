import os
import sys
import random
import shutil


'''这里是所有的读取文件路径并整成一个列表的东西'''

'''这里就是把'文件路径'下的所有文件和和子目录下的文件扔到了一个叫做'文件名列表'的地方'''
文件名列表 = []
def 得到所有文件名(文件路径):
    for root, dirs, files in os.walk(文件路径):
        文件名列表.append(files)

        # print('root_dir:', root)  # 当前目录路径
        # print('sub_dirs:', dirs)  # 当前路径下所有子目录
        # print('files:', files)  # 当前路径下所有非目录子文件

'''这里把'文件名列表'里的子列表展开'''
def 这是什么(li):
    return sum(([x] if not isinstance(x, list) else 这是什么(x) for x in li), [])

'''下面是输出'''
if os.path.exists('./dont_use_it'):
    if len(os.listdir('./dont_use_it')) != 0:
        print('检测到\'./dont_use_it\'不为空，删除或清空后再试')
        sys.exit()
询问文件路径 = input('输入文件夹路径以得到目录下的所有(子目录下)文件名:')
得到所有文件名(询问文件路径)
所有的文件名 = (这是什么(文件名列表))
所有的文件名 = list(set(所有的文件名))
print ("列表长度为：" ,len(所有的文件名))


print('现在要开始打乱文件名了w')
random.shuffle(所有的文件名)#打乱列表

if not os.path.exists('./dont_use_it'):
    os.mkdir('./dont_use_it')#建一个临时文件夹

'''这里是把所有文件复制到临时文件夹'''
if os.path.exists(询问文件路径):
# root 所指的是当前正在遍历的这个文件夹的本身的地址
# dirs 是一个 list，内容是该文件夹中所有的目录的名字(不包括子目录)
# files 同样是 list, 内容是该文件夹中所有的文件(不包括子目录)
    for root, dirs, files in os.walk(询问文件路径):
        for file in files:
            是源文件 = os.path.join(root, file)
            shutil.copy(是源文件, './dont_use_it')

            print(是源文件)

    print('把所有文件复制到了临时文件夹!')

'''重命名文件，从1开始'''
print('把所有文件首次重命名!')
最初的数字 = 1
临时目录 = r'./dont_use_it'
for file in os.listdir(临时目录):
    os.rename(os.path.join(临时目录,file),os.path.join(临时目录,str(最初的数字))+'.nbt')
    最初的数字 = 最初的数字 + 1

'''按照打乱的列表来重命名'''
print('把所有文件安装打乱的顺序重命名!')
某计数器 = 0
for (root, dirs, files) in os.walk(临时目录):
     root = os.path.join(root)
 # getlines会将该目录下的所有文件名生成一个列表，下面迭代并使用这个文件名
     for filename in files:
         第一个临时的文件名 = os.path.join(filename)
         第二个临时的文件名 = 所有的文件名[某计数器].replace("\n", ".nbt")
         第一个文件名 = os.path.join(root,第一个临时的文件名)
         第二个文件名 = os.path.join(root,第二个临时的文件名)
         某计数器 += 1
         os.rename(第一个文件名,第二个文件名)
         print("handleding the {0}".format(第二个文件名))


'''这里是找到完整的文件名及目录，并替换文件的代码'''
def findAllFile(base):
    global f
    #f是文件名，root是路径
    for root, ds, fs in os.walk(base):
        for f in fs:
            什么文件名 = os.path.join(root, f)
            yield 什么文件名
def main():
    for i in findAllFile(询问文件路径):
        print(i)
        shutil.copyfile('./dont_use_it/'+f, i)

print('准备替换文件w')
main()
print('替换文件已完成w')
是否删除临时目录 = input('是否删除临时目录? y/n :')
if 是否删除临时目录 == 'y':
    shutil.rmtree('./dont_use_it/')

print('一切皆完成w')
