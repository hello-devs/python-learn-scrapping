import wget

# Open the file containing the URLs
with open('pdf_link') as f:
    # Read each line (URL) in the file
    for url in f:
        # Remove any whitespace at the beginning and end of the URL
        url = url.strip()
        # Download the contents of the URL and save it to a file

        try:
            # Download the contents of the URL and save it to a file
            wget.download(url, "courses/")
        except Exception as e:
            # If an exception occurs, save the error message to a log file
            with open('error.log', 'a') as logfile:
                logfile.write(f'Error downloading {url}: {str(e)}\n')
