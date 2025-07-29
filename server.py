import requests
from datetime import datetime
from typing import Union, Literal, List
from mcp.server import FastMCP
from pydantic import Field
from typing import Annotated
from mcp.server.fastmcp import FastMCP
from fastmcp import FastMCP, Context
import os
from dotenv import load_dotenv
load_dotenv()
rapid_api_key = os.getenv("RAPID_API_KEY")

__rapidapi_url__ = 'https://rapidapi.com/tipsters/api/shazam-core'

mcp = FastMCP('shazam-core')

@mcp.tool()
def search_suggest(query: Annotated[str, Field(description='Query')]) -> dict: 
    '''Search suggest drop-down list. Live search'''
    url = 'https://shazam-core.p.rapidapi.com/v1/search/suggest'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'query': query,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def multi_search(search_type: Annotated[Literal['SONGS_ARTISTS', 'SONGS', 'ARTISTS'], Field(description='')],
                 query: Annotated[str, Field(description='Query')],
                 offset: Annotated[Union[int, float, None], Field(description='offset Default: 0 Minimum: 0 Maximum: 10000')] = None) -> dict: 
    '''Multi-search by query (song, artist). Use pagination'''
    url = 'https://shazam-core.p.rapidapi.com/v1/search/multi'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'search_type': search_type,
        'query': query,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_artist_details(artist_id: Annotated[Union[int, float], Field(description='Artist id Default: 136975 Minimum: 1')]) -> dict: 
    '''Get a details of artist. Ex: https://www.shazam.com/artist/the-beatles/136975'''
    url = 'https://shazam-core.p.rapidapi.com/v2/artists/details'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'artist_id': artist_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def track_youtube_video(track_id: Annotated[Union[int, float], Field(description='Track id Default: 216360 Minimum: 1')],
                        name: Annotated[str, Field(description='Video name')]) -> dict: 
    '''Get a youtube video for track. Search youtube video by name'''
    url = 'https://shazam-core.p.rapidapi.com/v1/tracks/youtube-video'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'track_id': track_id,
        'name': name,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def total_shazams(track_id: Annotated[Union[int, float], Field(description='Track id Default: 469270443 Minimum: 1')]) -> dict: 
    '''Get total times the specific tracks is detected'''
    url = 'https://shazam-core.p.rapidapi.com/v1/tracks/total-shazams'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'track_id': track_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def track_similarities(track_id: Annotated[Union[int, float], Field(description='Track id Default: 216360 Minimum: 1')]) -> dict: 
    '''Get similarities track'''
    url = 'https://shazam-core.p.rapidapi.com/v1/tracks/similarities'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'track_id': track_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def track_recognize(data: Annotated[dict, Field(description='')] = None) -> dict: 
    '''Enough 3-5 seconds of audio, no more than 3 mb. Optimally 500 kb. It is best practice to send in chunks until you find a match. Get details of recognizing track by file. Ex. https://disk.yandex.ru/d/0jCEoQP3hkPDzg https://disk.yandex.ru/d/sepd6XUnhls1aw'''
    url = 'https://shazam-core.p.rapidapi.com/v1/tracks/recognize'
    headers = {'Content-Type': 'application/x-www-form-urlencoded', 'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    response = requests.post(url, headers=headers, json=data)
    return response.json()

@mcp.tool()
def track_details(track_id: Annotated[Union[int, float], Field(description='Track id Default: 554591360 Minimum: 1')]) -> dict: 
    '''Get a details of track. Ex: https://www.shazam.com/track/216314/let-it-be'''
    url = 'https://shazam-core.p.rapidapi.com/v1/tracks/details'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'track_id': track_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def v2_track_details(track_id: Annotated[Union[int, float], Field(description='Track id Default: 1441164738 Minimum: 1')]) -> dict: 
    '''Get a details of track. Ex: https://www.shazam.com/track/216314/let-it-be'''
    url = 'https://shazam-core.p.rapidapi.com/v2/tracks/details'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'track_id': track_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def tracks_related(track_id: Annotated[Union[int, float], Field(description='Track id Default: 554591360 Minimum: 1')],
                   offset: Annotated[Union[int, float, None], Field(description='Offset Default: 0 Minimum: 0')] = None) -> dict: 
    '''Get a list of tracks related by track id'''
    url = 'https://shazam-core.p.rapidapi.com/v1/tracks/related'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'track_id': track_id,
        'offset': offset,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def schema_cities_and_genres() -> dict: 
    '''Get a list of countries, cities and genres'''
    url = 'https://shazam-core.p.rapidapi.com/v1/frame/cities'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def world_chart(country_code: Annotated[Literal['DZ', 'BY', 'CI', 'SN', 'TN', 'AU', 'AT', 'AZ', 'AR', 'BE', 'BG', 'BR', 'GB', 'HU', 'VE', 'VN', 'GH', 'DE', 'GR', 'DK', 'EG', 'ZM', 'IL', 'IN', 'ID', 'IE', 'ES', 'IT', 'KZ', 'CM', 'CA', 'KE', 'CN', 'CO', 'CR', 'MY', 'MA', 'MX', 'MZ', 'NG', 'NL', 'NZ', 'NO', 'AE', 'PE', 'PL', 'PT', 'RU', 'RO', 'SA', 'SG', 'US', 'TH', 'TZ', 'TR', 'UG', 'UZ', 'UA', 'UY', 'PH', 'FI', 'FR', 'HR', 'CZ', 'CL', 'CH', 'SE', 'ZA', 'KR', 'JP'], Field(description='')]) -> dict: 
    '''Get a list of tracks in word. Ex: https://www.app.shazam.com/charts/top-200/world'''
    url = 'https://shazam-core.p.rapidapi.com/v1/charts/world'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country_code': country_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def chart_by_city(country_code: Annotated[Literal['DZ', 'BY', 'CI', 'SN', 'TN', 'AU', 'AT', 'AZ', 'AR', 'BE', 'BG', 'BR', 'GB', 'HU', 'VE', 'VN', 'GH', 'DE', 'GR', 'DK', 'EG', 'ZM', 'IL', 'IN', 'ID', 'IE', 'ES', 'IT', 'KZ', 'CM', 'CA', 'KE', 'CN', 'CO', 'CR', 'MY', 'MA', 'MX', 'MZ', 'NG', 'NL', 'NZ', 'NO', 'AE', 'PE', 'PL', 'PT', 'RU', 'RO', 'SA', 'SG', 'US', 'TH', 'TZ', 'TR', 'UG', 'UZ', 'UA', 'UY', 'PH', 'FI', 'FR', 'HR', 'CZ', 'CL', 'CH', 'SE', 'ZA', 'KR', 'JP'], Field(description='')],
                  city_id: Annotated[Union[int, float], Field(description='City id Default: 2779674 Minimum: 0')]) -> dict: 
    '''Get a list of tracks by city id. Ex: https://www.app.shazam.com/charts/top-50/austria/feldkirch'''
    url = 'https://shazam-core.p.rapidapi.com/v1/charts/city'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country_code': country_code,
        'city_id': city_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def chart_by_genre_and_country(country_code: Annotated[Literal['DZ', 'BY', 'CI', 'SN', 'TN', 'AU', 'AT', 'AZ', 'AR', 'BE', 'BG', 'BR', 'GB', 'HU', 'VE', 'VN', 'GH', 'DE', 'GR', 'DK', 'EG', 'ZM', 'IL', 'IN', 'ID', 'IE', 'ES', 'IT', 'KZ', 'CM', 'CA', 'KE', 'CN', 'CO', 'CR', 'MY', 'MA', 'MX', 'MZ', 'NG', 'NL', 'NZ', 'NO', 'AE', 'PE', 'PL', 'PT', 'RU', 'RO', 'SA', 'SG', 'US', 'TH', 'TZ', 'TR', 'UG', 'UZ', 'UA', 'UY', 'PH', 'FI', 'FR', 'HR', 'CZ', 'CL', 'CH', 'SE', 'ZA', 'KR', 'JP'], Field(description='')],
                               genre_code: Annotated[Literal['POP', 'HIP_HOP_RAP', 'DANCE', 'ELECTRONIC', 'SOUL_RNB', 'ALTERNATIVE', 'ROCK', 'LATIN', 'FILM_TV', 'COUNTRY', 'AFRO_BEATS', 'WORLDWIDE', 'REGGAE_DANCE_HALL', 'HOUSE', 'K_POP', 'FRENCH_POP', 'SINGER_SONGWRITER', 'REG_MEXICO'], Field(description='')]) -> dict: 
    '''Get a list of tracks by genre and country code. Ex: https://www.app.shazam.com/charts/genre/australia/hip-hop-rap'''
    url = 'https://shazam-core.p.rapidapi.com/v1/charts/genre-country'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country_code': country_code,
        'genre_code': genre_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def world_chart_by_genre(genre_code: Annotated[Literal['POP', 'HIP_HOP_RAP', 'DANCE', 'ELECTRONIC', 'SOUL_RNB', 'ALTERNATIVE', 'ROCK', 'LATIN', 'FILM_TV', 'COUNTRY', 'AFRO_BEATS', 'WORLDWIDE', 'REGGAE_DANCE_HALL', 'HOUSE', 'K_POP', 'FRENCH_POP', 'SINGER_SONGWRITER', 'REG_MEXICO'], Field(description='')],
                         country_code: Annotated[Literal['DZ', 'BY', 'CI', 'SN', 'TN', 'AU', 'AT', 'AZ', 'AR', 'BE', 'BG', 'BR', 'GB', 'HU', 'VE', 'VN', 'GH', 'DE', 'GR', 'DK', 'EG', 'ZM', 'IL', 'IN', 'ID', 'IE', 'ES', 'IT', 'KZ', 'CM', 'CA', 'KE', 'CN', 'CO', 'CR', 'MY', 'MA', 'MX', 'MZ', 'NG', 'NL', 'NZ', 'NO', 'AE', 'PE', 'PL', 'PT', 'RU', 'RO', 'SA', 'SG', 'US', 'TH', 'TZ', 'TR', 'UG', 'UZ', 'UA', 'UY', 'PH', 'FI', 'FR', 'HR', 'CZ', 'CL', 'CH', 'SE', 'ZA', 'KR', 'JP'], Field(description='')]) -> dict: 
    '''Get a list of tracks in word by genre. Ex: https://www.app.shazam.com/charts/top-200/world'''
    url = 'https://shazam-core.p.rapidapi.com/v1/charts/genre-world'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'genre_code': genre_code,
        'country_code': country_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def chart_by_country(country_code: Annotated[Literal['DZ', 'BY', 'CI', 'SN', 'TN', 'AU', 'AT', 'AZ', 'AR', 'BE', 'BG', 'BR', 'GB', 'HU', 'VE', 'VN', 'GH', 'DE', 'GR', 'DK', 'EG', 'ZM', 'IL', 'IN', 'ID', 'IE', 'ES', 'IT', 'KZ', 'CM', 'CA', 'KE', 'CN', 'CO', 'CR', 'MY', 'MA', 'MX', 'MZ', 'NG', 'NL', 'NZ', 'NO', 'AE', 'PE', 'PL', 'PT', 'RU', 'RO', 'SA', 'SG', 'US', 'TH', 'TZ', 'TR', 'UG', 'UZ', 'UA', 'UY', 'PH', 'FI', 'FR', 'HR', 'CZ', 'CL', 'CH', 'SE', 'ZA', 'KR', 'JP'], Field(description='')]) -> dict: 
    '''Get a list of tracks by country code. Ex: https://www.app.shazam.com/charts/discovery/australia'''
    url = 'https://shazam-core.p.rapidapi.com/v1/charts/country'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'country_code': country_code,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_details(event_id: Annotated[str, Field(description='Event id')]) -> dict: 
    '''Get a Events details'''
    url = 'https://shazam-core.p.rapidapi.com/v1/events/details'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'event_id': event_id,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()

@mcp.tool()
def events_list(artist_id: Annotated[Union[int, float], Field(description='Artist id Default: 3996865 Minimum: 1')],
                date_from: Annotated[str, Field(description='Date from')],
                page_number: Annotated[Union[int, float, None], Field(description='Page number Default: 1 Minimum: 1 Maximum: 100')] = None) -> dict: 
    '''Get a list of Events by Artist ID'''
    url = 'https://shazam-core.p.rapidapi.com/v1/events/list'
    headers = {'x-rapidapi-host': 'shazam-core.p.rapidapi.com', 'x-rapidapi-key': rapid_api_key}
    payload = {
        'artist_id': artist_id,
        'date_from': date_from,
        'page_number': page_number,
    }
    payload = {k: v for k, v in payload.items() if v is not None}
    response = requests.get(url, headers=headers, params=payload)
    return response.json()



if __name__ == '__main__':
    import sys
    port = int(sys.argv[1]) if len(sys.argv) > 1 else 9997
    mcp.run(transport="stdio")
