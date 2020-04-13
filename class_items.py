import scrapy

class Offer(scrapy.Item):
	url = scrapy.Field()
	offer_name = scrapy.Field()
	company = scrapy.Field()
	company_size = scrapy.Field()
	job_location = scrapy.Field()
	salary_1 = scrapy.Field()
	salary_1_description = scrapy.Field()
	salary_2 = scrapy.Field()
	salary_2_description = scrapy.Field()
	salary_bonus = scrapy.Field() 
	seniority = scrapy.Field()
	seniority_1 = scrapy.Field()
	seniority_2 = scrapy.Field()
	job_description = scrapy.Field()
	must_have = scrapy.Field()
	nice_to_have = scrapy.Field()

	# work_methodology
	integration_tests = scrapy.Field()
	unit_tests = scrapy.Field()
	tester = scrapy.Field()
	agile_management = scrapy.Field()
	issue_tracking_tool = scrapy.Field()
	knowledge_repository = scrapy.Field()
	code_reviews = scrapy.Field()
	static_code_analysis = scrapy.Field()
	version_control_system = scrapy.Field()
	build_server = scrapy.Field()
	qa_manager = scrapy.Field()
	distributed_team = scrapy.Field()
	research_and_experimentation = scrapy.Field()
	pair_programming = scrapy.Field()
	workshops = scrapy.Field()
	e2e_tests = scrapy.Field()
	commit_on_the_first_day = scrapy.Field()
	one_command_build_possible = scrapy.Field()
	up_and_running_within_2h = scrapy.Field()
	high_level_and_low_level_designs = scrapy.Field()
	feature_development_and_porting = scrapy.Field()
	regression_testing = scrapy.Field()
	uat_testing = scrapy.Field()
	agile_testing = scrapy.Field()
	manual_tests = scrapy.Field()
	database = scrapy.Field()
	virtualization = scrapy.Field()
	cloud_infrastructure = scrapy.Field()
	databases = scrapy.Field()
	network_virtualization = scrapy.Field()
	provisioning = scrapy.Field()
	networking_hardware = scrapy.Field()
	security = scrapy.Field()
	application_stack = scrapy.Field()

	# equipment_supplied_category
	operating_system = scrapy.Field()
	computer = scrapy.Field()
	monitors = scrapy.Field()

	# specs_category
	job_profile = scrapy.Field()
	start = scrapy.Field()
	contract_duration = scrapy.Field()
	paid_holiday = scrapy.Field()
	part_time_work = scrapy.Field()
	remote_possible = scrapy.Field()
	flexible_hours = scrapy.Field()
	travel_involved = scrapy.Field()
	freedom_to_choose_tools = scrapy.Field()
	relocation_package = scrapy.Field()
	remote_work = scrapy.Field()
	open_minded_developers_in_team = scrapy.Field()
	work_with_international_client = scrapy.Field()

	perks_in_the_office = scrapy.Field()
	benefits = scrapy.Field()