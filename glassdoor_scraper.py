import scrapper
import pandas as pd
path = "C:\\Users\\almai\\PycharmProjects\\scrapper\\chromedriver"
df = scrapper.get_jobs("data science", 5, False, path, 5)
