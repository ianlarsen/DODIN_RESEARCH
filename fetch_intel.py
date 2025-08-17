import requests
import xml.etree.ElementTree as ET

def fetch_cisa_rss(rss_url):
    resp = requests.get(rss_url)
    resp.raise_for_status()
    root = ET.fromstring(resp.content)
    items = []
    for item in root.findall(".//item"):
        title = item.findtext("title")
        link = item.findtext("link")
        pub_date = item.findtext("pubDate")
        description = item.findtext("description")
        items.append({
            "id": link,  # Use link as unique ID
            "title": title,
            "link": link,
            "pub_date": pub_date,
            "description": description
        })
    return items