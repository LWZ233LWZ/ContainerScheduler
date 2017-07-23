import collections
import functools
import time

import filters
import utils

scheduler_default_filters = ['RamFilter', 'DiskFilter']

class HostManager(object):

    def __init__(self):
        self.host_state_map = {}
        self.filter_handler = filters.HostFilterHandler()
        filter_classes = self.filter_handler.get_matching_classes(
                ['scheduler.filters.all_filters'])
        self.filter_cls_map = {cls.__name__: cls for cls in filter_classes}
        self.default_filters = self._choose_host_filters(self._load_filters())

    def _load_filters(self):
        return scheduler_default_filters

    def _choose_host_filters(self, filter_cls_names):
        if not isinstance(filter_cls_names, (list, tuple)):
            filter_cls_names = [filter_cls_names]

        filters = []
        for filter_name in filter_cls_names:
            filter_cls = self.filter_cls_map[filter_name]
            self.filter_obj_map[filter_name] = filter_cls()
            filters.append(self.filter_obj_map[filter_name])
        return filters

    def get_filtered_hosts(self, hosts, filter_properties,
            filter_class_names=None, index=0):

        if filter_class_names is None:
            filters = self.default_filters
        else:
            filters = self._choose_host_filters(filter_class_names)

        return self.filter_handler.get_filtered_objects(filters,
                hosts, filter_properties, index)

    def get_all_host_states(self):
        pass
