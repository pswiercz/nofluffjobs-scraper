o['integration_tests']] = response.xpath(integration_tests_xpath).get()


o['job_profile'] = response.xpath(job_profile).get()
o['start'] = response.xpath(start).get()
o['contract_duration'] = response.xpath(contract_duration).get()
o['paid_holiday'] = response.xpath(paid_holiday).get()
o['part_time_work'] = response.xpath(part_time_work).get()
o['remote_possible'] = response.xpath(remote_possible).get()
o['flexible_hours'] = response.xpath(flexible_hours).get()
o['travel_involved'] = response.xpath(travel_involved).get()
o['freedom_to_choose_tools'] = response.xpath(freedom_to_choose_tools).get()
o['relocation_package'] = response.xpath(relocation_package).get()
o['remote_work'] = response.xpath(remote_work).get()
o['open_minded_developers_in_team'] = response.xpath(open_minded_developers_in_team).get()
o['work_with_international_client'] = response.xpath(work_with_international_client).get()

