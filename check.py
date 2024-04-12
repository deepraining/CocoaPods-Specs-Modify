import os
import re

# Specs目录
specsDir = os.path.expanduser('~') + '/.cocoapods/repos/trunk/Specs/'
# specsDir = './example/'

# 替换错误的
httpPattern = '"git@github.com:([^"]+)\.zip"'

def checkFile(filePath):
    f = open(filePath, 'r')
    content = f.read()
    f.close()
    matches = re.findall(httpPattern, content)
    if matches and len(matches) > 0:
        print(filePath)

for root, dirs, files in os.walk(specsDir, topdown=False):
    for name in files:
        checkFile(os.path.join(root, name))

print('done')
