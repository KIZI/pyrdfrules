import json
import logging
import unittest

from pyrdfrules.common.result.result import Result



class TestRuleParsing(unittest.TestCase):

    def test_rule_parsing(self):
        """
        Tests parsing of a rule.
        """
        
        data = '[{"body": [{"graphs": ["<dbpedia>"], "object": {"type": "variable", "value": "?b"}, "predicate": {"localName": "subsequentWork", "nameSpace": "http://dbpedia.org/ontology/", "prefix": "dbo"}, "subject": {"type": "variable", "value": "?c"}}, {"graphs": ["<dbpedia>"], "object": {"type": "variable", "value": "?a"}, "predicate": {"localName": "artist", "nameSpace": "http://dbpedia.org/ontology/", "prefix": "dbo"}, "subject": {"type": "variable", "value": "?c"}}], "head": {"graphs": ["<yago>"], "object": {"type": "variable", "value": "?b"}, "predicate": "<created>", "subject": {"type": "variable", "value": "?a"}}, "measures": [{"name": "Support", "value": 845}, {"name": "HeadSupport", "value": 5803}, {"name": "PcaBodySize", "value": 871}, {"name": "PcaConfidence", "value": 0.9701492537313433}, {"name": "HeadSize", "value": 5803}, {"name": "HeadCoverage", "value": 0.14561433741168361}]}]'
        
        rules = json.loads(data)
        
        print(rules)
        
        result = Result(rules)
        
        for rule in result.get_ruleset().get_rules():
            self.assertEqual(rule.as_text(), '(?c <subsequentWork> ?b) ^ (?c <artist> ?a) -> (?a <<created>> ?b)')
            print(rule.as_text())


if __name__ == '__main__':
    unittest.main()
