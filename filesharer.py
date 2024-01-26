from filestack import Client


class FileSharer:
    """
  Class that uploads the file specified by filepath to the cloud, and
  provides user with the URL to view the uploaded file.
  """

    def __init__(self, filepath, api_key="AQ0BAM2uSOZlEVqUzYmwYz"):
        self.filepath = filepath
        self.api_key = api_key

    def share(self):
        # Upload file to filestack, return URL to file for user
        client = Client(self.api_key)
        new_filelink = client.upload(filepath=self.filepath)
        return new_filelink.url
