import os
import requests

def download_media(media_url, filename, save_path):
    media_url = "https://packaged-media.redd.it/izchbn8eip1c1/pb/m2-res_1920p.mp4?m=DASHPlaylist.mpd&v=1&e=1700611200&s=3fb72aa238620b30c534b26927664715a7b6d9f8#t=0"
    # Ensure the save path exists, create if it doesn't
    if not os.path.exists(save_path):
        os.makedirs(save_path)

    # Construct the full path for the file
    full_file_path = os.path.join(save_path, filename)

    try:
        response = requests.get(media_url, stream=True)
        if response.status_code == 200:
            with open(full_file_path, 'wb') as f:
                for chunk in response.iter_content(1024):
                    f.write(chunk)
            print(f"Media downloaded successfully: {full_file_path}")
            return True
        else:
            print(f"Failed to download media: {media_url}")
            return False
    except Exception as e:
        print(f"Unexpected error: {e}")
        return False
