from config import price
from peewee import *
import datetime
 


db = SqliteDatabase('db.sqlite3')

class BaseModel(Model):
	class Meta:
		database = db

class Routing(BaseModel):
	btn 	 	= TextField(unique = True) 
	action		= TextField(null = True)

	@staticmethod
	def clear_table():
		Routing.create_table(fail_silently = True)
		q = Routing.delete()
		q.execute()


class Btn():
	def __init__(self):
		self.free_signals 	= "Сигналы FREE"
		self.vip_signals	= "Сигналы VIP"
		self.my_wallet		= "Мой кошелёк"
		self.my_balance		= "Мой баланс"
		self.three_days 	= "3 дня за {} Btc".format(price['3_days'])
		self.one_week 		= "1 неделя за {} Btc".format(price['1_week'])
		self.two_weeks 		= "2 недели за {} Btc".format(price['2_weeks'])
		self.one_month 		= "1 месяц за {} Btc".format(price['1_month'])
		self.back 			= "Назад"

		self.set_routing()

	def set_routing(self):
		btns = self.__dict__
		Routing.clear_table()
		for b in btns:
			r = Routing.create(btn = btns[b], action = b)



#	BUTTONS



# CALLBACKS
# free_signals_clbck 	= "free_signals"
# vip_signals_clbck	= "vip_signals"
# my_balance_clbck	= "my_balance"
# my_wallet_clbck		= "my_wallet"
# one_day_clbck		= "one_day"
# three_days_clbck	= "three_days"	
# one_week_clbck		= "one_week"
# one_month_clbck		= "one_month"


class Msg():
	def __init__(self):
		self.start = '''
		Доброго времени суток! Вы переходите на VIP канал сигналов и рекомендаций c криптовалютной биржи Bittrex. Канал ведут биржевые аналитики группы компаний SG Group, анализируя массу информации от источников со всего мира,  указывают на какие валюты стоит обратить внимание для Игры "в долгую", дают информацию о возможных пампах.. помогают наращивать количество Биткойна в вашем портфеле! Выберите дальнейшее действия:  
		'''

		self.my_balance = '''
		Ваш баланс составляет {} BTC.
		Выберите нужный период. Для пополнения баланса выберите **Мой кошелёк**. 
		'''

		self.my_wallet = '''
		Адрес вашего кошелька ниже.
		Переведите необходимую сумму btc на этот кошелек. 
		ВНИМАНИЕ! Средства зачисляются спустя 3 подтверждения сети. 
		После получения подтверждений на вашем балансе отобразятся перечисленные средства. 
		Вам остается лишь выбрать необходимый период доступа к сервису! Ссылка придет автоматически!
		'''

		self.wallet_address = '```{}```'	

		self.free_signals = '''
		Ознакомьтесь с результатами игры по сигналам группы за прошлый месяц:
		NXC 80%; BRK 107%; SNRG 70%; HKG 70%; GLD 70%; NEO168%; DAR 91%; QWARK 176%; XCP 85%; GCR 60%; THC 53%; XRP 62%; FLDC 77%; LSK 157%; QTUM 67%; MCO 102%; XVG 78%; KORE 330%; OMG 102%; PTOY 76%; NEO 73%; IOP 54%; ZEC 101%; ADX 117%; XLM 83%
		Присоединяйтесь к группе Профессионалов и наращивайте количество Биткойна на своем счету. 
			
		Ссылка: https://t.me/joinchat/Fxl6JkOKhf6kwLxnzCyJkg 
		'''

		self.vip_signals = '''
		Добро пожаловать в VIP
			
		Рады сообщить вам, что начиная с Октября 2017г. наш канал сотрудничает с очень серьезным источником информации, от Китов мира криптовалюты.. 
		
		  Все сигналы высоко-профитные, но результативность зависит от многих факторов, в том числе от опыта пользователя.
		
		ВНИМАНИЕ!!! Администрация канала не несет ответственности за возможные убытки пользователей. Все действия пользователи осуществляют на свой страх и риск и по своему личному усмотрению.
		
		Желаем Профитов!
		'''

		self.access_to_chat = '''
		Пополните свой баланс на необходимое количество BTC и Вы получите доступ в чат
		'''

		self.repare = 'Оплата пока на ремонте. Скоро всё будет'

		self.access_granted = '''Оплата произведена. Теперь чат доступен для Вас по ссылке https://t.me/joinchat/AFktb0KnIkcf5RrPM-uLQA
		Доступ оплачен до {} {}, {}
		'''

		self.not_enough_money = '''Оплата не произведена. На Вашем счёте недостаточно средств.'''

		self.select_action = 'Выберите действие:'

		self.subscription_ended = 'Подписка на канал VIP сигналов истекла. Чтобы продлить подписку пополните счёт и выберите срок подписки.'



class Message(BaseModel):
	sender		= IntegerField()
	text 		= TextField()
	msg_type	= TextField()
	timestamp	= DateTimeField(default = datetime.datetime.utcnow)

class Error(BaseModel):
	message 	= TextField()
	state		= TextField()
	exception 	= TextField()
	timestamp	= DateTimeField(default = datetime.datetime.utcnow)