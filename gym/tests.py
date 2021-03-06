from django.test import Client, TestCase
from .models import GymUser, GymNow, GymWaiting, Record
from django.utils import timezone, dateformat
from django.urls import reverse

class GymUserModelTest(TestCase):
	#This is test add the user to GymUser
	def setUp(self):
		self.user1 = GymUser.objects.create(id='12133174', name='Yuen Yiu Man', userType='S')
		self.user2 = GymUser.objects.create(id='654321', name='Oliver Au', userType='E')

	def test_User(self):
		self.assertEqual(self.user1.name,'Yuen Yiu Man')
		self.assertEqual(self.user2.userType,'E')
		#none user in GymUser
		self.assertFalse(GymUser.objects.filter(id='12345678').exists())


class GymNowModelTest(TestCase):
	#testing gymNow model
	def setUp(self):
		GymUser.objects.create(id='13345421', name='Peter Wong', userType='S')

	def test_addUser_to_gymRoom(self):
		user = GymUser.objects.get(pk='13345421')
		time = timezone.now()
		GymNow.objects.create(userId=user,entryTime=time)
		filterUser = GymNow.objects.filter(userId=user)[0]
		self.assertEqual(filterUser.userId, user)
		self.assertEqual(filterUser.entryTime, time)

class GymWaitingModelTest(TestCase):
	#testing gymWaiting model
	def setUp(self):
		GymUser.objects.create(id='13345421', name='Peter Wong', userType='S')

	def test_addUser_to_waitingList(self):
		user = GymUser.objects.get(pk='13345421')
		time = timezone.now()
		GymWaiting.objects.create(userId=user,waitTime=time)
		filterUser = GymWaiting.objects.filter(userId=user)[0]
		self.assertEqual(filterUser.userId, user)
		self.assertEqual(filterUser.waitTime, time)


class RecordModelTest(TestCase):
	#The record is saving the data of GymNow user leave
	#the data type will be userId(fk), entryTime and waitTime
	#This test is simulate a user leave the gym room and save the record
	def setUp(self):
		#create GymUser
		self.user = GymUser.objects.create(id='644987', name='Terri Wong', userType='E')
		#create GymNow user
		self.enTime = timezone.now()
		#create the gym user using the gym
		GymNow.objects.create(userId=self.user,entryTime=self.enTime)

	def test_leaveGymNow(self):
		user = GymNow.objects.all()
		# save the leave time
		leavetime = dateformat.format(timezone.now(), 'Y-m-d H:i:s')
		# the model is auto add the leave time
		Record.objects.create(userId=user[0].userId, entryTime=user[0].entryTime)
		result = Record.objects.filter(userId='644987')[0]
		#check the leave time
		self.assertEqual(dateformat.format(result.leaveTime, 'Y-m-d H:i:s'),leavetime)
		self.assertEqual(result.entryTime, self.enTime)

