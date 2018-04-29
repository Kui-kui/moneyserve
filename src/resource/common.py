"""
Define the common REST verbs
"""
from flask import jsonify, current_app
from flask.ext.restful import Resource


class CommonResource(Resource):
    """Base functions relative to common REST routes."""

    def get(self):
        """Get list of all routes."""
        output = []
        for rule in current_app.url_map.iter_rules():
            methods = ','.join(rule.methods)
            line = "{:50s} {:20s}".format(str(rule), methods)
            output.append(line)

        return jsonify(routes=output)
