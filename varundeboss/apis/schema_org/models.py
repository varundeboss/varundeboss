from __future__ import unicode_literals

from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Text(models.Model):

	text = models.TextField(verbose_name="Text")

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Text'
		verbose_name_plural = 'Text'


class URL(models.Model):

	uRL = models.TextField(verbose_name="URL")

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Url'
		verbose_name_plural = 'Url'


class Time(models.Model):

	time = models.TimeField(verbose_name="Time")

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Time'
		verbose_name_plural = 'Time'


class Number(models.Model):

	number = models.IntegerField(verbose_name="Number")

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Number'
		verbose_name_plural = 'Number'


class Boolean(models.Model):

	boolean = models.NullBooleanField(verbose_name="Boolean")

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Boolean'
		verbose_name_plural = 'Boolean'


class DateTime(models.Model):

	dateTime = models.DateTimeField(verbose_name="DateTime")

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Datetime'
		verbose_name_plural = 'Datetime'


class Integer(models.Model):

	integer = models.IntegerField(verbose_name="Integer")

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Integer'
		verbose_name_plural = 'Integer'


class Date(models.Model):

	date = models.DateField(verbose_name="Date")

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Date'
		verbose_name_plural = 'Date'


class Thing(models.Model):

	sameAs = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Sameas", help_text='''URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Freebase page, or official website.''', related_name="thing_sameas")
	potentialAction = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Potentialaction", help_text='''Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.''', related_name="thing_potentialaction")
	additionalType = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Additionaltype", help_text='''An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.''', related_name="thing_additionaltype")
	name = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Name", help_text='''The name of the item.''', related_name="thing_name")
	description = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Description", help_text='''A short description of the item.''', related_name="thing_description")
	alternateName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Alternatename", help_text='''An alias for the item.''', related_name="thing_alternatename")
	url = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Url", help_text='''URL of the item.''', related_name="thing_url")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Thing'
		verbose_name_plural = 'Thing'


class Action(models.Model):

	obj = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Object", help_text='''The object upon the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read *a book*.''', related_name="action_object")
	instrument = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Instrument", help_text='''The object that helped the agent perform the action. e.g. John wrote a book with *a pen*.''', related_name="action_instrument")
	error = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Error", help_text='''For failed actions, more information on the cause of the failure.''', related_name="action_error")
	actionStatus = models.ForeignKey('ActionStatusType', on_delete=models.CASCADE, verbose_name="Actionstatus", help_text='''Indicates the current disposition of the Action.''', related_name="action_actionstatus")
	result = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Result", help_text='''The result produced in the action. e.g. John wrote *a book*.''', related_name="action_result")
	target = models.ForeignKey('EntryPoint', on_delete=models.CASCADE, verbose_name="Target", help_text='''Indicates a target EntryPoint for an Action.''', related_name="action_target")
	startTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Starttime", help_text='''The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from *January* to December.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.''', related_name="action_starttime")
	endTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Endtime", help_text='''The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to *December*.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.''', related_name="action_endtime")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="action_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Action'
		verbose_name_plural = 'Action'


class LoseAction(models.Model):

	winner = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Winner", help_text='''A sub property of participant. The winner of the action.''', related_name="loseaction_winner")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="loseaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="loseaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Loseaction'
		verbose_name_plural = 'Loseaction'


class WinAction(models.Model):

	loser = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Loser", help_text='''A sub property of participant. The loser of the action.''', related_name="winaction_loser")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="winaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="winaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Winaction'
		verbose_name_plural = 'Winaction'


class ChooseAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="chooseaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="chooseaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Chooseaction'
		verbose_name_plural = 'Chooseaction'


class VoteAction(models.Model):

	candidate = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Candidate", help_text='''A sub property of object. The candidate subject of this action.''', related_name="voteaction_candidate")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="voteaction_action")
	chooseAction = models.ForeignKey('ChooseAction', on_delete=models.CASCADE, verbose_name="ChooseAction", related_name="voteaction_chooseaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="voteaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Voteaction'
		verbose_name_plural = 'Voteaction'


class EndorseAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="endorseaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="endorseaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Endorseaction'
		verbose_name_plural = 'Endorseaction'


class ReviewAction(models.Model):

	resultReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Resultreview", help_text='''A sub property of result. The review that resulted in the performing of the action.''', related_name="reviewaction_resultreview")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="reviewaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="reviewaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Reviewaction'
		verbose_name_plural = 'Reviewaction'


class ConsumeAction(models.Model):

	expectsAcceptanceOf = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Expectsacceptanceof", help_text='''An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.''', related_name="consumeaction_expectsacceptanceof")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="consumeaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="consumeaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Consumeaction'
		verbose_name_plural = 'Consumeaction'


class CookAction(models.Model):

	foodEvent = models.ForeignKey('FoodEvent', on_delete=models.CASCADE, verbose_name="Foodevent", help_text='''A sub property of location. The specific food event where the action occurred.''', related_name="cookaction_foodevent")
	recipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, verbose_name="Recipe", help_text='''A sub property of instrument. The recipe/instructions used to perform the action.''', related_name="cookaction_recipe")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="cookaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="cookaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Cookaction'
		verbose_name_plural = 'Cookaction'


class WriteAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="writeaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="writeaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Writeaction'
		verbose_name_plural = 'Writeaction'


class CommunicateAction(models.Model):

	about = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="About", help_text='''The subject matter of the content.''', related_name="communicateaction_about")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="communicateaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="communicateaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Communicateaction'
		verbose_name_plural = 'Communicateaction'


class AskAction(models.Model):

	question = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name="Question", help_text='''A sub property of object. A question.''', related_name="askaction_question")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="askaction_action")
	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="CommunicateAction", related_name="askaction_communicateaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="askaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Askaction'
		verbose_name_plural = 'Askaction'


class InformAction(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", help_text='''Upcoming or past event associated with this place, organization, or action. Supersedes events.''', related_name="informaction_event")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="informaction_action")
	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="CommunicateAction", related_name="informaction_communicateaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="informaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Informaction'
		verbose_name_plural = 'Informaction'


class RsvpAction(models.Model):

	comment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Comment", help_text='''Comments, typically from users.''', related_name="rsvpaction_comment")
	rsvpResponse = models.ForeignKey('RsvpResponseType', on_delete=models.CASCADE, verbose_name="Rsvpresponse", help_text='''The response (yes, no, maybe) to the RSVP.''', related_name="rsvpaction_rsvpresponse")
	additionalNumberOfGuests = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Additionalnumberofguests", help_text='''If responding yes, the number of guests who will attend in addition to the invitee.''', related_name="rsvpaction_additionalnumberofguests")
	informAction = models.ForeignKey('InformAction', on_delete=models.CASCADE, verbose_name="InformAction", related_name="rsvpaction_informaction")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="rsvpaction_action")
	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="CommunicateAction", related_name="rsvpaction_communicateaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="rsvpaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Rsvpaction'
		verbose_name_plural = 'Rsvpaction'


class ReplyAction(models.Model):

	resultComment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Resultcomment", help_text='''A sub property of result. The Comment created or sent as a result of this action.''', related_name="replyaction_resultcomment")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="replyaction_action")
	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="CommunicateAction", related_name="replyaction_communicateaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="replyaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Replyaction'
		verbose_name_plural = 'Replyaction'


class FollowAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="followaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="followaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Followaction'
		verbose_name_plural = 'Followaction'


class AllocateAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="allocateaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="allocateaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Allocateaction'
		verbose_name_plural = 'Allocateaction'


class PlanAction(models.Model):

	scheduledTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Scheduledtime", help_text='''The time the object is scheduled to.''', related_name="planaction_scheduledtime")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="planaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="planaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Planaction'
		verbose_name_plural = 'Planaction'


class PlayAction(models.Model):

	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", help_text='''An intended audience, i.e. a group for whom something was created. Supersedes serviceAudience.''', related_name="playaction_audience")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", help_text='''Upcoming or past event associated with this place, organization, or action. Supersedes events.''', related_name="playaction_event")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="playaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="playaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Playaction'
		verbose_name_plural = 'Playaction'


class ExerciseAction(models.Model):

	fromLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Fromlocation", help_text='''A sub property of location. The original location of the object or the agent before the action.''', related_name="exerciseaction_fromlocation")
	sportsTeam = models.ForeignKey('SportsTeam', on_delete=models.CASCADE, verbose_name="Sportsteam", help_text='''A sub property of participant. The sports team that participated on this action.''', related_name="exerciseaction_sportsteam")
	exerciseCourse = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Exercisecourse", help_text='''A sub property of location. The course where this action was taken. Supersedes course.''', related_name="exerciseaction_exercisecourse")
	sportsEvent = models.ForeignKey('SportsEvent', on_delete=models.CASCADE, verbose_name="Sportsevent", help_text='''A sub property of location. The sports event where this action occurred.''', related_name="exerciseaction_sportsevent")
	toLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Tolocation", help_text='''A sub property of location. The final location of the object or the agent after the action.''', related_name="exerciseaction_tolocation")
	exerciseType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Exercisetype", help_text='''Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.''', related_name="exerciseaction_exercisetype")
	opponent = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Opponent", help_text='''A sub property of participant. The opponent on this action.''', related_name="exerciseaction_opponent")
	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", help_text='''A sub property of location. The sports activity location where this action occurred.''', related_name="exerciseaction_sportsactivitylocation")
	exercisePlan = models.ForeignKey('ExercisePlan', on_delete=models.CASCADE, verbose_name="Exerciseplan", help_text='''A sub property of instrument. The exercise plan used on this action.''', related_name="exerciseaction_exerciseplan")
	exerciseRelatedDiet = models.ForeignKey('Diet', on_delete=models.CASCADE, verbose_name="Exerciserelateddiet", help_text='''A sub property of instrument. The diet used in this action. Supersedes diet.''', related_name="exerciseaction_exerciserelateddiet")
	distance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Distance", help_text='''The distance travelled, e.g. exercising or travelling.''', related_name="exerciseaction_distance")
	playAction = models.ForeignKey('PlayAction', on_delete=models.CASCADE, verbose_name="PlayAction", related_name="exerciseaction_playaction")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="exerciseaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="exerciseaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Exerciseaction'
		verbose_name_plural = 'Exerciseaction'


class SearchAction(models.Model):

	query = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Query", help_text='''A sub property of instrument. The query used on this action.''', related_name="searchaction_query")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="searchaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="searchaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Searchaction'
		verbose_name_plural = 'Searchaction'


class TradeAction(models.Model):

	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", help_text='''One or more detailed price specifications, indicating the unit price and delivery or payment charges.''', related_name="tradeaction_pricespecification")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="tradeaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="tradeaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Tradeaction'
		verbose_name_plural = 'Tradeaction'


class OrderAction(models.Model):

	deliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Deliverymethod", help_text='''A sub property of instrument. The method of delivery.''', related_name="orderaction_deliverymethod")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="orderaction_action")
	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="TradeAction", related_name="orderaction_tradeaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="orderaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Orderaction'
		verbose_name_plural = 'Orderaction'


class RentAction(models.Model):

	realEstateAgent = models.ForeignKey('RealEstateAgent', on_delete=models.CASCADE, verbose_name="Realestateagent", help_text='''A sub property of participant. The real estate agent involved in the action.''', related_name="rentaction_realestateagent")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="rentaction_action")
	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="TradeAction", related_name="rentaction_tradeaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="rentaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Rentaction'
		verbose_name_plural = 'Rentaction'


class SellAction(models.Model):

	buyer = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Buyer", help_text='''A sub property of participant. The participant/person/organization that bought the object.''', related_name="sellaction_buyer")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="sellaction_action")
	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="TradeAction", related_name="sellaction_tradeaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="sellaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Sellaction'
		verbose_name_plural = 'Sellaction'


class TipAction(models.Model):

	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="TradeAction", related_name="tipaction_tradeaction")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="tipaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="tipaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Tipaction'
		verbose_name_plural = 'Tipaction'


class TransferAction(models.Model):

	toLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Tolocation", help_text='''A sub property of location. The final location of the object or the agent after the action.''', related_name="transferaction_tolocation")
	fromLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Fromlocation", help_text='''A sub property of location. The original location of the object or the agent before the action.''', related_name="transferaction_fromlocation")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="transferaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="transferaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Transferaction'
		verbose_name_plural = 'Transferaction'


class BorrowAction(models.Model):

	lender = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Lender", help_text='''A sub property of participant. The person that lends the object being borrowed.''', related_name="borrowaction_lender")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="borrowaction_action")
	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="TransferAction", related_name="borrowaction_transferaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="borrowaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Borrowaction'
		verbose_name_plural = 'Borrowaction'


class LendAction(models.Model):

	borrower = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Borrower", help_text='''A sub property of participant. The person that borrows the object being lent.''', related_name="lendaction_borrower")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="lendaction_action")
	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="TransferAction", related_name="lendaction_transferaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="lendaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Lendaction'
		verbose_name_plural = 'Lendaction'


class ReceiveAction(models.Model):

	deliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Deliverymethod", help_text='''A sub property of instrument. The method of delivery.''', related_name="receiveaction_deliverymethod")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="receiveaction_action")
	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="TransferAction", related_name="receiveaction_transferaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="receiveaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Receiveaction'
		verbose_name_plural = 'Receiveaction'


class UpdateAction(models.Model):

	targetCollection = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Targetcollection", help_text='''A sub property of object. The collection target of the action. Supersedes collection.''', related_name="updateaction_targetcollection")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="updateaction_action")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="updateaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Updateaction'
		verbose_name_plural = 'Updateaction'


class ReplaceAction(models.Model):

	replacee = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Replacee", help_text='''A sub property of object. The object that is being replaced.''', related_name="replaceaction_replacee")
	replacer = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Replacer", help_text='''A sub property of object. The object that replaces.''', related_name="replaceaction_replacer")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", related_name="replaceaction_action")
	updateAction = models.ForeignKey('UpdateAction', on_delete=models.CASCADE, verbose_name="UpdateAction", related_name="replaceaction_updateaction")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="replaceaction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Replaceaction'
		verbose_name_plural = 'Replaceaction'


class CreativeWork(models.Model):

	video = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Video", help_text='''An embedded video object.''', related_name="creativework_video")
	fileFormat = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Fileformat", help_text='''Media type (aka MIME format, see IANA site) of the content e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, 'encoding' can be used to indicate each MediaObject alongside particular fileFormat information.''', related_name="creativework_fileformat")
	mainEntity = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Mainentity", help_text='''Indicates the primary entity described in some page or other CreativeWork. Inverse property: mainEntityOfPage.''', related_name="creativework_mainentity")
	mentions = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Mentions", help_text='''Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.''', related_name="creativework_mentions")
	commentCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Commentcount", help_text='''The number of comments this CreativeWork (e.g. Article, Question or Answer) has received. This is most applicable to works published in Web sites with commenting system; additional comments may exist elsewhere.''', related_name="creativework_commentcount")
	alternativeHeadline = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Alternativeheadline", help_text='''A secondary title of the CreativeWork.''', related_name="creativework_alternativeheadline")
	accessibilityFeature = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accessibilityfeature", help_text='''Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility (WebSchemas wiki lists possible values).''', related_name="creativework_accessibilityfeature")
	encoding = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="Encoding", help_text='''A media object that encodes this CreativeWork. This property is a synonym for associatedMedia. Supersedes encodings.''', related_name="creativework_encoding")
	educationalUse = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Educationaluse", help_text='''The purpose of a work in the context of education; for example, 'assignment', 'group work'.''', related_name="creativework_educationaluse")
	locationCreated = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Locationcreated", help_text='''The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork.''', related_name="creativework_locationcreated")
	interactivityType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Interactivitytype", help_text='''The predominant mode of learning supported by the learning resource. Acceptable values are 'active', 'expositive', or 'mixed'.''', related_name="creativework_interactivitytype")
	editor = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Editor", help_text='''Specifies the Person who edited the CreativeWork.''', related_name="creativework_editor")
	review = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", help_text='''A review of the item. Supersedes reviews.''', related_name="creativework_review")
	learningResourceType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Learningresourcetype", help_text='''The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.''', related_name="creativework_learningresourcetype")
	publication = models.ForeignKey('PublicationEvent', on_delete=models.CASCADE, verbose_name="Publication", help_text='''A publication event associated with the item.''', related_name="creativework_publication")
	accountablePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Accountableperson", help_text='''Specifies the Person that is legally accountable for the CreativeWork.''', related_name="creativework_accountableperson")
	recordedAt = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Recordedat", help_text='''The Event where the CreativeWork was recorded. The CreativeWork may capture all or part of the event. Inverse property: recordedIn.''', related_name="creativework_recordedat")
	educationalAlignment = models.ForeignKey('AlignmentObject', on_delete=models.CASCADE, verbose_name="Educationalalignment", help_text='''An alignment to an established educational framework.''', related_name="creativework_educationalalignment")
	aggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="creativework_aggregaterating")
	workExample = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Workexample", help_text='''Example/instance/realization/derivation of the concept of this creative work. eg. The paperback edition, first edition, or eBook. Inverse property: exampleOfWork.''', related_name="creativework_workexample")
	datePublished = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Datepublished", help_text='''Date of first broadcast/publication.''', related_name="creativework_datepublished")
	offers = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", help_text='''An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="creativework_offers")
	award = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", help_text='''An award won by or for this item. Supersedes awards.''', related_name="creativework_award")
	copyrightYear = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Copyrightyear", help_text='''The year during which the claimed copyright for the CreativeWork was first asserted.''', related_name="creativework_copyrightyear")
	hasPart = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Haspart", help_text='''Indicates a CreativeWork that is (in some sense) a part of this CreativeWork. Inverse property: isPartOf.''', related_name="creativework_haspart")
	keywords = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Keywords", help_text='''Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.''', related_name="creativework_keywords")
	text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Text", help_text='''The textual content of this CreativeWork.''', related_name="creativework_text")
	audio = models.ForeignKey('AudioObject', on_delete=models.CASCADE, verbose_name="Audio", help_text='''An embedded audio object.''', related_name="creativework_audio")
	sourceOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Sourceorganization", help_text='''The Organization on whose behalf the creator was working.''', related_name="creativework_sourceorganization")
	character = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Character", help_text='''Fictional person connected with a creative work.''', related_name="creativework_character")
	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", help_text='''An intended audience, i.e. a group for whom something was created. Supersedes serviceAudience.''', related_name="creativework_audience")
	isBasedOnUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Isbasedonurl", help_text='''A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.''', related_name="creativework_isbasedonurl")
	associatedMedia = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="Associatedmedia", help_text='''A media object that encodes this CreativeWork. This property is a synonym for encoding.''', related_name="creativework_associatedmedia")
	accessibilityControl = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accessibilitycontrol", help_text='''Identifies input methods that are sufficient to fully control the described resource (WebSchemas wiki lists possible values).''', related_name="creativework_accessibilitycontrol")
	timeRequired = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Timerequired", help_text='''Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience, e.g. 'P30M', 'P1H25M'.''', related_name="creativework_timerequired")
	comment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Comment", help_text='''Comments, typically from users.''', related_name="creativework_comment")
	publishingPrinciples = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Publishingprinciples", help_text='''Link to page describing the editorial principles of the organization primarily responsible for the creation of the CreativeWork.''', related_name="creativework_publishingprinciples")
	exampleOfWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Exampleofwork", help_text='''A creative work that this work is an example/instance/realization/derivation of. Inverse property: workExample.''', related_name="creativework_exampleofwork")
	accessibilityHazard = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accessibilityhazard", help_text='''A characteristic of the described resource that is physiologically dangerous to some users. Related to WCAG 2.0 guideline 2.3 (WebSchemas wiki lists possible values).''', related_name="creativework_accessibilityhazard")
	releasedEvent = models.ForeignKey('PublicationEvent', on_delete=models.CASCADE, verbose_name="Releasedevent", help_text='''The place and time the release was issued, expressed as a PublicationEvent.''', related_name="creativework_releasedevent")
	about = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="About", help_text='''The subject matter of the content.''', related_name="creativework_about")
	typicalAgeRange = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Typicalagerange", help_text='''The typical expected age range, e.g. '7-9', '11-'.''', related_name="creativework_typicalagerange")
	headline = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Headline", help_text='''Headline of the article.''', related_name="creativework_headline")
	version = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Version", help_text='''The version of the CreativeWork embodied by a specified resource.''', related_name="creativework_version")
	contentLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Contentlocation", help_text='''The location depicted or described in the content. For example, the location in a photograph or painting.''', related_name="creativework_contentlocation")
	interactionStatistic = models.ForeignKey('InteractionCounter', on_delete=models.CASCADE, verbose_name="Interactionstatistic", help_text='''The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used. Supersedes interactionCount.''', related_name="creativework_interactionstatistic")
	thumbnailUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Thumbnailurl", help_text='''A thumbnail image relevant to the Thing.''', related_name="creativework_thumbnailurl")
	isPartOf = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Ispartof", help_text='''Indicates a CreativeWork that this CreativeWork is (in some sense) part of. Inverse property: hasPart.''', related_name="creativework_ispartof")
	accessibilityAPI = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accessibilityapi", help_text='''Indicates that the resource is compatible with the referenced accessibility API (WebSchemas wiki lists possible values).''', related_name="creativework_accessibilityapi")
	isFamilyFriendly = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Isfamilyfriendly", help_text='''Indicates whether this content is family friendly.''', related_name="creativework_isfamilyfriendly")
	discussionUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Discussionurl", help_text='''A link to the page containing the comments of the CreativeWork.''', related_name="creativework_discussionurl")
	contentRating = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Contentrating", help_text='''Official rating of a piece of content—for example,'MPAA PG-13'.''', related_name="creativework_contentrating")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="creativework_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Creativework'
		verbose_name_plural = 'Creativework'


class Article(models.Model):

	articleSection = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Articlesection", help_text='''Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc.''', related_name="article_articlesection")
	articleBody = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Articlebody", help_text='''The actual body of the article.''', related_name="article_articlebody")
	wordCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Wordcount", help_text='''The number of words in the text of the Article.''', related_name="article_wordcount")
	pagination = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pagination", help_text='''Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".''', related_name="article_pagination")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="article_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="article_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Article'


class NewsArticle(models.Model):

	printEdition = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Printedition", help_text='''The edition of the print product in which the NewsArticle appears.''', related_name="newsarticle_printedition")
	dateline = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Dateline", help_text='''The location where the NewsArticle was produced.''', related_name="newsarticle_dateline")
	printColumn = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Printcolumn", help_text='''The number of the column in which the NewsArticle appears in the print edition.''', related_name="newsarticle_printcolumn")
	printPage = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Printpage", help_text='''If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18).''', related_name="newsarticle_printpage")
	printSection = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Printsection", help_text='''If this NewsArticle appears in print, this field indicates the print section in which the article appeared.''', related_name="newsarticle_printsection")
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", related_name="newsarticle_article")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="newsarticle_thing")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="newsarticle_creativework")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Newsarticle'
		verbose_name_plural = 'Newsarticle'


class Report(models.Model):

	reportNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Reportnumber", help_text='''The number or other unique designator assigned to a Report by the publishing organization.''', related_name="report_reportnumber")
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", related_name="report_article")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="report_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="report_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Report'
		verbose_name_plural = 'Report'


class MedicalScholarlyArticle(models.Model):

	publicationType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Publicationtype", help_text='''The type of the medical article, taken from the US NLM MeSH publication type catalog.''', related_name="medicalscholarlyarticle_publicationtype")
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", related_name="medicalscholarlyarticle_article")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalscholarlyarticle_thing")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="medicalscholarlyarticle_creativework")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalscholarlyarticle'
		verbose_name_plural = 'Medicalscholarlyarticle'


class SocialMediaPosting(models.Model):

	sharedContent = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Sharedcontent", help_text='''A CreativeWork such as an image, video, or audio clip shared as part of this posting.''', related_name="socialmediaposting_sharedcontent")
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", related_name="socialmediaposting_article")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="socialmediaposting_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="socialmediaposting_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Socialmediaposting'
		verbose_name_plural = 'Socialmediaposting'


class BlogPosting(models.Model):

	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", related_name="blogposting_article")
	socialMediaPosting = models.ForeignKey('SocialMediaPosting', on_delete=models.CASCADE, verbose_name="SocialMediaPosting", related_name="blogposting_socialmediaposting")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="blogposting_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="blogposting_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Blogposting'
		verbose_name_plural = 'Blogposting'


class LiveBlogPosting(models.Model):

	liveBlogUpdate = models.ForeignKey('BlogPosting', on_delete=models.CASCADE, verbose_name="Liveblogupdate", help_text='''An update to the LiveBlog.''', related_name="liveblogposting_liveblogupdate")
	coverageStartTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Coveragestarttime", help_text='''The time when the live blog will begin covering the Event. Note that coverage may begin before the Event's start time. The LiveBlogPosting may also be created before coverage begins.''', related_name="liveblogposting_coveragestarttime")
	coverageEndTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Coverageendtime", help_text='''The time when the live blog will stop covering the Event. Note that coverage may continue after the Event concludes.''', related_name="liveblogposting_coverageendtime")
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", related_name="liveblogposting_article")
	socialMediaPosting = models.ForeignKey('SocialMediaPosting', on_delete=models.CASCADE, verbose_name="SocialMediaPosting", related_name="liveblogposting_socialmediaposting")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="liveblogposting_thing")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="liveblogposting_creativework")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Liveblogposting'
		verbose_name_plural = 'Liveblogposting'


class TechArticle(models.Model):

	proficiencyLevel = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Proficiencylevel", help_text='''Proficiency needed for this content; expected values: 'Beginner', 'Expert'.''', related_name="techarticle_proficiencylevel")
	dependencies = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Dependencies", help_text='''Prerequisites needed to fulfill steps in article.''', related_name="techarticle_dependencies")
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", related_name="techarticle_article")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="techarticle_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="techarticle_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Techarticle'
		verbose_name_plural = 'Techarticle'


class APIReference(models.Model):

	targetPlatform = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Targetplatform", help_text='''Type of app development: phone, Metro style, desktop, XBox, etc.''', related_name="apireference_targetplatform")
	executableLibraryName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Executablelibraryname", help_text='''Library file name e.g., mscorlib.dll, system.web.dll. Supersedes assembly.''', related_name="apireference_executablelibraryname")
	programmingModel = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Programmingmodel", help_text='''Indicates whether API is managed or unmanaged.''', related_name="apireference_programmingmodel")
	assemblyVersion = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Assemblyversion", help_text='''Associated product/technology version. e.g., .NET Framework 4.5.''', related_name="apireference_assemblyversion")
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", related_name="apireference_article")
	techArticle = models.ForeignKey('TechArticle', on_delete=models.CASCADE, verbose_name="TechArticle", related_name="apireference_techarticle")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="apireference_thing")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="apireference_creativework")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Apireference'
		verbose_name_plural = 'Apireference'


class Blog(models.Model):

	blogPost = models.ForeignKey('BlogPosting', on_delete=models.CASCADE, verbose_name="Blogpost", help_text='''A posting that is part of this blog. Supersedes blogPosts.''', related_name="blog_blogpost")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="blog_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="blog_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Blog'
		verbose_name_plural = 'Blog'


class Book(models.Model):

	numberOfPages = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofpages", help_text='''The number of pages in the book.''', related_name="book_numberofpages")
	bookEdition = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Bookedition", help_text='''The edition of the book.''', related_name="book_bookedition")
	bookFormat = models.ForeignKey('BookFormatType', on_delete=models.CASCADE, verbose_name="Bookformat", help_text='''The format of the book.''', related_name="book_bookformat")
	isbn = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isbn", help_text='''The ISBN of the book.''', related_name="book_isbn")
	illustrator = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Illustrator", help_text='''The illustrator of the book.''', related_name="book_illustrator")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="book_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="book_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Book'
		verbose_name_plural = 'Book'


class Clip(models.Model):

	partOfSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Partofseason", help_text='''The season to which this episode belongs.''', related_name="clip_partofseason")
	partOfSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Partofseries", help_text='''The series to which this episode or season belongs. Supersedes partOfTVSeries.''', related_name="clip_partofseries")
	director = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", help_text='''A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.''', related_name="clip_director")
	actor = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", help_text='''An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.''', related_name="clip_actor")
	partOfEpisode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Partofepisode", help_text='''The episode to which this clip belongs.''', related_name="clip_partofepisode")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="clip_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="clip_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Clip'
		verbose_name_plural = 'Clip'


class Comment(models.Model):

	parentItem = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name="Parentitem", help_text='''The parent of a question, answer or item in general.''', related_name="comment_parentitem")
	upvoteCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Upvotecount", help_text='''The number of upvotes this question, answer or comment has received from the community.''', related_name="comment_upvotecount")
	downvoteCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Downvotecount", help_text='''The number of downvotes this question, answer or comment has received from the community.''', related_name="comment_downvotecount")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="comment_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="comment_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comment'


class Answer(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="answer_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="answer_thing")
	comment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Comment", related_name="answer_comment")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Answer'
		verbose_name_plural = 'Answer'


class CreativeWorkSeason(models.Model):

	startDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", help_text='''The start date and time of the item (in ISO 8601 date format).''', related_name="creativeworkseason_startdate")
	productionCompany = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="creativeworkseason_productioncompany")
	numberOfEpisodes = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofepisodes", help_text='''The number of episodes in this season or series.''', related_name="creativeworkseason_numberofepisodes")
	episode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", help_text='''An episode of a tv, radio or game media within a series or season. Supersedes episodes.''', related_name="creativeworkseason_episode")
	trailer = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="creativeworkseason_trailer")
	partOfSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Partofseries", help_text='''The series to which this episode or season belongs. Supersedes partOfTVSeries.''', related_name="creativeworkseason_partofseries")
	endDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", help_text='''The end date and time of the item (in ISO 8601 date format).''', related_name="creativeworkseason_enddate")
	director = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", help_text='''A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.''', related_name="creativeworkseason_director")
	actor = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", help_text='''An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.''', related_name="creativeworkseason_actor")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="creativeworkseason_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="creativeworkseason_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Creativeworkseason'
		verbose_name_plural = 'Creativeworkseason'


class CreativeWorkSeries(models.Model):

	startDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", help_text='''The start date and time of the item (in ISO 8601 date format).''', related_name="creativeworkseries_startdate")
	endDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", help_text='''The end date and time of the item (in ISO 8601 date format).''', related_name="creativeworkseries_enddate")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="creativeworkseries_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="creativeworkseries_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Creativeworkseries'
		verbose_name_plural = 'Creativeworkseries'


class Periodical(models.Model):

	issn = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Issn", help_text='''The International Standard Serial Number (ISSN) that identifies this periodical. You can repeat this property to (for example) identify different formats of this periodical.''', related_name="periodical_issn")
	creativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="CreativeWorkSeries", related_name="periodical_creativeworkseries")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="periodical_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="periodical_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Periodical'
		verbose_name_plural = 'Periodical'


class RadioSeries(models.Model):

	trailer = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="radioseries_trailer")
	numberOfEpisodes = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofepisodes", help_text='''The number of episodes in this season or series.''', related_name="radioseries_numberofepisodes")
	episode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", help_text='''An episode of a tv, radio or game media within a series or season. Supersedes episodes.''', related_name="radioseries_episode")
	productionCompany = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="radioseries_productioncompany")
	director = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", help_text='''A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.''', related_name="radioseries_director")
	actor = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", help_text='''An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.''', related_name="radioseries_actor")
	numberOfSeasons = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofseasons", help_text='''The number of seasons in this series.''', related_name="radioseries_numberofseasons")
	containsSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Containsseason", help_text='''A season that is part of the media series. Supersedes season.''', related_name="radioseries_containsseason")
	creativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="CreativeWorkSeries", related_name="radioseries_creativeworkseries")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="radioseries_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="radioseries_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Radioseries'
		verbose_name_plural = 'Radioseries'


class VideoGameSeries(models.Model):

	productionCompany = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="videogameseries_productioncompany")
	cheatCode = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Cheatcode", help_text='''Cheat codes to the game.''', related_name="videogameseries_cheatcode")
	episode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", help_text='''An episode of a tv, radio or game media within a series or season. Supersedes episodes.''', related_name="videogameseries_episode")
	gameItem = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Gameitem", help_text='''An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.''', related_name="videogameseries_gameitem")
	director = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", help_text='''A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.''', related_name="videogameseries_director")
	numberOfPlayers = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofplayers", help_text='''Indicate how many people can play this game (minimum, maximum, or range).''', related_name="videogameseries_numberofplayers")
	playMode = models.ForeignKey('GamePlayMode', on_delete=models.CASCADE, verbose_name="Playmode", help_text='''Indicates whether this game is multi-player, co-op or single-player. The game can be marked as multi-player, co-op and single-player at the same time.''', related_name="videogameseries_playmode")
	characterAttribute = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Characterattribute", help_text='''A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).''', related_name="videogameseries_characterattribute")
	numberOfEpisodes = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofepisodes", help_text='''The number of episodes in this season or series.''', related_name="videogameseries_numberofepisodes")
	trailer = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="videogameseries_trailer")
	quest = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Quest", help_text='''The task that a player-controlled character, or group of characters may complete in order to gain a reward.''', related_name="videogameseries_quest")
	actor = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", help_text='''An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.''', related_name="videogameseries_actor")
	numberOfSeasons = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofseasons", help_text='''The number of seasons in this series.''', related_name="videogameseries_numberofseasons")
	containsSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Containsseason", help_text='''A season that is part of the media series. Supersedes season.''', related_name="videogameseries_containsseason")
	creativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="CreativeWorkSeries", related_name="videogameseries_creativeworkseries")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="videogameseries_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="videogameseries_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Videogameseries'
		verbose_name_plural = 'Videogameseries'


class DataCatalog(models.Model):

	dataset = models.ForeignKey('Dataset', on_delete=models.CASCADE, verbose_name="Dataset", help_text='''A dataset contained in a catalog.''', related_name="datacatalog_dataset")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="datacatalog_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="datacatalog_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Datacatalog'
		verbose_name_plural = 'Datacatalog'


class Dataset(models.Model):

	distribution = models.ForeignKey('DataDownload', on_delete=models.CASCADE, verbose_name="Distribution", help_text='''A downloadable form of this dataset, at a specific location, in a specific format.''', related_name="dataset_distribution")
	datasetTimeInterval = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datasettimeinterval", help_text='''The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the year 2011 (in ISO 8601 time interval format). Supersedes temporal.''', related_name="dataset_datasettimeinterval")
	includedDataCatalog = models.ForeignKey('DataCatalog', on_delete=models.CASCADE, verbose_name="Includeddatacatalog", help_text='''A data catalog contained in the dataset. Supersedes catalog.''', related_name="dataset_includeddatacatalog")
	spatial = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Spatial", help_text='''The range of spatial applicability of a dataset, e.g. for a dataset of New York weather, the state of New York.''', related_name="dataset_spatial")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="dataset_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="dataset_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Dataset'
		verbose_name_plural = 'Dataset'


class DataFeed(models.Model):

	dataset = models.ForeignKey('Dataset', on_delete=models.CASCADE, verbose_name="Dataset", related_name="datafeed_dataset")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="datafeed_thing")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="datafeed_creativework")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Datafeed'
		verbose_name_plural = 'Datafeed'


class Diet(models.Model):

	dietFeatures = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Dietfeatures", help_text='''Nutritional information specific to the dietary plan. May include dietary recommendations on what foods to avoid, what foods to consume, and specific alterations/deviations from the USDA or other regulatory body's approved dietary guidelines.''', related_name="diet_dietfeatures")
	risks = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Risks", help_text='''Specific physiologic risks associated to the plan.''', related_name="diet_risks")
	physiologicalBenefits = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Physiologicalbenefits", help_text='''Specific physiologic benefits associated to the plan.''', related_name="diet_physiologicalbenefits")
	overview = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Overview", help_text='''Descriptive information establishing the overarching theory/philosophy of the plan. May include the rationale for the name, the population where the plan first came to prominence, etc.''', related_name="diet_overview")
	proprietaryName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Proprietaryname", help_text='''Proprietary name given to the diet plan, typically by its originator or creator.''', related_name="diet_proprietaryname")
	expertConsiderations = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Expertconsiderations", help_text='''Medical expert advice related to the plan.''', related_name="diet_expertconsiderations")
	medicalTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="MedicalTherapy", related_name="diet_medicaltherapy")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="diet_medicalentity")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="diet_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="diet_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Diet'
		verbose_name_plural = 'Diet'


class Episode(models.Model):

	trailer = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="episode_trailer")
	productionCompany = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="episode_productioncompany")
	partOfSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Partofseries", help_text='''The series to which this episode or season belongs. Supersedes partOfTVSeries.''', related_name="episode_partofseries")
	director = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", help_text='''A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.''', related_name="episode_director")
	actor = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", help_text='''An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.''', related_name="episode_actor")
	partOfSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Partofseason", help_text='''The season to which this episode belongs.''', related_name="episode_partofseason")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="episode_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="episode_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Episode'
		verbose_name_plural = 'Episode'


class TVEpisode(models.Model):

	countryOfOrigin = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Countryoforigin", help_text='''The country of the principal offices of the production company or individual responsible for the movie or program.''', related_name="tvepisode_countryoforigin")
	episode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", related_name="tvepisode_episode")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="tvepisode_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="tvepisode_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Tvepisode'
		verbose_name_plural = 'Tvepisode'


class ExercisePlan(models.Model):

	restPeriods = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Restperiods", help_text='''How often one should break from the activity.''', related_name="exerciseplan_restperiods")
	workload = models.ForeignKey('Energy', on_delete=models.CASCADE, verbose_name="Workload", help_text='''Quantitative measure of the physiologic output of the exercise; also referred to as energy expenditure.''', related_name="exerciseplan_workload")
	activityDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Activityduration", help_text='''Length of time to engage in the activity.''', related_name="exerciseplan_activityduration")
	intensity = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Intensity", help_text='''Quantitative measure gauging the degree of force involved in the exercise, for example, heartbeats per minute. May include the velocity of the movement.''', related_name="exerciseplan_intensity")
	activityFrequency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Activityfrequency", help_text='''How often one should engage in the activity.''', related_name="exerciseplan_activityfrequency")
	exerciseType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Exercisetype", help_text='''Type(s) of exercise or activity, such as strength training, flexibility training, aerobics, cardiac rehabilitation, etc.''', related_name="exerciseplan_exercisetype")
	repetitions = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Repetitions", help_text='''Number of times one should repeat the activity.''', related_name="exerciseplan_repetitions")
	additionalVariable = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Additionalvariable", help_text='''Any additional component of the exercise prescription that may need to be articulated to the patient. This may include the order of exercises, the number of repetitions of movement, quantitative distance, progressions over time, etc.''', related_name="exerciseplan_additionalvariable")
	medicalTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="MedicalTherapy", related_name="exerciseplan_medicaltherapy")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="exerciseplan_medicalentity")
	physicalActivity = models.ForeignKey('PhysicalActivity', on_delete=models.CASCADE, verbose_name="PhysicalActivity", related_name="exerciseplan_physicalactivity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="exerciseplan_thing")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="exerciseplan_creativework")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Exerciseplan'
		verbose_name_plural = 'Exerciseplan'


class Game(models.Model):

	gameItem = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Gameitem", help_text='''An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.''', related_name="game_gameitem")
	numberOfPlayers = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofplayers", help_text='''Indicate how many people can play this game (minimum, maximum, or range).''', related_name="game_numberofplayers")
	characterAttribute = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Characterattribute", help_text='''A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).''', related_name="game_characterattribute")
	quest = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Quest", help_text='''The task that a player-controlled character, or group of characters may complete in order to gain a reward.''', related_name="game_quest")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="game_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="game_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Game'
		verbose_name_plural = 'Game'


class VideoGame(models.Model):

	cheatCode = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Cheatcode", help_text='''Cheat codes to the game.''', related_name="videogame_cheatcode")
	gameServer = models.ForeignKey('GameServer', on_delete=models.CASCADE, verbose_name="Gameserver", help_text='''The server on which it is possible to play the game. Inverse property: game.''', related_name="videogame_gameserver")
	trailer = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="videogame_trailer")
	director = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", help_text='''A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.''', related_name="videogame_director")
	actor = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", help_text='''An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.''', related_name="videogame_actor")
	playMode = models.ForeignKey('GamePlayMode', on_delete=models.CASCADE, verbose_name="Playmode", help_text='''Indicates whether this game is multi-player, co-op or single-player. The game can be marked as multi-player, co-op and single-player at the same time.''', related_name="videogame_playmode")
	gameTip = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Gametip", help_text='''Links to tips, tactics, etc.''', related_name="videogame_gametip")
	softwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="SoftwareApplication", related_name="videogame_softwareapplication")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="videogame_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="videogame_thing")
	game = models.ForeignKey('Game', on_delete=models.CASCADE, verbose_name="Game", related_name="videogame_game")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Videogame'
		verbose_name_plural = 'Videogame'


class Map(models.Model):

	mapType = models.ForeignKey('MapCategoryType', on_delete=models.CASCADE, verbose_name="Maptype", help_text='''Indicates the kind of Map, from the MapCategoryType Enumeration.''', related_name="map_maptype")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="map_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="map_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Map'
		verbose_name_plural = 'Map'


class MediaObject(models.Model):

	productionCompany = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="mediaobject_productioncompany")
	contentSize = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Contentsize", help_text='''File size in (mega/kilo) bytes.''', related_name="mediaobject_contentsize")
	regionsAllowed = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Regionsallowed", help_text='''The regions where the media is allowed. If not specified, then it's assumed to be allowed everywhere. Specify the countries in ISO 3166 format.''', related_name="mediaobject_regionsallowed")
	associatedArticle = models.ForeignKey('NewsArticle', on_delete=models.CASCADE, verbose_name="Associatedarticle", help_text='''A NewsArticle associated with the Media Object.''', related_name="mediaobject_associatedarticle")
	contentUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Contenturl", help_text='''Actual bytes of the media object, for example the image file or video file.''', related_name="mediaobject_contenturl")
	expires = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Expires", help_text='''Date the content expires and is no longer useful or available. Useful for videos.''', related_name="mediaobject_expires")
	embedUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Embedurl", help_text='''A URL pointing to a player for a specific video. In general, this is the information in the src element of an embed tag and should not be the same as the content of the loc tag.''', related_name="mediaobject_embedurl")
	bitrate = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Bitrate", help_text='''The bitrate of the media object.''', related_name="mediaobject_bitrate")
	encodingFormat = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Encodingformat", help_text='''mp3, mpeg4, etc.''', related_name="mediaobject_encodingformat")
	requiresSubscription = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Requiressubscription", help_text='''Indicates if use of the media require a subscription (either paid or free). Allowed values are true or false (note that an earlier version had 'yes', 'no').''', related_name="mediaobject_requiressubscription")
	encodesCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Encodescreativework", help_text='''The CreativeWork encoded by this media object.''', related_name="mediaobject_encodescreativework")
	uploadDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Uploaddate", help_text='''Date when this media object was uploaded to this site.''', related_name="mediaobject_uploaddate")
	playerType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Playertype", help_text='''Player type required—for example, Flash or Silverlight.''', related_name="mediaobject_playertype")
	duration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", help_text='''The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.''', related_name="mediaobject_duration")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="mediaobject_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="mediaobject_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Mediaobject'
		verbose_name_plural = 'Mediaobject'


class AudioObject(models.Model):

	transcript = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Transcript", help_text='''If this MediaObject is an AudioObject or VideoObject, the transcript of that object.''', related_name="audioobject_transcript")
	mediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="MediaObject", related_name="audioobject_mediaobject")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="audioobject_thing")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="audioobject_creativework")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Audioobject'
		verbose_name_plural = 'Audioobject'


class DataDownload(models.Model):

	mediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="MediaObject", related_name="datadownload_mediaobject")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="datadownload_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="datadownload_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Datadownload'
		verbose_name_plural = 'Datadownload'


class ImageObject(models.Model):

	representativeOfPage = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Representativeofpage", help_text='''Indicates whether this image is representative of the content of the page.''', related_name="imageobject_representativeofpage")
	caption = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Caption", help_text='''The caption for this object.''', related_name="imageobject_caption")
	thumbnail = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Thumbnail", help_text='''Thumbnail image for an image or video.''', related_name="imageobject_thumbnail")
	mediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="MediaObject", related_name="imageobject_mediaobject")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="imageobject_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="imageobject_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Imageobject'
		verbose_name_plural = 'Imageobject'


class VideoObject(models.Model):

	transcript = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Transcript", help_text='''If this MediaObject is an AudioObject or VideoObject, the transcript of that object.''', related_name="videoobject_transcript")
	videoFrameSize = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Videoframesize", help_text='''The frame size of the video.''', related_name="videoobject_videoframesize")
	caption = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Caption", help_text='''The caption for this object.''', related_name="videoobject_caption")
	director = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", help_text='''A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.''', related_name="videoobject_director")
	actor = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", help_text='''An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.''', related_name="videoobject_actor")
	videoQuality = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Videoquality", help_text='''The quality of the video.''', related_name="videoobject_videoquality")
	thumbnail = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Thumbnail", help_text='''Thumbnail image for an image or video.''', related_name="videoobject_thumbnail")
	mediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="MediaObject", related_name="videoobject_mediaobject")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="videoobject_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="videoobject_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Videoobject'
		verbose_name_plural = 'Videoobject'


class Movie(models.Model):

	trailer = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="movie_trailer")
	productionCompany = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="movie_productioncompany")
	countryOfOrigin = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Countryoforigin", help_text='''The country of the principal offices of the production company or individual responsible for the movie or program.''', related_name="movie_countryoforigin")
	director = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", help_text='''A director of e.g. tv, radio, movie, video games etc. content. Directors can be associated with individual items or with a series, episode, clip. Supersedes directors.''', related_name="movie_director")
	actor = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", help_text='''An actor, e.g. in tv, radio, movie, video games etc. Actors can be associated with individual items or with a series, episode, clip. Supersedes actors.''', related_name="movie_actor")
	duration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", help_text='''The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.''', related_name="movie_duration")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="movie_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="movie_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Movie'
		verbose_name_plural = 'Movie'


class MusicComposition(models.Model):

	recordedAs = models.ForeignKey('MusicRecording', on_delete=models.CASCADE, verbose_name="Recordedas", help_text='''An audio recording of the work. Inverse property: recordingOf.''', related_name="musiccomposition_recordedas")
	iswcCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Iswccode", help_text='''The International Standard Musical Work Code for the composition.''', related_name="musiccomposition_iswccode")
	firstPerformance = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Firstperformance", help_text='''The date and place the work was first performed.''', related_name="musiccomposition_firstperformance")
	lyricist = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Lyricist", help_text='''The person who wrote the words.''', related_name="musiccomposition_lyricist")
	musicalKey = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Musicalkey", help_text='''The key, mode, or scale this composition uses.''', related_name="musiccomposition_musicalkey")
	musicArrangement = models.ForeignKey('MusicComposition', on_delete=models.CASCADE, verbose_name="Musicarrangement", help_text='''An arrangement derived from the composition.''', related_name="musiccomposition_musicarrangement")
	includedComposition = models.ForeignKey('MusicComposition', on_delete=models.CASCADE, verbose_name="Includedcomposition", help_text='''Smaller compositions included in this work (e.g. a movement in a symphony).''', related_name="musiccomposition_includedcomposition")
	lyrics = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Lyrics", help_text='''The words in the song.''', related_name="musiccomposition_lyrics")
	musicCompositionForm = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Musiccompositionform", help_text='''The type of composition (e.g. overture, sonata, symphony, etc.).''', related_name="musiccomposition_musiccompositionform")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="musiccomposition_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="musiccomposition_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Musiccomposition'
		verbose_name_plural = 'Musiccomposition'


class MusicPlaylist(models.Model):

	numTracks = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numtracks", help_text='''The number of tracks in this album or playlist.''', related_name="musicplaylist_numtracks")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="musicplaylist_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="musicplaylist_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Musicplaylist'
		verbose_name_plural = 'Musicplaylist'


class MusicAlbum(models.Model):

	albumRelease = models.ForeignKey('MusicRelease', on_delete=models.CASCADE, verbose_name="Albumrelease", help_text='''A release of this album. Inverse property: releaseOf.''', related_name="musicalbum_albumrelease")
	albumProductionType = models.ForeignKey('MusicAlbumProductionType', on_delete=models.CASCADE, verbose_name="Albumproductiontype", help_text='''Classification of the album by it's type of content: soundtrack, live album, studio album, etc.''', related_name="musicalbum_albumproductiontype")
	byArtist = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Byartist", help_text='''The artist that performed this album or recording.''', related_name="musicalbum_byartist")
	albumReleaseType = models.ForeignKey('MusicAlbumReleaseType', on_delete=models.CASCADE, verbose_name="Albumreleasetype", help_text='''The kind of release which this album is: single, EP or album.''', related_name="musicalbum_albumreleasetype")
	musicPlaylist = models.ForeignKey('MusicPlaylist', on_delete=models.CASCADE, verbose_name="MusicPlaylist", related_name="musicalbum_musicplaylist")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="musicalbum_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="musicalbum_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Musicalbum'
		verbose_name_plural = 'Musicalbum'


class MusicRelease(models.Model):

	releaseOf = models.ForeignKey('MusicAlbum', on_delete=models.CASCADE, verbose_name="Releaseof", help_text='''The album this is a release of. Inverse property: albumRelease.''', related_name="musicrelease_releaseof")
	recordLabel = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recordlabel", help_text='''The label that issued the release.''', related_name="musicrelease_recordlabel")
	catalogNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Catalognumber", help_text='''The catalog number for the release.''', related_name="musicrelease_catalognumber")
	musicReleaseFormat = models.ForeignKey('MusicReleaseFormatType', on_delete=models.CASCADE, verbose_name="Musicreleaseformat", help_text='''Format of this release (the type of recording media used, ie. compact disc, digital media, LP, etc.).''', related_name="musicrelease_musicreleaseformat")
	duration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", help_text='''The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.''', related_name="musicrelease_duration")
	musicPlaylist = models.ForeignKey('MusicPlaylist', on_delete=models.CASCADE, verbose_name="MusicPlaylist", related_name="musicrelease_musicplaylist")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="musicrelease_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="musicrelease_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Musicrelease'
		verbose_name_plural = 'Musicrelease'


class MusicRecording(models.Model):

	byArtist = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Byartist", help_text='''The artist that performed this album or recording.''', related_name="musicrecording_byartist")
	recordingOf = models.ForeignKey('MusicComposition', on_delete=models.CASCADE, verbose_name="Recordingof", help_text='''The composition this track is a recording of. Inverse property: recordedAs.''', related_name="musicrecording_recordingof")
	inPlaylist = models.ForeignKey('MusicPlaylist', on_delete=models.CASCADE, verbose_name="Inplaylist", help_text='''The playlist to which this recording belongs.''', related_name="musicrecording_inplaylist")
	isrcCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isrccode", help_text='''The International Standard Recording Code for the recording.''', related_name="musicrecording_isrccode")
	duration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", help_text='''The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.''', related_name="musicrecording_duration")
	inAlbum = models.ForeignKey('MusicAlbum', on_delete=models.CASCADE, verbose_name="Inalbum", help_text='''The album to which this recording belongs.''', related_name="musicrecording_inalbum")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="musicrecording_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="musicrecording_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Musicrecording'
		verbose_name_plural = 'Musicrecording'


class Photograph(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="photograph_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="photograph_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Photograph'
		verbose_name_plural = 'Photograph'


class PublicationIssue(models.Model):

	pagination = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pagination", help_text='''Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".''', related_name="publicationissue_pagination")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="publicationissue_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="publicationissue_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Publicationissue'
		verbose_name_plural = 'Publicationissue'


class PublicationVolume(models.Model):

	pagination = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pagination", help_text='''Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".''', related_name="publicationvolume_pagination")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="publicationvolume_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="publicationvolume_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Publicationvolume'
		verbose_name_plural = 'Publicationvolume'


class Question(models.Model):

	acceptedAnswer = models.ForeignKey('Answer', on_delete=models.CASCADE, verbose_name="Acceptedanswer", help_text='''The answer that has been accepted as best, typically on a Question/Answer site. Sites vary in their selection mechanisms, e.g. drawing on community opinion and/or the view of the Question author.''', related_name="question_acceptedanswer")
	suggestedAnswer = models.ForeignKey('Answer', on_delete=models.CASCADE, verbose_name="Suggestedanswer", help_text='''An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer site.''', related_name="question_suggestedanswer")
	answerCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Answercount", help_text='''The number of answers this question has received.''', related_name="question_answercount")
	upvoteCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Upvotecount", help_text='''The number of upvotes this question, answer or comment has received from the community.''', related_name="question_upvotecount")
	downvoteCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Downvotecount", help_text='''The number of downvotes this question, answer or comment has received from the community.''', related_name="question_downvotecount")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="question_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="question_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Question'
		verbose_name_plural = 'Question'


class Recipe(models.Model):

	recipeCuisine = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recipecuisine", help_text='''The cuisine of the recipe (for example, French or Ethiopian).''', related_name="recipe_recipecuisine")
	recipeIngredient = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recipeingredient", help_text='''A single ingredient used in the recipe, e.g. sugar, flour or garlic. Supersedes ingredients.''', related_name="recipe_recipeingredient")
	cookingMethod = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Cookingmethod", help_text='''The method of cooking, such as Frying, Steaming, ...''', related_name="recipe_cookingmethod")
	nutrition = models.ForeignKey('NutritionInformation', on_delete=models.CASCADE, verbose_name="Nutrition", help_text='''Nutrition information about the recipe.''', related_name="recipe_nutrition")
	recipeYield = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recipeyield", help_text='''The quantity produced by the recipe (for example, number of people served, number of servings, etc).''', related_name="recipe_recipeyield")
	totalTime = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Totaltime", help_text='''The total time it takes to prepare and cook the recipe, in ISO 8601 duration format.''', related_name="recipe_totaltime")
	prepTime = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Preptime", help_text='''The length of time it takes to prepare the recipe, in ISO 8601 duration format.''', related_name="recipe_preptime")
	cookTime = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Cooktime", help_text='''The time it takes to actually cook the dish, in ISO 8601 duration format.''', related_name="recipe_cooktime")
	recipeCategory = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recipecategory", help_text='''The category of the recipe—for example, appetizer, entree, etc.''', related_name="recipe_recipecategory")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="recipe_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="recipe_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Recipe'
		verbose_name_plural = 'Recipe'


class Review(models.Model):

	reviewBody = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Reviewbody", help_text='''The actual body of the review.''', related_name="review_reviewbody")
	itemReviewed = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Itemreviewed", help_text='''The item that is being reviewed/rated.''', related_name="review_itemreviewed")
	reviewRating = models.ForeignKey('Rating', on_delete=models.CASCADE, verbose_name="Reviewrating", help_text='''The rating given in this review. Note that reviews can themselves be rated. The reviewRating applies to rating given by the review. The aggregateRating property applies to the review itself, as a creative work.''', related_name="review_reviewrating")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="review_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="review_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Review'
		verbose_name_plural = 'Review'


class SoftwareApplication(models.Model):

	supportingData = models.ForeignKey('DataFeed', on_delete=models.CASCADE, verbose_name="Supportingdata", help_text='''Supporting data for a SoftwareApplication.''', related_name="softwareapplication_supportingdata")
	countriesNotSupported = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Countriesnotsupported", help_text='''Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.''', related_name="softwareapplication_countriesnotsupported")
	processorRequirements = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Processorrequirements", help_text='''Processor architecture required to run the application (e.g. IA64).''', related_name="softwareapplication_processorrequirements")
	installUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Installurl", help_text='''URL at which the app may be installed, if different from the URL of the item.''', related_name="softwareapplication_installurl")
	operatingSystem = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Operatingsystem", help_text='''Operating systems supported (Windows 7, OSX 10.6, Android 1.6).''', related_name="softwareapplication_operatingsystem")
	permissions = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Permissions", help_text='''Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi).''', related_name="softwareapplication_permissions")
	softwareHelp = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Softwarehelp", help_text='''Software application help.''', related_name="softwareapplication_softwarehelp")
	countriesSupported = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Countriessupported", help_text='''Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.''', related_name="softwareapplication_countriessupported")
	downloadUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Downloadurl", help_text='''If the file can be downloaded, URL to download the binary.''', related_name="softwareapplication_downloadurl")
	availableOnDevice = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Availableondevice", help_text='''Device required to run the application. Used in cases where a specific make/model is required to run the application. Supersedes device.''', related_name="softwareapplication_availableondevice")
	applicationSuite = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Applicationsuite", help_text='''The name of the application suite to which the application belongs (e.g. Excel belongs to Office).''', related_name="softwareapplication_applicationsuite")
	softwareVersion = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Softwareversion", help_text='''Version of the software instance.''', related_name="softwareapplication_softwareversion")
	fileSize = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Filesize", help_text='''Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.''', related_name="softwareapplication_filesize")
	softwareAddOn = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Softwareaddon", help_text='''Additional content for a software application.''', related_name="softwareapplication_softwareaddon")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="softwareapplication_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="softwareapplication_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Softwareapplication'
		verbose_name_plural = 'Softwareapplication'


class MobileApplication(models.Model):

	carrierRequirements = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Carrierrequirements", help_text='''Specifies specific carrier(s) requirements for the application (e.g. an application may only work on a specific carrier network).''', related_name="mobileapplication_carrierrequirements")
	softwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="SoftwareApplication", related_name="mobileapplication_softwareapplication")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="mobileapplication_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="mobileapplication_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Mobileapplication'
		verbose_name_plural = 'Mobileapplication'


class WebApplication(models.Model):

	browserRequirements = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Browserrequirements", help_text='''Specifies browser requirements in human-readable text. For example,"requires HTML5 support".''', related_name="webapplication_browserrequirements")
	softwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="SoftwareApplication", related_name="webapplication_softwareapplication")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="webapplication_thing")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="webapplication_creativework")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Webapplication'
		verbose_name_plural = 'Webapplication'


class SoftwareSourceCode(models.Model):

	runtimePlatform = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Runtimeplatform", help_text='''Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0). Supersedes runtime.''', related_name="softwaresourcecode_runtimeplatform")
	programmingLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Programminglanguage", help_text='''The computer programming language.''', related_name="softwaresourcecode_programminglanguage")
	targetProduct = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Targetproduct", help_text='''Target Operating System / Product to which the code applies. If applies to several versions, just the product name can be used.''', related_name="softwaresourcecode_targetproduct")
	codeSampleType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Codesampletype", help_text='''What type of code sample: full (compile ready) solution, code snippet, inline code, scripts, template. Supersedes sampleType.''', related_name="softwaresourcecode_codesampletype")
	codeRepository = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Coderepository", help_text='''Link to the repository where the un-compiled, human readable code and related code is located (SVN, github, CodePlex).''', related_name="softwaresourcecode_coderepository")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="softwaresourcecode_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="softwaresourcecode_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Softwaresourcecode'
		verbose_name_plural = 'Softwaresourcecode'


class VisualArtwork(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="visualartwork_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="visualartwork_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Visualartwork'
		verbose_name_plural = 'Visualartwork'


class WebPage(models.Model):

	mainContentOfPage = models.ForeignKey('WebPageElement', on_delete=models.CASCADE, verbose_name="Maincontentofpage", help_text='''Indicates if this web page element is the main subject of the page.''', related_name="webpage_maincontentofpage")
	lastReviewed = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Lastreviewed", help_text='''Date on which the content on this web page was last reviewed for accuracy and/or completeness.''', related_name="webpage_lastreviewed")
	significantLink = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Significantlink", help_text='''One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most. Supersedes significantLinks.''', related_name="webpage_significantlink")
	primaryImageOfPage = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Primaryimageofpage", help_text='''Indicates the main image on the page.''', related_name="webpage_primaryimageofpage")
	specialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, verbose_name="Specialty", help_text='''One of the domain specialities to which this web page's content applies.''', related_name="webpage_specialty")
	relatedLink = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Relatedlink", help_text='''A link related to this web page, for example to other related web pages.''', related_name="webpage_relatedlink")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="webpage_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="webpage_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Webpage'
		verbose_name_plural = 'Webpage'


class MedicalWebPage(models.Model):

	aspect = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Aspect", help_text='''An aspect of medical practice that is considered on the page, such as 'diagnosis', 'treatment', 'causes', 'prognosis', 'etiology', 'epidemiology', etc.''', related_name="medicalwebpage_aspect")
	webPage = models.ForeignKey('WebPage', on_delete=models.CASCADE, verbose_name="WebPage", related_name="medicalwebpage_webpage")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="medicalwebpage_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalwebpage_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalwebpage'
		verbose_name_plural = 'Medicalwebpage'


class WebPageElement(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="webpageelement_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="webpageelement_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Webpageelement'
		verbose_name_plural = 'Webpageelement'


class WebSite(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="CreativeWork", related_name="website_creativework")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="website_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Website'
		verbose_name_plural = 'Website'


class Event(models.Model):

	startDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", help_text='''The start date and time of the item (in ISO 8601 date format).''', related_name="event_startdate")
	workPerformed = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Workperformed", help_text='''A work performed in some event, for example a play performed in a TheaterEvent.''', related_name="event_workperformed")
	typicalAgeRange = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Typicalagerange", help_text='''The typical expected age range, e.g. '7-9', '11-'.''', related_name="event_typicalagerange")
	offers = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", help_text='''An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="event_offers")
	aggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="event_aggregaterating")
	recordedIn = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Recordedin", help_text='''The CreativeWork that captured all or part of this Event. Inverse property: recordedAt.''', related_name="event_recordedin")
	superEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Superevent", help_text='''An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.''', related_name="event_superevent")
	workFeatured = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Workfeatured", help_text='''A work featured in some event, e.g. exhibited in an ExhibitionEvent. Specific subproperties are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent).''', related_name="event_workfeatured")
	previousStartDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Previousstartdate", help_text='''Used in conjunction with eventStatus for rescheduled or cancelled events. This property contains the previously scheduled start date. For rescheduled events, the startDate property should be used for the newly scheduled start date. In the (rare) case of an event that has been postponed and rescheduled multiple times, this field may be repeated.''', related_name="event_previousstartdate")
	eventStatus = models.ForeignKey('EventStatusType', on_delete=models.CASCADE, verbose_name="Eventstatus", help_text='''An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled.''', related_name="event_eventstatus")
	subEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Subevent", help_text='''An Event that is part of this event. For example, a conference event includes many presentations, each of which is a subEvent of the conference. Supersedes subEvents.''', related_name="event_subevent")
	review = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", help_text='''A review of the item. Supersedes reviews.''', related_name="event_review")
	endDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", help_text='''The end date and time of the item (in ISO 8601 date format).''', related_name="event_enddate")
	duration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", help_text='''The duration of the item (movie, audio recording, event, etc.) in ISO 8601 date format.''', related_name="event_duration")
	doorTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Doortime", help_text='''The time admission will commence.''', related_name="event_doortime")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="event_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Event'
		verbose_name_plural = 'Event'


class DeliveryEvent(models.Model):

	availableFrom = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availablefrom", help_text='''When the item is available for pickup from the store, locker, etc.''', related_name="deliveryevent_availablefrom")
	hasDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Hasdeliverymethod", help_text='''Method used for delivery or shipping.''', related_name="deliveryevent_hasdeliverymethod")
	availableThrough = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availablethrough", help_text='''After this date, the item will no longer be available for pickup.''', related_name="deliveryevent_availablethrough")
	accessCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accesscode", help_text='''Password, PIN, or access code needed for delivery (e.g. from a locker).''', related_name="deliveryevent_accesscode")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", related_name="deliveryevent_event")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="deliveryevent_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Deliveryevent'
		verbose_name_plural = 'Deliveryevent'


class FoodEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", related_name="foodevent_event")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="foodevent_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Foodevent'
		verbose_name_plural = 'Foodevent'


class PublicationEvent(models.Model):

	publishedOn = models.ForeignKey('BroadcastService', on_delete=models.CASCADE, verbose_name="Publishedon", help_text='''A broadcast service associated with the publication event.''', related_name="publicationevent_publishedon")
	isAccessibleForFree = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Isaccessibleforfree", help_text='''A flag to signal that the publication is accessible for free. Supersedes free.''', related_name="publicationevent_isaccessibleforfree")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", related_name="publicationevent_event")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="publicationevent_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Publicationevent'
		verbose_name_plural = 'Publicationevent'


class BroadcastEvent(models.Model):

	isLiveBroadcast = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Islivebroadcast", help_text='''True is the broadcast is of a live event.''', related_name="broadcastevent_islivebroadcast")
	broadcastOfEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Broadcastofevent", help_text='''The event being broadcast such as a sporting event or awards ceremony.''', related_name="broadcastevent_broadcastofevent")
	videoFormat = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Videoformat", help_text='''The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).''', related_name="broadcastevent_videoformat")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", related_name="broadcastevent_event")
	publicationEvent = models.ForeignKey('PublicationEvent', on_delete=models.CASCADE, verbose_name="PublicationEvent", related_name="broadcastevent_publicationevent")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="broadcastevent_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Broadcastevent'
		verbose_name_plural = 'Broadcastevent'


class ScreeningEvent(models.Model):

	videoFormat = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Videoformat", help_text='''The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).''', related_name="screeningevent_videoformat")
	workPresented = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name="Workpresented", help_text='''The movie presented during this event.''', related_name="screeningevent_workpresented")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", related_name="screeningevent_event")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="screeningevent_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Screeningevent'
		verbose_name_plural = 'Screeningevent'


class SportsEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", related_name="sportsevent_event")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="sportsevent_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Sportsevent'
		verbose_name_plural = 'Sportsevent'


class UserComments(models.Model):

	discusses = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Discusses", help_text='''Specifies the CreativeWork associated with the UserComment.''', related_name="usercomments_discusses")
	commentTime = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Commenttime", help_text='''The time at which the UserComment was made.''', related_name="usercomments_commenttime")
	commentText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Commenttext", help_text='''The text of the UserComment.''', related_name="usercomments_commenttext")
	replyToUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Replytourl", help_text='''The URL at which a reply may be posted to the specified UserComment.''', related_name="usercomments_replytourl")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", related_name="usercomments_event")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="usercomments_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Usercomments'
		verbose_name_plural = 'Usercomments'


class AlignmentObject(models.Model):

	targetDescription = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Targetdescription", help_text='''The description of a node in an established educational framework.''', related_name="alignmentobject_targetdescription")
	targetName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Targetname", help_text='''The name of a node in an established educational framework.''', related_name="alignmentobject_targetname")
	alignmentType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Alignmenttype", help_text='''A category of alignment between the learning resource and the framework node. Recommended values include: 'assesses', 'teaches', 'requires', 'textComplexity', 'readingLevel', 'educationalSubject', and 'educationLevel'.''', related_name="alignmentobject_alignmenttype")
	educationalFramework = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Educationalframework", help_text='''The framework to which the resource being described is aligned.''', related_name="alignmentobject_educationalframework")
	targetUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Targeturl", help_text='''The URL of a node in an established educational framework.''', related_name="alignmentobject_targeturl")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="alignmentobject_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Alignmentobject'
		verbose_name_plural = 'Alignmentobject'


class Audience(models.Model):

	audienceType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Audiencetype", help_text='''The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).''', related_name="audience_audiencetype")
	geographicArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Geographicarea", help_text='''The geographic area associated with the audience.''', related_name="audience_geographicarea")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="audience_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Audience'
		verbose_name_plural = 'Audience'


class BusinessAudience(models.Model):

	yearsInOperation = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Yearsinoperation", help_text='''The age of the business.''', related_name="businessaudience_yearsinoperation")
	numberOfEmployees = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofemployees", help_text='''The number of employees in an organization e.g. business.''', related_name="businessaudience_numberofemployees")
	yearlyRevenue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Yearlyrevenue", help_text='''The size of the business in annual revenue.''', related_name="businessaudience_yearlyrevenue")
	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", related_name="businessaudience_audience")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="businessaudience_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Businessaudience'
		verbose_name_plural = 'Businessaudience'


class EducationalAudience(models.Model):

	educationalRole = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Educationalrole", help_text='''An educationalRole of an EducationalAudience.''', related_name="educationalaudience_educationalrole")
	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", related_name="educationalaudience_audience")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="educationalaudience_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Educationalaudience'
		verbose_name_plural = 'Educationalaudience'


class PeopleAudience(models.Model):

	suggestedGender = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Suggestedgender", help_text='''The gender of the person or audience.''', related_name="peopleaudience_suggestedgender")
	requiredGender = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Requiredgender", help_text='''Audiences defined by a person's gender.''', related_name="peopleaudience_requiredgender")
	requiredMaxAge = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Requiredmaxage", help_text='''Audiences defined by a person's maximum age.''', related_name="peopleaudience_requiredmaxage")
	healthCondition = models.ForeignKey('MedicalCondition', on_delete=models.CASCADE, verbose_name="Healthcondition", help_text='''Expectations for health conditions of target audience.''', related_name="peopleaudience_healthcondition")
	requiredMinAge = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Requiredminage", help_text='''Audiences defined by a person's minimum age.''', related_name="peopleaudience_requiredminage")
	suggestedMaxAge = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Suggestedmaxage", help_text='''Maximal age recommended for viewing content.''', related_name="peopleaudience_suggestedmaxage")
	suggestedMinAge = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Suggestedminage", help_text='''Minimal age recommended for viewing content.''', related_name="peopleaudience_suggestedminage")
	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", related_name="peopleaudience_audience")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="peopleaudience_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Peopleaudience'
		verbose_name_plural = 'Peopleaudience'


class ParentAudience(models.Model):

	childMinAge = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Childminage", help_text='''Minimal age of the child.''', related_name="parentaudience_childminage")
	childMaxAge = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Childmaxage", help_text='''Maximal age of the child.''', related_name="parentaudience_childmaxage")
	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", related_name="parentaudience_audience")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="parentaudience_thing")
	peopleAudience = models.ForeignKey('PeopleAudience', on_delete=models.CASCADE, verbose_name="PeopleAudience", related_name="parentaudience_peopleaudience")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Parentaudience'
		verbose_name_plural = 'Parentaudience'


class Brand(models.Model):

	review = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", help_text='''A review of the item. Supersedes reviews.''', related_name="brand_review")
	aggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="brand_aggregaterating")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="brand_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Brand'
		verbose_name_plural = 'Brand'


class BroadcastChannel(models.Model):

	broadcastChannelId = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Broadcastchannelid", help_text='''The unique address by which the BroadcastService can be identified in a provider lineup. In US, this is typically a number.''', related_name="broadcastchannel_broadcastchannelid")
	inBroadcastLineup = models.ForeignKey('CableOrSatelliteService', on_delete=models.CASCADE, verbose_name="Inbroadcastlineup", help_text='''The CableOrSatelliteService offering the channel.''', related_name="broadcastchannel_inbroadcastlineup")
	providesBroadcastService = models.ForeignKey('BroadcastService', on_delete=models.CASCADE, verbose_name="Providesbroadcastservice", help_text='''The BroadcastService offered on this channel.''', related_name="broadcastchannel_providesbroadcastservice")
	broadcastServiceTier = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Broadcastservicetier", help_text='''The type of service required to have access to the channel (e.g. Standard or Premium).''', related_name="broadcastchannel_broadcastservicetier")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="broadcastchannel_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Broadcastchannel'
		verbose_name_plural = 'Broadcastchannel'


class BusTrip(models.Model):

	busName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Busname", help_text='''The name of the bus (e.g. Bolt Express).''', related_name="bustrip_busname")
	arrivalTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Arrivaltime", help_text='''The expected arrival time.''', related_name="bustrip_arrivaltime")
	busNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Busnumber", help_text='''The unique identifier for the bus.''', related_name="bustrip_busnumber")
	departureTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Departuretime", help_text='''The expected departure time.''', related_name="bustrip_departuretime")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="bustrip_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Bustrip'
		verbose_name_plural = 'Bustrip'


class Class(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="class_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Class'
		verbose_name_plural = 'Class'


class DataFeedItem(models.Model):

	dateDeleted = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datedeleted", help_text='''The datetime the item was removed from the DataFeed.''', related_name="datafeeditem_datedeleted")
	item = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Item", help_text='''An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists')’.''', related_name="datafeeditem_item")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="datafeeditem_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Datafeeditem'
		verbose_name_plural = 'Datafeeditem'


class Demand(models.Model):

	itemCondition = models.ForeignKey('OfferItemCondition', on_delete=models.CASCADE, verbose_name="Itemcondition", help_text='''A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.''', related_name="demand_itemcondition")
	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", help_text='''One or more detailed price specifications, indicating the unit price and delivery or payment charges.''', related_name="demand_pricespecification")
	warranty = models.ForeignKey('WarrantyPromise', on_delete=models.CASCADE, verbose_name="Warranty", help_text='''The warranty promise(s) included in the offer. Supersedes warrantyPromise.''', related_name="demand_warranty")
	serialNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Serialnumber", help_text='''The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.''', related_name="demand_serialnumber")
	eligibleCustomerType = models.ForeignKey('BusinessEntityType', on_delete=models.CASCADE, verbose_name="Eligiblecustomertype", help_text='''The type(s) of customers for which the given offer is valid.''', related_name="demand_eligiblecustomertype")
	inventoryLevel = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Inventorylevel", help_text='''The current approximate inventory level for the item or items.''', related_name="demand_inventorylevel")
	sku = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Sku", help_text='''The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.''', related_name="demand_sku")
	availabilityEnds = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availabilityends", help_text='''The end of the availability of the product or service included in the offer.''', related_name="demand_availabilityends")
	eligibleQuantity = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligiblequantity", help_text='''The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.''', related_name="demand_eligiblequantity")
	advanceBookingRequirement = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Advancebookingrequirement", help_text='''The amount of time that is required between accepting the offer and the actual usage of the resource or service.''', related_name="demand_advancebookingrequirement")
	mpn = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mpn", help_text='''The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.''', related_name="demand_mpn")
	includesObject = models.ForeignKey('TypeAndQuantityNode', on_delete=models.CASCADE, verbose_name="Includesobject", help_text='''This links to a node or nodes indicating the exact quantity of the products included in the offer.''', related_name="demand_includesobject")
	eligibleDuration = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligibleduration", help_text='''The duration for which the given offer is valid.''', related_name="demand_eligibleduration")
	acceptedPaymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Acceptedpaymentmethod", help_text='''The payment method(s) accepted by seller for this offer.''', related_name="demand_acceptedpaymentmethod")
	availabilityStarts = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availabilitystarts", help_text='''The beginning of the availability of the product or service included in the offer.''', related_name="demand_availabilitystarts")
	gtin8 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin8", help_text='''The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See GS1 GTIN Summary for more details.''', related_name="demand_gtin8")
	eligibleTransactionVolume = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Eligibletransactionvolume", help_text='''The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.''', related_name="demand_eligibletransactionvolume")
	gtin14 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin14", help_text='''The GTIN-14 code of the product, or the product to which the offer refers. See GS1 GTIN Summary for more details.''', related_name="demand_gtin14")
	gtin13 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin13", help_text='''The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero. See GS1 GTIN Summary for more details.''', related_name="demand_gtin13")
	availability = models.ForeignKey('ItemAvailability', on_delete=models.CASCADE, verbose_name="Availability", help_text='''The availability of this item—for example In stock, Out of stock, Pre-order, etc.''', related_name="demand_availability")
	gtin12 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin12", help_text='''The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See GS1 GTIN Summary for more details.''', related_name="demand_gtin12")
	availableDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Availabledeliverymethod", help_text='''The delivery method(s) available for this offer.''', related_name="demand_availabledeliverymethod")
	businessFunction = models.ForeignKey('BusinessFunction', on_delete=models.CASCADE, verbose_name="Businessfunction", help_text='''The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.''', related_name="demand_businessfunction")
	deliveryLeadTime = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Deliveryleadtime", help_text='''The typical delay between the receipt of the order and the goods leaving the warehouse.''', related_name="demand_deliveryleadtime")
	validFrom = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", help_text='''The date when the item becomes valid.''', related_name="demand_validfrom")
	validThrough = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", help_text='''The end of the validity of offer, price specification, or opening hours data.''', related_name="demand_validthrough")
	availableAtOrFrom = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Availableatorfrom", help_text='''The place(s) from which the offer can be obtained (e.g. store locations).''', related_name="demand_availableatorfrom")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="demand_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Demand'
		verbose_name_plural = 'Demand'


class EntryPoint(models.Model):

	contentType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Contenttype", help_text='''The supported content type(s) for an EntryPoint response.''', related_name="entrypoint_contenttype")
	httpMethod = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Httpmethod", help_text='''An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP.''', related_name="entrypoint_httpmethod")
	encodingType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Encodingtype", help_text='''The supported encoding type(s) for an EntryPoint request.''', related_name="entrypoint_encodingtype")
	urlTemplate = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Urltemplate", help_text='''A url template (RFC6570) that will be used to construct the target of the execution of the action.''', related_name="entrypoint_urltemplate")
	actionApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Actionapplication", help_text='''An application that can complete the request. Supersedes application.''', related_name="entrypoint_actionapplication")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="entrypoint_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Entrypoint'
		verbose_name_plural = 'Entrypoint'


class Enumeration(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="enumeration_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Enumeration'
		verbose_name_plural = 'Enumeration'


class ActionStatusType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="actionstatustype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="actionstatustype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Actionstatustype'
		verbose_name_plural = 'Actionstatustype'


class BoardingPolicyType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="boardingpolicytype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="boardingpolicytype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Boardingpolicytype'
		verbose_name_plural = 'Boardingpolicytype'


class BookFormatType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="bookformattype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="bookformattype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Bookformattype'
		verbose_name_plural = 'Bookformattype'


class BusinessEntityType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="businessentitytype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="businessentitytype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Businessentitytype'
		verbose_name_plural = 'Businessentitytype'


class BusinessFunction(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="businessfunction_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="businessfunction_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Businessfunction'
		verbose_name_plural = 'Businessfunction'


class ContactPointOption(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="contactpointoption_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="contactpointoption_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Contactpointoption'
		verbose_name_plural = 'Contactpointoption'


class DayOfWeek(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="dayofweek_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="dayofweek_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Dayofweek'
		verbose_name_plural = 'Dayofweek'


class DeliveryMethod(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="deliverymethod_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="deliverymethod_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Deliverymethod'
		verbose_name_plural = 'Deliverymethod'


class DrugCostCategory(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="drugcostcategory_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="drugcostcategory_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="drugcostcategory_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Drugcostcategory'
		verbose_name_plural = 'Drugcostcategory'


class DrugPregnancyCategory(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="drugpregnancycategory_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="drugpregnancycategory_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="drugpregnancycategory_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Drugpregnancycategory'
		verbose_name_plural = 'Drugpregnancycategory'


class DrugPrescriptionStatus(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="drugprescriptionstatus_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="drugprescriptionstatus_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="drugprescriptionstatus_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Drugprescriptionstatus'
		verbose_name_plural = 'Drugprescriptionstatus'


class EventStatusType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="eventstatustype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="eventstatustype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Eventstatustype'
		verbose_name_plural = 'Eventstatustype'


class GamePlayMode(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="gameplaymode_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="gameplaymode_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Gameplaymode'
		verbose_name_plural = 'Gameplaymode'


class GameServerStatus(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="gameserverstatus_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="gameserverstatus_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Gameserverstatus'
		verbose_name_plural = 'Gameserverstatus'


class InfectiousAgentClass(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="infectiousagentclass_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="infectiousagentclass_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="infectiousagentclass_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Infectiousagentclass'
		verbose_name_plural = 'Infectiousagentclass'


class ItemAvailability(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="itemavailability_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="itemavailability_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Itemavailability'
		verbose_name_plural = 'Itemavailability'


class ItemListOrderType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="itemlistordertype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="itemlistordertype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Itemlistordertype'
		verbose_name_plural = 'Itemlistordertype'


class MapCategoryType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="mapcategorytype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="mapcategorytype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Mapcategorytype'
		verbose_name_plural = 'Mapcategorytype'


class MedicalDevicePurpose(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="medicaldevicepurpose_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicaldevicepurpose_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicaldevicepurpose_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicaldevicepurpose'
		verbose_name_plural = 'Medicaldevicepurpose'


class MedicalEvidenceLevel(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="medicalevidencelevel_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalevidencelevel_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalevidencelevel_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalevidencelevel'
		verbose_name_plural = 'Medicalevidencelevel'


class MedicalProcedureType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="medicalproceduretype_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalproceduretype_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalproceduretype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalproceduretype'
		verbose_name_plural = 'Medicalproceduretype'


class MedicalSpecialty(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="medicalspecialty_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalspecialty_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalspecialty_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalspecialty'
		verbose_name_plural = 'Medicalspecialty'


class MedicalStudyStatus(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="medicalstudystatus_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalstudystatus_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalstudystatus_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalstudystatus'
		verbose_name_plural = 'Medicalstudystatus'


class MedicalTrialDesign(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="medicaltrialdesign_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicaltrialdesign_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicaltrialdesign_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicaltrialdesign'
		verbose_name_plural = 'Medicaltrialdesign'


class MedicineSystem(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="medicinesystem_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicinesystem_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicinesystem_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicinesystem'
		verbose_name_plural = 'Medicinesystem'


class PhysicalActivityCategory(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="physicalactivitycategory_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="physicalactivitycategory_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="physicalactivitycategory_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Physicalactivitycategory'
		verbose_name_plural = 'Physicalactivitycategory'


class PhysicalExam(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="physicalexam_enumeration")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="physicalexam_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="physicalexam_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Physicalexam'
		verbose_name_plural = 'Physicalexam'


class MusicAlbumProductionType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="musicalbumproductiontype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="musicalbumproductiontype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Musicalbumproductiontype'
		verbose_name_plural = 'Musicalbumproductiontype'


class MusicAlbumReleaseType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="musicalbumreleasetype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="musicalbumreleasetype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Musicalbumreleasetype'
		verbose_name_plural = 'Musicalbumreleasetype'


class MusicReleaseFormatType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="musicreleaseformattype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="musicreleaseformattype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Musicreleaseformattype'
		verbose_name_plural = 'Musicreleaseformattype'


class OfferItemCondition(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="offeritemcondition_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="offeritemcondition_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Offeritemcondition'
		verbose_name_plural = 'Offeritemcondition'


class OrderStatus(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="orderstatus_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="orderstatus_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Orderstatus'
		verbose_name_plural = 'Orderstatus'


class PaymentMethod(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="paymentmethod_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="paymentmethod_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Paymentmethod'
		verbose_name_plural = 'Paymentmethod'


class PaymentStatusType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="paymentstatustype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="paymentstatustype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Paymentstatustype'
		verbose_name_plural = 'Paymentstatustype'


class QualitativeValue(models.Model):

	lesser = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Lesser", help_text='''This ordering relation for qualitative values indicates that the subject is lesser than the object.''', related_name="qualitativevalue_lesser")
	lesserOrEqual = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Lesserorequal", help_text='''This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object.''', related_name="qualitativevalue_lesserorequal")
	greaterOrEqual = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Greaterorequal", help_text='''This ordering relation for qualitative values indicates that the subject is greater than or equal to the object.''', related_name="qualitativevalue_greaterorequal")
	additionalProperty = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Additionalproperty", help_text='''A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.''', related_name="qualitativevalue_additionalproperty")
	nonEqual = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Nonequal", help_text='''This ordering relation for qualitative values indicates that the subject is not equal to the object.''', related_name="qualitativevalue_nonequal")
	equal = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Equal", help_text='''This ordering relation for qualitative values indicates that the subject is equal to the object.''', related_name="qualitativevalue_equal")
	greater = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Greater", help_text='''This ordering relation for qualitative values indicates that the subject is greater than the object.''', related_name="qualitativevalue_greater")
	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="qualitativevalue_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="qualitativevalue_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Qualitativevalue'
		verbose_name_plural = 'Qualitativevalue'


class DriveWheelConfigurationValue(models.Model):

	qualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="QualitativeValue", related_name="drivewheelconfigurationvalue_qualitativevalue")
	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="drivewheelconfigurationvalue_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="drivewheelconfigurationvalue_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Drivewheelconfigurationvalue'
		verbose_name_plural = 'Drivewheelconfigurationvalue'


class SteeringPositionValue(models.Model):

	qualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="QualitativeValue", related_name="steeringpositionvalue_qualitativevalue")
	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="steeringpositionvalue_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="steeringpositionvalue_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Steeringpositionvalue'
		verbose_name_plural = 'Steeringpositionvalue'


class ReservationStatusType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="reservationstatustype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="reservationstatustype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Reservationstatustype'
		verbose_name_plural = 'Reservationstatustype'


class RsvpResponseType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="rsvpresponsetype_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="rsvpresponsetype_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Rsvpresponsetype'
		verbose_name_plural = 'Rsvpresponsetype'


class Specialty(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="specialty_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="specialty_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Specialty'
		verbose_name_plural = 'Specialty'


class WarrantyScope(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", related_name="warrantyscope_enumeration")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="warrantyscope_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Warrantyscope'
		verbose_name_plural = 'Warrantyscope'


class Flight(models.Model):

	arrivalAirport = models.ForeignKey('Airport', on_delete=models.CASCADE, verbose_name="Arrivalairport", help_text='''The airport where the flight terminates.''', related_name="flight_arrivalairport")
	mealService = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mealservice", help_text='''Description of the meals that will be provided or available for purchase.''', related_name="flight_mealservice")
	departureGate = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Departuregate", help_text='''Identifier of the flight's departure gate.''', related_name="flight_departuregate")
	arrivalTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Arrivaltime", help_text='''The expected arrival time.''', related_name="flight_arrivaltime")
	departureTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Departuretime", help_text='''The expected departure time.''', related_name="flight_departuretime")
	departureAirport = models.ForeignKey('Airport', on_delete=models.CASCADE, verbose_name="Departureairport", help_text='''The airport where the flight originates.''', related_name="flight_departureairport")
	boardingPolicy = models.ForeignKey('BoardingPolicyType', on_delete=models.CASCADE, verbose_name="Boardingpolicy", help_text='''The type of boarding policy used by the airline (e.g. zone-based or group-based).''', related_name="flight_boardingpolicy")
	webCheckinTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Webcheckintime", help_text='''The time when a passenger can check into the flight online.''', related_name="flight_webcheckintime")
	departureTerminal = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Departureterminal", help_text='''Identifier of the flight's departure terminal.''', related_name="flight_departureterminal")
	arrivalGate = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Arrivalgate", help_text='''Identifier of the flight's arrival gate.''', related_name="flight_arrivalgate")
	flightNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Flightnumber", help_text='''The unique identifier for a flight including the airline IATA code. For example, if describing United flight 110, where the IATA code for United is 'UA', the flightNumber is 'UA110'.''', related_name="flight_flightnumber")
	arrivalTerminal = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Arrivalterminal", help_text='''Identifier of the flight's arrival terminal.''', related_name="flight_arrivalterminal")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="flight_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Flight'
		verbose_name_plural = 'Flight'


class GameServer(models.Model):

	serverStatus = models.ForeignKey('GameServerStatus', on_delete=models.CASCADE, verbose_name="Serverstatus", help_text='''Status of a game server.''', related_name="gameserver_serverstatus")
	game = models.ForeignKey('VideoGame', on_delete=models.CASCADE, verbose_name="Game", help_text='''Video game which is played on this server. Inverse property: gameServer.''', related_name="gameserver_game")
	playersOnline = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Playersonline", help_text='''Number of players on the server.''', related_name="gameserver_playersonline")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="gameserver_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Gameserver'
		verbose_name_plural = 'Gameserver'


class Invoice(models.Model):

	confirmationNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Confirmationnumber", help_text='''A number that confirms the given order or payment has been received.''', related_name="invoice_confirmationnumber")
	paymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Paymentmethod", help_text='''The name of the credit card or other method of payment for the order.''', related_name="invoice_paymentmethod")
	totalPaymentDue = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Totalpaymentdue", help_text='''The total amount due.''', related_name="invoice_totalpaymentdue")
	scheduledPaymentDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Scheduledpaymentdate", help_text='''The date the invoice is scheduled to be paid.''', related_name="invoice_scheduledpaymentdate")
	accountId = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accountid", help_text='''The identifier for the account the payment will be applied to.''', related_name="invoice_accountid")
	paymentDueDate = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Paymentduedate", help_text='''The date that payment is due. Supersedes paymentDue.''', related_name="invoice_paymentduedate")
	referencesOrder = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name="Referencesorder", help_text='''The Order(s) related to this Invoice. One or more Orders may be combined into a single Invoice.''', related_name="invoice_referencesorder")
	minimumPaymentDue = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Minimumpaymentdue", help_text='''The minimum payment required at this time.''', related_name="invoice_minimumpaymentdue")
	billingPeriod = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Billingperiod", help_text='''The time interval used to compute the invoice.''', related_name="invoice_billingperiod")
	paymentMethodId = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Paymentmethodid", help_text='''An identifier for the method of payment used (e.g. the last 4 digits of the credit card).''', related_name="invoice_paymentmethodid")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="invoice_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Invoice'
		verbose_name_plural = 'Invoice'


class ItemList(models.Model):

	numberOfItems = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofitems", help_text='''The number of items in an ItemList. Note that some descriptions might not fully describe all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems would be for the entire list.''', related_name="itemlist_numberofitems")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="itemlist_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Itemlist'
		verbose_name_plural = 'Itemlist'


class BreadcrumbList(models.Model):

	itemList = models.ForeignKey('ItemList', on_delete=models.CASCADE, verbose_name="ItemList", related_name="breadcrumblist_itemlist")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="breadcrumblist_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Breadcrumblist'
		verbose_name_plural = 'Breadcrumblist'


class OfferCatalog(models.Model):

	itemList = models.ForeignKey('ItemList', on_delete=models.CASCADE, verbose_name="ItemList", related_name="offercatalog_itemlist")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="offercatalog_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Offercatalog'
		verbose_name_plural = 'Offercatalog'


class JobPosting(models.Model):

	occupationalCategory = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Occupationalcategory", help_text='''Category or categories describing the job. Use BLS O*NET-SOC taxonomy: http://www.onetcenter.org/taxonomy.html. Ideally includes textual label and formal code, with the property repeated for each applicable value.''', related_name="jobposting_occupationalcategory")
	experienceRequirements = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Experiencerequirements", help_text='''Description of skills and experience needed for the position.''', related_name="jobposting_experiencerequirements")
	salaryCurrency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Salarycurrency", help_text='''The currency (coded using ISO 4217, http://en.wikipedia.org/wiki/ISO_4217 ) used for the main salary information in this job posting or for this employee.''', related_name="jobposting_salarycurrency")
	jobBenefits = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Jobbenefits", help_text='''Description of benefits associated with the job. Supersedes benefits.''', related_name="jobposting_jobbenefits")
	hiringOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Hiringorganization", help_text='''Organization offering the job position.''', related_name="jobposting_hiringorganization")
	responsibilities = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Responsibilities", help_text='''Responsibilities associated with this role.''', related_name="jobposting_responsibilities")
	industry = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Industry", help_text='''The industry associated with the job position.''', related_name="jobposting_industry")
	qualifications = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Qualifications", help_text='''Specific qualifications required for this role.''', related_name="jobposting_qualifications")
	specialCommitments = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Specialcommitments", help_text='''Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.''', related_name="jobposting_specialcommitments")
	workHours = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Workhours", help_text='''The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).''', related_name="jobposting_workhours")
	incentiveCompensation = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Incentivecompensation", help_text='''Description of bonus and commission compensation aspects of the job. Supersedes incentives.''', related_name="jobposting_incentivecompensation")
	datePosted = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Dateposted", help_text='''Publication date for the job posting.''', related_name="jobposting_dateposted")
	title = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Title", help_text='''The title of the job.''', related_name="jobposting_title")
	jobLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Joblocation", help_text='''A (typically single) geographic location associated with the job position.''', related_name="jobposting_joblocation")
	educationRequirements = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Educationrequirements", help_text='''Educational background needed for the position.''', related_name="jobposting_educationrequirements")
	skills = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Skills", help_text='''Skills required to fulfill this role.''', related_name="jobposting_skills")
	employmentType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Employmenttype", help_text='''Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).''', related_name="jobposting_employmenttype")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="jobposting_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Jobposting'
		verbose_name_plural = 'Jobposting'


class Language(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="language_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Language'
		verbose_name_plural = 'Language'


class ListItem(models.Model):

	previousItem = models.ForeignKey('ListItem', on_delete=models.CASCADE, verbose_name="Previousitem", help_text='''A link to the ListItem that preceeds the current one.''', related_name="listitem_previousitem")
	nextItem = models.ForeignKey('ListItem', on_delete=models.CASCADE, verbose_name="Nextitem", help_text='''A link to the ListItem that follows the current one.''', related_name="listitem_nextitem")
	item = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Item", help_text='''An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists')’.''', related_name="listitem_item")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="listitem_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Listitem'
		verbose_name_plural = 'Listitem'


class Offer(models.Model):

	itemCondition = models.ForeignKey('OfferItemCondition', on_delete=models.CASCADE, verbose_name="Itemcondition", help_text='''A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.''', related_name="offer_itemcondition")
	priceValidUntil = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Pricevaliduntil", help_text='''The date after which the price is no longer available.''', related_name="offer_pricevaliduntil")
	warranty = models.ForeignKey('WarrantyPromise', on_delete=models.CASCADE, verbose_name="Warranty", help_text='''The warranty promise(s) included in the offer. Supersedes warrantyPromise.''', related_name="offer_warranty")
	addOn = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Addon", help_text='''An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).''', related_name="offer_addon")
	serialNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Serialnumber", help_text='''The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.''', related_name="offer_serialnumber")
	eligibleCustomerType = models.ForeignKey('BusinessEntityType', on_delete=models.CASCADE, verbose_name="Eligiblecustomertype", help_text='''The type(s) of customers for which the given offer is valid.''', related_name="offer_eligiblecustomertype")
	inventoryLevel = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Inventorylevel", help_text='''The current approximate inventory level for the item or items.''', related_name="offer_inventorylevel")
	sku = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Sku", help_text='''The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.''', related_name="offer_sku")
	availabilityEnds = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availabilityends", help_text='''The end of the availability of the product or service included in the offer.''', related_name="offer_availabilityends")
	eligibleQuantity = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligiblequantity", help_text='''The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.''', related_name="offer_eligiblequantity")
	advanceBookingRequirement = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Advancebookingrequirement", help_text='''The amount of time that is required between accepting the offer and the actual usage of the resource or service.''', related_name="offer_advancebookingrequirement")
	review = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", help_text='''A review of the item. Supersedes reviews.''', related_name="offer_review")
	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", help_text='''One or more detailed price specifications, indicating the unit price and delivery or payment charges.''', related_name="offer_pricespecification")
	mpn = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mpn", help_text='''The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.''', related_name="offer_mpn")
	includesObject = models.ForeignKey('TypeAndQuantityNode', on_delete=models.CASCADE, verbose_name="Includesobject", help_text='''This links to a node or nodes indicating the exact quantity of the products included in the offer.''', related_name="offer_includesobject")
	eligibleDuration = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligibleduration", help_text='''The duration for which the given offer is valid.''', related_name="offer_eligibleduration")
	acceptedPaymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Acceptedpaymentmethod", help_text='''The payment method(s) accepted by seller for this offer.''', related_name="offer_acceptedpaymentmethod")
	availabilityStarts = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availabilitystarts", help_text='''The beginning of the availability of the product or service included in the offer.''', related_name="offer_availabilitystarts")
	gtin8 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin8", help_text='''The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See GS1 GTIN Summary for more details.''', related_name="offer_gtin8")
	eligibleTransactionVolume = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Eligibletransactionvolume", help_text='''The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.''', related_name="offer_eligibletransactionvolume")
	priceCurrency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricecurrency", help_text='''The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.''', related_name="offer_pricecurrency")
	gtin14 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin14", help_text='''The GTIN-14 code of the product, or the product to which the offer refers. See GS1 GTIN Summary for more details.''', related_name="offer_gtin14")
	gtin13 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin13", help_text='''The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero. See GS1 GTIN Summary for more details.''', related_name="offer_gtin13")
	availability = models.ForeignKey('ItemAvailability', on_delete=models.CASCADE, verbose_name="Availability", help_text='''The availability of this item—for example In stock, Out of stock, Pre-order, etc.''', related_name="offer_availability")
	aggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="offer_aggregaterating")
	gtin12 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin12", help_text='''The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See GS1 GTIN Summary for more details.''', related_name="offer_gtin12")
	availableDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Availabledeliverymethod", help_text='''The delivery method(s) available for this offer.''', related_name="offer_availabledeliverymethod")
	businessFunction = models.ForeignKey('BusinessFunction', on_delete=models.CASCADE, verbose_name="Businessfunction", help_text='''The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.''', related_name="offer_businessfunction")
	deliveryLeadTime = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Deliveryleadtime", help_text='''The typical delay between the receipt of the order and the goods leaving the warehouse.''', related_name="offer_deliveryleadtime")
	validFrom = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", help_text='''The date when the item becomes valid.''', related_name="offer_validfrom")
	validThrough = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", help_text='''The end of the validity of offer, price specification, or opening hours data.''', related_name="offer_validthrough")
	availableAtOrFrom = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Availableatorfrom", help_text='''The place(s) from which the offer can be obtained (e.g. store locations).''', related_name="offer_availableatorfrom")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="offer_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Offer'
		verbose_name_plural = 'Offer'


class AggregateOffer(models.Model):

	offers = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", help_text='''An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="aggregateoffer_offers")
	offerCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Offercount", help_text='''The number of offers for the product.''', related_name="aggregateoffer_offercount")
	offer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offer", related_name="aggregateoffer_offer")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="aggregateoffer_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Aggregateoffer'
		verbose_name_plural = 'Aggregateoffer'


class Order(models.Model):

	orderDelivery = models.ForeignKey('ParcelDelivery', on_delete=models.CASCADE, verbose_name="Orderdelivery", help_text='''The delivery of the parcel related to this order or order item.''', related_name="order_orderdelivery")
	discountCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Discountcode", help_text='''Code used to redeem a discount.''', related_name="order_discountcode")
	acceptedOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Acceptedoffer", help_text='''The offer(s) -- e.g., product, quantity and price combinations -- included in the order.''', related_name="order_acceptedoffer")
	orderDate = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Orderdate", help_text='''Date order was placed.''', related_name="order_orderdate")
	discountCurrency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Discountcurrency", help_text='''The currency (in 3-letter ISO 4217 format) of the discount.''', related_name="order_discountcurrency")
	paymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Paymentmethod", help_text='''The name of the credit card or other method of payment for the order.''', related_name="order_paymentmethod")
	orderNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Ordernumber", help_text='''The identifier of the transaction.''', related_name="order_ordernumber")
	orderStatus = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, verbose_name="Orderstatus", help_text='''The current status of the order.''', related_name="order_orderstatus")
	paymentUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Paymenturl", help_text='''The URL for sending a payment.''', related_name="order_paymenturl")
	paymentDueDate = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Paymentduedate", help_text='''The date that payment is due. Supersedes paymentDue.''', related_name="order_paymentduedate")
	partOfInvoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, verbose_name="Partofinvoice", help_text='''The order is being paid as part of the referenced Invoice.''', related_name="order_partofinvoice")
	confirmationNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Confirmationnumber", help_text='''A number that confirms the given order or payment has been received.''', related_name="order_confirmationnumber")
	billingAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Billingaddress", help_text='''The billing address for the order.''', related_name="order_billingaddress")
	isGift = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Isgift", help_text='''Was the offer accepted as a gift for someone other than the buyer.''', related_name="order_isgift")
	paymentMethodId = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Paymentmethodid", help_text='''An identifier for the method of payment used (e.g. the last 4 digits of the credit card).''', related_name="order_paymentmethodid")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="order_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Order'


class OrderItem(models.Model):

	orderDelivery = models.ForeignKey('ParcelDelivery', on_delete=models.CASCADE, verbose_name="Orderdelivery", help_text='''The delivery of the parcel related to this order or order item.''', related_name="orderitem_orderdelivery")
	orderItemNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Orderitemnumber", help_text='''The identifier of the order item.''', related_name="orderitem_orderitemnumber")
	orderQuantity = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Orderquantity", help_text='''The number of the item ordered. If the property is not set, assume the quantity is one.''', related_name="orderitem_orderquantity")
	orderItemStatus = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, verbose_name="Orderitemstatus", help_text='''The current status of the order item.''', related_name="orderitem_orderitemstatus")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="orderitem_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Orderitem'
		verbose_name_plural = 'Orderitem'


class ParcelDelivery(models.Model):

	partOfOrder = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name="Partoforder", help_text='''The overall order the items in this delivery were included in.''', related_name="parceldelivery_partoforder")
	expectedArrivalFrom = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Expectedarrivalfrom", help_text='''The earliest date the package may arrive.''', related_name="parceldelivery_expectedarrivalfrom")
	deliveryStatus = models.ForeignKey('DeliveryEvent', on_delete=models.CASCADE, verbose_name="Deliverystatus", help_text='''New entry added as the package passes through each leg of its journey (from shipment to final delivery).''', related_name="parceldelivery_deliverystatus")
	originAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Originaddress", help_text='''Shipper's address.''', related_name="parceldelivery_originaddress")
	trackingUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Trackingurl", help_text='''Tracking url for the parcel delivery.''', related_name="parceldelivery_trackingurl")
	deliveryAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Deliveryaddress", help_text='''Destination address.''', related_name="parceldelivery_deliveryaddress")
	hasDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Hasdeliverymethod", help_text='''Method used for delivery or shipping.''', related_name="parceldelivery_hasdeliverymethod")
	itemShipped = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Itemshipped", help_text='''Item(s) being shipped.''', related_name="parceldelivery_itemshipped")
	trackingNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Trackingnumber", help_text='''Shipper tracking number.''', related_name="parceldelivery_trackingnumber")
	expectedArrivalUntil = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Expectedarrivaluntil", help_text='''The latest date the package may arrive.''', related_name="parceldelivery_expectedarrivaluntil")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="parceldelivery_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Parceldelivery'
		verbose_name_plural = 'Parceldelivery'


class Permit(models.Model):

	validUntil = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Validuntil", help_text='''The date when the item is no longer valid.''', related_name="permit_validuntil")
	issuedThrough = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Issuedthrough", help_text='''The service through with the permit was granted.''', related_name="permit_issuedthrough")
	permitAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Permitaudience", help_text='''The target audience for this permit.''', related_name="permit_permitaudience")
	validFrom = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", help_text='''The date when the item becomes valid.''', related_name="permit_validfrom")
	validIn = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Validin", help_text='''The geographic area where the permit is valid.''', related_name="permit_validin")
	issuedBy = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Issuedby", help_text='''The organization issuing the ticket or permit.''', related_name="permit_issuedby")
	validFor = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Validfor", help_text='''The time validity of the permit.''', related_name="permit_validfor")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="permit_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Permit'
		verbose_name_plural = 'Permit'


class ProgramMembership(models.Model):

	hostingOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Hostingorganization", help_text='''The organization (airline, travelers' club, etc.) the membership is made with.''', related_name="programmembership_hostingorganization")
	programName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Programname", help_text='''The program providing the membership.''', related_name="programmembership_programname")
	membershipNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Membershipnumber", help_text='''A unique identifier for the membership.''', related_name="programmembership_membershipnumber")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="programmembership_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Programmembership'
		verbose_name_plural = 'Programmembership'


class Property(models.Model):

	inverseOf = models.ForeignKey('Property', on_delete=models.CASCADE, verbose_name="Inverseof", help_text='''Relates a property to a property that is its inverse. Inverse properties relate the same pairs of items to each other, but in reversed direction. For example, the 'alumni' and 'alumniOf' properties are inverseOf each other. Some properties don't have explicit inverses; in these situations RDFa and JSON-LD syntax for reverse properties can be used.''', related_name="property_inverseof")
	rangeIncludes = models.ForeignKey('Class', on_delete=models.CASCADE, verbose_name="Rangeincludes", help_text='''Relates a property to a class that constitutes (one of) the expected type(s) for values of the property.''', related_name="property_rangeincludes")
	domainIncludes = models.ForeignKey('Class', on_delete=models.CASCADE, verbose_name="Domainincludes", help_text='''Relates a property to a class that is (one of) the type(s) the property is expected to be used on.''', related_name="property_domainincludes")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="property_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Property'
		verbose_name_plural = 'Property'


class PropertyValueSpecification(models.Model):

	minValue = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Minvalue", help_text='''The lower value of some characteristic or property.''', related_name="propertyvaluespecification_minvalue")
	valueRequired = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Valuerequired", help_text='''Whether the property must be filled in to complete the action. Default is false.''', related_name="propertyvaluespecification_valuerequired")
	valueMinLength = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Valueminlength", help_text='''Specifies the minimum allowed range for number of characters in a literal value.''', related_name="propertyvaluespecification_valueminlength")
	valueMaxLength = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Valuemaxlength", help_text='''Specifies the allowed range for number of characters in a literal value.''', related_name="propertyvaluespecification_valuemaxlength")
	valueName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Valuename", help_text='''Indicates the name of the PropertyValueSpecification to be used in URL templates and form encoding in a manner analogous to HTML's input@name.''', related_name="propertyvaluespecification_valuename")
	stepValue = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Stepvalue", help_text='''The stepValue attribute indicates the granularity that is expected (and required) of the value in a PropertyValueSpecification.''', related_name="propertyvaluespecification_stepvalue")
	readonlyValue = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Readonlyvalue", help_text='''Whether or not a property is mutable. Default is false. Specifying this for a property that also has a value makes it act similar to a "hidden" input in an HTML form.''', related_name="propertyvaluespecification_readonlyvalue")
	multipleValues = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Multiplevalues", help_text='''Whether multiple values are allowed for the property. Default is false.''', related_name="propertyvaluespecification_multiplevalues")
	valuePattern = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Valuepattern", help_text='''Specifies a regular expression for testing literal values according to the HTML spec.''', related_name="propertyvaluespecification_valuepattern")
	maxValue = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Maxvalue", help_text='''The upper value of some characteristic or property.''', related_name="propertyvaluespecification_maxvalue")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="propertyvaluespecification_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Propertyvaluespecification'
		verbose_name_plural = 'Propertyvaluespecification'


class Distance(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="distance_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Distance'
		verbose_name_plural = 'Distance'


class Duration(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="duration_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Duration'
		verbose_name_plural = 'Duration'


class Energy(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="energy_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Energy'
		verbose_name_plural = 'Energy'


class Mass(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="mass_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Mass'
		verbose_name_plural = 'Mass'


class Rating(models.Model):

	ratingValue = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Ratingvalue", help_text='''The rating for the content.''', related_name="rating_ratingvalue")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="rating_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Rating'
		verbose_name_plural = 'Rating'


class AggregateRating(models.Model):

	reviewCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Reviewcount", help_text='''The count of total number of reviews.''', related_name="aggregaterating_reviewcount")
	itemReviewed = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Itemreviewed", help_text='''The item that is being reviewed/rated.''', related_name="aggregaterating_itemreviewed")
	ratingCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Ratingcount", help_text='''The count of total number of ratings.''', related_name="aggregaterating_ratingcount")
	rating = models.ForeignKey('Rating', on_delete=models.CASCADE, verbose_name="Rating", related_name="aggregaterating_rating")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="aggregaterating_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Aggregaterating'
		verbose_name_plural = 'Aggregaterating'


class Reservation(models.Model):

	bookingTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Bookingtime", help_text='''The date and time the reservation was booked.''', related_name="reservation_bookingtime")
	priceCurrency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricecurrency", help_text='''The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.''', related_name="reservation_pricecurrency")
	programMembershipUsed = models.ForeignKey('ProgramMembership', on_delete=models.CASCADE, verbose_name="Programmembershipused", help_text='''Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the reservation.''', related_name="reservation_programmembershipused")
	reservationFor = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Reservationfor", help_text='''The thing -- flight, event, restaurant,etc. being reserved.''', related_name="reservation_reservationfor")
	reservedTicket = models.ForeignKey('Ticket', on_delete=models.CASCADE, verbose_name="Reservedticket", help_text='''A ticket associated with the reservation.''', related_name="reservation_reservedticket")
	reservationId = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Reservationid", help_text='''A unique identifier for the reservation.''', related_name="reservation_reservationid")
	modifiedTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Modifiedtime", help_text='''The date and time the reservation was modified.''', related_name="reservation_modifiedtime")
	reservationStatus = models.ForeignKey('ReservationStatusType', on_delete=models.CASCADE, verbose_name="Reservationstatus", help_text='''The current status of the reservation.''', related_name="reservation_reservationstatus")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="reservation_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Reservation'
		verbose_name_plural = 'Reservation'


class FlightReservation(models.Model):

	boardingGroup = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Boardinggroup", help_text='''The airline-specific indicator of boarding order / preference.''', related_name="flightreservation_boardinggroup")
	securityScreening = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Securityscreening", help_text='''The type of security screening the passenger is subject to.''', related_name="flightreservation_securityscreening")
	passengerSequenceNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Passengersequencenumber", help_text='''The passenger's sequence number as assigned by the airline.''', related_name="flightreservation_passengersequencenumber")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", related_name="flightreservation_reservation")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="flightreservation_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Flightreservation'
		verbose_name_plural = 'Flightreservation'


class FoodEstablishmentReservation(models.Model):

	startTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Starttime", help_text='''The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from *January* to December.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.''', related_name="foodestablishmentreservation_starttime")
	endTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Endtime", help_text='''The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to *December*.Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.''', related_name="foodestablishmentreservation_endtime")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", related_name="foodestablishmentreservation_reservation")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="foodestablishmentreservation_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Foodestablishmentreservation'
		verbose_name_plural = 'Foodestablishmentreservation'


class LodgingReservation(models.Model):

	checkoutTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Checkouttime", help_text='''The latest someone may check out of a lodging establishment.''', related_name="lodgingreservation_checkouttime")
	lodgingUnitDescription = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Lodgingunitdescription", help_text='''A full description of the lodging unit.''', related_name="lodgingreservation_lodgingunitdescription")
	checkinTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Checkintime", help_text='''The earliest someone may check into a lodging establishment.''', related_name="lodgingreservation_checkintime")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", related_name="lodgingreservation_reservation")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="lodgingreservation_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Lodgingreservation'
		verbose_name_plural = 'Lodgingreservation'


class RentalCarReservation(models.Model):

	pickupLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Pickuplocation", help_text='''Where a taxi will pick up a passenger or a rental car can be picked up.''', related_name="rentalcarreservation_pickuplocation")
	dropoffTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Dropofftime", help_text='''When a rental car can be dropped off.''', related_name="rentalcarreservation_dropofftime")
	pickupTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Pickuptime", help_text='''When a taxi will pickup a passenger or a rental car can be picked up.''', related_name="rentalcarreservation_pickuptime")
	dropoffLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Dropofflocation", help_text='''Where a rental car can be dropped off.''', related_name="rentalcarreservation_dropofflocation")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", related_name="rentalcarreservation_reservation")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="rentalcarreservation_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Rentalcarreservation'
		verbose_name_plural = 'Rentalcarreservation'


class ReservationPackage(models.Model):

	subReservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Subreservation", help_text='''The individual reservations included in the package. Typically a repeated property.''', related_name="reservationpackage_subreservation")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", related_name="reservationpackage_reservation")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="reservationpackage_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Reservationpackage'
		verbose_name_plural = 'Reservationpackage'


class TaxiReservation(models.Model):

	pickupLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Pickuplocation", help_text='''Where a taxi will pick up a passenger or a rental car can be picked up.''', related_name="taxireservation_pickuplocation")
	pickupTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Pickuptime", help_text='''When a taxi will pickup a passenger or a rental car can be picked up.''', related_name="taxireservation_pickuptime")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", related_name="taxireservation_reservation")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="taxireservation_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Taxireservation'
		verbose_name_plural = 'Taxireservation'


class Role(models.Model):

	startDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", help_text='''The start date and time of the item (in ISO 8601 date format).''', related_name="role_startdate")
	endDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", help_text='''The end date and time of the item (in ISO 8601 date format).''', related_name="role_enddate")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="role_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Role'
		verbose_name_plural = 'Role'


class OrganizationRole(models.Model):

	numberedPosition = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Numberedposition", help_text='''A number associated with a role in an organization, for example, the number on an athlete's jersey.''', related_name="organizationrole_numberedposition")
	role = models.ForeignKey('Role', on_delete=models.CASCADE, verbose_name="Role", related_name="organizationrole_role")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="organizationrole_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Organizationrole'
		verbose_name_plural = 'Organizationrole'


class EmployeeRole(models.Model):

	salaryCurrency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Salarycurrency", help_text='''The currency (coded using ISO 4217, http://en.wikipedia.org/wiki/ISO_4217 ) used for the main salary information in this job posting or for this employee.''', related_name="employeerole_salarycurrency")
	role = models.ForeignKey('Role', on_delete=models.CASCADE, verbose_name="Role", related_name="employeerole_role")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="employeerole_thing")
	organizationRole = models.ForeignKey('OrganizationRole', on_delete=models.CASCADE, verbose_name="OrganizationRole", related_name="employeerole_organizationrole")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Employeerole'
		verbose_name_plural = 'Employeerole'


class PerformanceRole(models.Model):

	characterName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Charactername", help_text='''The name of a character played in some acting or performing role, i.e. in a PerformanceRole.''', related_name="performancerole_charactername")
	role = models.ForeignKey('Role', on_delete=models.CASCADE, verbose_name="Role", related_name="performancerole_role")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="performancerole_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Performancerole'
		verbose_name_plural = 'Performancerole'


class Seat(models.Model):

	seatNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Seatnumber", help_text='''The location of the reserved seat (e.g., 27).''', related_name="seat_seatnumber")
	seatSection = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Seatsection", help_text='''The section location of the reserved seat (e.g. Orchestra).''', related_name="seat_seatsection")
	seatRow = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Seatrow", help_text='''The row location of the reserved seat (e.g., B).''', related_name="seat_seatrow")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="seat_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Seat'
		verbose_name_plural = 'Seat'


class Service(models.Model):

	hasOfferCatalog = models.ForeignKey('OfferCatalog', on_delete=models.CASCADE, verbose_name="Hasoffercatalog", help_text='''Indicates an OfferCatalog listing for this Organization, Person, or Service.''', related_name="service_hasoffercatalog")
	offers = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", help_text='''An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="service_offers")
	aggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="service_aggregaterating")
	award = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", help_text='''An award won by or for this item. Supersedes awards.''', related_name="service_award")
	hoursAvailable = models.ForeignKey('OpeningHoursSpecification', on_delete=models.CASCADE, verbose_name="Hoursavailable", help_text='''The hours during which this service or contact is available.''', related_name="service_hoursavailable")
	review = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", help_text='''A review of the item. Supersedes reviews.''', related_name="service_review")
	serviceType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Servicetype", help_text='''The type of service being offered, e.g. veterans' benefits, emergency relief, etc.''', related_name="service_servicetype")
	providerMobility = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Providermobility", help_text='''Indicates the mobility of a provided service (e.g. 'static', 'dynamic').''', related_name="service_providermobility")
	serviceOutput = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Serviceoutput", help_text='''The tangible thing generated by the service, e.g. a passport, permit, etc. Supersedes produces.''', related_name="service_serviceoutput")
	availableChannel = models.ForeignKey('ServiceChannel', on_delete=models.CASCADE, verbose_name="Availablechannel", help_text='''A means of accessing the service (e.g. a phone bank, a web site, a location, etc.).''', related_name="service_availablechannel")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="service_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Service'
		verbose_name_plural = 'Service'


class BroadcastService(models.Model):

	videoFormat = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Videoformat", help_text='''The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).''', related_name="broadcastservice_videoformat")
	broadcastAffiliateOf = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Broadcastaffiliateof", help_text='''The media network(s) whose content is broadcast on this station.''', related_name="broadcastservice_broadcastaffiliateof")
	broadcaster = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Broadcaster", help_text='''The organization owning or operating the broadcast service.''', related_name="broadcastservice_broadcaster")
	broadcastTimezone = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Broadcasttimezone", help_text='''The timezone in ISO 8601 format for which the service bases its broadcasts.''', related_name="broadcastservice_broadcasttimezone")
	parentService = models.ForeignKey('BroadcastService', on_delete=models.CASCADE, verbose_name="Parentservice", help_text='''A broadcast service to which the broadcast service may belong to such as regional variations of a national channel.''', related_name="broadcastservice_parentservice")
	broadcastDisplayName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Broadcastdisplayname", help_text='''The name displayed in the channel guide. For many US affiliates, it is the network name.''', related_name="broadcastservice_broadcastdisplayname")
	service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Service", related_name="broadcastservice_service")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="broadcastservice_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Broadcastservice'
		verbose_name_plural = 'Broadcastservice'


class CableOrSatelliteService(models.Model):

	service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Service", related_name="cableorsatelliteservice_service")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="cableorsatelliteservice_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Cableorsatelliteservice'
		verbose_name_plural = 'Cableorsatelliteservice'


class GovernmentService(models.Model):

	serviceOperator = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Serviceoperator", help_text='''The operating organization, if different from the provider. This enables the representation of services that are provided by an organization, but operated by another organization like a subcontractor.''', related_name="governmentservice_serviceoperator")
	service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Service", related_name="governmentservice_service")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="governmentservice_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Governmentservice'
		verbose_name_plural = 'Governmentservice'


class ServiceChannel(models.Model):

	providesService = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Providesservice", help_text='''The service provided by this channel.''', related_name="servicechannel_providesservice")
	servicePostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Servicepostaladdress", help_text='''The address for accessing the service by mail.''', related_name="servicechannel_servicepostaladdress")
	processingTime = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Processingtime", help_text='''Estimated processing time for the service using this channel.''', related_name="servicechannel_processingtime")
	availableLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Availablelanguage", help_text='''A language someone may use with the item.''', related_name="servicechannel_availablelanguage")
	serviceLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Servicelocation", help_text='''The location (e.g. civic structure, local business, etc.) where a person can go to access the service.''', related_name="servicechannel_servicelocation")
	serviceSmsNumber = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Servicesmsnumber", help_text='''The number to access the service by text message.''', related_name="servicechannel_servicesmsnumber")
	serviceUrl = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Serviceurl", help_text='''The website to access the service.''', related_name="servicechannel_serviceurl")
	servicePhone = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Servicephone", help_text='''The phone number to use to access the service.''', related_name="servicechannel_servicephone")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="servicechannel_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Servicechannel'
		verbose_name_plural = 'Servicechannel'


class StructuredValue(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="structuredvalue_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Structuredvalue'
		verbose_name_plural = 'Structuredvalue'


class ContactPoint(models.Model):

	email = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Email", help_text='''Email address.''', related_name="contactpoint_email")
	telephone = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Telephone", help_text='''The telephone number.''', related_name="contactpoint_telephone")
	faxNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Faxnumber", help_text='''The fax number.''', related_name="contactpoint_faxnumber")
	hoursAvailable = models.ForeignKey('OpeningHoursSpecification', on_delete=models.CASCADE, verbose_name="Hoursavailable", help_text='''The hours during which this service or contact is available.''', related_name="contactpoint_hoursavailable")
	availableLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Availablelanguage", help_text='''A language someone may use with the item.''', related_name="contactpoint_availablelanguage")
	contactOption = models.ForeignKey('ContactPointOption', on_delete=models.CASCADE, verbose_name="Contactoption", help_text='''An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).''', related_name="contactpoint_contactoption")
	contactType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Contacttype", help_text='''A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.''', related_name="contactpoint_contacttype")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="contactpoint_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Contactpoint'
		verbose_name_plural = 'Contactpoint'


class PostalAddress(models.Model):

	postalCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Postalcode", help_text='''The postal code. For example, 94043.''', related_name="postaladdress_postalcode")
	postOfficeBoxNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Postofficeboxnumber", help_text='''The post office box number for PO box addresses.''', related_name="postaladdress_postofficeboxnumber")
	streetAddress = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Streetaddress", help_text='''The street address. For example, 1600 Amphitheatre Pkwy.''', related_name="postaladdress_streetaddress")
	addressRegion = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Addressregion", help_text='''The region. For example, CA.''', related_name="postaladdress_addressregion")
	addressLocality = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Addresslocality", help_text='''The locality. For example, Mountain View.''', related_name="postaladdress_addresslocality")
	contactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="ContactPoint", related_name="postaladdress_contactpoint")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="postaladdress_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Postaladdress'
		verbose_name_plural = 'Postaladdress'


class DatedMoneySpecification(models.Model):

	amount = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Amount", help_text='''The amount of money.''', related_name="datedmoneyspecification_amount")
	currency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Currency", help_text='''The currency in which the monetary amount is expressed (in 3-letter ISO 4217 format).''', related_name="datedmoneyspecification_currency")
	startDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", help_text='''The start date and time of the item (in ISO 8601 date format).''', related_name="datedmoneyspecification_startdate")
	endDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", help_text='''The end date and time of the item (in ISO 8601 date format).''', related_name="datedmoneyspecification_enddate")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="datedmoneyspecification_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Datedmoneyspecification'
		verbose_name_plural = 'Datedmoneyspecification'


class EngineSpecification(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="enginespecification_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Enginespecification'
		verbose_name_plural = 'Enginespecification'


class GeoCoordinates(models.Model):

	postalCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Postalcode", help_text='''The postal code. For example, 94043.''', related_name="geocoordinates_postalcode")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="geocoordinates_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Geocoordinates'
		verbose_name_plural = 'Geocoordinates'


class GeoShape(models.Model):

	postalCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Postalcode", help_text='''The postal code. For example, 94043.''', related_name="geoshape_postalcode")
	line = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Line", help_text='''A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space.''', related_name="geoshape_line")
	box = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Box", help_text='''A box is the area enclosed by the rectangle formed by two points. The first point is the lower corner, the second point is the upper corner. A box is expressed as two points separated by a space character.''', related_name="geoshape_box")
	circle = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Circle", help_text='''A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters.''', related_name="geoshape_circle")
	polygon = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Polygon", help_text='''A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more space delimited points where the first and final points are identical.''', related_name="geoshape_polygon")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="geoshape_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Geoshape'
		verbose_name_plural = 'Geoshape'


class GeoCircle(models.Model):

	geoMidpoint = models.ForeignKey('GeoCoordinates', on_delete=models.CASCADE, verbose_name="Geomidpoint", help_text='''Indicates the GeoCoordinates at the centre of a GeoShape e.g. GeoCircle.''', related_name="geocircle_geomidpoint")
	geoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="GeoShape", related_name="geocircle_geoshape")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="geocircle_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Geocircle'
		verbose_name_plural = 'Geocircle'


class InteractionCounter(models.Model):

	userInteractionCount = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Userinteractioncount", help_text='''The number of interactions for the CreativeWork using the WebSite or SoftwareApplication.''', related_name="interactioncounter_userinteractioncount")
	interactionType = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Interactiontype", help_text='''The Action representing the type of interaction. For up votes, +1s, etc. use LikeAction. For down votes use DislikeAction. Otherwise, use the most specific Action.''', related_name="interactioncounter_interactiontype")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="interactioncounter_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Interactioncounter'
		verbose_name_plural = 'Interactioncounter'


class NutritionInformation(models.Model):

	fiberContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Fibercontent", help_text='''The number of grams of fiber.''', related_name="nutritioninformation_fibercontent")
	cholesterolContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Cholesterolcontent", help_text='''The number of milligrams of cholesterol.''', related_name="nutritioninformation_cholesterolcontent")
	transFatContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Transfatcontent", help_text='''The number of grams of trans fat.''', related_name="nutritioninformation_transfatcontent")
	carbohydrateContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Carbohydratecontent", help_text='''The number of grams of carbohydrates.''', related_name="nutritioninformation_carbohydratecontent")
	unsaturatedFatContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Unsaturatedfatcontent", help_text='''The number of grams of unsaturated fat.''', related_name="nutritioninformation_unsaturatedfatcontent")
	servingSize = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Servingsize", help_text='''The serving size, in terms of the number of volume or mass.''', related_name="nutritioninformation_servingsize")
	calories = models.ForeignKey('Energy', on_delete=models.CASCADE, verbose_name="Calories", help_text='''The number of calories.''', related_name="nutritioninformation_calories")
	sodiumContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Sodiumcontent", help_text='''The number of milligrams of sodium.''', related_name="nutritioninformation_sodiumcontent")
	proteinContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Proteincontent", help_text='''The number of grams of protein.''', related_name="nutritioninformation_proteincontent")
	sugarContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Sugarcontent", help_text='''The number of grams of sugar.''', related_name="nutritioninformation_sugarcontent")
	fatContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Fatcontent", help_text='''The number of grams of fat.''', related_name="nutritioninformation_fatcontent")
	saturatedFatContent = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Saturatedfatcontent", help_text='''The number of grams of saturated fat.''', related_name="nutritioninformation_saturatedfatcontent")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="nutritioninformation_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Nutritioninformation'
		verbose_name_plural = 'Nutritioninformation'


class OpeningHoursSpecification(models.Model):

	dayOfWeek = models.ForeignKey('DayOfWeek', on_delete=models.CASCADE, verbose_name="Dayofweek", help_text='''The day of the week for which these opening hours are valid.''', related_name="openinghoursspecification_dayofweek")
	closes = models.ForeignKey('Time', on_delete=models.CASCADE, verbose_name="Closes", help_text='''The closing hour of the place or service on the given day(s) of the week.''', related_name="openinghoursspecification_closes")
	validFrom = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", help_text='''The date when the item becomes valid.''', related_name="openinghoursspecification_validfrom")
	validThrough = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", help_text='''The end of the validity of offer, price specification, or opening hours data.''', related_name="openinghoursspecification_validthrough")
	opens = models.ForeignKey('Time', on_delete=models.CASCADE, verbose_name="Opens", help_text='''The opening hour of the place or service on the given day(s) of the week.''', related_name="openinghoursspecification_opens")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="openinghoursspecification_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Openinghoursspecification'
		verbose_name_plural = 'Openinghoursspecification'


class OwnershipInfo(models.Model):

	typeOfGood = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Typeofgood", help_text='''The product that this structured value is referring to.''', related_name="ownershipinfo_typeofgood")
	ownedFrom = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Ownedfrom", help_text='''The date and time of obtaining the product.''', related_name="ownershipinfo_ownedfrom")
	ownedThrough = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Ownedthrough", help_text='''The date and time of giving up ownership on the product.''', related_name="ownershipinfo_ownedthrough")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="ownershipinfo_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Ownershipinfo'
		verbose_name_plural = 'Ownershipinfo'


class PriceSpecification(models.Model):

	valueAddedTaxIncluded = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Valueaddedtaxincluded", help_text='''Specifies whether the applicable value-added tax (VAT) is included in the price specification or not.''', related_name="pricespecification_valueaddedtaxincluded")
	eligibleTransactionVolume = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Eligibletransactionvolume", help_text='''The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.''', related_name="pricespecification_eligibletransactionvolume")
	priceCurrency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricecurrency", help_text='''The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.''', related_name="pricespecification_pricecurrency")
	eligibleQuantity = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligiblequantity", help_text='''The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.''', related_name="pricespecification_eligiblequantity")
	maxPrice = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Maxprice", help_text='''The highest price if the price is a range.''', related_name="pricespecification_maxprice")
	validFrom = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", help_text='''The date when the item becomes valid.''', related_name="pricespecification_validfrom")
	minPrice = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Minprice", help_text='''The lowest price if the price is a range.''', related_name="pricespecification_minprice")
	validThrough = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", help_text='''The end of the validity of offer, price specification, or opening hours data.''', related_name="pricespecification_validthrough")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="pricespecification_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Pricespecification'
		verbose_name_plural = 'Pricespecification'


class DeliveryChargeSpecification(models.Model):

	appliesToDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Appliestodeliverymethod", help_text='''The delivery method(s) to which the delivery charge or payment charge specification applies.''', related_name="deliverychargespecification_appliestodeliverymethod")
	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="PriceSpecification", related_name="deliverychargespecification_pricespecification")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="deliverychargespecification_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Deliverychargespecification'
		verbose_name_plural = 'Deliverychargespecification'


class PaymentChargeSpecification(models.Model):

	appliesToDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Appliestodeliverymethod", help_text='''The delivery method(s) to which the delivery charge or payment charge specification applies.''', related_name="paymentchargespecification_appliestodeliverymethod")
	appliesToPaymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Appliestopaymentmethod", help_text='''The payment method(s) to which the payment charge specification applies.''', related_name="paymentchargespecification_appliestopaymentmethod")
	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="PriceSpecification", related_name="paymentchargespecification_pricespecification")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="paymentchargespecification_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Paymentchargespecification'
		verbose_name_plural = 'Paymentchargespecification'


class UnitPriceSpecification(models.Model):

	billingIncrement = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Billingincrement", help_text='''This property specifies the minimal quantity and rounding increment that will be the basis for the billing. The unit of measurement is specified by the unitCode property.''', related_name="unitpricespecification_billingincrement")
	unitText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unittext", help_text='''A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code forunitCode.''', related_name="unitpricespecification_unittext")
	priceType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricetype", help_text='''A short text or acronym indicating multiple price specifications for the same offer, e.g. SRP for the suggested retail price or INVOICE for the invoice price, mostly used in the car industry.''', related_name="unitpricespecification_pricetype")
	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="PriceSpecification", related_name="unitpricespecification_pricespecification")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="unitpricespecification_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Unitpricespecification'
		verbose_name_plural = 'Unitpricespecification'


class PropertyValue(models.Model):

	minValue = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Minvalue", help_text='''The lower value of some characteristic or property.''', related_name="propertyvalue_minvalue")
	maxValue = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Maxvalue", help_text='''The upper value of some characteristic or property.''', related_name="propertyvalue_maxvalue")
	unitText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unittext", help_text='''A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code forunitCode.''', related_name="propertyvalue_unittext")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="propertyvalue_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Propertyvalue'
		verbose_name_plural = 'Propertyvalue'


class QuantitativeValue(models.Model):

	minValue = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Minvalue", help_text='''The lower value of some characteristic or property.''', related_name="quantitativevalue_minvalue")
	maxValue = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Maxvalue", help_text='''The upper value of some characteristic or property.''', related_name="quantitativevalue_maxvalue")
	additionalProperty = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Additionalproperty", help_text='''A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.''', related_name="quantitativevalue_additionalproperty")
	unitText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unittext", help_text='''A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code forunitCode.''', related_name="quantitativevalue_unittext")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="quantitativevalue_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Quantitativevalue'
		verbose_name_plural = 'Quantitativevalue'


class TypeAndQuantityNode(models.Model):

	typeOfGood = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Typeofgood", help_text='''The product that this structured value is referring to.''', related_name="typeandquantitynode_typeofgood")
	businessFunction = models.ForeignKey('BusinessFunction', on_delete=models.CASCADE, verbose_name="Businessfunction", help_text='''The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.''', related_name="typeandquantitynode_businessfunction")
	unitText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unittext", help_text='''A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code forunitCode.''', related_name="typeandquantitynode_unittext")
	amountOfThisGood = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Amountofthisgood", help_text='''The quantity of the goods included in the offer.''', related_name="typeandquantitynode_amountofthisgood")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="typeandquantitynode_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Typeandquantitynode'
		verbose_name_plural = 'Typeandquantitynode'


class WarrantyPromise(models.Model):

	durationOfWarranty = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Durationofwarranty", help_text='''The duration of the warranty promise. Common unitCode values are ANN for year, MON for months, or DAY for days.''', related_name="warrantypromise_durationofwarranty")
	warrantyScope = models.ForeignKey('WarrantyScope', on_delete=models.CASCADE, verbose_name="Warrantyscope", help_text='''The scope of the warranty promise.''', related_name="warrantypromise_warrantyscope")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="warrantypromise_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Warrantypromise'
		verbose_name_plural = 'Warrantypromise'


class Ticket(models.Model):

	dateIssued = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Dateissued", help_text='''The date the ticket was issued.''', related_name="ticket_dateissued")
	priceCurrency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricecurrency", help_text='''The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.''', related_name="ticket_pricecurrency")
	ticketNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Ticketnumber", help_text='''The unique identifier for the ticket.''', related_name="ticket_ticketnumber")
	ticketedSeat = models.ForeignKey('Seat', on_delete=models.CASCADE, verbose_name="Ticketedseat", help_text='''The seat associated with the ticket.''', related_name="ticket_ticketedseat")
	issuedBy = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Issuedby", help_text='''The organization issuing the ticket or permit.''', related_name="ticket_issuedby")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="ticket_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Ticket'
		verbose_name_plural = 'Ticket'


class TrainTrip(models.Model):

	departurePlatform = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Departureplatform", help_text='''The platform from which the train departs.''', related_name="traintrip_departureplatform")
	trainName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Trainname", help_text='''The name of the train (e.g. The Orient Express).''', related_name="traintrip_trainname")
	trainNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Trainnumber", help_text='''The unique identifier for the train.''', related_name="traintrip_trainnumber")
	arrivalTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Arrivaltime", help_text='''The expected arrival time.''', related_name="traintrip_arrivaltime")
	arrivalPlatform = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Arrivalplatform", help_text='''The platform where the train arrives.''', related_name="traintrip_arrivalplatform")
	departureTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Departuretime", help_text='''The expected departure time.''', related_name="traintrip_departuretime")
	departureStation = models.ForeignKey('TrainStation', on_delete=models.CASCADE, verbose_name="Departurestation", help_text='''The station from which the train departs.''', related_name="traintrip_departurestation")
	arrivalStation = models.ForeignKey('TrainStation', on_delete=models.CASCADE, verbose_name="Arrivalstation", help_text='''The station where the train trip ends.''', related_name="traintrip_arrivalstation")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="traintrip_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Traintrip'
		verbose_name_plural = 'Traintrip'


class MedicalEntity(models.Model):

	guideline = models.ForeignKey('MedicalGuideline', on_delete=models.CASCADE, verbose_name="Guideline", help_text='''A medical guideline related to this entity.''', related_name="medicalentity_guideline")
	medicineSystem = models.ForeignKey('MedicineSystem', on_delete=models.CASCADE, verbose_name="Medicinesystem", help_text='''The system of medicine that includes this MedicalEntity, for example 'evidence-based', 'homeopathic', 'chiropractic', etc.''', related_name="medicalentity_medicinesystem")
	code = models.ForeignKey('MedicalCode', on_delete=models.CASCADE, verbose_name="Code", help_text='''A medical code for the entity, taken from a controlled vocabulary or ontology such as ICD-9, DiseasesDB, MeSH, SNOMED-CT, RxNorm, etc.''', related_name="medicalentity_code")
	relevantSpecialty = models.ForeignKey('MedicalSpecialty', on_delete=models.CASCADE, verbose_name="Relevantspecialty", help_text='''If applicable, a medical specialty in which this entity is relevant.''', related_name="medicalentity_relevantspecialty")
	study = models.ForeignKey('MedicalStudy', on_delete=models.CASCADE, verbose_name="Study", help_text='''A medical study or trial related to this entity.''', related_name="medicalentity_study")
	recognizingAuthority = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recognizingauthority", help_text='''If applicable, the organization that officially recognizes this entity as part of its endorsed system of medicine.''', related_name="medicalentity_recognizingauthority")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalentity_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalentity'
		verbose_name_plural = 'Medicalentity'


class AnatomicalStructure(models.Model):

	connectedTo = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Connectedto", help_text='''Other anatomical structures to which this structure is connected.''', related_name="anatomicalstructure_connectedto")
	relatedCondition = models.ForeignKey('MedicalCondition', on_delete=models.CASCADE, verbose_name="Relatedcondition", help_text='''A medical condition associated with this anatomy.''', related_name="anatomicalstructure_relatedcondition")
	diagram = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Diagram", help_text='''An image containing a diagram that illustrates the structure and/or its component substructures and/or connections with other structures.''', related_name="anatomicalstructure_diagram")
	bodyLocation = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Bodylocation", help_text='''Location in the body of the anatomical structure.''', related_name="anatomicalstructure_bodylocation")
	subStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Substructure", help_text='''Component (sub-)structure(s) that comprise this anatomical structure.''', related_name="anatomicalstructure_substructure")
	relatedTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="Relatedtherapy", help_text='''A medical therapy related to this anatomy.''', related_name="anatomicalstructure_relatedtherapy")
	associatedPathophysiology = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Associatedpathophysiology", help_text='''If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.''', related_name="anatomicalstructure_associatedpathophysiology")
	partOfSystem = models.ForeignKey('AnatomicalSystem', on_delete=models.CASCADE, verbose_name="Partofsystem", help_text='''The anatomical or organ system that this structure is part of.''', related_name="anatomicalstructure_partofsystem")
	function = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Function", help_text='''Function of the anatomical structure.''', related_name="anatomicalstructure_function")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="anatomicalstructure_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="anatomicalstructure_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Anatomicalstructure'
		verbose_name_plural = 'Anatomicalstructure'


class BrainStructure(models.Model):

	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="brainstructure_medicalentity")
	anatomicalStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="AnatomicalStructure", related_name="brainstructure_anatomicalstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="brainstructure_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Brainstructure'
		verbose_name_plural = 'Brainstructure'


class Joint(models.Model):

	structuralClass = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Structuralclass", help_text='''The name given to how bone physically connects to each other.''', related_name="joint_structuralclass")
	functionalClass = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Functionalclass", help_text='''The degree of mobility the joint allows.''', related_name="joint_functionalclass")
	biomechnicalClass = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Biomechnicalclass", help_text='''The biomechanical properties of the bone.''', related_name="joint_biomechnicalclass")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="joint_medicalentity")
	anatomicalStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="AnatomicalStructure", related_name="joint_anatomicalstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="joint_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Joint'
		verbose_name_plural = 'Joint'


class Muscle(models.Model):

	insertion = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Insertion", help_text='''The place of attachment of a muscle, or what the muscle moves.''', related_name="muscle_insertion")
	muscleAction = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Muscleaction", help_text='''The movement the muscle generates. Supersedes action.''', related_name="muscle_muscleaction")
	bloodSupply = models.ForeignKey('Vessel', on_delete=models.CASCADE, verbose_name="Bloodsupply", help_text='''The blood vessel that carries blood from the heart to the muscle.''', related_name="muscle_bloodsupply")
	antagonist = models.ForeignKey('Muscle', on_delete=models.CASCADE, verbose_name="Antagonist", help_text='''The muscle whose action counteracts the specified muscle.''', related_name="muscle_antagonist")
	nerve = models.ForeignKey('Nerve', on_delete=models.CASCADE, verbose_name="Nerve", help_text='''The underlying innervation associated with the muscle.''', related_name="muscle_nerve")
	origin = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Origin", help_text='''The place or point where a muscle arises.''', related_name="muscle_origin")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="muscle_medicalentity")
	anatomicalStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="AnatomicalStructure", related_name="muscle_anatomicalstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="muscle_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Muscle'
		verbose_name_plural = 'Muscle'


class Nerve(models.Model):

	sourcedFrom = models.ForeignKey('BrainStructure', on_delete=models.CASCADE, verbose_name="Sourcedfrom", help_text='''The neurological pathway that originates the neurons.''', related_name="nerve_sourcedfrom")
	nerveMotor = models.ForeignKey('Muscle', on_delete=models.CASCADE, verbose_name="Nervemotor", help_text='''The neurological pathway extension that involves muscle control.''', related_name="nerve_nervemotor")
	branch = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Branch", help_text='''The branches that delineate from the nerve bundle.''', related_name="nerve_branch")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="nerve_medicalentity")
	anatomicalStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="AnatomicalStructure", related_name="nerve_anatomicalstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="nerve_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Nerve'
		verbose_name_plural = 'Nerve'


class Vessel(models.Model):

	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="vessel_medicalentity")
	anatomicalStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="AnatomicalStructure", related_name="vessel_anatomicalstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="vessel_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Vessel'
		verbose_name_plural = 'Vessel'


class Artery(models.Model):

	source = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Source", help_text='''The anatomical or organ system that the artery originates from.''', related_name="artery_source")
	arterialBranch = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Arterialbranch", help_text='''The branches that comprise the arterial structure.''', related_name="artery_arterialbranch")
	supplyTo = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Supplyto", help_text='''The area to which the artery supplies blood.''', related_name="artery_supplyto")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="artery_medicalentity")
	anatomicalStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="AnatomicalStructure", related_name="artery_anatomicalstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="artery_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Artery'
		verbose_name_plural = 'Artery'


class LymphaticVessel(models.Model):

	runsTo = models.ForeignKey('Vessel', on_delete=models.CASCADE, verbose_name="Runsto", help_text='''The vasculature the lymphatic structure runs, or efferents, to.''', related_name="lymphaticvessel_runsto")
	originatesFrom = models.ForeignKey('Vessel', on_delete=models.CASCADE, verbose_name="Originatesfrom", help_text='''The vasculature the lymphatic structure originates, or afferents, from.''', related_name="lymphaticvessel_originatesfrom")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="lymphaticvessel_medicalentity")
	anatomicalStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="AnatomicalStructure", related_name="lymphaticvessel_anatomicalstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="lymphaticvessel_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Lymphaticvessel'
		verbose_name_plural = 'Lymphaticvessel'


class Vein(models.Model):

	drainsTo = models.ForeignKey('Vessel', on_delete=models.CASCADE, verbose_name="Drainsto", help_text='''The vasculature that the vein drains into.''', related_name="vein_drainsto")
	tributary = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Tributary", help_text='''The anatomical or organ system that the vein flows into; a larger structure that the vein connects to.''', related_name="vein_tributary")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="vein_medicalentity")
	anatomicalStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="AnatomicalStructure", related_name="vein_anatomicalstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="vein_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Vein'
		verbose_name_plural = 'Vein'


class AnatomicalSystem(models.Model):

	associatedPathophysiology = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Associatedpathophysiology", help_text='''If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.''', related_name="anatomicalsystem_associatedpathophysiology")
	relatedCondition = models.ForeignKey('MedicalCondition', on_delete=models.CASCADE, verbose_name="Relatedcondition", help_text='''A medical condition associated with this anatomy.''', related_name="anatomicalsystem_relatedcondition")
	relatedStructure = models.ForeignKey('AnatomicalStructure', on_delete=models.CASCADE, verbose_name="Relatedstructure", help_text='''Related anatomical structure(s) that are not part of the system but relate or connect to it, such as vascular bundles associated with an organ system.''', related_name="anatomicalsystem_relatedstructure")
	relatedTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="Relatedtherapy", help_text='''A medical therapy related to this anatomy.''', related_name="anatomicalsystem_relatedtherapy")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="anatomicalsystem_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="anatomicalsystem_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Anatomicalsystem'
		verbose_name_plural = 'Anatomicalsystem'


class MedicalCause(models.Model):

	causeOf = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="Causeof", help_text='''The condition, complication, symptom, sign, etc. caused.''', related_name="medicalcause_causeof")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalcause_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalcause_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalcause'
		verbose_name_plural = 'Medicalcause'


class MedicalCondition(models.Model):

	expectedPrognosis = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Expectedprognosis", help_text='''The likely outcome in either the short term or long term of the medical condition.''', related_name="medicalcondition_expectedprognosis")
	epidemiology = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Epidemiology", help_text='''The characteristics of associated patients, such as age, gender, race etc.''', related_name="medicalcondition_epidemiology")
	differentialDiagnosis = models.ForeignKey('DDxElement', on_delete=models.CASCADE, verbose_name="Differentialdiagnosis", help_text='''One of a set of differential diagnoses for the condition. Specifically, a closely-related or competing diagnosis typically considered later in the cognitive process whereby this medical condition is distinguished from others most likely responsible for a similar collection of signs and symptoms to reach the most parsimonious diagnosis or diagnoses in a patient.''', related_name="medicalcondition_differentialdiagnosis")
	typicalTest = models.ForeignKey('MedicalTest', on_delete=models.CASCADE, verbose_name="Typicaltest", help_text='''A medical test typically performed given this condition.''', related_name="medicalcondition_typicaltest")
	signOrSymptom = models.ForeignKey('MedicalSignOrSymptom', on_delete=models.CASCADE, verbose_name="Signorsymptom", help_text='''A sign or symptom of this condition. Signs are objective or physically observable manifestations of the medical condition while symptoms are the subjective experience of the medical condition.''', related_name="medicalcondition_signorsymptom")
	possibleTreatment = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="Possibletreatment", help_text='''A possible treatment to address this condition, sign or symptom.''', related_name="medicalcondition_possibletreatment")
	stage = models.ForeignKey('MedicalConditionStage', on_delete=models.CASCADE, verbose_name="Stage", help_text='''The stage of the condition, if applicable.''', related_name="medicalcondition_stage")
	naturalProgression = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Naturalprogression", help_text='''The expected progression of the condition if it is not treated and allowed to progress naturally.''', related_name="medicalcondition_naturalprogression")
	secondaryPrevention = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="Secondaryprevention", help_text='''A preventative therapy used to prevent reoccurrence of the medical condition after an initial episode of the condition.''', related_name="medicalcondition_secondaryprevention")
	riskFactor = models.ForeignKey('MedicalRiskFactor', on_delete=models.CASCADE, verbose_name="Riskfactor", help_text='''A modifiable or non-modifiable factor that increases the risk of a patient contracting this condition, e.g. age, coexisting condition.''', related_name="medicalcondition_riskfactor")
	pathophysiology = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pathophysiology", help_text='''Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.''', related_name="medicalcondition_pathophysiology")
	subtype = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Subtype", help_text='''A more specific type of the condition, where applicable, for example 'Type 1 Diabetes', 'Type 2 Diabetes', or 'Gestational Diabetes' for Diabetes.''', related_name="medicalcondition_subtype")
	primaryPrevention = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="Primaryprevention", help_text='''A preventative therapy used to prevent an initial occurrence of the medical condition, such as vaccination.''', related_name="medicalcondition_primaryprevention")
	cause = models.ForeignKey('MedicalCause', on_delete=models.CASCADE, verbose_name="Cause", help_text='''An underlying cause. More specifically, one of the causative agent(s) that are most directly responsible for the pathophysiologic process that eventually results in the occurrence.''', related_name="medicalcondition_cause")
	possibleComplication = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Possiblecomplication", help_text='''A possible unexpected and unfavorable evolution of a medical condition. Complications may include worsening of the signs or symptoms of the disease, extension of the condition to other organ systems, etc.''', related_name="medicalcondition_possiblecomplication")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalcondition_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalcondition_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalcondition'
		verbose_name_plural = 'Medicalcondition'


class InfectiousDisease(models.Model):

	infectiousAgent = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Infectiousagent", help_text='''The actual infectious agent, such as a specific bacterium.''', related_name="infectiousdisease_infectiousagent")
	infectiousAgentClass = models.ForeignKey('InfectiousAgentClass', on_delete=models.CASCADE, verbose_name="Infectiousagentclass", help_text='''The class of infectious agent (bacteria, prion, etc.) that causes the disease.''', related_name="infectiousdisease_infectiousagentclass")
	transmissionMethod = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Transmissionmethod", help_text='''How the disease spreads, either as a route or vector, for example 'direct contact', 'Aedes aegypti', etc.''', related_name="infectiousdisease_transmissionmethod")
	medicalCondition = models.ForeignKey('MedicalCondition', on_delete=models.CASCADE, verbose_name="MedicalCondition", related_name="infectiousdisease_medicalcondition")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="infectiousdisease_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="infectiousdisease_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Infectiousdisease'
		verbose_name_plural = 'Infectiousdisease'


class MedicalContraindication(models.Model):

	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalcontraindication_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalcontraindication_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalcontraindication'
		verbose_name_plural = 'Medicalcontraindication'


class MedicalDevice(models.Model):

	seriousAdverseOutcome = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="Seriousadverseoutcome", help_text='''A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.''', related_name="medicaldevice_seriousadverseoutcome")
	postOp = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Postop", help_text='''A description of the postoperative procedures, care, and/or followups for this device.''', related_name="medicaldevice_postop")
	contraindication = models.ForeignKey('MedicalContraindication', on_delete=models.CASCADE, verbose_name="Contraindication", help_text='''A contraindication for this therapy.''', related_name="medicaldevice_contraindication")
	indication = models.ForeignKey('MedicalIndication', on_delete=models.CASCADE, verbose_name="Indication", help_text='''A factor that indicates use of this therapy for treatment and/or prevention of a condition, symptom, etc. For therapies such as drugs, indications can include both officially-approved indications as well as off-label uses. These can be distinguished by using the ApprovedIndication subtype of MedicalIndication.''', related_name="medicaldevice_indication")
	procedure = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Procedure", help_text='''A description of the procedure involved in setting up, using, and/or installing the device.''', related_name="medicaldevice_procedure")
	adverseOutcome = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="Adverseoutcome", help_text='''A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or is otherwise life-threatening or requires immediate medical attention), tag it as a seriouseAdverseOutcome instead.''', related_name="medicaldevice_adverseoutcome")
	preOp = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Preop", help_text='''A description of the workup, testing, and other preparations required before implanting this device.''', related_name="medicaldevice_preop")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicaldevice_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicaldevice_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicaldevice'
		verbose_name_plural = 'Medicaldevice'


class MedicalGuideline(models.Model):

	guidelineSubject = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="Guidelinesubject", help_text='''The medical conditions, treatments, etc. that are the subject of the guideline.''', related_name="medicalguideline_guidelinesubject")
	evidenceLevel = models.ForeignKey('MedicalEvidenceLevel', on_delete=models.CASCADE, verbose_name="Evidencelevel", help_text='''Strength of evidence of the data used to formulate the guideline (enumerated).''', related_name="medicalguideline_evidencelevel")
	guidelineDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Guidelinedate", help_text='''Date on which this guideline's recommendation was made.''', related_name="medicalguideline_guidelinedate")
	evidenceOrigin = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Evidenceorigin", help_text='''Source of the data used to formulate the guidance, e.g. RCT, consensus opinion, etc.''', related_name="medicalguideline_evidenceorigin")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalguideline_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalguideline_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalguideline'
		verbose_name_plural = 'Medicalguideline'


class MedicalGuidelineRecommendation(models.Model):

	recommendationStrength = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recommendationstrength", help_text='''Strength of the guideline's recommendation (e.g. 'class I').''', related_name="medicalguidelinerecommendation_recommendationstrength")
	medicalGuideline = models.ForeignKey('MedicalGuideline', on_delete=models.CASCADE, verbose_name="MedicalGuideline", related_name="medicalguidelinerecommendation_medicalguideline")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalguidelinerecommendation_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalguidelinerecommendation_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalguidelinerecommendation'
		verbose_name_plural = 'Medicalguidelinerecommendation'


class MedicalIndication(models.Model):

	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalindication_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalindication_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalindication'
		verbose_name_plural = 'Medicalindication'


class DDxElement(models.Model):

	distinguishingSign = models.ForeignKey('MedicalSignOrSymptom', on_delete=models.CASCADE, verbose_name="Distinguishingsign", help_text='''One of a set of signs and symptoms that can be used to distinguish this diagnosis from others in the differential diagnosis.''', related_name="ddxelement_distinguishingsign")
	diagnosis = models.ForeignKey('MedicalCondition', on_delete=models.CASCADE, verbose_name="Diagnosis", help_text='''One or more alternative conditions considered in the differential diagnosis process.''', related_name="ddxelement_diagnosis")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="ddxelement_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="ddxelement_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Ddxelement'
		verbose_name_plural = 'Ddxelement'


class DoseSchedule(models.Model):

	targetPopulation = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Targetpopulation", help_text='''Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'.''', related_name="doseschedule_targetpopulation")
	doseUnit = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Doseunit", help_text='''The unit of the dose, e.g. 'mg'.''', related_name="doseschedule_doseunit")
	doseValue = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Dosevalue", help_text='''The value of the dose, e.g. 500.''', related_name="doseschedule_dosevalue")
	frequency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Frequency", help_text='''How often the dose is taken, e.g. 'daily'.''', related_name="doseschedule_frequency")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="doseschedule_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="doseschedule_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Doseschedule'
		verbose_name_plural = 'Doseschedule'


class MaximumDoseSchedule(models.Model):

	doseSchedule = models.ForeignKey('DoseSchedule', on_delete=models.CASCADE, verbose_name="DoseSchedule", related_name="maximumdoseschedule_doseschedule")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="maximumdoseschedule_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="maximumdoseschedule_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Maximumdoseschedule'
		verbose_name_plural = 'Maximumdoseschedule'


class RecommendedDoseSchedule(models.Model):

	doseSchedule = models.ForeignKey('DoseSchedule', on_delete=models.CASCADE, verbose_name="DoseSchedule", related_name="recommendeddoseschedule_doseschedule")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="recommendeddoseschedule_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="recommendeddoseschedule_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Recommendeddoseschedule'
		verbose_name_plural = 'Recommendeddoseschedule'


class DrugCost(models.Model):

	applicableLocation = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Applicablelocation", help_text='''The location in which the status applies.''', related_name="drugcost_applicablelocation")
	costCategory = models.ForeignKey('DrugCostCategory', on_delete=models.CASCADE, verbose_name="Costcategory", help_text='''The category of cost, such as wholesale, retail, reimbursement cap, etc.''', related_name="drugcost_costcategory")
	costOrigin = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Costorigin", help_text='''Additional details to capture the origin of the cost data. For example, 'Medicare Part B'.''', related_name="drugcost_costorigin")
	costCurrency = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Costcurrency", help_text='''The currency (in 3-letter ISO 4217 format) of the drug cost.''', related_name="drugcost_costcurrency")
	drugUnit = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Drugunit", help_text='''The unit in which the drug is measured, e.g. '5 mg tablet'.''', related_name="drugcost_drugunit")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="drugcost_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="drugcost_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Drugcost'
		verbose_name_plural = 'Drugcost'


class DrugLegalStatus(models.Model):

	applicableLocation = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Applicablelocation", help_text='''The location in which the status applies.''', related_name="druglegalstatus_applicablelocation")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="druglegalstatus_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="druglegalstatus_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Druglegalstatus'
		verbose_name_plural = 'Druglegalstatus'


class DrugStrength(models.Model):

	activeIngredient = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Activeingredient", help_text='''An active ingredient, typically chemical compounds and/or biologic substances.''', related_name="drugstrength_activeingredient")
	availableIn = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Availablein", help_text='''The location in which the strength is available.''', related_name="drugstrength_availablein")
	strengthValue = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Strengthvalue", help_text='''The value of an active ingredient's strength, e.g. 325.''', related_name="drugstrength_strengthvalue")
	strengthUnit = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Strengthunit", help_text='''The units of an active ingredient's strength, e.g. mg.''', related_name="drugstrength_strengthunit")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="drugstrength_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="drugstrength_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Drugstrength'
		verbose_name_plural = 'Drugstrength'


class MedicalCode(models.Model):

	codingSystem = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Codingsystem", help_text='''The coding system, e.g. 'ICD-10'.''', related_name="medicalcode_codingsystem")
	codeValue = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Codevalue", help_text='''The actual code.''', related_name="medicalcode_codevalue")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalcode_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalcode_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalcode'
		verbose_name_plural = 'Medicalcode'


class MedicalConditionStage(models.Model):

	stageAsNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Stageasnumber", help_text='''The stage represented as a number, e.g. 3.''', related_name="medicalconditionstage_stageasnumber")
	subStageSuffix = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Substagesuffix", help_text='''The substage, e.g. 'a' for Stage IIIa.''', related_name="medicalconditionstage_substagesuffix")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalconditionstage_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalconditionstage_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalconditionstage'
		verbose_name_plural = 'Medicalconditionstage'


class MedicalProcedure(models.Model):

	preparation = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Preparation", help_text='''Typical preparation that a patient must undergo before having the procedure performed.''', related_name="medicalprocedure_preparation")
	procedureType = models.ForeignKey('MedicalProcedureType', on_delete=models.CASCADE, verbose_name="Proceduretype", help_text='''The type of procedure, for example Surgical, Noninvasive, or Percutaneous.''', related_name="medicalprocedure_proceduretype")
	howPerformed = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Howperformed", help_text='''How the procedure is performed.''', related_name="medicalprocedure_howperformed")
	followup = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Followup", help_text='''Typical or recommended followup care after the procedure is performed.''', related_name="medicalprocedure_followup")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalprocedure_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalprocedure_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalprocedure'
		verbose_name_plural = 'Medicalprocedure'


class MedicalRiskEstimator(models.Model):

	estimatesRiskOf = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="Estimatesriskof", help_text='''The condition, complication, or symptom whose risk is being estimated.''', related_name="medicalriskestimator_estimatesriskof")
	includedRiskFactor = models.ForeignKey('MedicalRiskFactor', on_delete=models.CASCADE, verbose_name="Includedriskfactor", help_text='''A modifiable or non-modifiable risk factor included in the calculation, e.g. age, coexisting condition.''', related_name="medicalriskestimator_includedriskfactor")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalriskestimator_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalriskestimator_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalriskestimator'
		verbose_name_plural = 'Medicalriskestimator'


class MedicalRiskScore(models.Model):

	algorithm = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Algorithm", help_text='''The algorithm or rules to follow to compute the score.''', related_name="medicalriskscore_algorithm")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalriskscore_medicalentity")
	medicalRiskEstimator = models.ForeignKey('MedicalRiskEstimator', on_delete=models.CASCADE, verbose_name="MedicalRiskEstimator", related_name="medicalriskscore_medicalriskestimator")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalriskscore_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalriskscore'
		verbose_name_plural = 'Medicalriskscore'


class MedicalRiskFactor(models.Model):

	increasesRiskOf = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="Increasesriskof", help_text='''The condition, complication, etc. influenced by this factor.''', related_name="medicalriskfactor_increasesriskof")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalriskfactor_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalriskfactor_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalriskfactor'
		verbose_name_plural = 'Medicalriskfactor'


class MedicalSignOrSymptom(models.Model):

	possibleTreatment = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="Possibletreatment", help_text='''A possible treatment to address this condition, sign or symptom.''', related_name="medicalsignorsymptom_possibletreatment")
	cause = models.ForeignKey('MedicalCause', on_delete=models.CASCADE, verbose_name="Cause", help_text='''An underlying cause. More specifically, one of the causative agent(s) that are most directly responsible for the pathophysiologic process that eventually results in the occurrence.''', related_name="medicalsignorsymptom_cause")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalsignorsymptom_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalsignorsymptom_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalsignorsymptom'
		verbose_name_plural = 'Medicalsignorsymptom'


class MedicalSign(models.Model):

	identifyingExam = models.ForeignKey('PhysicalExam', on_delete=models.CASCADE, verbose_name="Identifyingexam", help_text='''A physical examination that can identify this sign.''', related_name="medicalsign_identifyingexam")
	identifyingTest = models.ForeignKey('MedicalTest', on_delete=models.CASCADE, verbose_name="Identifyingtest", help_text='''A diagnostic test that can identify this sign.''', related_name="medicalsign_identifyingtest")
	medicalSignOrSymptom = models.ForeignKey('MedicalSignOrSymptom', on_delete=models.CASCADE, verbose_name="MedicalSignOrSymptom", related_name="medicalsign_medicalsignorsymptom")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalsign_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalsign_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalsign'
		verbose_name_plural = 'Medicalsign'


class MedicalStudy(models.Model):

	population = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Population", help_text='''Any characteristics of the population used in the study, e.g. 'males under 65'.''', related_name="medicalstudy_population")
	studySubject = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="Studysubject", help_text='''A subject of the study, i.e. one of the medical conditions, therapies, devices, drugs, etc. investigated by the study.''', related_name="medicalstudy_studysubject")
	status = models.ForeignKey('MedicalStudyStatus', on_delete=models.CASCADE, verbose_name="Status", help_text='''The status of the study (enumerated).''', related_name="medicalstudy_status")
	outcome = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Outcome", help_text='''Expected or actual outcomes of the study.''', related_name="medicalstudy_outcome")
	sponsor = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Sponsor", help_text='''Sponsor of the study.''', related_name="medicalstudy_sponsor")
	studyLocation = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Studylocation", help_text='''The location in which the study is taking/took place.''', related_name="medicalstudy_studylocation")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicalstudy_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalstudy_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalstudy'
		verbose_name_plural = 'Medicalstudy'


class MedicalTrial(models.Model):

	phase = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Phase", help_text='''The phase of the trial.''', related_name="medicaltrial_phase")
	trialDesign = models.ForeignKey('MedicalTrialDesign', on_delete=models.CASCADE, verbose_name="Trialdesign", help_text='''Specifics about the trial design (enumerated).''', related_name="medicaltrial_trialdesign")
	medicalStudy = models.ForeignKey('MedicalStudy', on_delete=models.CASCADE, verbose_name="MedicalStudy", related_name="medicaltrial_medicalstudy")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicaltrial_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicaltrial_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicaltrial'
		verbose_name_plural = 'Medicaltrial'


class MedicalTest(models.Model):

	signDetected = models.ForeignKey('MedicalSign', on_delete=models.CASCADE, verbose_name="Signdetected", help_text='''A sign detected by the test.''', related_name="medicaltest_signdetected")
	usedToDiagnose = models.ForeignKey('MedicalCondition', on_delete=models.CASCADE, verbose_name="Usedtodiagnose", help_text='''A condition the test is used to diagnose.''', related_name="medicaltest_usedtodiagnose")
	normalRange = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Normalrange", help_text='''Range of acceptable values for a typical patient, when applicable.''', related_name="medicaltest_normalrange")
	affectedBy = models.ForeignKey('Drug', on_delete=models.CASCADE, verbose_name="Affectedby", help_text='''Drugs that affect the test's results.''', related_name="medicaltest_affectedby")
	usesDevice = models.ForeignKey('MedicalDevice', on_delete=models.CASCADE, verbose_name="Usesdevice", help_text='''Device used to perform the test.''', related_name="medicaltest_usesdevice")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicaltest_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicaltest_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicaltest'
		verbose_name_plural = 'Medicaltest'


class MedicalTestPanel(models.Model):

	subTest = models.ForeignKey('MedicalTest', on_delete=models.CASCADE, verbose_name="Subtest", help_text='''A component test of the panel.''', related_name="medicaltestpanel_subtest")
	medicalTest = models.ForeignKey('MedicalTest', on_delete=models.CASCADE, verbose_name="MedicalTest", related_name="medicaltestpanel_medicaltest")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicaltestpanel_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicaltestpanel_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicaltestpanel'
		verbose_name_plural = 'Medicaltestpanel'


class PathologyTest(models.Model):

	tissueSample = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Tissuesample", help_text='''The type of tissue sample required for the test.''', related_name="pathologytest_tissuesample")
	medicalTest = models.ForeignKey('MedicalTest', on_delete=models.CASCADE, verbose_name="MedicalTest", related_name="pathologytest_medicaltest")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="pathologytest_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="pathologytest_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Pathologytest'
		verbose_name_plural = 'Pathologytest'


class MedicalTherapy(models.Model):

	seriousAdverseOutcome = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="Seriousadverseoutcome", help_text='''A possible serious complication and/or serious side effect of this therapy. Serious adverse outcomes include those that are life-threatening; result in death, disability, or permanent damage; require hospitalization or prolong existing hospitalization; cause congenital anomalies or birth defects; or jeopardize the patient and may require medical or surgical intervention to prevent one of the outcomes in this definition.''', related_name="medicaltherapy_seriousadverseoutcome")
	contraindication = models.ForeignKey('MedicalContraindication', on_delete=models.CASCADE, verbose_name="Contraindication", help_text='''A contraindication for this therapy.''', related_name="medicaltherapy_contraindication")
	adverseOutcome = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="Adverseoutcome", help_text='''A possible complication and/or side effect of this therapy. If it is known that an adverse outcome is serious (resulting in death, disability, or permanent damage; requiring hospitalization; or is otherwise life-threatening or requires immediate medical attention), tag it as a seriouseAdverseOutcome instead.''', related_name="medicaltherapy_adverseoutcome")
	indication = models.ForeignKey('MedicalIndication', on_delete=models.CASCADE, verbose_name="Indication", help_text='''A factor that indicates use of this therapy for treatment and/or prevention of a condition, symptom, etc. For therapies such as drugs, indications can include both officially-approved indications as well as off-label uses. These can be distinguished by using the ApprovedIndication subtype of MedicalIndication.''', related_name="medicaltherapy_indication")
	duplicateTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="Duplicatetherapy", help_text='''A therapy that duplicates or overlaps this one.''', related_name="medicaltherapy_duplicatetherapy")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="medicaltherapy_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicaltherapy_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicaltherapy'
		verbose_name_plural = 'Medicaltherapy'


class DietarySupplement(models.Model):

	targetPopulation = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Targetpopulation", help_text='''Characteristics of the population for which this is intended, or which typically uses it, e.g. 'adults'.''', related_name="dietarysupplement_targetpopulation")
	background = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Background", help_text='''Descriptive information establishing a historical perspective on the supplement. May include the rationale for the name, the population where the supplement first came to prominence, etc.''', related_name="dietarysupplement_background")
	nonProprietaryName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Nonproprietaryname", help_text='''The generic name of this drug or supplement.''', related_name="dietarysupplement_nonproprietaryname")
	manufacturer = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Manufacturer", help_text='''The manufacturer of the product.''', related_name="dietarysupplement_manufacturer")
	recommendedIntake = models.ForeignKey('RecommendedDoseSchedule', on_delete=models.CASCADE, verbose_name="Recommendedintake", help_text='''Recommended intake of this supplement for a given population as defined by a specific recommending authority.''', related_name="dietarysupplement_recommendedintake")
	dosageForm = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Dosageform", help_text='''A dosage form in which this drug/supplement is available, e.g. 'tablet', 'suspension', 'injection'.''', related_name="dietarysupplement_dosageform")
	activeIngredient = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Activeingredient", help_text='''An active ingredient, typically chemical compounds and/or biologic substances.''', related_name="dietarysupplement_activeingredient")
	maximumIntake = models.ForeignKey('MaximumDoseSchedule', on_delete=models.CASCADE, verbose_name="Maximumintake", help_text='''Recommended intake of this supplement for a given population as defined by a specific recommending authority.''', related_name="dietarysupplement_maximumintake")
	mechanismOfAction = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mechanismofaction", help_text='''The specific biochemical interaction through which this drug or supplement produces its pharmacological effect.''', related_name="dietarysupplement_mechanismofaction")
	safetyConsideration = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Safetyconsideration", help_text='''Any potential safety concern associated with the supplement. May include interactions with other drugs and foods, pregnancy, breastfeeding, known adverse reactions, and documented efficacy of the supplement.''', related_name="dietarysupplement_safetyconsideration")
	isProprietary = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Isproprietary", help_text='''True if this item's name is a proprietary/brand name (vs. generic name).''', related_name="dietarysupplement_isproprietary")
	legalStatus = models.ForeignKey('DrugLegalStatus', on_delete=models.CASCADE, verbose_name="Legalstatus", help_text='''The drug or supplement's legal status, including any controlled substance schedules that apply.''', related_name="dietarysupplement_legalstatus")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="dietarysupplement_medicalentity")
	medicalTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="MedicalTherapy", related_name="dietarysupplement_medicaltherapy")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="dietarysupplement_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Dietarysupplement'
		verbose_name_plural = 'Dietarysupplement'


class Drug(models.Model):

	foodWarning = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Foodwarning", help_text='''Any precaution, guidance, contraindication, etc. related to consumption of specific foods while taking this drug.''', related_name="drug_foodwarning")
	labelDetails = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Labeldetails", help_text='''Link to the drug's label details.''', related_name="drug_labeldetails")
	activeIngredient = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Activeingredient", help_text='''An active ingredient, typically chemical compounds and/or biologic substances.''', related_name="drug_activeingredient")
	overdosage = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Overdosage", help_text='''Any information related to overdose on a drug, including signs or symptoms, treatments, contact information for emergency response.''', related_name="drug_overdosage")
	dosageForm = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Dosageform", help_text='''A dosage form in which this drug/supplement is available, e.g. 'tablet', 'suspension', 'injection'.''', related_name="drug_dosageform")
	availableStrength = models.ForeignKey('DrugStrength', on_delete=models.CASCADE, verbose_name="Availablestrength", help_text='''An available dosage strength for the drug.''', related_name="drug_availablestrength")
	prescriptionStatus = models.ForeignKey('DrugPrescriptionStatus', on_delete=models.CASCADE, verbose_name="Prescriptionstatus", help_text='''Indicates whether this drug is available by prescription or over-the-counter.''', related_name="drug_prescriptionstatus")
	interactingDrug = models.ForeignKey('Drug', on_delete=models.CASCADE, verbose_name="Interactingdrug", help_text='''Another drug that is known to interact with this drug in a way that impacts the effect of this drug or causes a risk to the patient. Note: disease interactions are typically captured as contraindications.''', related_name="drug_interactingdrug")
	relatedDrug = models.ForeignKey('Drug', on_delete=models.CASCADE, verbose_name="Relateddrug", help_text='''Any other drug related to this one, for example commonly-prescribed alternatives.''', related_name="drug_relateddrug")
	administrationRoute = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Administrationroute", help_text='''A route by which this drug may be administered, e.g. 'oral'.''', related_name="drug_administrationroute")
	isProprietary = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Isproprietary", help_text='''True if this item's name is a proprietary/brand name (vs. generic name).''', related_name="drug_isproprietary")
	doseSchedule = models.ForeignKey('DoseSchedule', on_delete=models.CASCADE, verbose_name="Doseschedule", help_text='''A dosing schedule for the drug for a given population, either observed, recommended, or maximum dose based on the type used.''', related_name="drug_doseschedule")
	alcoholWarning = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Alcoholwarning", help_text='''Any precaution, guidance, contraindication, etc. related to consumption of alcohol while taking this drug.''', related_name="drug_alcoholwarning")
	nonProprietaryName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Nonproprietaryname", help_text='''The generic name of this drug or supplement.''', related_name="drug_nonproprietaryname")
	manufacturer = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Manufacturer", help_text='''The manufacturer of the product.''', related_name="drug_manufacturer")
	pregnancyWarning = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pregnancywarning", help_text='''Any precaution, guidance, contraindication, etc. related to this drug's use during pregnancy.''', related_name="drug_pregnancywarning")
	breastfeedingWarning = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Breastfeedingwarning", help_text='''Any precaution, guidance, contraindication, etc. related to this drug's use by breastfeeding mothers.''', related_name="drug_breastfeedingwarning")
	prescribingInfo = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Prescribinginfo", help_text='''Link to prescribing information for the drug.''', related_name="drug_prescribinginfo")
	isAvailableGenerically = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Isavailablegenerically", help_text='''True if the drug is available in a generic form (regardless of name).''', related_name="drug_isavailablegenerically")
	pregnancyCategory = models.ForeignKey('DrugPregnancyCategory', on_delete=models.CASCADE, verbose_name="Pregnancycategory", help_text='''Pregnancy category of this drug.''', related_name="drug_pregnancycategory")
	mechanismOfAction = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mechanismofaction", help_text='''The specific biochemical interaction through which this drug or supplement produces its pharmacological effect.''', related_name="drug_mechanismofaction")
	clinicalPharmacology = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Clinicalpharmacology", help_text='''Description of the absorption and elimination of drugs, including their concentration (pharmacokinetics, pK) and biological effects (pharmacodynamics, pD). Supersedes clincalPharmacology.''', related_name="drug_clinicalpharmacology")
	drugClass = models.ForeignKey('DrugClass', on_delete=models.CASCADE, verbose_name="Drugclass", help_text='''The class of drug this belongs to (e.g., statins).''', related_name="drug_drugclass")
	cost = models.ForeignKey('DrugCost', on_delete=models.CASCADE, verbose_name="Cost", help_text='''Cost per unit of the drug, as reported by the source being tagged.''', related_name="drug_cost")
	legalStatus = models.ForeignKey('DrugLegalStatus', on_delete=models.CASCADE, verbose_name="Legalstatus", help_text='''The drug or supplement's legal status, including any controlled substance schedules that apply.''', related_name="drug_legalstatus")
	medicalTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="MedicalTherapy", related_name="drug_medicaltherapy")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="drug_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="drug_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Drug'
		verbose_name_plural = 'Drug'


class DrugClass(models.Model):

	drug = models.ForeignKey('Drug', on_delete=models.CASCADE, verbose_name="Drug", help_text='''A drug in this drug class.''', related_name="drugclass_drug")
	medicalTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="MedicalTherapy", related_name="drugclass_medicaltherapy")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="drugclass_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="drugclass_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Drugclass'
		verbose_name_plural = 'Drugclass'


class PhysicalActivity(models.Model):

	epidemiology = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Epidemiology", help_text='''The characteristics of associated patients, such as age, gender, race etc.''', related_name="physicalactivity_epidemiology")
	pathophysiology = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pathophysiology", help_text='''Changes in the normal mechanical, physical, and biochemical functions that are associated with this activity or condition.''', related_name="physicalactivity_pathophysiology")
	medicalTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="MedicalTherapy", related_name="physicalactivity_medicaltherapy")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="physicalactivity_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="physicalactivity_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Physicalactivity'
		verbose_name_plural = 'Physicalactivity'


class SuperficialAnatomy(models.Model):

	significance = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Significance", help_text='''The significance associated with the superficial anatomy; as an example, how characteristics of the superficial anatomy can suggest underlying medical conditions or courses of treatment.''', related_name="superficialanatomy_significance")
	associatedPathophysiology = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Associatedpathophysiology", help_text='''If applicable, a description of the pathophysiology associated with the anatomical system, including potential abnormal changes in the mechanical, physical, and biochemical functions of the system.''', related_name="superficialanatomy_associatedpathophysiology")
	relatedCondition = models.ForeignKey('MedicalCondition', on_delete=models.CASCADE, verbose_name="Relatedcondition", help_text='''A medical condition associated with this anatomy.''', related_name="superficialanatomy_relatedcondition")
	relatedTherapy = models.ForeignKey('MedicalTherapy', on_delete=models.CASCADE, verbose_name="Relatedtherapy", help_text='''A medical therapy related to this anatomy.''', related_name="superficialanatomy_relatedtherapy")
	medicalEntity = models.ForeignKey('MedicalEntity', on_delete=models.CASCADE, verbose_name="MedicalEntity", related_name="superficialanatomy_medicalentity")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="superficialanatomy_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Superficialanatomy'
		verbose_name_plural = 'Superficialanatomy'


class Organization(models.Model):

	foundingLocation = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Foundinglocation", help_text='''The place where the Organization was founded.''', related_name="organization_foundinglocation")
	hasOfferCatalog = models.ForeignKey('OfferCatalog', on_delete=models.CASCADE, verbose_name="Hasoffercatalog", help_text='''Indicates an OfferCatalog listing for this Organization, Person, or Service.''', related_name="organization_hasoffercatalog")
	telephone = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Telephone", help_text='''The telephone number.''', related_name="organization_telephone")
	faxNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Faxnumber", help_text='''The fax number.''', related_name="organization_faxnumber")
	email = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Email", help_text='''Email address.''', related_name="organization_email")
	aggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="organization_aggregaterating")
	award = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", help_text='''An award won by or for this item. Supersedes awards.''', related_name="organization_award")
	makesOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Makesoffer", help_text='''A pointer to products or services offered by the organization or person. Inverse property: offeredBy.''', related_name="organization_makesoffer")
	foundingDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Foundingdate", help_text='''The date that this organization was founded.''', related_name="organization_foundingdate")
	parentOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Parentorganization", help_text='''The larger organization that this organization is a branch of, if any. Supersedes branchOf. Inverse property: subOrganization.''', related_name="organization_parentorganization")
	globalLocationNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Globallocationnumber", help_text='''The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.''', related_name="organization_globallocationnumber")
	hasPOS = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Haspos", help_text='''Points-of-Sales operated by the organization or person.''', related_name="organization_haspos")
	review = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", help_text='''A review of the item. Supersedes reviews.''', related_name="organization_review")
	seeks = models.ForeignKey('Demand', on_delete=models.CASCADE, verbose_name="Seeks", help_text='''A pointer to products or services sought by the organization or person (demand).''', related_name="organization_seeks")
	legalName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Legalname", help_text='''The official name of the organization, e.g. the registered company name.''', related_name="organization_legalname")
	employee = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Employee", help_text='''Someone working for this organization. Supersedes employees.''', related_name="organization_employee")
	isicV4 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isicv4", help_text='''The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.''', related_name="organization_isicv4")
	contactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Contactpoint", help_text='''A contact point for a person or organization. Supersedes contactPoints.''', related_name="organization_contactpoint")
	department = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Department", help_text='''A relationship between an organization and a department of that organization, also described as an organization (allowing different urls, logos, opening hours). For example: a store with a pharmacy, or a bakery with a cafe.''', related_name="organization_department")
	founder = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Founder", help_text='''A person who founded this organization. Supersedes founders.''', related_name="organization_founder")
	subOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Suborganization", help_text='''A relationship between two organizations where the first includes the second, e.g., as a subsidiary. See also: the more specific 'department' property. Inverse property: parentOrganization.''', related_name="organization_suborganization")
	duns = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Duns", help_text='''The Dun & Bradstreet DUNS number for identifying an organization or business person.''', related_name="organization_duns")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", help_text='''Upcoming or past event associated with this place, organization, or action. Supersedes events.''', related_name="organization_event")
	dissolutionDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Dissolutiondate", help_text='''The date that this organization was dissolved.''', related_name="organization_dissolutiondate")
	numberOfEmployees = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofemployees", help_text='''The number of employees in an organization e.g. business.''', related_name="organization_numberofemployees")
	naics = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Naics", help_text='''The North American Industry Classification System (NAICS) code for a particular organization or business person.''', related_name="organization_naics")
	alumni = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Alumni", help_text='''Alumni of an organization. Inverse property: alumniOf.''', related_name="organization_alumni")
	taxID = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Taxid", help_text='''The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.''', related_name="organization_taxid")
	vatID = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vatid", help_text='''The Value-added Tax ID of the organization or person.''', related_name="organization_vatid")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="organization_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Organization'
		verbose_name_plural = 'Organization'


class Airline(models.Model):

	iataCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Iatacode", help_text='''IATA identifier for an airline or airport.''', related_name="airline_iatacode")
	boardingPolicy = models.ForeignKey('BoardingPolicyType', on_delete=models.CASCADE, verbose_name="Boardingpolicy", help_text='''The type of boarding policy used by the airline (e.g. zone-based or group-based).''', related_name="airline_boardingpolicy")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="airline_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="airline_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Airline'
		verbose_name_plural = 'Airline'


class Corporation(models.Model):

	tickerSymbol = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Tickersymbol", help_text='''The exchange traded instrument associated with a Corporation object. The tickerSymbol is expressed as an exchange and an instrument name separated by a space character. For the exchange component of the tickerSymbol attribute, we reccommend using the controlled vocaulary of Market Identifier Codes (MIC) specified in ISO15022.''', related_name="corporation_tickersymbol")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="corporation_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="corporation_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Corporation'
		verbose_name_plural = 'Corporation'


class EducationalOrganization(models.Model):

	alumni = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Alumni", help_text='''Alumni of an organization. Inverse property: alumniOf.''', related_name="educationalorganization_alumni")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="educationalorganization_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="educationalorganization_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Educationalorganization'
		verbose_name_plural = 'Educationalorganization'


class LocalBusiness(models.Model):

	paymentAccepted = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Paymentaccepted", help_text='''Cash, credit card, etc.''', related_name="localbusiness_paymentaccepted")
	currenciesAccepted = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Currenciesaccepted", help_text='''The currency accepted (in ISO 4217 currency format).''', related_name="localbusiness_currenciesaccepted")
	priceRange = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricerange", help_text='''The price range of the business, for example $$$.''', related_name="localbusiness_pricerange")
	branchCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Branchcode", help_text='''A short textual code (also called "store code") that uniquely identifies a place of business. The code is typically assigned by the parentOrganization and used in structured URLs. For example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047 the code "3047" is a branchCode for a particular branch.''', related_name="localbusiness_branchcode")
	openingHours = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Openinghours", help_text='''The opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.- Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su.- Times are specified using 24:00 time. For example, 3pm is specified as 15:00. - Here is an example: <time itemprop="openingHours" datetime="Tu,Th 16:00-20:00">Tuesdays and Thursdays 4-8pm</time>. - If a business is open 7 days a week, then it can be specified as <time itemprop="openingHours" datetime="Mo-Su">Monday through Sunday, all day</time>.''', related_name="localbusiness_openinghours")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="localbusiness_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="localbusiness_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="localbusiness_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Localbusiness'
		verbose_name_plural = 'Localbusiness'


class Hospital(models.Model):

	medicalSpecialty = models.ForeignKey('MedicalSpecialty', on_delete=models.CASCADE, verbose_name="Medicalspecialty", help_text='''A medical specialty of the provider.''', related_name="hospital_medicalspecialty")
	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="LocalBusiness", related_name="hospital_localbusiness")
	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="CivicStructure", related_name="hospital_civicstructure")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="hospital_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="hospital_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="hospital_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Hospital'
		verbose_name_plural = 'Hospital'


class MovieTheater(models.Model):

	screenCount = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Screencount", help_text='''The number of screens in the movie theater.''', related_name="movietheater_screencount")
	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="LocalBusiness", related_name="movietheater_localbusiness")
	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="CivicStructure", related_name="movietheater_civicstructure")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="movietheater_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="movietheater_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="movietheater_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Movietheater'
		verbose_name_plural = 'Movietheater'


class FoodEstablishment(models.Model):

	servesCuisine = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Servescuisine", help_text='''The cuisine of the restaurant.''', related_name="foodestablishment_servescuisine")
	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="LocalBusiness", related_name="foodestablishment_localbusiness")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="foodestablishment_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="foodestablishment_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="foodestablishment_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Foodestablishment'
		verbose_name_plural = 'Foodestablishment'


class DiagnosticLab(models.Model):

	availableTest = models.ForeignKey('MedicalTest', on_delete=models.CASCADE, verbose_name="Availabletest", help_text='''A diagnostic test or procedure offered by this lab.''', related_name="diagnosticlab_availabletest")
	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="LocalBusiness", related_name="diagnosticlab_localbusiness")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="diagnosticlab_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="diagnosticlab_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="diagnosticlab_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Diagnosticlab'
		verbose_name_plural = 'Diagnosticlab'


class MedicalClinic(models.Model):

	medicalSpecialty = models.ForeignKey('MedicalSpecialty', on_delete=models.CASCADE, verbose_name="Medicalspecialty", help_text='''A medical specialty of the provider.''', related_name="medicalclinic_medicalspecialty")
	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="LocalBusiness", related_name="medicalclinic_localbusiness")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="medicalclinic_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="medicalclinic_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="medicalclinic_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Medicalclinic'
		verbose_name_plural = 'Medicalclinic'


class Physician(models.Model):

	medicalSpecialty = models.ForeignKey('MedicalSpecialty', on_delete=models.CASCADE, verbose_name="Medicalspecialty", help_text='''A medical specialty of the provider.''', related_name="physician_medicalspecialty")
	hospitalAffiliation = models.ForeignKey('Hospital', on_delete=models.CASCADE, verbose_name="Hospitalaffiliation", help_text='''A hospital with which the physician or office is affiliated.''', related_name="physician_hospitalaffiliation")
	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="LocalBusiness", related_name="physician_localbusiness")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="physician_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="physician_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="physician_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Physician'
		verbose_name_plural = 'Physician'


class RealEstateAgent(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="LocalBusiness", related_name="realestateagent_localbusiness")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="realestateagent_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="realestateagent_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="realestateagent_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Realestateagent'
		verbose_name_plural = 'Realestateagent'


class SportsActivityLocation(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="LocalBusiness", related_name="sportsactivitylocation_localbusiness")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="sportsactivitylocation_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="sportsactivitylocation_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="sportsactivitylocation_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Sportsactivitylocation'
		verbose_name_plural = 'Sportsactivitylocation'


class MusicGroup(models.Model):

	album = models.ForeignKey('MusicAlbum', on_delete=models.CASCADE, verbose_name="Album", help_text='''A music album. Supersedes albums.''', related_name="musicgroup_album")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="musicgroup_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="musicgroup_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Musicgroup'
		verbose_name_plural = 'Musicgroup'


class SportsOrganization(models.Model):

	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="sportsorganization_organization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="sportsorganization_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Sportsorganization'
		verbose_name_plural = 'Sportsorganization'


class SportsTeam(models.Model):

	athlete = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Athlete", help_text='''A person that acts as performing member of a sports team; a player as opposed to a coach.''', related_name="sportsteam_athlete")
	coach = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Coach", help_text='''A person that acts in a coaching role for a sports team.''', related_name="sportsteam_coach")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", related_name="sportsteam_organization")
	sportsOrganization = models.ForeignKey('SportsOrganization', on_delete=models.CASCADE, verbose_name="SportsOrganization", related_name="sportsteam_sportsorganization")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="sportsteam_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Sportsteam'
		verbose_name_plural = 'Sportsteam'


class Person(models.Model):

	knows = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Knows", help_text='''The most generic bi-directional social/work relation.''', related_name="person_knows")
	affiliation = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Affiliation", help_text='''An organization that this person is affiliated with. For example, a school/university, a club, or a team.''', related_name="person_affiliation")
	email = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Email", help_text='''Email address.''', related_name="person_email")
	award = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", help_text='''An award won by or for this item. Supersedes awards.''', related_name="person_award")
	performerIn = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Performerin", help_text='''Event that this person is a performer or participant in.''', related_name="person_performerin")
	weight = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Weight", help_text='''The weight of the product or person.''', related_name="person_weight")
	netWorth = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Networth", help_text='''The total financial value of the person as calculated by subtracting assets from liabilities.''', related_name="person_networth")
	honorificSuffix = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Honorificsuffix", help_text='''An honorific suffix preceding a Person's name such as M.D. /PhD/MSCSW.''', related_name="person_honorificsuffix")
	givenName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Givenname", help_text='''Given name. In the U.S., the first name of a Person. This can be used along with familyName instead of the name property.''', related_name="person_givenname")
	spouse = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Spouse", help_text='''The person's spouse.''', related_name="person_spouse")
	seeks = models.ForeignKey('Demand', on_delete=models.CASCADE, verbose_name="Seeks", help_text='''A pointer to products or services sought by the organization or person (demand).''', related_name="person_seeks")
	follows = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Follows", help_text='''The most generic uni-directional social relation.''', related_name="person_follows")
	faxNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Faxnumber", help_text='''The fax number.''', related_name="person_faxnumber")
	jobTitle = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Jobtitle", help_text='''The job title of the person (for example, Financial Manager).''', related_name="person_jobtitle")
	duns = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Duns", help_text='''The Dun & Bradstreet DUNS number for identifying an organization or business person.''', related_name="person_duns")
	nationality = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Nationality", help_text='''Nationality of the person.''', related_name="person_nationality")
	birthDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Birthdate", help_text='''Date of birth.''', related_name="person_birthdate")
	hasOfferCatalog = models.ForeignKey('OfferCatalog', on_delete=models.CASCADE, verbose_name="Hasoffercatalog", help_text='''Indicates an OfferCatalog listing for this Organization, Person, or Service.''', related_name="person_hasoffercatalog")
	globalLocationNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Globallocationnumber", help_text='''The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.''', related_name="person_globallocationnumber")
	familyName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Familyname", help_text='''Family name. In the U.S., the last name of an Person. This can be used along with givenName instead of the name property.''', related_name="person_familyname")
	isicV4 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isicv4", help_text='''The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.''', related_name="person_isicv4")
	children = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Children", help_text='''A child of the person.''', related_name="person_children")
	relatedTo = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Relatedto", help_text='''The most generic familial relation.''', related_name="person_relatedto")
	makesOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Makesoffer", help_text='''A pointer to products or services offered by the organization or person. Inverse property: offeredBy.''', related_name="person_makesoffer")
	gender = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gender", help_text='''Gender of the person.''', related_name="person_gender")
	sibling = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Sibling", help_text='''A sibling of the person. Supersedes siblings.''', related_name="person_sibling")
	deathPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Deathplace", help_text='''The place where the person died.''', related_name="person_deathplace")
	hasPOS = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Haspos", help_text='''Points-of-Sales operated by the organization or person.''', related_name="person_haspos")
	contactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Contactpoint", help_text='''A contact point for a person or organization. Supersedes contactPoints.''', related_name="person_contactpoint")
	additionalName = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Additionalname", help_text='''An additional name for a Person, can be used for a middle name.''', related_name="person_additionalname")
	deathDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Deathdate", help_text='''Date of death.''', related_name="person_deathdate")
	telephone = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Telephone", help_text='''The telephone number.''', related_name="person_telephone")
	birthPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Birthplace", help_text='''The place where the person was born.''', related_name="person_birthplace")
	honorificPrefix = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Honorificprefix", help_text='''An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.''', related_name="person_honorificprefix")
	parent = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Parent", help_text='''A parent of this person. Supersedes parents.''', related_name="person_parent")
	worksFor = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Worksfor", help_text='''Organizations that the person works for.''', related_name="person_worksfor")
	naics = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Naics", help_text='''The North American Industry Classification System (NAICS) code for a particular organization or business person.''', related_name="person_naics")
	vatID = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vatid", help_text='''The Value-added Tax ID of the organization or person.''', related_name="person_vatid")
	taxID = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Taxid", help_text='''The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.''', related_name="person_taxid")
	colleague = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Colleague", help_text='''A colleague of the person. Supersedes colleagues.''', related_name="person_colleague")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="person_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'Person'


class Place(models.Model):

	containsPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Containsplace", help_text='''The basic containment relation between a place and another that it contains. Inverse property: containsPlace.''', related_name="place_containsplace")
	isicV4 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isicv4", help_text='''The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.''', related_name="place_isicv4")
	telephone = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Telephone", help_text='''The telephone number.''', related_name="place_telephone")
	faxNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Faxnumber", help_text='''The fax number.''', related_name="place_faxnumber")
	additionalProperty = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Additionalproperty", help_text='''A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.''', related_name="place_additionalproperty")
	aggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="place_aggregaterating")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", help_text='''Upcoming or past event associated with this place, organization, or action. Supersedes events.''', related_name="place_event")
	globalLocationNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Globallocationnumber", help_text='''The Global Location Number (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.''', related_name="place_globallocationnumber")
	review = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", help_text='''A review of the item. Supersedes reviews.''', related_name="place_review")
	openingHoursSpecification = models.ForeignKey('OpeningHoursSpecification', on_delete=models.CASCADE, verbose_name="Openinghoursspecification", help_text='''The opening hours of a certain place.''', related_name="place_openinghoursspecification")
	branchCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Branchcode", help_text='''A short textual code (also called "store code") that uniquely identifies a place of business. The code is typically assigned by the parentOrganization and used in structured URLs. For example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047 the code "3047" is a branchCode for a particular branch.''', related_name="place_branchcode")
	containedInPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Containedinplace", help_text='''The basic containment relation between a place and one that contains it. Supersedes containedIn. Inverse property: containsPlace.''', related_name="place_containedinplace")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="place_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Place'
		verbose_name_plural = 'Place'


class AdministrativeArea(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="administrativearea_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="administrativearea_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Administrativearea'
		verbose_name_plural = 'Administrativearea'


class Country(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="country_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="country_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Country'


class CivicStructure(models.Model):

	openingHours = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Openinghours", help_text='''The opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.- Days are specified using the following two-letter combinations: Mo, Tu, We, Th, Fr, Sa, Su.- Times are specified using 24:00 time. For example, 3pm is specified as 15:00. - Here is an example: <time itemprop="openingHours" datetime="Tu,Th 16:00-20:00">Tuesdays and Thursdays 4-8pm</time>. - If a business is open 7 days a week, then it can be specified as <time itemprop="openingHours" datetime="Mo-Su">Monday through Sunday, all day</time>.''', related_name="civicstructure_openinghours")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="civicstructure_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="civicstructure_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Civicstructure'
		verbose_name_plural = 'Civicstructure'


class Airport(models.Model):

	iataCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Iatacode", help_text='''IATA identifier for an airline or airport.''', related_name="airport_iatacode")
	icaoCode = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Icaocode", help_text='''IACO identifier for an airport.''', related_name="airport_icaocode")
	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="CivicStructure", related_name="airport_civicstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="airport_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="airport_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Airport'
		verbose_name_plural = 'Airport'


class BusStation(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="CivicStructure", related_name="busstation_civicstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="busstation_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="busstation_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Busstation'
		verbose_name_plural = 'Busstation'


class BusStop(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="CivicStructure", related_name="busstop_civicstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="busstop_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="busstop_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Busstop'
		verbose_name_plural = 'Busstop'


class TrainStation(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="CivicStructure", related_name="trainstation_civicstructure")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="trainstation_thing")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", related_name="trainstation_place")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Trainstation'
		verbose_name_plural = 'Trainstation'


class Product(models.Model):

	releaseDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Releasedate", help_text='''The release date of a product or product model. This can be used to distinguish the exact variant of a product.''', related_name="product_releasedate")
	purchaseDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Purchasedate", help_text='''The date the item e.g. vehicle was purchased by the current owner.''', related_name="product_purchasedate")
	itemCondition = models.ForeignKey('OfferItemCondition', on_delete=models.CASCADE, verbose_name="Itemcondition", help_text='''A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.''', related_name="product_itemcondition")
	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", help_text='''An intended audience, i.e. a group for whom something was created. Supersedes serviceAudience.''', related_name="product_audience")
	productID = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Productid", help_text='''The product identifier, such as ISBN. For example: <meta itemprop='productID' content='isbn:123-456-789'/>.''', related_name="product_productid")
	additionalProperty = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Additionalproperty", help_text='''A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.''', related_name="product_additionalproperty")
	isConsumableFor = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Isconsumablefor", help_text='''A pointer to another product (or multiple products) for which this product is a consumable.''', related_name="product_isconsumablefor")
	award = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", help_text='''An award won by or for this item. Supersedes awards.''', related_name="product_award")
	weight = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Weight", help_text='''The weight of the product or person.''', related_name="product_weight")
	gtin8 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin8", help_text='''The GTIN-8 code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See GS1 GTIN Summary for more details.''', related_name="product_gtin8")
	sku = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Sku", help_text='''The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.''', related_name="product_sku")
	isRelatedTo = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Isrelatedto", help_text='''A pointer to another, somehow related product (or multiple products).''', related_name="product_isrelatedto")
	review = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", help_text='''A review of the item. Supersedes reviews.''', related_name="product_review")
	mpn = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mpn", help_text='''The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.''', related_name="product_mpn")
	productionDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Productiondate", help_text='''The date of production of the item, e.g. vehicle.''', related_name="product_productiondate")
	gtin13 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin13", help_text='''The GTIN-13 code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero. See GS1 GTIN Summary for more details.''', related_name="product_gtin13")
	isAccessoryOrSparePartFor = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Isaccessoryorsparepartfor", help_text='''A pointer to another product (or multiple products) for which this product is an accessory or spare part.''', related_name="product_isaccessoryorsparepartfor")
	manufacturer = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Manufacturer", help_text='''The manufacturer of the product.''', related_name="product_manufacturer")
	offers = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", help_text='''An offer to provide this item—for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="product_offers")
	aggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="product_aggregaterating")
	gtin14 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin14", help_text='''The GTIN-14 code of the product, or the product to which the offer refers. See GS1 GTIN Summary for more details.''', related_name="product_gtin14")
	isSimilarTo = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Issimilarto", help_text='''A pointer to another, functionally similar product (or multiple products).''', related_name="product_issimilarto")
	color = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Color", help_text='''The color of the product.''', related_name="product_color")
	gtin12 = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin12", help_text='''The GTIN-12 code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See GS1 GTIN Summary for more details.''', related_name="product_gtin12")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="product_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Product'


class ProductModel(models.Model):

	isVariantOf = models.ForeignKey('ProductModel', on_delete=models.CASCADE, verbose_name="Isvariantof", help_text='''A pointer to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive.''', related_name="productmodel_isvariantof")
	predecessorOf = models.ForeignKey('ProductModel', on_delete=models.CASCADE, verbose_name="Predecessorof", help_text='''A pointer from a previous, often discontinued variant of the product to its newer variant.''', related_name="productmodel_predecessorof")
	successorOf = models.ForeignKey('ProductModel', on_delete=models.CASCADE, verbose_name="Successorof", help_text='''A pointer from a newer variant of a product to its previous, often discontinued predecessor.''', related_name="productmodel_successorof")
	product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product", related_name="productmodel_product")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="productmodel_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Productmodel'
		verbose_name_plural = 'Productmodel'


class Vehicle(models.Model):

	purchaseDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Purchasedate", help_text='''The date the item e.g. vehicle was purchased by the current owner.''', related_name="vehicle_purchasedate")
	vehicleInteriorColor = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehicleinteriorcolor", help_text='''The color or color combination of the interior of the vehicle.''', related_name="vehicle_vehicleinteriorcolor")
	cargoVolume = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Cargovolume", help_text='''The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.Typical unit code(s): LTR for liters, FTQ for cubic foot/feetNote: You can use minValue and maxValue to indicate ranges.''', related_name="vehicle_cargovolume")
	vehicleIdentificationNumber = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehicleidentificationnumber", help_text='''The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles.''', related_name="vehicle_vehicleidentificationnumber")
	steeringPosition = models.ForeignKey('SteeringPositionValue', on_delete=models.CASCADE, verbose_name="Steeringposition", help_text='''The position of the steering wheel or similar device (mostly for cars).''', related_name="vehicle_steeringposition")
	productionDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Productiondate", help_text='''The date of production of the item, e.g. vehicle.''', related_name="vehicle_productiondate")
	dateVehicleFirstRegistered = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Datevehiclefirstregistered", help_text='''The date of the first registration of the vehicle with the respective public authorities.''', related_name="vehicle_datevehiclefirstregistered")
	vehicleModelDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Vehiclemodeldate", help_text='''The release date of a vehicle model (often used to differentiate versions of the same make and model).''', related_name="vehicle_vehiclemodeldate")
	vehicleInteriorType = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehicleinteriortype", help_text='''The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.). While most interior types are characterized by the material used, an interior type can also be based on vehicle usage or target audience.''', related_name="vehicle_vehicleinteriortype")
	fuelEfficiency = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Fuelefficiency", help_text='''The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers per liter (km/L).Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter.Use unitText to indicate the unit of measurement, e.g. mpg or km/L.Note 2: There are two ways of indicating the fuel consumption, fuelConsumption (e.g. 8 liters per 100 km) and fuelEfficiency (e.g. 30 miles per gallon). They are reciprocal.Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use valueReference to link the value for the fuel economy to another value.''', related_name="vehicle_fuelefficiency")
	knownVehicleDamages = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Knownvehicledamages", help_text='''A textual description of known damages, both repaired and unrepaired.''', related_name="vehicle_knownvehicledamages")
	vehicleConfiguration = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehicleconfiguration", help_text='''A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'.''', related_name="vehicle_vehicleconfiguration")
	vehicleEngine = models.ForeignKey('EngineSpecification', on_delete=models.CASCADE, verbose_name="Vehicleengine", help_text='''Information about the engine or engines of the vehicle.''', related_name="vehicle_vehicleengine")
	mileageFromOdometer = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Mileagefromodometer", help_text='''The total distance travelled by the particular vehicle since its initial production, as read from its odometer.Typical unit code(s): KMT for kilometers, SMI for statute miles''', related_name="vehicle_mileagefromodometer")
	fuelConsumption = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Fuelconsumption", help_text='''The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km).Note 1: There are unfortunately no standard unit codes for liters per 100 km.Use unitText to indicate the unit of measurement, e.g. L/100 km.Note 2: There are two ways of indicating the fuel consumption, fuelConsumption (e.g. 8 liters per 100 km) and fuelEfficiency (e.g. 30 miles per gallon). They are reciprocal.Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use valueReference to link the value for the fuel consumption to another value.''', related_name="vehicle_fuelconsumption")
	product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product", related_name="vehicle_product")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", related_name="vehicle_thing")

	content_type = models.ForeignKey(ContentType)
	object_id = models.PositiveIntegerField()
	content_object = GenericForeignKey('content_type', 'object_id')

	def __str__(self):
		return self.id

	class Meta:
		verbose_name = 'Vehicle'
		verbose_name_plural = 'Vehicle'
