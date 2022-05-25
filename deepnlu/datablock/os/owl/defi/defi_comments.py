
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

class DefiComments(object):

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
 'config': {'classname': 'DefiComments',
            'filename': 'defi_comments',
            'queries': ['comments.sparql'],
            'transformers': ['comments']},
 'source': 'defi.owl',
 'time': '2022-04-27 21:15:55.034356'}

    __data = {
    'affects': ['The most popular application of x is y\nx affects y'],
    'asic_hardware': [   'In order to discourage centralisation due to the use '
                         'of specialised hardware (e.g. asics)',
                         'As has occurred in the bitcoin network',
                         'Ethereum chose a memory-hard computational problem. '
                         'if the problem requires memory as well as cpu',
                         'The ideal hardware is in fact the general computer. '
                         'this makes ethereum’s proof of work asic-resistant',
                         'Allowing a more decentralized distribution of '
                         'security than blockchains whose mining is dominated '
                         'by specialized hardware',
                         'Like bitcoin.\n'
                         '\n'
                         'https://ethdocs.org/en/latest/introduction/what-is-ethereum.html'],
    'asymmetric_key_cryptography': [   'No one can post a false transaction '
                                       'without ownership of the corresponding '
                                       'account due to the asymmetric key '
                                       'cryptography protecting the accounts. '
                                       'you have one “public” key representing '
                                       'an address to receive tokens and a '
                                       '“private” key used to unlock and spend '
                                       'tokens over which you have custody. \n'
                                       '\n'
                                       'this same type of cryptography is used '
                                       'to protect your credit card '
                                       'information and data when using the '
                                       'internet. a single account cannot '
                                       '“double spend” its tokens because the '
                                       'ledger keeps an audit of the balance '
                                       'at any given time and the faulty '
                                       'transaction would not clear.\n'
                                       '\n'
                                       'the ability to prevent a double spend '
                                       'without a central authority '
                                       'illustrates the primary advantage of '
                                       'using a blockchain to maintain the '
                                       'underlying ledger.'],
    'basis_cash': ['Decentralized stablecoin with an algorithmic central bank'],
    'blockchain': [   'Fundamentally',
                      'Blockchains are software protocols that allow multiple '
                      'parties to operate under shared assumptions and data '
                      'without trusting each other. these data can be anything',
                      'Such as location and destination information of items '
                      'in a supply chain or account balances of a token. '
                      'updates are packaged into “blocks” and are “chained” '
                      'together cryptographically to allow an audit of the '
                      'prior history – hence the name.'],
    'consensus_problem': [   'The ability to trust the result of a transaction '
                             'or block',
                             'Without trusting the parties involved in the '
                             'transaction',
                             'Or the party that verified it.'],
    'cryptocurrency_wallet': [   'The role of a wallet is to identify which '
                                 'addresses the user has keys to'],
    'dark_pool_stock_trading': [   'An even earlier example was the rise of '
                                   'dark pool stock trading. in 1979',
                                   'The u.s. securities and exchange '
                                   'commission (sec) instituted rule 19c3',
                                   'Which allowed stocks listed on one '
                                   'exchange',
                                   'Such as the new york stock exchange (nyse)',
                                   'To be traded off-exchange. many large '
                                   'institutions moved their trading large '
                                   'blocks to these dark pools',
                                   'Where they traded peer to peer with far '
                                   'lower costs than traditional '
                                   'exchange-based trading.'],
    'decentralized_application': [   'Ethereum and other smart contract '
                                     'platforms specifically gave rise to the '
                                     'decentralized application',
                                     'Or dapp. the backend components of these '
                                     'applications are built with '
                                     'interoperable',
                                     'Transparent smart contracts that '
                                     'continue to exist if the chain they live '
                                     'on exists. dapps allow peers to interact '
                                     'directly and remove the need for a '
                                     'company to act as a central clearing '
                                     'house for app interactions. it quickly '
                                     'became apparent that the first killer '
                                     'dapps would be financial ones.'],
    'decentralized_autonomous_organization': [   'A separate but related '
                                                 'concept is a decentralized '
                                                 'autonomous organization '
                                                 '(dao)',
                                                 'Which has its rules of '
                                                 'operation encoded in smart '
                                                 'contracts that determine who '
                                                 'can execute what behavior or '
                                                 'upgrade. it is common for a '
                                                 'dao to have some kind of '
                                                 'governance token',
                                                 'Which gives an owner some '
                                                 'percentage of the vote on '
                                                 'future outcomes. we will '
                                                 'explore governance in much '
                                                 'more detail later.'],
    'defi': [   'Defi is fundamentally a competitive marketplace of financial '
                'dapps that function as various financial “primitives” such as '
                'exchange',
                'Lend',
                'And tokenize. they benefit from the network effects of '
                'combining and recombining defi products and attracting '
                'increasingly more market share from the traditional financial '
                'ecosystem.'],
    'distributed_system': [   'A number of independent computers linked by a '
                              'network.'],
    'electronic_coin': ['A chain of digital signatures'],
    'empty_set_dollar': [   'Empty set dollar (esd) is an algorithmic '
                            'stablecoin built to be the reserve currency of '
                            'decentralized finance.'],
    'erc-721': [   'The non-fungible token standard',
                   'Which are unique and often used for collectibles or assets '
                   'such as peer-to-peer loans.'],
    'erc_20': [   'Erc-20 is the standard for fungible tokens and defines an '
                  'interface for tokens whose units are identical in utility '
                  'and functionality.\n'
                  '\n'
                  'it includes behavior such as transferring units and '
                  "approving operators for using a certain portion of a user's "
                  'balance.'],
    'fei': [   'Fei is a decentralized',
               'Scalable',
               'And defi-native stablecoin protocol'],
    'fiat_collaterialized': [   'By far the largest class of stablecoins are '
                                'fiat collateralized. these are backed by an '
                                'off-chain reserve of the target asset. '
                                'usually they are custodied by an external '
                                'entity or group of entities that undergo '
                                "routine audits to verify the collateral's "
                                'existence.'],
    'fractional_algorithm_stablecoin': [   'The frax protocol introduced the '
                                           'world to the concept of a '
                                           'cryptocurrency being partially '
                                           'backed by collateral and partially '
                                           'stabilized algorithmically.'],
    'gas_fee': [   'Ethereum charges a gas fee for every transaction – similar '
                   'to how driving a car takes a certain amount of gas',
                   'Which costs money. imagine ethereum as one giant computer '
                   'with many applications (i.e.',
                   'Smart contracts). if people want to use the computer',
                   'They must pay for each unit of computation. a simple '
                   'computation such as sending ether (eth) requires minimal '
                   'work to update a few account balances and thus has a '
                   'relatively small gas fee. a complex computation involving '
                   'minting tokens and checking various conditions across many '
                   'contracts requires more gas and thus will have a higher '
                   'fee.'],
    'liquidity': [   'Almost everything comes down to liquidity',
                     'But we consistently underestimate its importance. higher '
                     'liquidity results in tighter spreads and greater market '
                     'efficiency. lower liquidity exaggerates market movements '
                     'and amplifies sell-offs. it creates a flywheel on the '
                     'way up but a cliff on the way down.'],
    'nonce': [   'Typically',
                 'A nonce is a value that varies with time to verify that '
                 'specific values are not reused. a nonce can be a timestamp',
                 'A visit counter on a webpage or a special marker intended to '
                 'limit or prevent the unauthorized replay or reproduction of '
                 'a file.\n'
                 '\n'
                 'https://www.techtarget.com/searchsecurity/definition/nonce'],
    'oracle': [   'An oracle is any data source for reporting information '
                  'external to the blockchain.'],
    'proof_of_stake': [   'Validators in pos commit some capital (the stake) '
                          'to attest that the block is valid and make '
                          'themselves available by staking their '
                          'cryptocurrency. then',
                          'They may be selected to propose a block',
                          'Which needs to be attested by many of the other '
                          'validators. validators profit by both proposing a '
                          'block and attesting to the validity of others’ '
                          'proposed blocks. pos is much less computationally '
                          'intensive and requires vastly less energy.'],
    'proof_of_work': [   'The blockchains we focus on currently use the proof '
                         'of work (pow) consensus protocol',
                         'Which relies on a computationally and energy '
                         'intensive lottery to determine which block to add. '
                         'the participants agree that the longest chain of '
                         'blocks is the truth. \n'
                         '\n'
                         'if attackers want to make a longer chain that '
                         'contains malicious transactions',
                         'They must outpace all the computational work of the '
                         'entire rest of the network. in theory',
                         'They would need most of the network power (“hash '
                         'rate”) to accomplish this – hence',
                         'The famous 51 percent attack being the boundary of '
                         'pow security. \n'
                         '\n'
                         'luckily',
                         'It is extraordinarily difficult for any actor',
                         'Even an entire country',
                         'To amass this much network power on the most widely '
                         'used blockchains',
                         'Such as bitcoin or ethereum. even if most of the '
                         'network power can be temporarily acquired',
                         'The amount of block history that can be overwritten '
                         'is constrained by how long this majority can be '
                         'maintained.'],
    'proto_coinage': [   'Proto-Coinage presents enormous challenges to '
                         'potential collectors. it falls into the category of '
                         'antiquities or “archaeological artifacts” rather '
                         'than numismatic collectibles. few coin dealers are '
                         'willing to handle such material',
                         'Due to problems of authentication',
                         'Provenance and documentation'],
    'protocol_controlled_value': [   'Many of the latest iterations of '
                                     'stablecoins (fei',
                                     'Ohm',
                                     'Float',
                                     'Frax) leverage protocol controlled value '
                                     '(pcv). this is a concept in which the '
                                     'collateral backing a stablecoin is not '
                                     'redeemable by users but rather is owned '
                                     'by the protocol (which decides '
                                     'whether/how to invest it',
                                     'Can use it to restore the peg',
                                     'Etc.)'],
    'smart_contract': [   'A smart contract is code that can create and '
                          'transform arbitrary data or tokens on top of the '
                          'blockchain to which it belongs. \n'
                          '\n'
                          'powerfully',
                          'It allows the user to trustlessly encode rules for '
                          'any type of transaction and even create scarce '
                          'assets with specialized functionality. many of the '
                          'clauses of traditional business agreements could be '
                          'shifted to a smart contract',
                          'Which not only would enumerate but also '
                          'algorithmically enforce those clauses. \n'
                          '\n'
                          'smart contracts go beyond finance to include gaming',
                          'Data stewardship',
                          'And supply chain.'],
    'specie_currency': [   'The latin term specie[6] (meaning “kind',
                           'Or type”) is used to describe precious metals used '
                           'as money',
                           'The word “specie” refers not only to money or “in '
                           'kind',
                           '” but more specifically to a denomination of '
                           'currency',
                           'Most often to coin.'],
    'stablecoin': [   'Stablecoins are an important component of defi '
                      'infrastructure because they allow users to benefit from '
                      'the functionality of the applications without risking '
                      'unnecessary price volatility.'],
    'stake': ['Some form of share in the network'],
    'transaction': ['An individual user interaction with the ledger'],
    'unspent_transaction_output': [   'Bitcoin',
                                      'And many protocols based on it',
                                      'Store data about transactions and user '
                                      'balances in the form of unspent '
                                      'transaction outputs',
                                      'Which are a list of “unspent” bitcoin '
                                      'amounts that have been sent to a user',
                                      'But have not yet been sent from '
                                      'him/her. the sum of these outputs is '
                                      'the user’s total balance. on the '
                                      'blockchain',
                                      'They appear to be a collection of '
                                      'bitcoin amounts on different addresses',
                                      'And the role of a wallet is to identify '
                                      'which addresses the user has keys to. '
                                      'individual bitcoin are easy to track '
                                      'because they are signed from one person '
                                      'to another. a transaction is valid if '
                                      'one can prove ownership over the actual '
                                      'bitcoin s/he is trying to send.\n'
                                      '\n'
                                      'https://smithandcrown.com/glossary/unspent-transaction-outputs-utxo/'],
    'user_sovereignity': [   'No entity other than the user can determine how '
                             'to use funds'],
    'valid_transaction': [   'A transaction is valid if one can prove '
                             'ownership over the actual bitcoin s/he is trying '
                             'to send.']}

    def data(self) -> dict:
        return self.__data

    def find(self,
             term: str) -> str or None:
        if term in self.__data:
            return self.__data[term]
