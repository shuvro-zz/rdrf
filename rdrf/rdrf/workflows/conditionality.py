from sexpdata import loads, Symbol

class FormData:
    def __init__(self, post_data):
        self.form_name = None
        self.cde_data = []
        

class ConditionalWorkflow:
    def __init__(self, workflow_spec):
        self.spec = self._parse_spec(workflow_spec)

    def _parse_spec(self, workflow_spec):
        return []

    def process_request(self, form_data):
        # this is run on valid data that has already been persisted
        form_spec = self._get_form_spec(form_data.form_name)
        next_function = self._get_condition_function(form_spec)
        next_form_name= next_function(form_data)

        return next_form_name

    def _get_form_spec(self, form_name):
        form_symbol = Symbol(form_name)
        for form_spec in self._form_specs(self.spec):
            if form_symbol == form_spec[0]:
                return form_spec

    def _get_condition_function(self, form_spec):
        cond_blk = form_spec[2]
        function = cond_blk[0]
        
        

            
        
        
