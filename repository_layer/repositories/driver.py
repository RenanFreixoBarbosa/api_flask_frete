from database import db
from repository_layer.models.driver import Driver

class DriverRepository:

    def create(self, data):
        driver = Driver(**data)
        db.session.add(driver)
        db.session.commit()
        return driver

    def list_all(self):
        return Driver.query.all()

    def get_by_id(self, driver_id):
        return Driver.query.get(driver_id)

    def delete_by_id(self, driver_id):
        driver = Driver.query.get(driver_id)
        if driver:
            db.session.delete(driver)
            db.session.commit()
            return driver
        return "driver não encontrado"
    
    def update_by_id(self, driver_id, data):
        driver = Driver.query.get(driver_id)
        if driver:
            for key, value in data.items():
                setattr(driver, key, value)
            db.session.commit()
            return driver
        return "driver não encontrado"