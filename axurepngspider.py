import  requests
import  re
url = 'http://cloud.axureshop.com/1izgnl/'
allurl = ['登录页','首页','地府大数据','生死簿-已删除','生死簿-批量操作验证','勾魂管理-退单','阎王殿审判记录-司马貌','阎王殿审判记录-老人模式','十八层地狱-设备管理','六道轮回-猪刚烈','冥币管理','日志管理','角色管理']
path = 'img/'
for name in allurl:
    response = requests.get(url+name+".html")
    response.encoding='utf-8'
    id = re.findall(r'img id="(.*?)_img".*?src="(.*?)"',response.text,re.S)
    for reslut in id:
        r=requests.get(reslut[1])
        with open(path+reslut[0]+".png",'wb') as f:
            f.write(r.content)