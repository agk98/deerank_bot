import requests

class joke:
    def __init__(self):
        self.url=["https://dad-jokes.p.rapidapi.com/random/jokes", "https://icanhazdadjoke.com/"]
        self.headers=[
                        {
                            'x-rapidapi-host': "dad-jokes.p.rapidapi.com",
                            'x-rapidapi-key': "ab3c4f173amsh0191d362a3bcf2ep105d5ejsnef7899ff987c"
                        }, 
                        {
                            "Accept":"application/json"
                        }
                    ]

    def get_joke(self):
        response=requests.request("GET", url=self.url[0], headers=self.headers[0])
        if response.status_code==200:
            response=response.json()
            return(response["setup"]+"\n"+response['punchline'])
        else:
            response=requests.request("GET",url=self.url[1],headers=self.headers[1])
            if response.status_code==200:
                response=response.json()
                return(response["joke"])
            else:
                return 0

    
def request_joke():
    joke_obj=joke()
    return joke_obj.get_joke()