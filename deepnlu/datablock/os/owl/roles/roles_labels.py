
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

class RolesLabels(object):

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
 'time': '2022-04-27 21:17:15.538356'}

    __data = {
    'accountant': ['Accountant'],
    'accounting': ['Accounting'],
    'accounts': ['Accounts'],
    'activity': ['Activity'],
    'administration': ['Administration'],
    'administrative_accounting': ['Administrative Accounting'],
    'agent': ['Agent'],
    'analyst': ['Analyst'],
    'architect': ['Architect'],
    'auditing': ['Auditing'],
    'auditor': ['Auditor'],
    'budget_allocation': ['Budget Allocation'],
    'communication_manager': ['Communication Manager'],
    'communication_technician': ['Communication Technician'],
    'conduct_interviews': ['Conduct Interviews'],
    'customer_service': ['Customer Service'],
    'data_analyst': ['Data Analyst'],
    'data_gathering': ['Data Gathering'],
    'delivery_coordination': ['Delivery Coordination'],
    'department': ['Department'],
    'designer': ['Designer'],
    'developer': ['Developer'],
    'director': ['Director'],
    'edp': ['Edp'],
    'employee_onboarding': ['Employee Onboarding'],
    'employee_safety': ['Employee Safety'],
    'engineer': ['Engineer'],
    'engineering': ['Engineering'],
    'event_marketing': ['Event Marketing'],
    'export': ['Export'],
    'external_auditor': ['External Auditor'],
    'finance': ['Finance'],
    'financial_analyst': ['Financial Analyst'],
    'financial_statement_preparation': ['Financial Statement Preparation'],
    'forecasting': ['Forecasting'],
    'freight_shipping': ['Freight Shipping'],
    'hiring_manager': ['Hiring Manager'],
    'historical_analysis': ['Historical Analysis'],
    'human_resources': ['Human Resources'],
    'imports': ['Imports'],
    'internal_auditor': ['Internal Auditor'],
    'inventory_analysis': ['Inventory Analysis'],
    'inventory_manager': ['Inventory Manager'],
    'inventory_tracking': ['Inventory Tracking'],
    'invoice_preparation': ['Invoice Preparation'],
    'ip_protection': ['Ip Protection'],
    'it': ['It'],
    'knowledge_organization': ['Knowledge Organization'],
    'logistics': ['Logistics'],
    'manager': ['Manager'],
    'manufacturing': ['Manufacturing'],
    'marketing': ['Marketing'],
    'marketing_director': ['Marketing Director'],
    'materials_administration': ['Materials Administration'],
    'model_development': ['Model Development'],
    'model_generation': ['Model Generation'],
    'order_processing': ['Order Processing'],
    'production': ['Production'],
    'public_relations': ['Public Relations'],
    'purchasing': ['Purchasing'],
    'quality_assurance': ['Quality Assurance'],
    'record_maintenance': ['Record Maintenance'],
    'recruitment': ['Recruitment'],
    'reporting': ['Reporting'],
    'research': ['Research'],
    'researcher': ['Researcher'],
    'retail_replenishment': ['Retail Replenishment'],
    'risk_analysis': ['Risk Analysis'],
    'sales': ['Sales'],
    'sales_person': ['Sales Person'],
    'sales_role': ['Sales Role'],
    'senior_support_agent': ['Senior Support Agent', 'technical_support'],
    'service': ['Service'],
    'software_support': ['Software Support'],
    'specialist': ['Specialist'],
    'stock_level_reporting': ['Stock Level Reporting'],
    'support_agent': ['technical_support', 'Support Agent'],
    'tax_preparation': ['Tax Preparation'],
    'technical_role': ['Technical Role'],
    'technical_support': ['Technical Support'],
    'transport_operator': ['Transport Operator'],
    'trend_analysis': ['Trend Analysis'],
    'vehicle_maintenance': ['Vehicle Maintenance'],
    'warehousing': ['Warehousing']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
