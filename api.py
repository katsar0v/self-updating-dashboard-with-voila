# Let's get this party started!
import falcon
import json
import random
import numpy


# Falcon follows the REST architectural style, meaning (among
# other things) that you think in terms of resources and state
# transitions, which map to HTTP verbs.
class SampleAPI(object):
    def on_get(self, req, resp):
        """Handles GET requests"""
        resp.status = falcon.HTTP_200  
        resp.content_type = 'application/json'
        resp.body = json.dumps([numpy.random.normal(size = 2).tolist() for x in range(random.randint(100,1000))])

app = falcon.API()

app.add_route('/api', SampleAPI())