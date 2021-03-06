
from .latest_activity import LatestActivity


class Tagged(object):
    """Base class for wrapping `values` dictionaries of related
    tag information
    """

    def __init__(self, **kwargs):
        self._latest_translation = kwargs.pop(
            "latest_translation", None)
        self.approved_strings = kwargs.get('approved_strings')
        self.fuzzy_strings = kwargs.get('fuzzy_strings')
        self.total_strings = kwargs.get('total_strings')
        self.translated_strings = kwargs.get('translated_strings')
        self.kwargs = kwargs

    @property
    def chart(self):
        """Generate a dict of chart information
        """
        return (
            {k: v
             for k, v
             in self.kwargs.items()
             if k in ['approved_strings',
                      'fuzzy_strings',
                      'total_strings',
                      'translated_strings']}
            if self.kwargs.get('total_strings')
            else None)

    @property
    def latest_translation(self):
        return self._latest_translation

    @property
    def latest_activity(self):
        """Returns wrapped LatestActivity data if available
        """
        return (
            LatestActivity(self.latest_translation)
            if self.latest_translation
            else None)

    @property
    def tag(self):
        return self.kwargs.get('slug')


class TaggedLocale(Tagged):
    """Wraps a Locale to provide stats and latest information
    """

    @property
    def code(self):
        return self.kwargs.get('code')

    @property
    def name(self):
        return self.kwargs.get('name')

    @property
    def population(self):
        return self.kwargs.get('population')

    @property
    def project(self):
        return self.kwargs.get('project')
