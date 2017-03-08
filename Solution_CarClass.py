class Car(the_object):
	"""The class of the object car"""
	def status(self,car_type,car_name,car_model,car_property):
		"""attributes of the object"""
		car_type="honda"
		if car_name==" ":
			return "General"
		if car_model==" ":
			return "GM"
		car_property= car_name and car_model
		self.car_type = car_type
		self.car_model = car_model
		self.car_name = car_name
		self.car_speed = 0

		if name == "Porshe" or "Koenigsegg":
			self.num_of_doors = 2
		else:
			self.num_of_doors = 4
		if car_type == "trailer":
			self.num_of_wheels = 8
		else:
			self.num_of_wheels = 4


	def car_doors(self,num_of_doors):
		pass

    def drive_car(self, moving_man):
        return moving_man

    def drive_car(self, spd):
        if self.car_type == 'trailer':
            self.speed = spd * 11
        else:
            self.speed = 10 ** spd

        return self

    def car_wheels(self, num_of_wheels):
        return num_of_wheels


    def car_is_saloon(self):
        if self.car_type ==  'trailer':
            return False
        else:
return True


