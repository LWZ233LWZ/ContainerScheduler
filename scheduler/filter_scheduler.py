import random

import driver

class FilterScheduler(driver.Scheduler):
    def __init__(self, *args, **kwargs):
        super(FilterScheduler, self).__init__(*args, **kwargs)

    def select_destinations(self, request_spec, filter_properties):
        num_insts = request_spec['num_insts']
        selected_hosts = self._schedule(request_spec,
                                        filter_properties)

        if len(selected_hosts) < num_insts:
            return None 

        dests = [ host for host in selected_hosts]
        return dests

    def _schedule(self, request_spec, filter_properties):
        hosts = self._get_all_host_states()

        selected_hosts = []
        num_insts = request_spec.get('num_insts', 1)

        for num in range(num_insts):
            hosts = self.host_manager.get_filtered_hosts(hosts,
                    filter_properties, index=num)
            if not hosts:
                break

            chosen_host = random.choice(
                hosts[0:len(hosts])
            selected_hosts.append(chosen_host)

        return selected_hosts

    def _get_all_host_states(self):
        return self.host_manager.get_all_host_states()
