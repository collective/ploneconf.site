from plone.restapi.interfaces import IJSONSummarySerializerMetadata
from zope.interface import implementer


@implementer(IJSONSummarySerializerMetadata)
class JSONSummarySerializerMetadata:
    """Additional metadata to be exposed on listings."""

    def default_metadata_fields(self):
        set_of_fields = {"image_field", "image_scales", "effective", "Subject"}
        set_of_fields.update({"speaker", "room", "audience"})
        return set_of_fields
