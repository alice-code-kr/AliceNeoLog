from langchain_ollama import ChatOllama
import requests




class Scrap:
    def get_data(self):
        url = "https://nct-jp.net/en/"
        response = requests.get(url)
        html = response.text
        return html

        
       

