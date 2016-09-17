# -*- coding: utf-8 -*-


from selenium import webdriver
import selenium.webdriver.support.ui as ui
import time
from Tkinter import *


print "---------------system loading...please wait...---------------"

#获取电影名及URL
def getURL_Title():
    global save_name
    SUMRESOURCES=0
    url="https://movie.douban.com/"
    driver_item=webdriver.Firefox()
    wait = ui.WebDriverWait(driver_item,15)

    Class_Dict={'Movies':1,'TV':2,'TOP10 M&T':3}
    
    Kind_Dict={'Hot':1,'Newest/American TV':2,'Classics/UK TV':3,'Playable/Korean TV':4,'High Scores/Japanese TV':5,
              'Wonderful but not popular/Chinese TV':6,'Chinese film/TVB':7,'Hollywood/Cartoon':8,
              'Korea':9,'Japan':10,'Action movies':11,'Comedy':12,'Love story':13,
              'Science fiction':14,'Thriller':15,'Horror film':16,'Whatever':17}
    #最后一个电影
    Sort_Dict={'Sort by hot':1,'Sort by time':2,'Sort by score':3}
    Ask_Dict={'*No film reviews':0,'*I like film reviews':1}

    
    try:
        kind=Kind_Dict[Kind_Select.get(Kind_Select.curselection()).encode('utf-8')]
        sort = Sort_Dict[Sort_Select.get(Sort_Select.curselection()).encode('utf-8')]
        number = int(input_Top.get())
    except:
        print 'if you are using TOP10 M&T ,it\'s all right\n if not,please choice kind/sort/number '

    class_MT = Class_Dict[MT_Select.get(MT_Select.curselection()).encode('utf=8')]
    ask_comments = Ask_Dict[Comment_Select.get(Comment_Select.curselection()).encode('utf-8')]
    save_name=input_SN.get()

    Ans.insert(END,"#####################################################################")
    Ans.insert(END,"                                                          Reloading                                           ")
    Ans.insert(END,",#####################################################################")
    Ans.insert(END,"---------------------------------------system loading...please wait...------------------------------------------")
    Ans.insert(END,"----------------------------------------------crawling----------------------------------------------")
    Write_txt('\n##########################################################################################','\n##########################################################################################',save_name)
    print "---------------------crawling...---------------------"

#等待电影get完再读取
    if class_MT==1:
        
        driver_item.get(url)
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[%s]"%kind))
        driver_item.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[%s]"%kind).click()
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div[3]/div/label[%s]"%sort))
        driver_item.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div[3]/div/label[%s]"%sort).click()

        num=number+1

        
        num_time = num/20+2
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list-wp']/div/a[20]"))
        for times in range(1,num_time):
            driver_item.find_element_by_xpath("//div[@class='list-wp']/a[@class='more']").click()
            wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list-wp']/div/a[%d]"%(20*(times+1))))


        

        for i in range(1,num):
            wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list']/a[%d]"%num))
            list_title=driver_item.find_element_by_xpath("//div[@class='list']/a[%d]"%i)
            print '----------------------------------------------'+'NO' + str(SUMRESOURCES +1)+'----------------------------------------------'
            print u'电影名: ' + list_title.text
            print u'链接: ' + list_title.get_attribute('href')
            

            
            while list_title.text==driver_item.find_element_by_xpath("//div[@class='list']/a[%d]"%(i+20)).text:
                print u'遇到页面加载重复项bug，开始重新加载...'
                driver_item.quit()
                getURL_Title()

            
            list_title_wr=list_title.text.encode('utf-8')
            list_title_url_wr=list_title.get_attribute('href')
            
            Ans.insert(END,'\n-------------------------------------------Movies--'+'NO' + str(SUMRESOURCES +1)+'----------------------------------------------',list_title_wr,list_title_url_wr)
            
            Write_txt('\n------------------------------------------Movies--'+'NO' + str(SUMRESOURCES +1)+'----------------------------------------------','',save_name)
            Write_txt(list_title_wr,list_title_url_wr,save_name)

            SUMRESOURCES = SUMRESOURCES +1


            
            try:
                getDetails(str(list_title.get_attribute('href')),ask_comments)
            except:
                print 'can not get the details!'

        
        driver_item.quit()


    #选择电视剧之后的操作
    if class_MT == 2:
        
        driver_item.get(url)
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/h2/a[2]"))
        driver_item.find_element_by_xpath("//div[@class='fliter-wp']/h2/a[2]").click()

        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[%s]"%kind))
        driver_item.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div/div/label[%s]"%kind).click()
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div[3]/div/label[%s]"%sort))
        driver_item.find_element_by_xpath("//div[@class='fliter-wp']/div/form/div[3]/div/label[%s]"%sort).click()

        num=number+1

        
        num_time = num/20+2
        wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list-wp']/div/a[20]"))
        for times in range(1,num_time):
            driver_item.find_element_by_xpath("//div[@class='list-wp']//a[@class='more']").click()
            wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list-wp']/div/a[%d]"%(20*(times+1))))

        

        for i in range(1,num):
            wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='list']/a[%d]"%num))
            list_title=driver_item.find_element_by_xpath("//div[@class='list']/a[%d]"%i)
            print '-------------------------------------------TV--'+'NO' + str(SUMRESOURCES +1)+'----------------------------------------------'
            print u'电视剧名: ' + list_title.text
            print u'链接: ' + list_title.get_attribute('href')
            


            
            while list_title.text==driver_item.find_element_by_xpath("//div[@class='list']/a[%d]"%(i+20)).text:
                print u'遇到页面加载重复项bug，开始重新加载...'
                driver_item.quit()
                getURL_Title()


            
            list_title_wr=list_title.text.encode('utf-8')
            list_title_url_wr=list_title.get_attribute('href')
            
            Ans.insert(END,'\n------------------------------------------TV--'+'NO' + str(SUMRESOURCES +1)+'----------------------------------------------',list_title_wr,list_title_url_wr)
            #写入txt中
            Write_txt('\n----------------------------------------TV--'+'NO' + str(SUMRESOURCES +1)+'----------------------------------------------','',save_name)
            Write_txt(list_title_wr,list_title_url_wr,save_name)

            SUMRESOURCES = SUMRESOURCES +1


            
            try:
                getDetails(str(list_title.get_attribute('href')),ask_comments)
            except:
                print 'can not get the details!'

        
        driver_item.quit()


    #TOP10
    if class_MT==3:
        
        driver_item.get(url)

        for i in range(1,11):
            wait.until(lambda driver: driver.find_element_by_xpath("//div[@class='billboard-bd']/table/tbody/tr"))
            list_title=driver_item.find_element_by_xpath("//div[@class='billboard-bd']/table/tbody/tr[%d]/td[2]/a"%i)
            print '----------------------------------------------'+'NO' + str(SUMRESOURCES +1)+'----------------------------------------------'
            print u'影视名: ' + list_title.text
            print u'链接: ' + list_title.get_attribute('href')
            
            list_title_wr=list_title.text.encode('utf-8')
            list_title_url_wr=list_title.get_attribute('href')
            
            Ans.insert(END,'\n-------------------------------------------WeekTOP--'+'NO' + str(SUMRESOURCES +1)+'----------------------------------------------',list_title_wr,list_title_url_wr)
            
            Write_txt('\n------------------------------------------WeekTOP--'+'NO' + str(SUMRESOURCES +1)+'----------------------------------------------','',save_name)
            Write_txt(list_title_wr,list_title_url_wr,save_name)

            SUMRESOURCES = SUMRESOURCES +1


            
            try:
                getDetails(str(list_title.get_attribute('href')),ask_comments)
            except:
                print 'can not get the details!'

        
        driver_item.quit()




#当选择一部电影后要进入超链接
#元素加载的问题
#在加载长评论的时候，注意模拟点击一次小三角，不然可能会使内容隐藏


def getDetails(url,comments):
    driver_detail = webdriver.PhantomJS(executable_path="phantomjs.exe")
    wait1 = ui.WebDriverWait(driver_detail,15)
    driver_detail.get(url)
    wait1.until(lambda driver: driver.find_element_by_xpath("//div[@id='link-report']/span"))
    drama = driver_detail.find_element_by_xpath("//div[@id='link-report']/span")
    print u"剧情简介："+drama.text

    drama_wr=drama.text.encode('utf-8')
    
    Ans.insert(END,drama_wr)
    
    Write_txt(drama_wr,'',save_name)

    
    if comments == 1:

        print "--------------------------------------------Hot comments TOP----------------------------------------------"
        #加载四个短评
        for i in range(1,5):
            try:
                comments_hot = driver_detail.find_element_by_xpath("//div[@id='hot-comments']/div[%s]/div/p"%i)
                print u"最新热评："+comments_hot.text
                comments_hot_wr=comments_hot.text.encode('utf-8')
                Ans.insert(END,"--------------------------------------------Hot comments TOP%d----------------------------------------------"%i,comments_hot_wr)
                Write_txt("--------------------------------------------Hot comments TOP%d----------------------------------------------"%i,'',save_name)
                Write_txt(comments_hot_wr,'',save_name)
            except:
                print 'can not caught the comments!'

        #加载长评
        try:
            driver_detail.find_element_by_xpath("//img[@class='bn-arrow']").click()
            
            time.sleep(1)

            
            comments_get = driver_detail.find_element_by_xpath("//div[@class='review-bd']/div[2]/div")
            if comments_get.text.encode('utf-8')=='提示: 这篇影评可能有剧透':
                comments_deep=driver_detail.find_element_by_xpath("//div[@class='review-bd']/div[2]/div[2]")
            else:
                comments_deep = comments_get

            print "--------------------------------------------long-comments---------------------------------------------"
            print u"深度长评："+comments_deep.text
            comments_deep_wr=comments_deep.text.encode('utf-8')
           
            Ans.insert(END,"--------------------------------------------long-comments---------------------------------------------\n",comments_deep_wr)
            Write_txt("--------------------------------------------long-comments---------------------------------------------\n",'',save_name)
            Write_txt(comments_deep_wr,'',save_name)

        except:
            print 'can not caught the deep_comments!'



def Write_txt(text1='',text2='',title='douban.txt'):

        with open(title,"a") as f:
            for i in text1:
                f.write(i)
            f.write("\n")
            for j in text2:
                f.write(j)
            f.write("\n")


def Clea():
    input_Top.delete(0,END)#这里entry的delect用0
    input_SN.delete(0,END)
    Ans.delete(0,END)#text中的用0.0
    Ans.insert(END,"Pay Attention: ","if you are using 'Movies'or 'TV',please select all parameters,and 'TV' share the same parameters but use the latter one","if you are using 'TOP10 M&T', please select parameters with '*'",'####################################################################')


#GUI

root=Tk()
root.title('豆瓣影视抓取器1.0--by哈士奇说喵')
frame_select=Frame(root)
title_label=Label(root,text='豆瓣影视TOP抓取器')
title_label.pack()


MT_Select=Listbox(frame_select,exportselection=False,width=12,height=4)
list_item1 = ['Movies','TV','TOP10 M&T']
for i in list_item1:
    MT_Select.insert(END,i)

scr_MT = Scrollbar(frame_select)
MT_Select.configure(yscrollcommand = scr_MT.set)
scr_MT['command']=MT_Select.yview




Kind_Select=Listbox(frame_select,exportselection=False,width=22,height=4)
list_item2 = ['Hot','Newest/American TV','Classics/UK TV','Playable/Korean TV','High Scores/Japanese TV',
              'Wonderful but not popular/Chinese TV','Chinese film/TVB','Hollywood/Cartoon',
              'Korea','Japan','Action movies','Comedy','Love story',
              'Science fiction','Thriller','Horror film','Whatever']


for i in list_item2:
    Kind_Select.insert(END,i)

scr_Kind = Scrollbar(frame_select)
Kind_Select.configure(yscrollcommand = scr_Kind.set)
scr_Kind['command']=Kind_Select.yview




Sort_Select=Listbox(frame_select,exportselection=False,width=12,height=4)
list_item3 = ['Sort by hot','Sort by time','Sort by score']
for i in list_item3:
    Sort_Select.insert(END,i)

scr_Sort = Scrollbar(frame_select)
Sort_Select.configure(yscrollcommand = scr_Sort.set)
scr_Sort['command']=Sort_Select.yview



Comment_Select=Listbox(frame_select,exportselection=False,width=16,height=4)
list_item4 = ['*No film reviews','*I like film reviews']
for i in list_item4:
    Comment_Select.insert(END,i)

scr_Com = Scrollbar(frame_select)
Comment_Select.configure(yscrollcommand = scr_Com.set)
scr_Com['command']=Comment_Select.yview


Label_TOP=Label(frame_select, text='TOP(xx)', font=('',10))
var_Top = StringVar()
input_Top = Entry(frame_select, textvariable=var_Top,width=8)


Label_SN=Label(frame_select, text='*SAVE_NAME(xx.txt)', font=('',10))
var_SN = StringVar()
input_SN = Entry(frame_select, textvariable=var_SN,width=8)




frame_output=Frame(root)
out_label=Label(frame_output,text='Details')
Ans = Listbox(frame_output,selectmode=MULTIPLE, height=15,width=100)
Ans.insert(END,"Pay Attention: ","if you are using 'Movies'or 'TV',please select all parameters,and 'TV' share the same parameters but use the latter one","if you are using 'TOP10 M&T', please select parameters with '*'",'####################################################################')


crawl_button = Button(frame_output,text='crawl', command=getURL_Title)
clear_button = Button(frame_output,text='clear', command=Clea)



scr_Out_y = Scrollbar(frame_output)
Ans.configure(yscrollcommand = scr_Out_y.set)
scr_Out_y['command']=Ans.yview

scr_Out_x = Scrollbar(frame_output,orient='horizontal')#ans x
Ans.configure(xscrollcommand = scr_Out_x.set)
scr_Out_x['command']=Ans.xview





frame_select.pack()

MT_Select.pack(side=LEFT)
scr_MT.pack(side=LEFT)

Kind_Select.pack(side=LEFT)
scr_Kind.pack(side=LEFT)

Sort_Select.pack(side=LEFT)
scr_Sort.pack(side=LEFT)

Comment_Select.pack(side=LEFT)
scr_Com.pack(side=LEFT)

Label_TOP.pack()
input_Top.pack()

Label_SN.pack()
input_SN.pack()


frame_output.pack()
out_label.pack()
crawl_button.pack(side=LEFT)

clear_button.pack(side=RIGHT)
scr_Out_y.pack(side=RIGHT)
Ans.pack()
scr_Out_x.pack()

root.mainloop()