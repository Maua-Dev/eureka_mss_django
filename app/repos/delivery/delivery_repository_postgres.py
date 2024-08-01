from app.models import Project, User, Task, Delivery
from app.repos.delivery.delivery_repository_interface import IDeliveryRepository


class DeliveryRepositoryPostgres(IDeliveryRepository):


    def __init__(self):
        pass

    def create_delivery(self, delivery: dict, user: dict, task: dict, project: dict):
        try:
            advisors = set([User(**user) for user in project["advisors"]])
            responsibles = set([User(**user) for user in project["responsibles"]])
            students = set([User(**user) for user in project["students"]])
            
            project.pop("advisors")
            project.pop("responsibles")
            project.pop("students")
            
            project_model = Project(**project)
            
            project_model.advisors.set(advisors)
            project_model.responsibles.set(responsibles)
            project_model.students.set(students)
            
            result = Delivery.objects.create(
                task=Task(**task),
                project=Project(**project),
                user=User(**user),
                content=delivery['content']
            )
            result.save()

            delivery_dict = result.__dict__

            return delivery_dict
        
        except Exception as e:
            raise e
        


    def get_delivery(self, delivery_id):
        try:
            delivery_set = Delivery.objects.get(delivery_id=delivery_id)
        except:
            return None

        if not delivery_set:
            return None

        delivery_dict = delivery_set.to_dict()

        return delivery_dict

    def get_deliveries(self, project_id):
        try:
            deliveries_set = Delivery.objects.filter(project_id=project_id)
        except:
            return []

        if not deliveries_set:
            return []

        deliveries = [delivery.to_dict() for delivery in deliveries_set]

        return deliveries

