
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


