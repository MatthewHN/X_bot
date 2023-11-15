from media_downloader import download_media

def test_download_media():
    test_url = 'https://v.redd.it/dn9zy4a7z50c1'  # Replace with a valid image URL
    test_filename = 'downloaded_image'  # This will be the base name for the downloaded file

    downloaded_file = download_media(test_url, test_filename)
    if downloaded_file:
        print(f"Media downloaded successfully: {downloaded_file}")
    else:
        print("Failed to download media.")

if __name__ == "__main__":
    test_download_media()
