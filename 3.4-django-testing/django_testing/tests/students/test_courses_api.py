import pytest
from rest_framework.test import APIClient
from model_bakery import baker
from students.models import Course, Student


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)

    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)

    return factory


@pytest.mark.django_db
def test_course_retrieve(client, course_factory):
    the_course = course_factory(_quantity=1)

    response = client.get('http://127.0.0.1:8000/api/v1/courses/' + f'{the_course[0].id}/')

    assert response.status_code == 200
    data = response.json()
    assert data['id'] == the_course[0].id
    assert data['name'] == the_course[0].name


@pytest.mark.django_db
def test_get_list_courses(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('http://127.0.0.1:8000/api/v1/courses/')

    assert response.status_code == 200
    assert len(courses) == 10


@pytest.mark.django_db
def test_filter_course_id(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('http://127.0.0.1:8000/api/v1/courses/', {'id': courses[7].id})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['id'] == courses[7].id


@pytest.mark.django_db
def test_filter_course_name(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.get('http://127.0.0.1:8000/api/v1/courses/', {'name': courses[3].name})

    assert response.status_code == 200
    data = response.json()
    assert data[0]['name'] == courses[3].name


@pytest.mark.django_db
def test_create_course(client):
    data = {"name": "Информатика"}

    response = client.post('http://127.0.0.1:8000/api/v1/courses/', data)

    assert response.status_code == 201
    assert Course.objects.count() == 1
    course = Course.objects.first()
    assert course.name == 'Информатика'


@pytest.mark.django_db
def test_update_course(client, course_factory):
    courses = course_factory(_quantity=10)
    data = {"name": "Информатика"}

    response = client.patch('http://127.0.0.1:8000/api/v1/courses/' + f'{courses[5].id}/', data)

    assert response.status_code == 200
    resp_data = response.json()
    assert resp_data['name'] == 'Информатика'


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=10)

    response = client.delete('http://127.0.0.1:8000/api/v1/courses/' + f'{courses[3].id}/')

    assert response.status_code == 204
    assert Course.objects.count() == 9
