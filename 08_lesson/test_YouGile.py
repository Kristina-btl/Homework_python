from YouGileApi import YouGileApi


api = YouGileApi("https://ru.yougile.com/api-v2/")
users = {'USER_ID': "admin"}


def test_create_project_positive():
    resp = api.create_project("New_Project_Test", users)

    assert resp.status_code == 201

    project_data = resp.json()
    assert 'id' in project_data

    projects_resp = api.get_project_list()
    assert projects_resp.status_code == 200

    api.edit_project(project_data['id'], True, "Deleted_Project")


def test_create_project_negative():
    resp = api.create_project("", users)

    assert resp.status_code == 400
    assert resp.json()["message"][0] == "title should not be empty"


def test_get_project_with_id_positive():
    create_resp = api.create_project("Get_Project_Test", users)

    project_id = create_resp.json()['id']
    resp = api.get_project_with_id(project_id)
    assert resp.status_code == 200

    project_data = resp.json()
    assert project_data['title'] == "Get_Project_Test"

    api.edit_project(project_id, True, "Deleted_Project")


def test_get_project_with_id_negative():
    resp = api.get_project_with_id("123")

    assert resp.status_code == 404
    assert resp.json()["message"] == "Проект не найден"


def test_edit_project_positive():
    create_resp = api.create_project("Original_Title", users)
    project_id = create_resp.json()['id']
    resp = api.edit_project(project_id, False, "Updated_Title")

    assert resp.status_code == 200

    resp_get = api.get_project_with_id(project_id)
    project_data = resp_get.json()
    assert project_data['title'] == "Updated_Title"

    api.edit_project(project_id, True, "Deleted_Project")


def test_edit_project_negative():
    create_resp = api.create_project("Original_Title", users)
    project_id = create_resp.json()['id']
    resp = api.edit_project(project_id, False, "")

    assert resp.status_code == 400
    assert resp.json()["message"][0] == "title should not be empty"
