
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

class DefiLabelsRev(object):

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
 'config': {'classname': 'DefiLabels',
            'filename': 'defi_labels',
            'queries': ['labels.sparql'],
            'reverse': True,
            'transformers': ['labels']},
 'source': 'defi.owl',
 'time': '2022-04-27 21:15:55.016355'}

    __data = {
    'Acceptable': ['acceptable'],
    'Access': ['access'],
    'Action': ['action'],
    'Actor': ['actor'],
    'Agency': ['agency'],
    'Algorithmic Stablecoin': ['algorithmic_stablecoin'],
    'Anonymous Founding Team': ['anonymous_founding_team'],
    'Application': ['application'],
    'Arbitrage': ['arbitrage'],
    'Artefact': ['artefact'],
    'Asic Hardware': ['asic_hardware'],
    'Asset': ['asset'],
    'Asset Transfer': ['asset_transfer'],
    'Asymmetric Key Cryptography': ['asymmetric_key_cryptography'],
    'Attribute': ['attribute'],
    'Autonomous Monitoring': ['autonomous_monitoring'],
    'Autonomous Organization': ['autonomous_organization'],
    'Bank': ['bank'],
    'Banking Platform': ['banking_platform'],
    'Banking System': ['banking_system'],
    'Barter': ['barter'],
    'Base Rate': ['base_rate'],
    'Basis Cash': ['basis_cash'],
    'Bitcoin': ['bitcoin'],
    'Bitcoin Foundation': ['bitcoin_foundation'],
    'Block Mine': ['block_mine'],
    'Blockchain': ['blockchain'],
    'Blockchain Contract': ['blockchain_contract'],
    'Bonding Curve': ['bonding_curve'],
    'Bullion': ['bullion'],
    'Canadian Dollar': ['canadian_dollar'],
    'Capability': ['capability'],
    'Cash Economy': ['cash_economy'],
    'Censorship': ['censorship'],
    'Central Bank': ['central_bank'],
    'Centralized Exchange': ['centralized_exchange'],
    'Centralized Finance': ['centralized_control'],
    'Coinbase': ['coinbase'],
    'Coindesk': ['coindesk'],
    'Coinshares': ['coinshares'],
    'Collateral': ['collateral'],
    'Company': ['company'],
    'Consensus': ['consensus'],
    'Consensus Mechanism': ['consensus_mechanism'],
    'Contract': ['contract'],
    'Council': ['council'],
    'Cryptocollateral': ['cryptocollateral'],
    'Cryptocollateralized Stablecoin': ['cryptocollateralized_stablecoin'],
    'Cryptocurrency': ['cryptocurrency'],
    'Cryptographic Scarcity': ['cryptographic_scarcity'],
    'Cryptography': ['cryptography'],
    'Currency': ['currency'],
    'Currency Transfer': ['currency_transfer'],
    'Dai Savings Rate': ['dai_savings_rate'],
    'Dark Pool Stock Trading': ['dark_pool_stock_trading'],
    'Data Source': ['data_source'],
    'Decentralized Application': ['decentralized_application'],
    'Decentralized Autonomous Organization': [   'decentralized_autonomous_organization'],
    'Decentralized Currency': ['decentralized_currency'],
    'Decentralized Exchange': ['decentralized_exchange'],
    'Decentralized Organization': ['decentralized_organization'],
    'Defi': ['defi'],
    'Defi Protocol': ['defi_protocol'],
    'Defi Version 1': ['defi_version_1'],
    'Defi Version 2': ['defi_version_2'],
    'Defi Version 3': ['defi_version_3'],
    'Deposit': ['deposit'],
    'Digital Asset': ['digital_asset'],
    'Digital Currency': ['digital_currency'],
    'Digital Currency Group': ['digital_currency_group'],
    'Document': ['document'],
    'Dollar': ['dollar'],
    'Durable': ['durabilty'],
    'Economy': ['economy'],
    'Empty Set Dollar': ['empty_set_dollar'],
    'Equality': ['equality'],
    'Equality of Opportunity': ['equality_of_opportunity'],
    'Erc-20': ['erc_20'],
    'Erc-721': ['erc-721'],
    'Esd Governance': ['esd_governance'],
    'Ethereum': ['ethereum'],
    'Euro': ['euro'],
    'Excessive Volatility': ['excessive_volatility'],
    'Exchange': ['exchange'],
    'Exchange Medium': ['exchange_medium'],
    'Exchange Rate': ['exchange_rate'],
    'Expansion': ['expansion'],
    'Explainability': ['explainability'],
    'Fee': ['fee'],
    'Fiat Collaterialized': ['fiat_collaterialized'],
    'Fiat Currency': ['fiat_currency'],
    'Finance': ['finance'],
    'Financial Censorship': ['financial_censorship'],
    'Financial Infrastructure': ['financial_infrastructure'],
    'Financial Primitive': ['financial_primitive'],
    'Financial System': ['financial_system'],
    'Fixed Exchange Rate': ['fixed_exchange_rate'],
    'Float Protocol': ['float_protocol'],
    'Foundation': ['foundation'],
    'Founding Team': ['founding_team'],
    'Fractional Algorithm Stablecoin': ['fractional_algorithm_stablecoin'],
    'Fractional Stablecoin': ['fractional_stablecoin'],
    'Funding Mechanism': ['funding_mechanism'],
    'Fungible Token': ['fungible_token'],
    'Gas Fee': ['gas_fee'],
    'Global Access': ['global_access'],
    'Gold': ['gold'],
    'Gold Standard': ['gold_standard'],
    'Governance': ['governance'],
    'Government Agency': ['government_agency'],
    'Immutable Ledger': ['immutable_ledger'],
    'Incentive Mechanism': ['incentive_mechanism'],
    'Inefficient': ['inefficient'],
    'Inequality': ['inequality'],
    'Inequality of Opportunity': ['inequality_of_opportunity'],
    'Inflation': ['inflation'],
    'Inflation Hedge': ['inflation_hedge'],
    'Infrastructure': ['infrastructure'],
    'Insurance': ['insurance'],
    'Insured Deposit': ['insured_deposit'],
    'Intangible Value': ['intangible_value'],
    'Internet': ['internet'],
    'Internet of Bodies': ['internet_of_bodies'],
    'Internet of Money': ['internet_of_money'],
    'Internet of Things': ['internet_of_things'],
    'Interoperability': ['interoperability'],
    'Jewelry': ['jewelry'],
    'Lack of Access': ['lack_of_access'],
    'Lack of Interoperability': ['lack_of_interoperability'],
    'Ledger': ['ledger'],
    'Leverage': ['leverage'],
    'Limited Access': ['limited_access'],
    'Limited Supply': ['limited_supply'],
    'Linear Bonding Curve': ['linear_bonding_curve'],
    'Liquidity': ['liquidity'],
    'Long Term': ['long_term'],
    'Malicious Action': ['malicious_action'],
    'Malicious Transaction': ['malicious_transaction'],
    'Market Exchange': ['market_exchange'],
    'Mechanism': ['mechanism'],
    'Medium': ['medium'],
    'Metal': ['metal'],
    'Mine': ['mine'],
    'Monitor': ['monitor'],
    'Mutable Ledger': ['mutable_ledger'],
    'Nft': ['nft'],
    'Non Physical Transfer': ['non_physical_transfer'],
    'On Chain Governance': ['on_chain_governance'],
    'Opaque': ['opaque'],
    'Opportunity': ['opportunity'],
    'Oracle': ['oracle'],
    'Organization': ['organization'],
    'Paper Currency': ['paper_currency'],
    'Payment System': ['payment_system'],
    'Paypal': ['paypal'],
    'Physical Transfer': ['physical_transfer'],
    'Platform': ['platform'],
    'Policy': ['policy'],
    'Portable': ['portable'],
    'Position': ['position'],
    'Precious Metal': ['precious_metal'],
    'Primitive': ['primitive'],
    'Privacy': ['privacy'],
    'Private Agency': ['private_agency'],
    'Proof of Stake': ['proof_of_stake'],
    'Proof of Work': ['proof_of_work'],
    'Proto Coinage': ['proto_coinage'],
    'Protocol': ['protocol'],
    'Protocol Controlled Value': ['protocol_controlled_value'],
    'Protocol Governance': ['protocol_governance'],
    'Public Agency': ['public_agency'],
    'Rate': ['rate'],
    'Research Company': ['research_company'],
    'Reserve Currency': ['reserve_currency'],
    'Ring Money': ['ring_money'],
    'Risk': ['risk'],
    'Risk Factor': ['risk_factor'],
    'Scalability': ['scalability'],
    'Scarcity': ['scarcity'],
    'Sec': ['sec'],
    'Security': ['security'],
    'Short Term': ['short_term'],
    'Silver': ['silver'],
    'Smart Contract': ['smart_contract'],
    'Software Protocol': ['software_protocol'],
    'Sovereign Currency': ['sovereign_currency'],
    'Sovereignity': ['sovereignity'],
    'Specie Currency': ['specie_currency'],
    'Stable': ['stable'],
    'Stablecoin': ['stablecoin'],
    'Stablecoin Protocol': ['stablecoin_protocol'],
    'Standard': ['standard'],
    'State': ['state'],
    'Stock Trade': ['stock_trade'],
    'Storage': ['storage'],
    'Store of Wealth': ['store_of_wealth'],
    'Supply': ['supply'],
    'Supply Expansion': ['supply_expansion'],
    'System': ['system'],
    'Tangible Value': ['tangible_value'],
    'Team': ['team'],
    'Token': ['token'],
    'Token Standard': ['token_standard'],
    'Token Swap': ['token_swap'],
    'Trade': ['trade'],
    'Trading Platform': ['trading_platform'],
    'Transaction': ['transaction'],
    'Transfer': ['transfer'],
    'Treasury Governance': ['treasury_governance'],
    'Uncollateralized Stablecoin': ['uncollateralized_stablecoin'],
    'Uniform': ['uniform'],
    'Unlimited Access': ['universal_access'],
    'Unlimited Supply': ['unlimited_supply'],
    'Us Dollar': ['us_dollar'],
    'User Issued Asset': ['user_issued_asset'],
    'User Sovereignity': ['user_sovereignity'],
    'Value': ['value'],
    'Value Standard': ['value_standard'],
    'Value Transfer': ['value_transfer'],
    'Virtual Transfer': ['virtual_transfer'],
    'Volatile': ['volatile'],
    'Zelle': ['zelle']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]