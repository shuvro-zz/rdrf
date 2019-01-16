class ReviewView(View):
    def get(self, request, token):
        workflow_request = WorkflowRequest.objects.get(token=token)
        
