def getLowestCommonManager(topManager, reportOne, reportTwo):
    return get_org_info(topManager, reportOne, reportTwo).lowest_common_manager


def get_org_info(manager, report_one, report_two):
    num_important_reports = 0
    for direct_report in manager.direct_reports:
        org_info = OrgInfo(direct_report, report_one, report_two)
        if org_info.lowest_common_manager is not None:
            return org_info
        num_important_reports += org_info.num_important_reports
    if manager == report_one or manager == report_two:
        num_important_reports += 1


    lowest_common_manager =  manager if num_important_reports  == 2 else None
    return OrgInfo(lowest_common_manager, num_important_reports)
    
class OrgInfo:
    def __init__(self, lowest_common_manager, num_important_reports):
        self.lowest_common_manager = lowest_common_manager
        self.num_important_reports = num_important_reports





