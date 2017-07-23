import random
import driver

class ChanceScheduler(driver.Scheduler):
    def _filter_hosts(self, request_spec, hosts, filter_properties):
        """Filter a list of hosts based on request_spec."""

        ignore_hosts = filter_properties.get('ignore_hosts', [])
        hosts = [host for host in hosts if host not in ignore_hosts]
        return hosts

    def _schedule(self, request_spec, filter_properties):
        hosts = self._filter_hosts(request_spec, hosts, filter_properties)
        if not hosts:
            print "Could not find a node"
            return 
        return random.choice(hosts)

    def select_destinations(self, request_spec, filter_properties):
        num_insts = request_spec['num_insts']
        dests = []
        for i in range(num_insts):
            host = self._schedule(request_spec, filter_properties)
            dests.append(host)

        if len(dests) < num_insts:
            print 'There are not enough hosts available.'
            return 

        return dests
