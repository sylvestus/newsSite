
import urllib.request,json
from.models import Sources, Articles
from datetime import datetime


#Getting the api key
api_key = None

# Getting the source base url
sources_base_url = None

#Getting source articles base url
articles_base_url = None

def configure_request(app):
    global api_key, sources_base_url, articles_base_url
    api_key = app.config['NEWS_API_KEY']
    sources_base_url = app.config['NEWS_SOURCES_URL']
    articles_base_url = app.config['NEWS_ARTICLES_URL']

def get_sources(category):
    """
    Function to get the json response to our url request
    """
    get_sources_url = sources_base_url.format(category, api_key)

    with urllib.request.urlopen(get_sources_url) as url:
        get_sources_data = url.read()
        get_sources_response = json.loads(get_sources_data)

        sources_results = None

        if get_sources_response['sources']:
            sources_results_list = get_sources_response['sources']
            sources_results =process_results(sources_results_list)

    return sources_results


def process_results(sources_result_list):
    """
    Function  that processes the sources result and transform them to a list of Objects
    """
    sources_results = []
    for individual_source in sources_result_list:
        id = individual_source.get('id')
        name = individual_source.get('name')
        description = individual_source.get('description')
        category = individual_source.get('category')
        url = individual_source.get('url')
        country = individual_source.get('country')
        author= individual_source.get('author')

        source_object = Sources(id,name, description, category, url, country,author)
        sources_results.append(source_object)

    return sources_results

def get_articles(id):
    """
    Function to get the articles json response to our url request
    """


    get_article_url = articles_base_url.format(id,api_key)
    with urllib.request.urlopen(get_article_url) as url:
        articles_data = url.read()
        articles_response = json.loads(articles_data)
        articles_results = None
        
        if articles_response['articles']:
            source_article_list = articles_response['articles']
            articles_results = process_articles_results(source_article_list)
    return articles_results




def process_articles_results(articles_results_list):
    """
    Function that process the list of article from the request.
    """
    articles_results = []
    for individual_article in articles_results_list:
        title = individual_article.get('title')
        description = individual_article.get('description')
        url = individual_article.get('url')
        urlToImage = individual_article.get('urlToImage')
        publishedAt = individual_article.get('publishedAt')

        # convert date from json to string and backto my specific  format
        publishing_date = datetime.strptime(publishedAt, '%Y-%m-%dT%H:%M:%SZ')
        publishedAt = publishing_date.strftime('%d.%m.%Y')


        article_object = Articles(title, description, url, urlToImage, publishedAt)
        articles_results.append(article_object)

    return articles_results

