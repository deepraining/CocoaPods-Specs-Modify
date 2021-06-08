# CocoaPods-Specs-Modify

因为执行 `pod install` 会安装 `github.com` 上的包，但 `github.com` 很不稳定。
所以这个项目的目的是，使用脚本将 `github.com` 的资源转换为其他域的资源。

CocoaPods 从 1.7.2 版本开始使用 `https://cdn.cocoapods.org/` 代替原有的 `https://github.com/CocoaPods/Specs.git`，
这样可以按需下载需要的包定义，而不用一次性下载整个 `Specs` 库（整个库是3GB左右），参考 [CocoaPods 1.7.2 — Master Repo CDN is Finalized!](https://blog.cocoapods.org/CocoaPods-1.7.2/)。

```
source 'https://github.com/artsy/Specs.git'
- source 'https://github.com/CocoaPods/Specs.git'
+ source 'https://cdn.cocoapods.org/'
```

脚本使用方法(可以自行更改脚本里的设置)：

```
python modify.py
```
