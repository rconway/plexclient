#!/usr/bin/env python3

import os
import requests
import xml.etree.ElementTree as ET
from dotenv import load_dotenv


def main():
    load_dotenv()
    PLEX_SERVER = os.getenv('PLEX_SERVER', "localhost")
    PLEX_PORT = os.getenv('PLEX_PORT', "32400")
    PLEX_TOKEN = os.getenv('PLEX_TOKEN', "8xACJJEra1WzvnMAVkKw")
    if PLEX_TOKEN:
        try:
            url = f"http://{PLEX_SERVER}:{PLEX_PORT}/status/sessions?X-Plex-Token={PLEX_TOKEN}"
            print(f"Plex URL: {url}")
            r = requests.get(url)
            r.raise_for_status()
        except Exception as e:
            print(f"ERROR: got an exception: {e}")
        else:
            # parse response body as XML
            root = ET.fromstring(r.text)
            # video
            video = root.find("./Video")
            if video:
                title = video.get("title")
                duration = video.get("duration")
                year = video.get("year")
                art_path = video.get("art")
                thumbnail_path = video.get("thumb")
                progress_msecs = video.get("viewOffset")
                print(f"title: {title}")
                print(f"duration (msecs): {duration}")
                print(f"year: {year}")
                print(f"art (path): {art_path}")
                print(f"thumbnail (path): {thumbnail_path}")
                print(f"progress (msecs): {progress_msecs}")
                # media
                media = video.find("Media")
                if media:
                    audio_codec = media.get("audioCodec")
                    container = media.get("container")
                    video_codec = media.get("videoCodec")
                    height = media.get("videoResolution")
                    width = media.get("width")
                    print(f"audio_codec: {audio_codec}")
                    print(f"container: {container}")
                    print(f"video_codec: {video_codec}")
                    print(f"height: {height}")
                    print(f"width: {width}")
                else:
                    print("No media found in video")
            else:
                print("No video playing")
    else:
        print("ERROR: no auth token for PLex. Aborting...")


if __name__ == "__main__":
    main()
