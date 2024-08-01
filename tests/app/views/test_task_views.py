from django.test import TestCase, RequestFactory

from app.views.task_views import TaskViews


class TestTaskView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()

    def test_get_all_tasks_view(self):
        request = self.factory.get('/get_all_tasks')

        response = TaskViews.get_all_tasks(request)

        assert response.status_code == 200
