import utils

SCHEDULER_HOST_MANAGER = scheduler.host_manager.HostManager

class Scheduler(object):
    def __init__(self):
        self.host_manager = utils.import_class(
                SCHEDULER_HOST_MANAGER)()
