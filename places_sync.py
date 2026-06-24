import requests

def get_google_maps_photos(api_key, place_id):
    """
    Fetches image URLs from Google Places API (New) for reviews and user-uploaded media.
    """
    # API Endpoint for retrieving place data fields
    url = f"https://places.googleapis.com/v1/places/{place_id}"
    
    headers = {
        "Content-Type": "application/json",
        "X-Goog-Api-Key": api_key,
        # Field mask limits response payload strictly to photo metadata arrays
        "X-Goog-FieldMask": "photos"
    }
    
    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        print("Failed to query Google Places API resource.")
        return []
        
    place_data = response.json()
    photo_records = place_data.get("photos", [])
    
    image_urls = []
    # Loop through retrieved user-uploaded media objects (Max 10 tokens typically returned)
    for photo in photo_records[:6]:
        photo_name = photo.get("name") # Format: places/{place_id}/photos/{photo_id}
        
        # Build direct accessible thumbnail or image URL via Places Media endpoint
        media_url = (
            f"https://places.googleapis.com/v1/{photo_name}/media"
            f"?key={api_key}&maxHeightPx=800"
        )
        image_urls.append(media_url)
        
    return image_urls