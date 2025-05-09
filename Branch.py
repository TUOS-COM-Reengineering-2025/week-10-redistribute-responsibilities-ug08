from Staff import Staff


class Branch:

    def __init__(self, location, opening_time="9:00", staff=[]):
        self._location = location
        self._opening_time = opening_time
        self._staff = staff

    def get_location(self):
        return self._location

    def set_location(self, location):
        self._location = location

    def get_staff(self):
        return self._staff

    def close(self, transfer_branch):
        for staff in self._staff:
            self.transfer_staff_member(staff, transfer_branch)

    def transfer_staff_member(self, staff, transfer_branch):
        self._staff.remove(staff)
        transfer_branch.append(staff)