# -*- coding: utf-8 -*-

class OperatorCheck:

    def __init__(self, operator_type, element, comparison_value=None):
        self.operator_type = operator_type
        self.element = element
        self.comparison_value = comparison_value

        self.method_mapping = {
            'equal to': 'equal_to',
            'larger than': 'larger_than',
            'less than': 'less_than',
            'exists': 'exists'
        }

    def check(self):

        # return false if there should be an element and it does not exist
        if not self.element and self.operator_type != 'not existing':
            return False

        return getattr(self, self.method_mapping[self.operator_type])()

    def exists(self):
        if self.element:
            return True
        else:
            return False

    def equal_to(self):
        print self.element.text
        if self.element.text == self.comparison_value:
            return True
        else:
            return False

    def larger_than(self):
        if float(self.element.text) > float(self.comparison_value):
            return True
        else:
            return False

    def less_than(self):
        if float(self.element.text) < float(self.comparison_value):
            return True
        else:
            return False
