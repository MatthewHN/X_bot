import requests


def download_media(media_url, filename):
    try:
        response = requests.get(media_url, stream=True)
        if response.status_code == 200:
            with open(filename, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            return True
        else:
            print(f"Failed to download media: {media_url}")
            return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
