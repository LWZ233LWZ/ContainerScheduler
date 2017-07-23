"""
Scheduler Service
"""
import utils


DEFAULT_SCHEDULER_DRIVER = scheduler.filter_scheduler.FilterScheduler

class SchedulerManager(Object):

    def __init__(self, scheduler_driver=None, *args, **kwargs):
        if not scheduler_driver:
            scheduler_driver = DEFAULT_SCHEDULER_DRIVER
        self.driver = utils.import_class(scheduler_driver)(*args, **kwargs)

    def select_destinations(self, request_spec, filter_properties):
        dests = self.driver.select_destinations(request_spec,
            filter_properties)
        return dests
