import csv
import math


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


def main():

    # Example list of URLs to request
    print(get_urls()) 


if __name__ == "__main__":
    main()
