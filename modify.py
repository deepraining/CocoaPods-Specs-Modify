import os
import re

# Specs目录
specsDir = os.path.expanduser('~') + '/.cocoapods/repos/trunk/Specs/'
# specsDir = './example/'

# https://github.com/Alamofire/Alamofire.git => git@github.com:Alamofire/Alamofire.git
# 只更改git repo路径，其他的资源路径不改，如https://github.com/Alamofire/Alamofire/releases/v1.0.0.zip
httpPattern = '"https://github.com/([^"]+).git"'

# 更改包计数
modifyCount = 0

def modifyFile(filePath):
    f = open(filePath, 'r')
    content = f.read()
    f.close()
    matches = re.findall(httpPattern, content)
    if matches and len(matches) > 0:
        global modifyCount
        modifyCount += 1
        newContent = content
        for match in matches:
            httpStr = '"https://github.com/'+match+'.git"'
            sshStr = '"git@github.com:'+match+'.git"'
            newContent = newContent.replace(httpStr, sshStr)
        f2 = open(filePath, 'w')
        f2.write(newContent)
        f2.close()

for root, dirs, files in os.walk(specsDir, topdown=False):
    for name in files:
        modifyFile(os.path.join(root, name))

print(f'完成，更改包{modifyCount}个')
