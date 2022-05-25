
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

class DefiTypes(object):

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
 'config': {'classname': 'DefiTypes',
            'filename': 'defi_types',
            'queries': ['subclass.sparql'],
            'reverse': True,
            'transformers': ['types']},
 'source': 'defi.owl',
 'time': '2022-04-27 21:15:54.975855'}

    __data = {
    'acceptable': ['attribute'],
    'access': ['action'],
    'account': ['artefact'],
    'adaptable': ['attribute'],
    'advantage': ['attribute'],
    'algorithmic_stablecoin': ['stablecoin'],
    'anonymous_founding_team': ['founding_team'],
    'arbitrage': ['financial_primitive'],
    'asic_hardware': ['hardware'],
    'asset': ['artefact'],
    'asset_fund': ['fund'],
    'asset_transfer': ['transfer'],
    'asymmetric_key_cryptography': ['cryptography'],
    'attacker_node': ['node'],
    'autonomous_monitoring': ['monitor'],
    'autonomous_organization': ['organization'],
    'balance': ['state'],
    'bank': ['financial_institution'],
    'banking_platform': ['platform'],
    'banking_system': ['system'],
    'barter': ['exchange'],
    'base_rate': ['rate'],
    'basis_cash': ['algorithmic_stablecoin'],
    'bitcoin': ['blockchain'],
    'bitcoin_foundation': ['foundation'],
    'bitcoin_transaction': ['predefined_transaction'],
    'block_creation': ['creation'],
    'block_mine': ['mine'],
    'blockchain': ['software_protocol'],
    'blockchain_consensus': ['distributed_system_consensus'],
    'blockchain_contract': ['smart_contract'],
    'blockchain_council': ['council'],
    'bonding_curve': ['measurement'],
    'bonus': ['reward'],
    'bullion': ['precious_metal'],
    'canadian_dollar': ['dollar'],
    'capability': ['attribute'],
    'cash_economy': ['economy'],
    'censorship': ['action'],
    'censorship_resistant': ['attribute'],
    'central_bank': ['bank'],
    'centralized_control': ['financial_system'],
    'centralized_currency': ['currency'],
    'centralized_exchange': ['exchange_platform'],
    'centralized_system': ['system'],
    'coinbase': ['company'],
    'coindesk': ['company'],
    'coinshares': ['company'],
    'collateral_liquidation': ['liquidation'],
    'collateral_requirement': ['requirement'],
    'collateralization_ratio': ['ratio'],
    'collateralized_loan': ['loan'],
    'collective_trust_model': ['trust_model'],
    'company': ['organization'],
    'complete_redundancy': ['redundancy'],
    'complete_slashing': ['slashing_condition'],
    'computational_node': ['node'],
    'computing_cost': ['cost'],
    'computing_power': ['power'],
    'consensus': ['action'],
    'consensus_mechanism': ['mechanism'],
    'consensus_problem': ['problem'],
    'contract': ['artefact'],
    'contract_account': ['ethereum_account'],
    'contract_risk': ['risk'],
    'cost': ['attribute'],
    'council': ['organization'],
    'counterparty_risk': ['risk'],
    'creation': ['action'],
    'cryptoasset': ['digital_asset'],
    'cryptocollateral': ['collateral'],
    'cryptocollateralized_stablecoin': ['stablecoin'],
    'cryptocurrency': ['decentralized_currency'],
    'cryptocurrency_wallet': ['wallet'],
    'cryptographic_hashing_problem': ['hashing_problem'],
    'cryptographic_proof': ['proof'],
    'cryptographic_scarcity': ['scarcity'],
    'cryptography': ['security'],
    'currency': ['exchange_medium'],
    'currency_transfer': ['asset_transfer'],
    'dai_savings_rate': ['mechanism'],
    'dark_pool_stock_trading': ['stock_trade'],
    'data_source': ['artefact'],
    'debt': ['financial_mechanism'],
    'debt_ceiling': ['mechanism'],
    'decentralized_application': ['application'],
    'decentralized_autonomous_organization': ['autonomous_organization'],
    'decentralized_consensus': ['consensus_mechanism'],
    'decentralized_currency': ['currency'],
    'decentralized_exchange': ['exchange_platform'],
    'decentralized_organization': ['organization'],
    'decrease': ['action'],
    'defi': ['financial_system'],
    'defi_protocol': ['protocol'],
    'defi_version_1': ['defi'],
    'defi_version_2': ['defi'],
    'defi_version_3': ['defi'],
    'delegated_byzantine_fault_tolerance': ['consensus_mechanism'],
    'delegated_proof_of_stake': ['proof_of_stake'],
    'denial_of_service': ['malicious_action'],
    'deploy': ['action'],
    'deposit': ['action'],
    'desktop': ['computational_node'],
    'difference': ['attribute'],
    'digital_asset': ['asset'],
    'digital_asset_fund': ['asset_fund'],
    'digital_currency': ['currency'],
    'digital_currency_group': ['company'],
    'digital_signature': ['signature'],
    'digital_yuan': ['digital_currency'],
    'direct_incentive': ['incentive_mechanism'],
    'direct_reward': ['reward'],
    'disadvantage': ['attribute'],
    'dispute': ['state'],
    'distributed_consensus': ['consensus'],
    'distributed_immutable_ledger': ['distributed_ledger'],
    'distributed_ledger': ['ledger'],
    'distributed_mutable_ledger': ['distributed_ledger'],
    'distributed_node': ['computational_node'],
    'distributed_system': ['system'],
    'distributed_system_consensus': ['distributed_consensus'],
    'distributed_timestamp_server': ['distributed_node'],
    'document': ['artefact'],
    'dollar': ['centralized_currency'],
    'double_spend': ['malicious_transaction'],
    'durabilty': ['attribute'],
    'duration_risk': ['risk'],
    'early_investor': ['investor'],
    'efficiency': ['attribute'],
    'electronic_coin': ['digital_currency'],
    'electronic_payment': ['payment'],
    'electronic_payment_system': ['payment_system'],
    'empty_set_dollar': ['algorithmic_stablecoin'],
    'energy_cost': ['cost'],
    'equality': ['attribute'],
    'equality_of_opportunity': ['equality'],
    'erc-721': ['token_standard'],
    'erc_20': ['token_standard'],
    'escrow_mechanism': ['mechanism'],
    'esd_governance': ['governance'],
    'ethereum': ['cryptocurrency'],
    'ethereum_account': ['account'],
    'ethereum_virtual_machine': ['virtual_machine'],
    'euro': ['centralized_currency'],
    'excessive_volatility': ['volatile'],
    'exchange': ['action'],
    'exchange_medium': ['medium'],
    'exchange_platform': ['platform'],
    'exchange_rate': ['rate'],
    'explainability': ['attribute'],
    'external_actor': ['actor'],
    'externally_owned_account': ['ethereum_account'],
    'fault_tolerant': ['tolerant'],
    'fee': ['funding_mechanism'],
    'fei': ['stablecoin_protocol'],
    'fiat_collaterialized': ['stablecoin'],
    'fiat_currency': ['currency'],
    'financial_censorship': ['censorship'],
    'financial_infrastructure': ['infrastructure'],
    'financial_institution': ['organization'],
    'financial_mechanism': ['mechanism'],
    'financial_primitive': ['primitive'],
    'financial_system': ['system'],
    'fixed_exchange_rate': ['exchange_rate'],
    'fixed_interest_rate': ['interest_rate'],
    'flash_loan': ['loan'],
    'flexible': ['attribute'],
    'float_protocol': ['stablecoin_protocol'],
    'foreclosure_risk': ['risk'],
    'foundation': ['organization'],
    'founding_team': ['team'],
    'fractional_algorithm_stablecoin': ['algorithmic_stablecoin'],
    'fractional_stablecoin': ['stablecoin'],
    'function': ['measurement'],
    'fund': ['organization'],
    'funding_mechanism': ['mechanism'],
    'fungible_cryptoasset': ['cryptoasset'],
    'fungible_token': ['token'],
    'gas_fee': ['fee'],
    'global_access': ['access'],
    'gold': ['bullion'],
    'gold_standard': ['financial_system'],
    'governance': ['action'],
    'government_agency': ['public_agency'],
    'hardware': ['infrastructure'],
    'hash': ['artefact'],
    'hashing': ['action'],
    'hashing_problem': ['problem'],
    'identical': ['attribute'],
    'immutability': ['attribute'],
    'immutable': ['attribute'],
    'immutable_ledger': ['ledger'],
    'impermanent_loss': ['loss'],
    'incentive_fee': ['incentive_mechanism'],
    'incentive_mechanism': ['mechanism'],
    'increase': ['action'],
    'inefficient': ['attribute'],
    'inequality': ['attribute'],
    'inequality_of_opportunity': ['inequality'],
    'inflation': ['action'],
    'inflation_hedge': ['position'],
    'input_utxo': ['unspent_transaction_output'],
    'insured_deposit': ['deposit'],
    'intangible_value': ['value'],
    'interest_rate': ['rate'],
    'internet_of_bodies': ['internet'],
    'internet_of_money': ['internet'],
    'internet_of_things': ['internet'],
    'interoperability': ['capability'],
    'invalid_transaction': ['transaction'],
    'investor': ['actor'],
    'irreversible_transaction': ['transaction'],
    'jewelry': ['precious_metal'],
    'keeper': ['external_actor'],
    'keeper_auction': ['public_auction'],
    'keeper_reward': ['reward'],
    'lack_of_access': ['limited_access'],
    'lack_of_interoperability': ['capability'],
    'laptop': ['computational_node'],
    'latency': ['attribute'],
    'ledger': ['artefact'],
    'leverage': ['financial_primitive'],
    'limited_access': ['access'],
    'limited_supply': ['supply'],
    'linear_bonding_curve': ['bonding_curve'],
    'linear_function': ['function'],
    'liquidation': ['slashing_condition'],
    'liquidator': ['actor'],
    'liquidity': ['financial_primitive'],
    'loan': ['financial_mechanism'],
    'logistic_bonding_curve': ['bonding_curve'],
    'long_term': ['horizon'],
    'loss': ['state'],
    'mainstream': ['attribute'],
    'malicious_action': ['action'],
    'malicious_transaction': ['malicious_action'],
    'market_exchange': ['exchange'],
    'mediate': ['action'],
    'metal': ['exchange_medium'],
    'mine': ['action'],
    'miner': ['actor'],
    'miner_fee': ['fee'],
    'monitor': ['action'],
    'monotonical_decrease': ['decrease'],
    'monotonical_increase': ['increase'],
    'mutability': ['attribute'],
    'mutable': ['attribute'],
    'mutable_ledger': ['ledger'],
    'negative_incentive': ['incentive_mechanism'],
    'negative_staked_incentive': ['negative_incentive'],
    'network_protocol': ['protocol'],
    'nft': ['token'],
    'niche': ['attribute'],
    'non_fungible_cryptoasset': ['cryptoasset'],
    'non_physical_transfer': ['transfer'],
    'nonce': ['number'],
    'on_chain_governance': ['governance'],
    'online_payment': ['payment'],
    'opaque': ['explainability'],
    'oracle': ['data_source'],
    'output_utxo': ['unspent_transaction_output'],
    'overcollaterized_debt': ['debt'],
    'paper_currency': ['physical_currency'],
    'partial_redundancy': ['redundancy'],
    'partial_slashing': ['slashing_condition'],
    'payment': ['action'],
    'payment_system': ['platform'],
    'paypal': ['electronic_payment_system'],
    'peer_node': ['computational_node'],
    'peer_to_peer_distributed_timestamp_server': [   'distributed_timestamp_server'],
    'peer_to_peer_network': ['network'],
    'peer_to_peer_network_protocol': ['network_protocol'],
    'peer_to_peer_node': ['distributed_node'],
    'peer_to_peer_timestamp_server': ['timestamp_server'],
    'permanent_loss': ['loss'],
    'physical_currency': ['currency'],
    'physical_transfer': ['transfer'],
    'platform': ['organization'],
    'policy': ['artefact'],
    'portable': ['attribute'],
    'position': ['state'],
    'positive_incentive': ['incentive_mechanism'],
    'positive_staked_incentive': ['positive_incentive'],
    'power': ['attribute'],
    'precious_metal': ['store_of_wealth'],
    'predefined_transaction': ['transaction'],
    'predictable': ['attribute'],
    'private_agency': ['agency'],
    'pro_rata_basis': ['basis'],
    'problem': ['state'],
    'programmable_blockchain': ['blockchain'],
    'proof_of_activity': ['consensus_mechanism'],
    'proof_of_authority': ['consensus_mechanism'],
    'proof_of_capacity': ['consensus_mechanism'],
    'proof_of_elapsed_time': ['consensus_mechanism'],
    'proof_of_identity': ['consensus_mechanism'],
    'proof_of_stake': ['consensus_mechanism'],
    'proof_of_work': ['consensus_mechanism'],
    'proto_coinage': ['physical_currency'],
    'protocol_controlled_value': ['value'],
    'protocol_governance': ['governance'],
    'public_agency': ['agency'],
    'public_auction': ['auction'],
    'random_number': ['number'],
    'rate': ['attribute'],
    'ratio': ['measurement'],
    'redundancy': ['redundant'],
    'redundant': ['attribute'],
    'refinance': ['action'],
    'reliable': ['attribute'],
    'requirement': ['artefact'],
    'research_company': ['company'],
    'reserve_currency': ['currency'],
    'reversible_transaction': ['transaction'],
    'ring_money': ['proto_coinage'],
    'risk': ['financial_primitive'],
    'risk_factor': ['factor'],
    'robust': ['attribute'],
    'scalability': ['attribute'],
    'scarcity': ['attribute'],
    'sec': ['government_agency'],
    'security': ['attribute'],
    'semi_random_number': ['number'],
    'server': ['computational_node'],
    'server_rack': ['server'],
    'short_term': ['horizon'],
    'sigmoid_bonding_curve': ['bonding_curve'],
    'signature': ['artefact'],
    'silver': ['bullion'],
    'slashing_condition': ['mechanism'],
    'smart_contract': ['contract'],
    'smart_contract_risk': ['contract_risk'],
    'software_protocol': ['protocol'],
    'solution': ['state'],
    'sovereign_currency': ['currency'],
    'sovereignity': ['attribute'],
    'specie_currency': ['physical_currency'],
    'spend': ['action'],
    'stability_fee': ['mechanism'],
    'stable': ['attribute'],
    'stablecoin': ['artefact'],
    'stablecoin_protocol': ['defi_protocol'],
    'stake': ['state'],
    'staked_incentive': ['incentive_mechanism'],
    'staking_balance': ['balance'],
    'staking_requirement': ['requirement'],
    'staking_reward': ['reward'],
    'standard': ['artefact'],
    'stock_trade': ['trade'],
    'store_of_wealth': ['storage'],
    'super_linear_bonding_curve': ['bonding_curve'],
    'super_linear_function': ['function'],
    'supply_expansion': ['expansion'],
    'synthetic_token': ['token'],
    'system_consensus': ['consensus'],
    'tangible_value': ['value'],
    'third_party': ['actor'],
    'timestamp': ['artefact'],
    'timestamp_server': ['server'],
    'token_balance': ['balance'],
    'token_minting': ['action'],
    'token_standard': ['standard'],
    'token_swap': ['exchange'],
    'token_utilization': ['action'],
    'tolerant': ['attribute'],
    'trade': ['action'],
    'trading_platform': ['platform'],
    'transaction': ['action'],
    'transaction_fee': ['fee'],
    'transaction_number': ['number'],
    'transaction_output': ['output'],
    'transfer': ['action'],
    'transparency': ['explainability'],
    'treasury_governance': ['governance'],
    'trust': ['attribute'],
    'trust_model': ['model'],
    'trusted_actor': ['actor'],
    'trusted_node': ['node'],
    'trusted_third_party': ['third_party'],
    'trustworthy': ['attribute'],
    'uncollateralized_stablecoin': ['stablecoin'],
    'uncollaterialized_loan': ['loan'],
    'uniform': ['attribute'],
    'universal_access': ['access'],
    'unlimited_supply': ['supply'],
    'unspent_transaction_output': ['transaction_output'],
    'untrusted_actor': ['actor'],
    'us_dollar': ['dollar'],
    'user_issued_asset': ['asset'],
    'user_sovereignity': ['sovereignity'],
    'valid_transaction': ['transaction'],
    'value': ['action'],
    'value_standard': ['standard'],
    'value_transfer': ['transfer'],
    'variable_interest_rate': ['interest_rate'],
    'vault': ['artefact'],
    'vault_holder': ['actor'],
    'verify': ['action'],
    'virtual_machine': ['node'],
    'virtual_transfer': ['non_physical_transfer'],
    'volatile': ['state'],
    'voting_token': ['token'],
    'vulnerable': ['attribute'],
    'wallet': ['artefact'],
    'yuan': ['centralized_currency'],
    'zelle': ['electronic_payment_system'],
    'zero_downtime': ['attribute'],
    'zero_knowledge_proof': ['proof']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
