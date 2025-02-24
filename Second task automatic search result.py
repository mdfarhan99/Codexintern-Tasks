import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

def google_search(query, num_results=10):
    print("Starting WebDriver...")  
    options = webdriver.ChromeOptions()
    options.add_argument("user-agent=Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36")

    driver = webdriver.Chrome(options=options)

    try:
        print("Opening Google...")  
        driver.get("https://www.google.com")
        search_box = driver.find_element(By.NAME, "q")
        search_box.send_keys(query)
        search_box.send_keys(Keys.RETURN)

        print("\nSearching for:", query)  
        time.sleep(60)  

        print("Extracting search results...")  
        
        results = driver.find_elements(By.XPATH,"//div[@class='tF2Cxc' or @class='MjjYud']")[:num_results]
        search_data = []
        
        for i,result in enumerate(results):
            try:
                title = result.find_element(By.TAG_NAME, "h3").text
                link = result.find_element(By.TAG_NAME, "a").get_attribute("href")
                try:
                    description = result.find_element(By.CSS_SELECTOR, "div.VwiC3b").text
                except:
                    description = "No description available."
                
                search_data.append({"Title": title, "Link": link, "Description": description})
                print(i + 1, ".", title, "-", link)  
            except:
                print("Skipping an entry (missing data)...")  
                continue  

        return search_data

    except Exception as e:
        print("Error:", e)  
        return None
    
    finally:
        driver.quit()

if __name__ == "__main__":
    query = input("Enter your search query: ")
    print("\nReceived query:", query)  
    results = google_search(query)

    if results:
        print("\nTop Google Search Results:")
        for idx, res in enumerate(results, 1):
            print("\n", idx, ".", res["Title"])
            print("   Link:", res["Link"])
            print("   Description:", res["Description"])
    else:
        print("\nNo results found.")
