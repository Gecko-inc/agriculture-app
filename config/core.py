def get_upload_to(instance, filename) -> str:
    """
      Returns the path to the media
    """
    try:
        return f'{instance.IMAGE_PATH}/{instance.id}/{filename}'
    except Exception:
        # TODO: Exception?
        return f'upload/{instance.id}/{filename}'
