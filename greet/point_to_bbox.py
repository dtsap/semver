import csv
import math
import requests
import time
from concurrent.futures import ThreadPoolExecutor, as_completed


# Function to calculate the bbox
def calculate_bbox(lat, lon, distance_km):
    # Earth radius in kilometers
    earth_radius_km = 6371.0

    # Calculate the distance in degrees
    lat_distance_deg = distance_km / earth_radius_km * (180 / math.pi)
    lon_distance_deg = distance_km / (earth_radius_km * math.cos(math.pi * lat / 180)) * (180 / math.pi)

    # Calculate the bounding box
    min_lat = lat - lat_distance_deg
    max_lat = lat + lat_distance_deg
    min_lon = lon - lon_distance_deg
    max_lon = lon + lon_distance_deg

    return min_lat, min_lon, max_lat, max_lon



def get_urls():
    with open("FCC-Grids-CA.csv") as fp:
        reader = csv.DictReader(fp)
        requests = {}

        for index, row in enumerate(reader):
            lon = row["maxPopCentroid_Longitude"]
            lat = row["maxPopCentroid_Latitude"]
            click = f"{lat},{lon}"
            bbox = ",".join([str(i) for i in calculate_bbox(float(lat), float(lon), 10)])
            requests[row["\ufeffgridKey"]] = ("https://gsc.t-mobile.com/api/fcc-grid-cells/"
                "?schema=gsc_tmo:fcc_grids_v2&layers=gsc_tmo:fcc_grids_v2&propertyName=Accessible&resultsNumber=4&styles=fcc_grids_v2_default&cql_filter=1=1&format_data=geo&token=b7b0ee97882588f71f6e076f9ebba3d47ff18081&"
                "mktname=San%20Francisco&mktid=2&mktsuffix=SF&email=christina.liakopoulou1@t-mobile.com&"
                "bbox=37.708404,-122.548559,37.855473,-122.357328&center=37.781939,-122.452943&zoom=13&trigger=click&"
                f"click={click}&tbbox={bbox}&tsize=256,256&tp=1309,3165&pclick=40.91740798884793,98.9341449782324&_dc=1718278190769"
            )
            
            if index == 40:
                break
            
    return requests


def make_request(url):
    try:
        response = requests.get(url)
        response.raise_for_status()
        return response.text
    except requests.RequestException as e:
        print(f"Request failed: {e}")
        return None


def process_chunk(urls, rate_limit, max_workers):
    results = []
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        future_to_url = {executor.submit(make_request, url): url for url in urls}
        for future in as_completed(future_to_url):
            url = future_to_url[future]
            try:
                result = future.result()
                results.append((url, result))
            except Exception as e:
                print(f"Exception occurred for {url}: {e}")
            time.sleep(rate_limit)
    return results


def make_requests_in_chunks(urls, chunk_size, rate_limit=1, max_workers=5):
    all_results = {}
    for i in range(0, len(urls), chunk_size):
        chunk = list(urls.values())[i:i + chunk_size]
        print(f"Processing chunk: {chunk}")
        results = process_chunk(chunk, rate_limit, max_workers)

        grids = list(urls.keys())[i:i + chunk_size]
        for result, grid in zip(results, grids):
            all_results[grid] = result
        # Optional delay between chunks to further reduce server load
        time.sleep(rate_limit)
    return all_results


def main():

    # Example list of URLs to request
    urls = get_urls()

    # Make requests in chunks
    chunk_size = 20  # Number of requests per chunk
    results = make_requests_in_chunks(urls, chunk_size, rate_limit=1, max_workers=5)

    # Print the results
    for grid, result in results.items():
        print(f"URL: {grid}\nResponse: {result}\n")

