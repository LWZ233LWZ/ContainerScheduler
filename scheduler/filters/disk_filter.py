import filters

class DiskFilter(filters.BaseHostFilter):
    def _get_disk_allocation_ratio(self, host_state, filter_properties):
        return 1.0

    def host_passes(self, host_state, filter_properties):
        instance_type = filter_properties.get('instance_type')
        requested_disk = (1024 * (instance_type['disk_gb'])

        free_disk_mb = host_state.free_disk_mb
        total_usable_disk_mb = host_state.total_usable_disk_gb * 1024

        disk_allocation_ratio = self._get_disk_allocation_ratio(
            host_state, filter_properties)

        disk_mb_limit = total_usable_disk_mb * disk_allocation_ratio
        used_disk_mb = total_usable_disk_mb - free_disk_mb
        usable_disk_mb = disk_mb_limit - used_disk_mb

        if not usable_disk_mb >= requested_disk:
            return False

        disk_gb_limit = disk_mb_limit / 1024
        host_state.limits['disk_gb'] = disk_gb_limit
        return True
