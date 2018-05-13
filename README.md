# 半自动方式破解计算机等级考试查询成绩

## 需要社工手段查找考生的家乡及生日，之后只需破解身份证号后四位，在确定性别后只需尝试5000次

## 运行先将`ckl.py`中填入浏览器cookie对应字段以及姓名和身份证号前14位

## 运行时下载验证码到本地，opencv库显示图片，点击空格图片窗口关闭输入验证码。验证码输入错误时进入循环，直到验证码正确再进入下一个数字尝试。每次退出程序会显示当前尝试数字，可手动删除字典中已尝试的数字，使下一次可以接上上一次的进度

## 采用手工打码的方式识别验证码，效率较低，理想状态全自动运行，AI识别验证码。但试了tesseract识别率感人。希望有深度学习大佬pull request

![](https://upload-images.jianshu.io/upload_images/11356161-d644619c681eabb0.gif?imageMogr2/auto-orient/strip)

![](https://upload-images.jianshu.io/upload_images/11356161-2a3a9b6c7a47e746.png?imageMogr2/auto-orient/strip%7CimageView2/2/w/1240)
