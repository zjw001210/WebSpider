from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import MoveTargetOutOfBoundsException
from selenium.webdriver.chrome.options import Options
import time
import os


def click_by_time(driver,xpath,maxTime):
    t=0
    while t<=maxTime:
        if driver.find_element_by_xpath(xpath)!=None: 
            driver.find_element_by_xpath(xpath).click()
            break
        time.sleep(1)
        t+=1  

big_companys = []
eng_companys = []
with open('company_name.txt','r+') as f:
    for line in f.readlines():
        big_companys.append(line.replace('\n',''))

with open('E_company_name.txt','r+') as f:
    for line in f.readlines():
        eng_companys.append(line.replace('\n',''))

    
surname_list = ['王','李','张','刘','陈','杨','黄','赵','吴','周','徐','孙','马','朱','胡','郭','何','林','高','罗','郑','梁','谢','宋','唐','许','邓','韩','冯','曹','彭','曾','肖','田','董','潘','袁','蔡','蒋','余','于','杜','叶','程','魏','苏','吕','丁','任','卢','姚','沈','钟','姜','崔','谭','陆','范','汪','廖','石','金','韦','贾','夏','付','方','邹','熊','白','孟','秦','邱','侯','江','尹','薛','闫','段','雷','龙','黎','史','陶','贺','毛','郝','顾','龚','邵','万','覃','武','钱','戴','严','欧','莫','孔','向']
occupation_list = ['Manager','Engineer','Software','Hardware','Electronic','System','Vice','Purchasing','Logistics','R&D','Vice','工程','技术','经理','电气','底盘','供应','物流']



for i in range(0,10):
    company_urls = []
    addition_list = surname_list + occupation_list

    if big_companys[i] in eng_companys:
        addition_list = occupation_list

    for adKey in addition_list:
        #try:
        key = adKey + ' ' + big_companys[i] + ' ' + ' site:linkedin.com'
        print(key)

        chrome_driver = "/usr/bin/chromedriver"  # 更换成运行电脑chromedriver.exe的路径

        chrome_options = Options()
        chrome_options.add_argument('--headless')
        chrome_options.add_argument('--no-sandbox')
        chrome_options.add_argument('--disable-dev-shm-usage')
        chrome_options.add_argument('--remote-debugging-port=9222')
        # chrome_options.add_experimental_option("debuggerAddress", "127.0.0.1:9222")
        driver = webdriver.Chrome(chrome_driver, options=chrome_options)
        driver.get('https://cn.bing.com/')
        searchingBox = driver.find_element_by_xpath('//*[@id="sb_form_q"]')
        searchingBox.send_keys(key)
        click_by_time(driver, '//*[@id="sb_form_go"]', 10)
        count = 0
        records = 0
        
        #except:
            #continue
        while(True):
            if count == 100:
                break
            count += 1
            time.sleep(5)#防止title未加载是空列表
            try:
                titles = driver.find_elements_by_class_name('b_algo')
                for title in titles:
                    result = title.find_element_by_tag_name('a')
                    if ('|' in result.text and '-' in result.text):
                        spans = title.find_elements_by_xpath('.//div/div[2]/cite')
                        for span in spans:
                            href = span.text
                            if 'www.linkedin' in str(href) or 'cn.linkedin' in str(href):
                                print(str(href))
                                path = os.getcwd()
                                company_urls.append(str(href))
                                with open(path + '/data/' + big_companys[i].replace(' ','') + 'urls.txt','a+') as f:
                                    f.write(str(href))
                                    f.write('\n')
                                records += 1
                            break
                time.sleep(1)
                company_urls = list(set(company_urls))
            except:
                continue
            print(count,'页','第',i,'家企业',big_companys[i],'目前找到',len(company_urls),'条有效记录,辅助关键词为 ',adKey)
            try:
                pagebar = driver.find_element_by_class_name('b_pag') 
                next_page = pagebar.find_elements_by_tag_name('a')[-1]
                driver.execute_script("arguments[0].click();", next_page)
            except:
                print('next error')
                break
            
            #next_page.click()

        driver.quit()
        #time.sleep(360)
        
    time.sleep(1800)