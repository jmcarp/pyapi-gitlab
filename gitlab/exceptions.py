class HttpError(Exception):
    """
    An http error occurred
    """
    pass

class GitlabError(Exception):
    def __init__(self, response):
        super(GitlabError, self).__init__(response)
