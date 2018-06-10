# Extracting the company names from the raw news files
We have scraped the news from various news sources. But there are all kinds of news available like political, education, sports, business etc.

We are interested only in the news which are related to the companies listed in the National Stock Exchange (NSE). To do this, we have a list of companies which are listed in the NSE.
We check every news content with the NSE list and if the match is found, the news article is associated with that company name.
This helps in getting which news was related to which company.

The input files to the iPythonNotebook is _companyNamesList.csv_ and _newsFile.csv_ and it generates a news file _newsWithCompanyName.csv_ containing the names of the company along with the news.
