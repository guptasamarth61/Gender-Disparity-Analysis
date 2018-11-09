# Gender-Disparity-Analysis
This contain my code for data collection and analysis for my research paper **Gender Disparity in Engineering research** to examine the trends of gender ratio in engineering with time.
## Data Collection:
  Data was collected from various papers published in reputed journals of engineering research during the last decade. I collected information about the name of the authors, co-authors, journal name and citation through web scrapping in Python using BeautifulSoup.
My next main task was to infer the gender from names if authirs and co-authors. For this task, I used **Genderise.io** a software to infer gender from names. I collected this data in the form of csv files.

## Data Analysis:
  I did most part of data analysis using pandas and numpy library of Python. I analysed the gender ratio on various parameters such as gender ratio of authors, gender ratio of co-authors and regression between authors and co-authors. I also performed t-test to test the confidence level. Using matplotlib I plotted various bar and scatter plots to visualise the results.
  
