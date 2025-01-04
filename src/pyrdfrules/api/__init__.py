"""
API module contains the classes that are used to interact with RDFRules, mainly using the HTTP interface.

Each API domain contains a base class and concrete implementations (e.g. `CacheApi` and `CacheHttpApi`).
This allows for mocking and testing, but also future changes in the API without changing the client code.
"""