
import falcon

class AutoresResource:
    def on_get(self, req, resp):
        """Handles GET requests"""
        autores = {
            'autores': (
                "Creado Por- Oscar Rubio Garcia"
            )
        }

        resp.media = autores

api = falcon.API()
api.add_route('/', AutoresResource())