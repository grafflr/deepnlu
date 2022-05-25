
#!/usr/bin/env python
# -*- coding: UTF-8 -*-

# pylint:disable=bad-whitespace
# pylint:disable=line-too-long
# pylint:disable=too-many-lines
# pylint:disable=invalid-name

# #########################################################
#
#       ************** !! WARNING !! ***************
#       ******* THIS FILE WAS AUTO-GENERATED *******
#       ********* DO NOT MODIFY THIS FILE **********
#
# #########################################################

class RolesLabelsRev(object):

    @staticmethod
    def prov() -> dict:
        return {
 'action': ['router.py',
            'plac_core.py',
            'owl2py_orchestrator.py',
            'generate_runtime_dictionaries.py',
            'generate_runtime_dictionary.py',
            'owl_data_load_dict.py',
            'common_utils.py'],
 'config': {'classname': 'RolesLabels',
            'filename': 'roles_labels',
            'queries': ['labels.sparql'],
            'reverse': True,
            'transformers': ['labels']},
 'source': 'roles.owl',
 'time': '2022-04-27 21:17:15.540355'}

    __data = {
    'Accountant': ['accountant'],
    'Accounting': ['accounting'],
    'Accounts': ['accounts'],
    'Activity': ['activity'],
    'Administration': ['administration'],
    'Administrative Accounting': ['administrative_accounting'],
    'Agent': ['agent'],
    'Analyst': ['analyst'],
    'Architect': ['architect'],
    'Auditing': ['auditing'],
    'Auditor': ['auditor'],
    'Budget Allocation': ['budget_allocation'],
    'Communication Manager': ['communication_manager'],
    'Communication Technician': ['communication_technician'],
    'Conduct Interviews': ['conduct_interviews'],
    'Customer Service': ['customer_service'],
    'Data Analyst': ['data_analyst'],
    'Data Gathering': ['data_gathering'],
    'Delivery Coordination': ['delivery_coordination'],
    'Department': ['department'],
    'Designer': ['designer'],
    'Developer': ['developer'],
    'Director': ['director'],
    'Edp': ['edp'],
    'Employee Onboarding': ['employee_onboarding'],
    'Employee Safety': ['employee_safety'],
    'Engineer': ['engineer'],
    'Engineering': ['engineering'],
    'Event Marketing': ['event_marketing'],
    'Export': ['export'],
    'External Auditor': ['external_auditor'],
    'Finance': ['finance'],
    'Financial Analyst': ['financial_analyst'],
    'Financial Statement Preparation': ['financial_statement_preparation'],
    'Forecasting': ['forecasting'],
    'Freight Shipping': ['freight_shipping'],
    'Hiring Manager': ['hiring_manager'],
    'Historical Analysis': ['historical_analysis'],
    'Human Resources': ['human_resources'],
    'Imports': ['imports'],
    'Internal Auditor': ['internal_auditor'],
    'Inventory Analysis': ['inventory_analysis'],
    'Inventory Manager': ['inventory_manager'],
    'Inventory Tracking': ['inventory_tracking'],
    'Invoice Preparation': ['invoice_preparation'],
    'Ip Protection': ['ip_protection'],
    'It': ['it'],
    'Knowledge Organization': ['knowledge_organization'],
    'Logistics': ['logistics'],
    'Manager': ['manager'],
    'Manufacturing': ['manufacturing'],
    'Marketing': ['marketing'],
    'Marketing Director': ['marketing_director'],
    'Materials Administration': ['materials_administration'],
    'Model Development': ['model_development'],
    'Model Generation': ['model_generation'],
    'Order Processing': ['order_processing'],
    'Production': ['production'],
    'Public Relations': ['public_relations'],
    'Purchasing': ['purchasing'],
    'Quality Assurance': ['quality_assurance'],
    'Record Maintenance': ['record_maintenance'],
    'Recruitment': ['recruitment'],
    'Reporting': ['reporting'],
    'Research': ['research'],
    'Researcher': ['researcher'],
    'Retail Replenishment': ['retail_replenishment'],
    'Risk Analysis': ['risk_analysis'],
    'Sales': ['sales'],
    'Sales Person': ['sales_person'],
    'Sales Role': ['sales_role'],
    'Senior Support Agent': ['senior_support_agent'],
    'Service': ['service'],
    'Software Support': ['software_support'],
    'Specialist': ['specialist'],
    'Stock Level Reporting': ['stock_level_reporting'],
    'Support Agent': ['support_agent'],
    'Tax Preparation': ['tax_preparation'],
    'Technical Role': ['technical_role'],
    'Technical Support': ['technical_support'],
    'Transport Operator': ['transport_operator'],
    'Trend Analysis': ['trend_analysis'],
    'Vehicle Maintenance': ['vehicle_maintenance'],
    'Warehousing': ['warehousing'],
    'technical_support': ['support_agent', 'senior_support_agent']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
