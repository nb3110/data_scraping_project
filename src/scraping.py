import pandas as pd
import requests
import os
from dotenv import load_dotenv

########################################################

load_dotenv() 


api_key = os.getenv("movie_api_cred_key")
api_host = os.getenv("movie_api_cred_host")


url = "https://moviesdatabase.p.rapidapi.com/titles"

headers = {"X-RapidAPI-Key": api_key ,'X-RapidAPI-Host': api_host}

# 1 page per request with 10 movies per page --> looping parameter to get the top 100 movies
requests_list = [requests.request("GET", url, headers=headers, params={"list":"top_rated_250", "page":f"{i}","info":"base_info"}).json() for i in range(1,11)]


def series_req(api_lvl_1,api_lvl_2): 
    return [requests_list[i]["results"][j][api_lvl_1][api_lvl_2] for i in range(len(requests_list)) for j in range(len(requests_list[i]["results"]))]


# Call series_req, a function that creates list comprehensions to extract data, defining the dictionary keys as parameters.

rating_list = series_req("ratingsSummary","aggregateRating")
votecount_list = series_req("ratingsSummary","voteCount")
title_list = series_req("titleText","text")
title_year = series_req("releaseYear","year")


imbd_dict= {
"imbd_rating":rating_list,
"imbd_votecount":votecount_list,
"imbd_title":title_list,
"year":title_year
}


imbd_table = pd.DataFrame(imbd_dict)

imbd_table.to_csv('csv\imbd_table.csv')

