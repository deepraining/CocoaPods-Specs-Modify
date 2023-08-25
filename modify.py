import os

# Specs目录
specsDir = os.path.expanduser('~') + '/.cocoapods/repos/trunk/Specs/'
# specsDir = './example/'
# github 域名
githubSite = '"https://github.com/'
# 替换域名
# 镜像站点：https://ghproxy.com、https://gitclone.com
targetSite = '"https://ghproxy.com/https://github.com/'

# 更改包计数
modifyCount = 0

def modifyFile(filePath):
    f = open(filePath, 'r')
    content = f.read()
    f.close()
    if content.find(githubSite) > -1:
        global modifyCount
        modifyCount += 1
        newContent = content.replace(githubSite, targetSite)
        f2 = open(filePath, 'w')
        f2.write(newContent)
        f2.close()

for root, dirs, files in os.walk(specsDir, topdown=False):
    for name in files:
        modifyFile(os.path.join(root, name))

print(f'完成，更改包{modifyCount}个')
