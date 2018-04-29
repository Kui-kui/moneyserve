"""
Define an Abstract Base Class (ABC)
Not an actual ABC to avoid metaclasses conflicts
"""
from datetime import date
from itertools import chain
from flask.ext.restful import Resource


class BaseResource(Resource):
    """ Factor methods usually needed by resources """
    @staticmethod
    def iter_result(result):
        """ Wrap the way to iter on a SQLAlchemy result """
        return getattr(result, '_asdict', dict)().items()

    def results_to_dict(self, *results, to_exclude=()):
        """ Transform an SQLAlchemy result returned by a query into a dict with formatted dates
            Date formatting is done the same way it's done in the models' ABC """
        return {
            key: value if not isinstance(value, date) else value.strftime('%Y-%m-%d')
            for key, value in chain.from_iterable(map(self.iter_result, results))
            if key not in to_exclude
        }

    def result_to_dict_list(self, results, to_exclude=()):
        """ Transform an SQLAlchemy result returned by a query into a list of dicts, using `result_to_dict`
            The `to_exclude` parameter is forwarded to `result_to_dict` """
        return [
            self.results_to_dict(result, to_exclude=to_exclude)
            for result in results
        ]
