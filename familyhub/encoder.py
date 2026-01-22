#########################################################
# GENERATED FILE - DO NOT EDIT
# Safe to regenerate at any time 
#########################################################
from connexion.jsonifier import JSONEncoder as ConnexionJSONEncoder

from familyhub.models.base_model import Model


class JSONEncoder(ConnexionJSONEncoder):
    include_nulls = False

    def default(self, o):
        if isinstance(o, Model):
            dikt = {}
            for attr in o.openapi_types:
                value = getattr(o, attr)
                if value is None and not self.include_nulls:
                    continue
                attr = o.attribute_map[attr]
                dikt[attr] = value
            return dikt
        return JSONEncoder.default(self, o)
