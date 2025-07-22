from crewai.tools import tool   
import requests
from bs4 import BeautifulSoup
import json
import os 
from datetime import datetime
from urllib.parse import urljoin, urlparse

@tool("Web Page Scraper")
def scraper_tool(url: str) -> str:
    """
    Scrape a web page and return its structure.
    """
    try:
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36'
        }
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() # This function returns http exception if one occurs
        soup = BeautifulSoup(response.content, 'html.parser')

        elements = {
            'buttons': [{'text': btn.get_text().strip(), 'id': btn.get('id'), 'class': btn.get('class')} 
                       for btn in soup.find_all(['button', 'input']) if btn.get('type') in ['button', 'submit', None]],
            'forms': [{'id': form.get('id'), 'class': form.get('class'), 'action': form.get('action')} 
                     for form in soup.find_all('form')],
            'links': [{'text': link.get_text().strip(), 'href': link.get('href'), 'id': link.get('id')} 
                     for link in soup.find_all('a') if link.get('href')],
            'inputs': [{'type': inp.get('type'), 'name': inp.get('name'), 'id': inp.get('id'), 'placeholder': inp.get('placeholder')} 
                      for inp in soup.find_all('input')],
            'headings': [{'level': h.name, 'text': h.get_text().strip(), 'id': h.get('id')} 
                        for h in soup.find_all(['h1', 'h2', 'h3', 'h4', 'h5', 'h6'])],
            'page_title': soup.title.string if soup.title else 'No title',
            'meta_description': soup.find('meta', attrs={'name': 'description'})['content'] if soup.find('meta', attrs={'name': 'description'}) else ''
        }

        return f"Successfully scraped {url}. Found: {len(elements['buttons'])} buttons, {len(elements['forms'])} forms, {len(elements['links'])} links, {len(elements['inputs'])} inputs. Page structure: {json.dumps(elements, indent=2)}"
    
    except Exception as e:
        return f"Error scraping {url}: {str(e)}"
    
@tool("File Tool")
def file_tool(action: str, filename: str = "", content: str = "") -> str:
    """
    Manage file operations for snapshot storage.
    """
    try:
        snapshot_dir = "snapshots"
        os.makedirs(snapshot_dir, exist_ok=True)

        if action == "save":
            filepath = os.path.join(snapshot_dir, filename)
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            return f"Saved snapshot to {filepath}"
        
        elif action == "load":
            filepath = os.path.join(snapshot_dir, filename)
            if os.path.exists(filepath):
                with open(filepath, 'r', encoding='utf-8') as f:
                    return f.read()
                
            return f"File {filename} not found"
        
        elif action == "list":
            files = os.listdir(snapshot_dir) if os.path.exists(snapshot_dir) else []
            return f"Available snapshots: {', '.join(files)}"
        
        return "Invalid action. Use 'save', 'load', or 'list'"
    
    except Exception as e:
        return f"File operation error: {str(e)}"
