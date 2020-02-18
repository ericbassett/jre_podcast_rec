import requests
import time, os

def get_page(url, sleep=0.5, retry=3):
    """
    Use requests to get a page with multiple retries and error
    handling
    """
    # try 'requests' 3 times to get success (status_code == 200)
    for i in range(retry):
        try:
            response = requests.get(url)
            if response.status_code == 200:
                if i > 0:
                    print(f'done in {i+1} tries')
                break
            time.sleep(sleep)

        # try again if error, probably network connection reset
        except:
            time.sleep(5)
            print('Error, retrying')
            continue
    # sleep
    time.sleep(sleep)
    return response

def rec_progress(num, tot, file, text):
    # progress log
    file.write(
        str.format(
            '{}/{}\t\t{}\n',
            num,
            tot,
            text
        ),
    )
    
    # flush so you can check on it remotely
    file.flush()

def rec_error(file, text):
    # write error and newline
    file.write(
        str.format('{}\n', text)
    )

    # flush file
    file.flush()
