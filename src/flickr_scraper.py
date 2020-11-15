import argparse
import os
import startexe
import time

from flickrapi import FlickrAPI

import urllib.request

key = "fb0352a263e142ec5cd9b2845ed2470b"  # Flickr API key https://www.flickr.com/services/apps/create/apply
secret = "4f6486ee2d6d0acb"

SAVE_FOLDER = "images"


def main():
    if not os.path.exists(SAVE_FOLDER):
        os.mkdir(SAVE_FOLDER)
    findImage()


def findImage(n=1):
    t = time.time()
    flickr = FlickrAPI(key, secret)
    license = ()  # https://www.flickr.com/services/api/explore/?method=flickr.photos.licenses.getInfo

    # search = "morning"
    search = input("What are you looking for? ")
    while not len(search) > 0:
        print("Please provide a query")
        search = input("What are you looking for? ")

    photos = flickr.walk(
        text=search,  # http://www.flickr.com/services/api/flickr.photos.search.html
        extras="url_o",
        per_page=500,
        license=license,
        sort="relevance",
    )

    for i, photo in enumerate(photos):
        if i < n:
            try:
                # construct url https://www.flickr.com/services/api/misc.urls.html
                url = photo.get("url_o")  # original size

                if url is None:
                    url = "https://farm%s.staticflickr.com/%s/%s_%s_b.jpg" % (
                        photo.get("farm"),
                        photo.get("server"),
                        photo.get("id"),
                        photo.get("secret"),
                    )

                # download
                saveImage(url, search)

                print("\033[95m%g/%g %s\033[0m" % (i + 1, n, url))
            except OSError as err:
                print("OS error: {0}".format(err))
                # print("%g/%g error..." % (i, n))
        else:
            break

    print("\033[92mDone! (%.1fs)\033[0m" % (time.time() - t))


def saveImage(url, search):
    urllib.request.urlretrieve(url, "images/" + search + ".jpg")
    urllib.request.urlretrieve(url, "temp_image/image.jpg")
    startexe.executeProcessingSystem()


if __name__ == "__main__":
    main()
