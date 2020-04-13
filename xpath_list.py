work_methodology_category = ['', 'Integration tests', 'Unit tests', 'Tester', 'Agile management', 'Issue tracking tool', 
'Knowledge repository', 'Code reviews', 'Static code analysis', 'Version control system', 
'Build server', 'QA manager', 'Distributed team', 'Research and Experimentation', 'Pair programming', 
'Workshops', 'e2e tests', 'Commit on the first day', 'One command build possible', 'Up and running within 2h', 
'High level and low level designs', 'Feature development and porting', 'Regression testing', 
'UAT testing', 'Agile Testing', 'Manual tests', 'Database', 'Virtualization', 'Cloud infrastructure', 
'Operating system', 'Databases', 'Network virtualization', 'Provisioning', 'Networking hardware', 'Security', 
'Application stack', 'Operating systems']

equipment_supplied_category = ['Operating System', 'Computer', 'Monitors']

specs_category = ['Job profile', 'Start', 'Contract duration', 'Paid holiday', 'Part time work', 'Remote possible',
'Flexible hours', 'Travel involved', 'Freedom to choose tools', 'Relocation package', 'Remote work', 
'Open-minded developers in team', 'Work with international client']


offer_name_xpath = '//nfj-posting-header/div/div/h1/text()'
company_xpath = '//nfj-posting-header//dt[text()="Company:"]//parent::*/dd/text()'
company_size_xpath = '//nfj-posting-header//dt[text()="Company size:"]//parent::*/dd/text()'
job_location_xpath = '//nfj-posting-apply-box//div[@class="additional-info border-top"]/div/nfj-postings-locations//li/text()'
salary_1_xpath = '//nfj-posting-apply-box/div/div/nfj-posting-salaries//div[1]//h4/text()'
salary_1_description_xpath = '//nfj-posting-apply-box/div/div/nfj-posting-salaries//div[1]//p/text()'
salary_2_xpath = '//nfj-posting-apply-box/div/div/nfj-posting-salaries//div[2]//h4/text()'
salary_2_description_xpath = '//nfj-posting-apply-box/div/div/nfj-posting-salaries//div[2]//p/text()'
salary_bonus_xpath = '//nfj-postings-bonus//span[@class="about-bonuses"]/a/text()'
seniority_1_xpath = '//nfj-posting-seniority//div[@class="col star-section text-center active"][1]/p/text()'
seniority_2_xpath = '//nfj-posting-seniority//div[@class="col star-section text-center active"][2]/p/text()'
job_description_xpath = '//nfj-posting-description/div/p/text()'

must_have_xpath = '//nfj-posting-requirements//h3[text()="Must have"]//parent::*//button//text()'
nice_to_have_xpath = '//nfj-posting-requirements//h3[text()="Nice to have"]//parent::*//button//text()'

# work_methodology
integration_tests_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[1]}.")]//parent::*//parent::*//dd//text()'
unit_tests_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[2]}.")]//parent::*//parent::*//dd//text()'
tester_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".Tester(s).")]//parent::*//parent::*//dd//text()'
agile_management_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[4]}.")]//parent::*//parent::*//dd//text()'
issue_tracking_tool_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[5]}.")]//parent::*//parent::*//dd//text()'
knowledge_repository_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[6]}.")]//parent::*//parent::*//dd//text()'
code_reviews_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[7]}.")]//parent::*//parent::*//dd//text()'
static_code_analysis_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[8]}.")]//parent::*//parent::*//dd//text()'
version_control_system_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[9]}.")]//parent::*//parent::*//dd//text()'
build_server_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[10]}.")]//parent::*//parent::*//dd//text()'
qa_manager_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[11]}.")]//parent::*//parent::*//dd//text()'
distributed_team_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[12]}.")]//parent::*//parent::*//dd//text()'
research_and_experimentation_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[13]}.")]//parent::*//parent::*//dd//text()'
pair_programming_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[14]}.")]//parent::*//parent::*//dd//text()'
workshops_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[15]}.")]//parent::*//parent::*//dd//text()'
e2e_tests_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[16]}.")]//parent::*//parent::*//dd//text()'
commit_on_the_first_day_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[17]}.")]//parent::*//parent::*//dd//text()'
one_command_build_possible_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[18]}.")]//parent::*//parent::*//dd//text()'
up_and_running_within_2h_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[19]}.")]//parent::*//parent::*//dd//text()'
high_level_and_low_level_designs_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[20]}.")]//parent::*//parent::*//dd//text()'
feature_development_and_porting_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[21]}.")]//parent::*//parent::*//dd//text()'
regression_testing_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[22]}.")]//parent::*//parent::*//dd//text()'
uat_testing_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[23]}.")]//parent::*//parent::*//dd//text()'
agile_testing_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[24]}.")]//parent::*//parent::*//dd//text()'
manual_tests_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[25]}.")]//parent::*//parent::*//dd//text()'
database_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[26]}.")]//parent::*//parent::*//dd//text()'
virtualization_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[27]}.")]//parent::*//parent::*//dd//text()'
cloud_infrastructure_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[28]}.")]//parent::*//parent::*//dd//text()'
operating_system_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[29]}.")]//parent::*//parent::*//dd//text()'
databases_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[30]}.")]//parent::*//parent::*//dd//text()'
network_virtualization_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[31]}.")]//parent::*//parent::*//dd//text()'
provisioning_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[32]}.")]//parent::*//parent::*//dd//text()'
networking_hardware_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[33]}.")]//parent::*//parent::*//dd//text()'
security_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[34]}.")]//parent::*//parent::*//dd//text()'
application_stack_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[35]}.")]//parent::*//parent::*//dd//text()'
operating_systems_xpath = f'//nfj-posting-methodologies//div//span[re:test(text(), ".{work_methodology_category[36]}.")]//parent::*//parent::*//dd//text()'

# operating_system_xpath = f'//nfj-posting-benefits//div[re:test(text(), ".{equipment_supplied_category[0]}.")]//parent::*//svg-icon-sprite//@class'
operating_system_1_xpath = f'//nfj-posting-benefits//div[re:test(text(), ".{equipment_supplied_category[0]}.")]//parent::*//svg-icon-sprite/@class'
operating_system_2_xpath = f'//nfj-posting-benefits//div[re:test(text(), ".{equipment_supplied_category[0]}.")]//parent::*//svg-icon-sprite/@src'
computer_xpath = f'//nfj-posting-benefits//div//div[re:test(text(), ".{equipment_supplied_category[1]}.")]//parent::*//div[2]//text()'
monitors_xpath = f'//nfj-posting-benefits//div//div[re:test(text(), ".{equipment_supplied_category[2]}.")]//parent::*//div[2]//text()'

# specs_category
# job_profile_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[0]}.")]//parent::*//div[2]//text()'

job_profile_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[0]}.")]//parent::*//div[2]//text()'
start_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[1]}.")]//parent::*//div[2]//text()'
contract_duration_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[2]}.")]//parent::*//div[2]//text()'
paid_holiday_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[3]}.")]//parent::*//div[2]//text()'
part_time_work_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[4]}.")]//parent::*//div[2]//text()'
remote_possible_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[5]}.")]//parent::*//div[2]//text()'
flexible_hours_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[6]}.")]//parent::*//div[2]//text()'
travel_involved_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[7]}.")]//parent::*//div[2]//text()'
freedom_to_choose_tools_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[8]}.")]//parent::*//div[2]//text()'
relocation_package_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[9]}.")]//parent::*//div[2]//text()'
remote_work_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[10]}.")]//parent::*//div[2]//text()'
open_minded_developers_in_team_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[11]}.")]//parent::*//div[2]//text()'
work_with_international_client_xpath = f'//nfj-posting-specs//div[re:test(text(), ".{specs_category[12]}.")]//parent::*//div[2]//text()'

perks_in_the_office_xpath = '//nfj-posting-perks//h3[text()="Perks in the office"]//parent::*//text()'
benefits_xpath = '//nfj-posting-perks//h3[text()="Benefits"]//parent::*//text()'