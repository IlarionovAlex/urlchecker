from prometheus_client import start_http_server, Gauge
import requests
import time

# Define Prometheus metrics
url_up = Gauge('sample_external_url_up', '1 if URL is up, 0 if URL is down', ['url'])
url_response_ms = Gauge('sample_external_url_response_ms', 'Response time in ms', ['url'])

# URLs to check
urls = ["https://httpstat.us/503", "https://httpstat.us/200"]

def check_urls():
    for url in urls:
        try:
            start = time.time()
            response = requests.get(url)
            elapsed_time = (time.time() - start) * 1000  # Convert to milliseconds
            url_up.labels(url=url).set(1 if response.status_code == 200 else 0)
            url_response_ms.labels(url=url).set(elapsed_time)
        except requests.exceptions.RequestException:
            # In case of network error or invalid URL
            url_up.labels(url=url).set(0)
            url_response_ms.labels(url=url).set(0)

if __name__ == '__main__':
    # Start the Prometheus server on port 8000
    start_http_server(8000)
    while True:
        check_urls()
        time.sleep(5)  # Check every 5 seconds
