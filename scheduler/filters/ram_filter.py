import filters

class BaseRamFilter(filters.BaseHostFilter):

    def host_passes(self, host_state, filter_properties):
        instance_type = filter_properties.get('instance_type')
        requested_ram = instance_type['memory_mb']
        free_ram_mb = host_state.free_ram_mb
        total_usable_ram_mb = host_state.total_usable_ram_mb

        if not total_usable_ram_mb >= requested_ram:
            return False

        ram_allocation_ratio = self._get_ram_allocation_ratio(host_state,
                                                          filter_properties)

        memory_mb_limit = total_usable_ram_mb * ram_allocation_ratio
        used_ram_mb = total_usable_ram_mb - free_ram_mb
        usable_ram = memory_mb_limit - used_ram_mb
        if not usable_ram >= requested_ram:
            return False

        host_state.limits['memory_mb'] = memory_mb_limit
        return True


class RamFilter(BaseRamFilter):
    def _get_ram_allocation_ratio(self, host_state, filter_properties):
        return host_state.ram_allocation_ratio

