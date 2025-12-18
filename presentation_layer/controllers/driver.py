from repository_layer.repositories.driver import DriverRepository

class DriverController:

    def __init__(self):
        self.repository = DriverRepository()

    def create_driver(self, data):
        return self.repository.create(data)

    def list_drivers(self):
        return self.repository.list_all()
    
    def get_driver_by_id(self, driver_id):
        return self.repository.get_by_id(driver_id)
    
    def delete_driver_by_id(self, driver_id):
        return self.repository.delete_by_id(driver_id)
    
    def update_driver_by_id(self, driver_id, data):
        return self.repository.update_by_id(driver_id, data)