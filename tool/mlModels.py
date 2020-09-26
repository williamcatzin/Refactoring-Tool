import urllib.request
import ast
import json

class MLmodels:
    """ url and api_key are assigned to strings that are incased in parenthesis.
        I did this to shorten the number of characters in each line by breaking
        the string into a multiline string.
    """
    def __init__(self, message):
        self.__msg = message

    # private function
    def __encodeMessage(self):
        """ encodeMessage encodes the commit message into JSON formatted string
            and returns a byte object containing the encoded message.
        """
        data = {
            "Inputs": {
                "input1": {
                    "ColumnNames": ["Commit message"],
                    "Values": [[self.__msg]]
                },
            },
            "GlobalParameters": {}
        }
        return str.encode(json.dumps(data))

    # private function
    def __classificationResult(self, url, body, header, classifier):
        """ returns the result of running the machine learning model based
            on the classifier.
        """
        req = urllib.request.Request(url, body, header)
        response = urllib.request.urlopen(req)
        result = response.read()
        decoded_data = result.decode()
        info = ast.literal_eval(decoded_data)

        if classifier == "binary":
            return info.get('Results').get('output1').get('value').get('Values')[0][0]
        elif classifier == "type":
            return info.get("Results").get("output1").get("value").get("Values")[0][6]
        else:
            return info.get("Results").get("output1").get("value").get("Values")[0][3]


    def sarClassification(self):
        """ binary classification model classifies a commit message as
            self-admitted refactoring(SAR) or non-self-admitted refactoring(nonSAR).
        """
        body = self.__encodeMessage()
        url = ('https://ussouthcentral.services.azureml.net/workspaces/'
               '41654fb2238f449daf8dc7954f22ee9b/services/628f9a5ba374448cac4e9fe95e3fd603/'
               'execute?api-version=2.0&details=true')

        api_key = ('CS9V8O3u0neqll8VdENSv+cdSNxw9TsRMukb1kJXrrwIHHDZac6YlRgVz/'
                   '6jIlv4/wX9gaCdOK/Z6aJmb26oTw==')

        headers = {'Content-Type': 'application/json',
                   'Authorization': ('Bearer ' + api_key)}

        sar = self.__classificationResult(url, body, headers, "binary")

        if sar == "SAR":
            typeSAR = self.__typeClassification()
            intention = self.__intentionClassification()
            return [sar, typeSAR, intention]
        else:
            return [sar]


    #private function
    def __typeClassification(self):
        """ type classification model determines the type of refactoring based on
            the information of a commit message.
        """
        body = self.__encodeMessage()
        url = ('https://ussouthcentral.services.azureml.net/workspaces/'
               '41654fb2238f449daf8dc7954f22ee9b/services/a666752915904df79ec245f221dd07a3/'
               'execute?api-version=2.0&details=true')

        api_key = ('itNiZ0CAp/JPbD2pl7hH2dvejy4KMhEmtGyQ9WE5RLrD71fS1Ajtme3RW7xlhS3mjC873'
                   'RCSPsBkOU/Tdevv8w==')

        headers = {'Content-Type': 'application/json',
                   'Authorization': ('Bearer ' + api_key)}

        return self.__classificationResult(url, body, headers, "type")

    #private function
    def __intentionClassification(self):
        """ intention classification model determines the intention of refactoring based on
            the information of a commit message.
        """
        body = self.__encodeMessage()
        url = ('https://ussouthcentral.services.azureml.net/workspaces/'
               '41654fb2238f449daf8dc7954f22ee9b/services/302e5e0d464b4091a5319f145a2c51a5/'
               'execute?api-version=2.0&details=true')

        api_key = ('QRTkbxApvlKxcjxkqAN1IfRYF1ZB3T2F82lXzqSSjG4mqpn+kIj1MvTUVGLOqGO+'
                   'pnToQ+BepklBncjozOpjXw==')

        headers = {'Content-Type': 'application/json',
                   'Authorization': ('Bearer ' + api_key)}

        return self.__classificationResult(url, body, headers, "intention")
