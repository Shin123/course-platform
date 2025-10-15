def get_cloudinary_image_object(instance, field_name="image", as_html=False, width=200):
    if not hasattr(instance, field_name):
        return None
    image_object = getattr(instance, field_name)
    if not image_object:
        return None
    image_option = {"width": width}
    if as_html:
        return image_object.image(**image_option)
    url = image_object.build_url(**image_option)
    return url


video_html = """
<video controls autoplay>
<source src="{video_url}" />
</video>
"""


def get_cloudinary_video_object(
    instance,
    field_name="video",
    as_html=False,
    width=None,
    height=None,
    sign_url=False,
    fetch_format="auto",
    quality="auto",
    controls=True,
    autoplay=True,
):
    if not hasattr(instance, field_name):
        return ""
    video_object = getattr(instance, field_name)
    if not video_object:
        return ""
    video_option = {
        "sign_url": sign_url,
        "fetch_format": fetch_format,
        "quality": quality,
        "controls": controls,
        "autoplay": autoplay,
    }
    if width:
        video_option["width"] = width
    if height:
        video_option["height"] = height
    if height and width:
        video_option["crop"] = "limit"
    url = video_object.build_url(**video_option)
    if as_html:
        return video_html.format(video_url=url)
    return url
