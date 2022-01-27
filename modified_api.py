import json

from mouser.base import MouserBaseRequest




class MouserPartSearchRequest(MouserBaseRequest):
    """ Mouser Part Search Request """

    name = 'Part Search'
    operations = {
        'keyword': ('', ''),
        'keywordandmanufacturer': ('', ''),
        'partnumber': ('POST', '/search/partnumber'),
        'partnumberandmanufacturer': ('', ''),
        'manufacturerlist': ('', ''),
    }

    def get_clean_response(self):
        cleaned_data = {
            'Availability': '',
            
        }

        response = self.get_response()
        if self.get_response():
            try:
                parts = response['SearchResults'].get('Parts', [])
            except AttributeError:
                parts = None

            if parts:
                # Process first part
                part_data = parts[0]
                # Merge
                for key in cleaned_data:
                    cleaned_data[key] = part_data[key]

        return cleaned_data

    def print_clean_response(self):
        response_data = self.get_clean_response()
        return response_data

    def get_body(self, **kwargs):

        body = {}

        if self.operation == 'partnumber':
            part_number = kwargs.get('part_number', None)
            option = kwargs.get('option', 'None')

            if part_number:
                body = {
                    'SearchByPartRequest': {
                        'mouserPartNumber': part_number,
                        'partSearchOptions': option,
                    }
                }

        return body

    def part_search(self, part_number, option='None'):
        '''Mouser Part Number Search '''

        kwargs = {
            'part_number': part_number,
            'option': option,
        }

        self.body = self.get_body(**kwargs)

        if self.api_key:
            return self.run(self.body)
        else:
            return False
