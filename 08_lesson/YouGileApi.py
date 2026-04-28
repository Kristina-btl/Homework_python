import requests

class YouGileApi:
    
    def __init__(self, url):
        self.url = url
        self.login = {'LOGIN'}
        self.password = {'PASSWORD'}
        self.company_id = {'COMPANY_ID'}
        self.key = self.get_token()
        self.headers = {
            'Authorization': f'Bearer {self.key}',
            'Content-Type': 'application/json'
        }


    def get_token(self):
        payload = {
            "login": self.login,
            "password": self.password,
            "companyId": self.company_id
        }
        resp = requests.post(self.url + 'auth/keys/get', json=payload)
        return resp.json()[0]['key']
    
    def get_project_list(self):
        resp = requests.get(self.url + 'projects', headers=self.headers)
        return resp

    def create_project(self, title, users):
        body = {"title": title, "users": users}
        resp = requests.post(self.url + 'projects',
                            headers=self.headers,
                            json=body)
        return resp

    def get_project_with_id(self, project_id):
        url = self.url + f'projects/{project_id}'
        resp = requests.get(url, headers=self.headers)
        return resp

    def edit_project(self, project_id, new_deleted, new_title):
        project = {"deleted": new_deleted, "title": new_title}
        url = self.url + f'projects/{project_id}'
        resp = requests.put(url, headers=self.headers, json=project)
        return resp