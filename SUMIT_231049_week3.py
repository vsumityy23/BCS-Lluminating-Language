
import undetected_chromedriver as uc 
import time 
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
 
 
options = uc.ChromeOptions() 
options.headless = False  # Set headless to False to run in non-headless mode
chrome_options = Options()
prefs = {
    "profile.managed_default_content_settings.images": 2
}
chrome_options.add_experimental_option("prefs", prefs)
driver = uc.Chrome(use_subprocess=True, options=options) 

url="https://www.researchgate.net/institution/Indian-Institute-of-Technology-Kanpur/members"
driver.get(url) 
driver.implicitly_wait(10)



with open("output.txt",'w') as file:
    
    for i in range(1,18):

    
    
    
        #ON A HOME PAGE
        res_aut_home=driver.find_elements(By.XPATH,'//*[@class="nova-legacy-e-text nova-legacy-e-text--size-l nova-legacy-e-text--family-display nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-person-list-item__title"]/a')
        length_resarchers = len(res_aut_home)
        
        for j in range(length_resarchers):
            
            
                #ON A RESARCHER PAGE
            time.sleep(2)
            
            res_aut_home=driver.find_elements(By.XPATH,'//*[@class="nova-legacy-e-text nova-legacy-e-text--size-l nova-legacy-e-text--family-display nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-person-list-item__title"]/a')
            
            try:    
                res_aut_home[j].click()
                time.sleep(2)
            
            except:
                pass    
                
            elements = driver.find_elements(By.XPATH,'//*[@itemprop="headline"]/a')
            length=len(elements)
            # for resarches in resarch_list:
            for k in range(length):
                time.sleep(2)
                elements = driver.find_elements(By.XPATH,'//*[@itemprop="headline"]/a')
            
                elements[k].click()
                time.sleep(2)
                            #TITLE
                try:
                    title_text=driver.find_element(By.XPATH,'//*[@class="research-detail-header-section__ie11"]/h1').text
                    file.write("\n\nTitle\n"+title_text+"\n\n")
                    # print(title_text)
                    #AUTHORS NAME 
                    file.write("Authors\n")
                    authors_elem=driver.find_elements(By.XPATH,'//*[@class="nova-legacy-e-text nova-legacy-e-text--size-m nova-legacy-e-text--family-display nova-legacy-e-text--spacing-none nova-legacy-e-text--color-inherit nova-legacy-v-person-list-item__title"]/a')
                    for author in authors_elem:
                        authorname_text=author.text
                        # print(authorname_text)
                        file.write(authorname_text+"\n")
                    file.write("\n")
                    #ABSTRACT
                    absc=driver.find_element(By.XPATH,'//*[@itemprop="description"]')
                    abs_text=absc.text
                    # print(abs_text)
                    file.write("Abstract\n")
                    file.write(abs_text)
                    driver.back()
                    time.sleep(2)     
                except:
                    pass
                    driver.back()
                    time.sleep(2) 
                    
            driver.back()
            time.sleep(3)
                    
        elements = driver.find_element(By.XPATH,'/html/body/div[2]/div[1]/div[1]/div/div/div[2]/div/div[1]/div/div[3]/div/div/nav/a[2]')
        elements.click()
        time.sleep(2)
            
                
               
                
                
                
            
       

time.sleep(1)
driver.close()






