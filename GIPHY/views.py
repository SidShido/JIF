from django.http import HttpResponse
from django.http import JsonResponse
from .models import GIFS_urls
import giphy_client

def index(request):
    return HttpResponse("Hello, world. Welcome on JIF Web App")

def listing(request):
    # On recup l'url du gif depuis le dico qui est dans model, oon les mets dans une liste en y ajoutant les balises img html
    url_list =["<li><img src={}></li>".format(gifs['url']) for gifs in GIFS_urls] 
    message=url_list
    return HttpResponse(message)

def search(request):

    # create an instance of the API class
    api_instance = giphy_client.DefaultApi()
    api_key = '41tWThuAiSlXr4T2bajIh77n8JlG4kSX' # str | Giphy API Key.
    q = 'hi' # str | Search query term or prhase.
    limit = 50 # int | The maximum number of records to return. (optional) (default to 25)
    offset = 0 # int | An optional results offset. Defaults to 0. (optional) (default to 0)
    rating = 'g' # str | Filters results by specified rating. (optional)
    lang = 'en' # str | Specify default country for regional content; use a 2-letter ISO 639-1 country code. See list of supported languages <a href = \"../language-support\">here</a>. (optional)
    fmt = 'json' # str | Used to indicate the expected response format. Default is Json. (optional) (default to json)

    try: 
        # Search Endpoint
        api_response = api_instance.gifs_search_get(api_key, q, limit=limit, offset=offset, rating=rating, lang=lang, fmt=fmt)


    except ApiException as e:
        print("Exception when calling DefaultApi->gifs_search_get: %s\n" % e)

    result = [0 for _ in range(limit+1)]
    url_list = [0 for _ in range(limit+1)]
    
    for i in range(limit):
        result[i] = api_response.data[i].to_dict() 
        url_list[i] = result[i]['images']['downsized']['url']
        print(url_list[i],"\n")

    
    url_list =["<li><img src={}></li>".format(url_list[i]) for i in range(len(url_list))] 
    #url_list ="""<img src={}>""".format(url)

    return HttpResponse(url_list)