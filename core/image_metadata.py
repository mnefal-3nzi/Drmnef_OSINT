from PIL import Image
from PIL.ExifTags import TAGS
import os

def extract_metadata(image_path):
    result = {}
    try:
        image = Image.open(image_path)
        exif_data = image._getexif()
        if not exif_data:
            return {"Error": "لا توجد بيانات EXIF"}
        for tag_id, value in exif_data.items():
            tag = TAGS.get(tag_id, tag_id)
            result[tag] = value
    except Exception as e:
        result = {"Error": str(e)}
    return result