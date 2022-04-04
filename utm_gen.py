#import pandas
import pandas as pd

#import slugify
from slugify import slugify


# create dataframe
df = pd.DataFrame(columns=['url','source','medium','term','content','generated_url'])

# Pegar innputs
url=input("Digite a URL: ")
campaign_source=input("Digite a Origem: ")
campaign_medium=input("Digite o Meio: ")
campaign_name=input("Digite o Nome da Campanha: ")
campaign_content=input("Digite a tag do conteúdo: ")
campaign_term=input("Digite um termo (se houver): ")

generated_url=url

if campaign_source:
    generated_url=generated_url+'?utm_source='+ slugify(campaign_source)
    if campaign_medium:
        generated_url=generated_url+'&utm_medium='+ slugify(campaign_medium)
    if campaign_name:
        generated_url=generated_url+'&utm_campaign='+ slugify(campaign_name)
    if campaign_term:
        generated_url=generated_url+'&utm_term='+ slugify(campaign_term)
    if campaign_content:
        generated_url=generated_url+'&utm_content='+ slugify(campaign_content)
    print("\n")
    print("Generated url is:""\n"+ generated_url)
else:
    print("\n")
    print("Campaign Source cannot be empty!")

#Add to DataFrame

dict = {'url': url , 'source': campaign_source , 'medium': campaign_medium, 'term': campaign_term , 'content': campaign_content, 'generated_url': generated_url}
df = df.append(dict, ignore_index=True)
df
