import inspect

class BaseFilter(object):
    def _filter_one(self, obj, filter_properties):
        return True

    def filter_all(self, filter_obj_list, filter_properties):
        for obj in filter_obj_list:
            if self._filter_one(obj, filter_properties):
                yield obj

    run_filter_once_per_request = False

    def run_filter_for_index(self, index):
        if self.run_filter_once_per_request and index > 0:
            return False
        else:
            return True

class BaseFilterHandler(object):
    def get_matching_classes(self, loadable_class_names):
        classes = []
        for cls_name in loadable_class_names:
            obj = utils.import_class(cls_name)
            if inspect.isfunction(obj):
                for cls in obj():
                    classes.append(cls)
        return classes

    def get_filtered_objects(self, filters, objs, filter_properties, index=0):
        list_objs = list(objs)
        for filter_ in filters:
            if filter_.run_filter_for_index(index):
                cls_name = filter_.__class__.__name__
                start_count = len(list_objs)
                objs = filter_.filter_all(list_objs, filter_properties)
                if objs is None:
                    return
                list_objs = list(objs)
                end_count = len(list_objs)
        return list_objs

class BaseHostFilter(BaseFilter):
    def _filter_one(self, obj, filter_properties):
        return self.host_passes(obj, filter_properties)

    def host_passes(self, host_state, filter_properties):
        pass


class HostFilterHandler(BaseFilterHandler):
    def __init__(self):
        super(HostFilterHandler, self).__init__(BaseHostFilter)


def all_filters():
    return []
