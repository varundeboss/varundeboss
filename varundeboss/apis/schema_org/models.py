from __future__ import unicode_literals

from django.db import models

from django.contrib.contenttypes.fields import GenericForeignKey
from django.contrib.contenttypes.models import ContentType

# Create your models here.

class Preschool(models.Model):

	educationalOrganization = models.ForeignKey('EducationalOrganization', on_delete=models.CASCADE, verbose_name="Educationalorganization", blank=True, null=True, help_text='''An educational organization.''', related_name="preschool_educationalorganization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Preschool'
		verbose_name_plural = 'Preschool'


class LiteraryEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="literaryevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LiteraryEvent'
		verbose_name_plural = 'LiteraryEvent'


class AllocateAction(models.Model):

	organizeAction = models.ForeignKey('OrganizeAction', on_delete=models.CASCADE, verbose_name="Organizeaction", blank=True, null=True, help_text='''The act of manipulating/administering/supervising/controlling one or more objects.''', related_name="allocateaction_organizeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AllocateAction'
		verbose_name_plural = 'AllocateAction'


class LoseAction(models.Model):

	achieveAction = models.ForeignKey('AchieveAction', on_delete=models.CASCADE, verbose_name="Achieveaction", blank=True, null=True, help_text='''The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process.''', related_name="loseaction_achieveaction")
	winnerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Winner", blank=True, null=True, help_text='''A sub property of participant. The winner of the action.''', related_name="loseaction_winner_person")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LoseAction'
		verbose_name_plural = 'LoseAction'


class AutoRental(models.Model):

	automotiveBusiness = models.ForeignKey('AutomotiveBusiness', on_delete=models.CASCADE, verbose_name="Automotivebusiness", blank=True, null=True, help_text='''Car repair, sales, or parts.''', related_name="autorental_automotivebusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AutoRental'
		verbose_name_plural = 'AutoRental'


class LodgingReservation(models.Model):

	lodgingUnitTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Lodgingunittype", blank=True, null=True, help_text='''Textual description of the unit type (including suite vs. room, size of bed, etc.).''', related_name="lodgingreservation_lodgingunittype_text")
	lodgingUnitTypeQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Lodgingunittype", blank=True, null=True, help_text='''Textual description of the unit type (including suite vs. room, size of bed, etc.).''', related_name="lodgingreservation_lodgingunittype_qualitativevalue")
	numChildrenInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numchildren", blank=True, null=True, help_text='''The number of children staying in the unit.''', related_name="lodgingreservation_numchildren_integer")
	numChildrenQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numchildren", blank=True, null=True, help_text='''The number of children staying in the unit.''', related_name="lodgingreservation_numchildren_quantitativevalue")
	numAdultsQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numadults", blank=True, null=True, help_text='''The number of adults staying in the unit.''', related_name="lodgingreservation_numadults_quantitativevalue")
	numAdultsInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numadults", blank=True, null=True, help_text='''The number of adults staying in the unit.''', related_name="lodgingreservation_numadults_integer")
	lodgingUnitDescriptionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Lodgingunitdescription", blank=True, null=True, help_text='''A full description of the lodging unit.''', related_name="lodgingreservation_lodgingunitdescription_text")
	checkoutTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Checkouttime", blank=True, null=True, help_text='''The latest someone may check out of a lodging establishment.''', related_name="lodgingreservation_checkouttime_datetime")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", blank=True, null=True, help_text='''Describes a reservation for travel, dining or an event. Some reservations require tickets.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use http://schema.org/Offer.''', related_name="lodgingreservation_reservation")
	checkinTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Checkintime", blank=True, null=True, help_text='''The earliest someone may check into a lodging establishment.''', related_name="lodgingreservation_checkintime_datetime")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LodgingReservation'
		verbose_name_plural = 'LodgingReservation'


class ActionStatusType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="actionstatustype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ActionStatusType'
		verbose_name_plural = 'ActionStatusType'


class ItemPage(models.Model):

	webPage = models.ForeignKey('WebPage', on_delete=models.CASCADE, verbose_name="Webpage", blank=True, null=True, help_text='''A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.''', related_name="itempage_webpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ItemPage'
		verbose_name_plural = 'ItemPage'


class PerformingGroup(models.Model):

	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", blank=True, null=True, help_text='''An organization such as a school, NGO, corporation, club, etc.''', related_name="performinggroup_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PerformingGroup'
		verbose_name_plural = 'PerformingGroup'


class Casino(models.Model):

	entertainmentBusiness = models.ForeignKey('EntertainmentBusiness', on_delete=models.CASCADE, verbose_name="Entertainmentbusiness", blank=True, null=True, help_text='''A business providing entertainment.''', related_name="casino_entertainmentbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Casino'
		verbose_name_plural = 'Casino'


class URL(models.Model):

	text = models.TextField(blank=True, null=True, verbose_name="Text", help_text='''Data type: Text.''')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'URL'
		verbose_name_plural = 'URL'


class HomeAndConstructionBusiness(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="homeandconstructionbusiness_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HomeAndConstructionBusiness'
		verbose_name_plural = 'HomeAndConstructionBusiness'


class InviteAction(models.Model):

	eventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''Upcoming or past event associated with this place, organization, or action.''', related_name="inviteaction_event_event")
	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="Communicateaction", blank=True, null=True, help_text='''The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.''', related_name="inviteaction_communicateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'InviteAction'
		verbose_name_plural = 'InviteAction'


class Flight(models.Model):

	departureTerminalText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Departureterminal", blank=True, null=True, help_text='''Identifier of the flight's departure terminal.''', related_name="flight_departureterminal_text")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="flight_intangible")
	aircraftText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Aircraft", blank=True, null=True, help_text='''The kind of aircraft (e.g., "Boeing 747").''', related_name="flight_aircraft_text")
	aircraftVehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, verbose_name="Aircraft", blank=True, null=True, help_text='''The kind of aircraft (e.g., "Boeing 747").''', related_name="flight_aircraft_vehicle")
	arrivalTerminalText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Arrivalterminal", blank=True, null=True, help_text='''Identifier of the flight's arrival terminal.''', related_name="flight_arrivalterminal_text")
	flightNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Flightnumber", blank=True, null=True, help_text='''The unique identifier for a flight including the airline IATA code. For example, if describing United flight 110, where the IATA code for United is 'UA', the flightNumber is 'UA110'.''', related_name="flight_flightnumber_text")
	departureTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Departuretime", blank=True, null=True, help_text='''The expected departure time.''', related_name="flight_departuretime_datetime")
	mealServiceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mealservice", blank=True, null=True, help_text='''Description of the meals that will be provided or available for purchase.''', related_name="flight_mealservice_text")
	sellerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="flight_seller_organization")
	sellerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="flight_seller_person")
	arrivalTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Arrivaltime", blank=True, null=True, help_text='''The expected arrival time.''', related_name="flight_arrivaltime_datetime")
	departureGateText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Departuregate", blank=True, null=True, help_text='''Identifier of the flight's departure gate.''', related_name="flight_departuregate_text")
	estimatedFlightDurationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Estimatedflightduration", blank=True, null=True, help_text='''The estimated time the flight will take.''', related_name="flight_estimatedflightduration_text")
	estimatedFlightDurationDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Estimatedflightduration", blank=True, null=True, help_text='''The estimated time the flight will take.''', related_name="flight_estimatedflightduration_duration")
	departureAirportAirport = models.ForeignKey('Airport', on_delete=models.CASCADE, verbose_name="Departureairport", blank=True, null=True, help_text='''The airport where the flight originates.''', related_name="flight_departureairport_airport")
	flightDistanceDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Flightdistance", blank=True, null=True, help_text='''The distance of the flight.''', related_name="flight_flightdistance_distance")
	flightDistanceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Flightdistance", blank=True, null=True, help_text='''The distance of the flight.''', related_name="flight_flightdistance_text")
	arrivalAirportAirport = models.ForeignKey('Airport', on_delete=models.CASCADE, verbose_name="Arrivalairport", blank=True, null=True, help_text='''The airport where the flight terminates.''', related_name="flight_arrivalairport_airport")
	providerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="flight_provider_organization")
	providerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="flight_provider_person")
	webCheckinTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Webcheckintime", blank=True, null=True, help_text='''The time when a passenger can check into the flight online.''', related_name="flight_webcheckintime_datetime")
	boardingPolicyBoardingPolicyType = models.ForeignKey('BoardingPolicyType', on_delete=models.CASCADE, verbose_name="Boardingpolicy", blank=True, null=True, help_text='''The type of boarding policy used by the airline (e.g. zone-based or group-based).''', related_name="flight_boardingpolicy_boardingpolicytype")
	arrivalGateText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Arrivalgate", blank=True, null=True, help_text='''Identifier of the flight's arrival gate.''', related_name="flight_arrivalgate_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Flight'
		verbose_name_plural = 'Flight'


class ClothingStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="clothingstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ClothingStore'
		verbose_name_plural = 'ClothingStore'


class ContactPointOption(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="contactpointoption_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ContactPointOption'
		verbose_name_plural = 'ContactPointOption'


class PropertyValue(models.Model):

	unitCodeURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Unitcode", blank=True, null=True, help_text='''The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.''', related_name="propertyvalue_unitcode_url")
	unitCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unitcode", blank=True, null=True, help_text='''The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.''', related_name="propertyvalue_unitcode_text")
	minValueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Minvalue", blank=True, null=True, help_text='''The lower value of some characteristic or property.''', related_name="propertyvalue_minvalue_number")
	unitTextText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unittext", blank=True, null=True, help_text='''A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
<a href='unitCode'>unitCode</a>.''', related_name="propertyvalue_unittext_text")
	valueReferencePropertyValue = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="propertyvalue_valuereference_propertyvalue")
	valueReferenceEnumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="propertyvalue_valuereference_enumeration")
	valueReferenceStructuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="propertyvalue_valuereference_structuredvalue")
	valueReferenceQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="propertyvalue_valuereference_quantitativevalue")
	valueReferenceQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="propertyvalue_valuereference_qualitativevalue")
	propertyIDURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Propertyid", blank=True, null=True, help_text='''A commonly used identifier for the characteristic represented by the property, e.g. a manufacturer or a standard code for a property. propertyID can be
(1) a prefixed string, mainly meant to be used with standards for product properties; (2) a site-specific, non-prefixed string (e.g. the primary key of the property or the vendor-specific id of the property), or (3)
a URL indicating the type of the property, either pointing to an external vocabulary, or a Web resource that describes the property (e.g. a glossary entry).
Standards bodies should promote a standard prefix for the identifiers of properties from their standards.''', related_name="propertyvalue_propertyid_url")
	propertyIDText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Propertyid", blank=True, null=True, help_text='''A commonly used identifier for the characteristic represented by the property, e.g. a manufacturer or a standard code for a property. propertyID can be
(1) a prefixed string, mainly meant to be used with standards for product properties; (2) a site-specific, non-prefixed string (e.g. the primary key of the property or the vendor-specific id of the property), or (3)
a URL indicating the type of the property, either pointing to an external vocabulary, or a Web resource that describes the property (e.g. a glossary entry).
Standards bodies should promote a standard prefix for the identifiers of properties from their standards.''', related_name="propertyvalue_propertyid_text")
	valueStructuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="propertyvalue_value_structuredvalue")
	valueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="propertyvalue_value_number")
	valueBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="propertyvalue_value_boolean")
	valueText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="propertyvalue_value_text")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="propertyvalue_structuredvalue")
	maxValueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Maxvalue", blank=True, null=True, help_text='''The upper value of some characteristic or property.''', related_name="propertyvalue_maxvalue_number")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PropertyValue'
		verbose_name_plural = 'PropertyValue'


class BusinessEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="businessevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BusinessEvent'
		verbose_name_plural = 'BusinessEvent'


class FollowAction(models.Model):

	interactAction = models.ForeignKey('InteractAction', on_delete=models.CASCADE, verbose_name="Interactaction", blank=True, null=True, help_text='''The act of interacting with another person or organization.''', related_name="followaction_interactaction")
	followeeOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Followee", blank=True, null=True, help_text='''A sub property of object. The person or organization being followed.''', related_name="followaction_followee_organization")
	followeePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Followee", blank=True, null=True, help_text='''A sub property of object. The person or organization being followed.''', related_name="followaction_followee_person")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FollowAction'
		verbose_name_plural = 'FollowAction'


class TieAction(models.Model):

	achieveAction = models.ForeignKey('AchieveAction', on_delete=models.CASCADE, verbose_name="Achieveaction", blank=True, null=True, help_text='''The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process.''', related_name="tieaction_achieveaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TieAction'
		verbose_name_plural = 'TieAction'


class BodyOfWater(models.Model):

	landform = models.ForeignKey('Landform', on_delete=models.CASCADE, verbose_name="Landform", blank=True, null=True, help_text='''A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.''', related_name="bodyofwater_landform")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BodyOfWater'
		verbose_name_plural = 'BodyOfWater'


class ReservationPackage(models.Model):

	subReservationReservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Subreservation", blank=True, null=True, help_text='''The individual reservations included in the package. Typically a repeated property.''', related_name="reservationpackage_subreservation_reservation")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", blank=True, null=True, help_text='''Describes a reservation for travel, dining or an event. Some reservations require tickets.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use http://schema.org/Offer.''', related_name="reservationpackage_reservation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReservationPackage'
		verbose_name_plural = 'ReservationPackage'


class Message(models.Model):

	senderAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Sender", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the sending end of the action.''', related_name="message_sender_audience")
	senderOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Sender", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the sending end of the action.''', related_name="message_sender_organization")
	senderPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Sender", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the sending end of the action.''', related_name="message_sender_person")
	dateReceivedDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datereceived", blank=True, null=True, help_text='''The date/time the message was received if a single recipient exists.''', related_name="message_datereceived_datetime")
	dateReadDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Dateread", blank=True, null=True, help_text='''The date/time at which the message has been read by the recipient if a single recipient exists.''', related_name="message_dateread_datetime")
	dateSentDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datesent", blank=True, null=True, help_text='''The date/time at which the message was sent.''', related_name="message_datesent_datetime")
	messageAttachmentCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Messageattachment", blank=True, null=True, help_text='''A CreativeWork attached to the message.''', related_name="message_messageattachment_creativework")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="message_creativework")
	recipientPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="message_recipient_person")
	recipientAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="message_recipient_audience")
	recipientOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="message_recipient_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Message'
		verbose_name_plural = 'Message'


class EducationEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="educationevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EducationEvent'
		verbose_name_plural = 'EducationEvent'


class EntryPoint(models.Model):

	contentTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Contenttype", blank=True, null=True, help_text='''The supported content type(s) for an EntryPoint response.''', related_name="entrypoint_contenttype_text")
	actionPlatformURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Actionplatform", blank=True, null=True, help_text='''The high level platform(s) where the Action can be performed for the given URL. To specify a specific application or operating system instance, use actionApplication.''', related_name="entrypoint_actionplatform_url")
	actionPlatformText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Actionplatform", blank=True, null=True, help_text='''The high level platform(s) where the Action can be performed for the given URL. To specify a specific application or operating system instance, use actionApplication.''', related_name="entrypoint_actionplatform_text")
	actionApplicationSoftwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Actionapplication", blank=True, null=True, help_text='''An application that can complete the request.''', related_name="entrypoint_actionapplication_softwareapplication")
	urlTemplateText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Urltemplate", blank=True, null=True, help_text='''An url template (RFC6570) that will be used to construct the target of the execution of the action.''', related_name="entrypoint_urltemplate_text")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="entrypoint_intangible")
	httpMethodText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Httpmethod", blank=True, null=True, help_text='''An HTTP method that specifies the appropriate HTTP method for a request to an HTTP EntryPoint. Values are capitalized strings as used in HTTP.''', related_name="entrypoint_httpmethod_text")
	encodingTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Encodingtype", blank=True, null=True, help_text='''The supported encoding type(s) for an EntryPoint request.''', related_name="entrypoint_encodingtype_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EntryPoint'
		verbose_name_plural = 'EntryPoint'


class DeliveryEvent(models.Model):

	accessCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accesscode", blank=True, null=True, help_text='''Password, PIN, or access code needed for delivery (e.g. from a locker).''', related_name="deliveryevent_accesscode_text")
	availableThroughDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availablethrough", blank=True, null=True, help_text='''After this date, the item will no longer be available for pickup.''', related_name="deliveryevent_availablethrough_datetime")
	availableFromDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availablefrom", blank=True, null=True, help_text='''When the item is available for pickup from the store, locker, etc.''', related_name="deliveryevent_availablefrom_datetime")
	hasDeliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Hasdeliverymethod", blank=True, null=True, help_text='''Method used for delivery or shipping.''', related_name="deliveryevent_hasdeliverymethod_deliverymethod")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="deliveryevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DeliveryEvent'
		verbose_name_plural = 'DeliveryEvent'


class WebSite(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="website_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WebSite'
		verbose_name_plural = 'WebSite'


class LiveBlogPosting(models.Model):

	coverageEndTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Coverageendtime", blank=True, null=True, help_text='''The time when the live blog will stop covering the Event. Note that coverage may continue after the Event concludes.''', related_name="liveblogposting_coverageendtime_datetime")
	coverageStartTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Coveragestarttime", blank=True, null=True, help_text='''The time when the live blog will begin covering the Event. Note that coverage may begin before the Event's start time. The LiveBlogPosting may also be created before coverage begins.''', related_name="liveblogposting_coveragestarttime_datetime")
	blogPosting = models.ForeignKey('BlogPosting', on_delete=models.CASCADE, verbose_name="Blogposting", blank=True, null=True, help_text='''A blog post.''', related_name="liveblogposting_blogposting")
	liveBlogUpdateBlogPosting = models.ForeignKey('BlogPosting', on_delete=models.CASCADE, verbose_name="Liveblogupdate", blank=True, null=True, help_text='''An update to the LiveBlog.''', related_name="liveblogposting_liveblogupdate_blogposting")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LiveBlogPosting'
		verbose_name_plural = 'LiveBlogPosting'


class CompoundPriceSpecification(models.Model):

	priceComponentUnitPriceSpecification = models.ForeignKey('UnitPriceSpecification', on_delete=models.CASCADE, verbose_name="Pricecomponent", blank=True, null=True, help_text='''This property links to all UnitPriceSpecification nodes that apply in parallel for the CompoundPriceSpecification node.''', related_name="compoundpricespecification_pricecomponent_unitpricespecification")
	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", blank=True, null=True, help_text='''A structured value representing a price or price range. Typically, only the subclasses of this type are used for markup. It is recommended to use [[MonetaryAmount]] to describe independent amounts of money such as a salary, credit card limits, etc.''', related_name="compoundpricespecification_pricespecification")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CompoundPriceSpecification'
		verbose_name_plural = 'CompoundPriceSpecification'


class VisualArtsEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="visualartsevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'VisualArtsEvent'
		verbose_name_plural = 'VisualArtsEvent'


class TrainReservation(models.Model):

	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", blank=True, null=True, help_text='''Describes a reservation for travel, dining or an event. Some reservations require tickets.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use http://schema.org/Offer.''', related_name="trainreservation_reservation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TrainReservation'
		verbose_name_plural = 'TrainReservation'


class MensClothingStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="mensclothingstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MensClothingStore'
		verbose_name_plural = 'MensClothingStore'


class PresentationDigitalDocument(models.Model):

	digitalDocument = models.ForeignKey('DigitalDocument', on_delete=models.CASCADE, verbose_name="Digitaldocument", blank=True, null=True, help_text='''An electronic file or document.''', related_name="presentationdigitaldocument_digitaldocument")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PresentationDigitalDocument'
		verbose_name_plural = 'PresentationDigitalDocument'


class PerformanceRole(models.Model):

	characterNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Charactername", blank=True, null=True, help_text='''The name of a character played in some acting or performing role, i.e. in a PerformanceRole.''', related_name="performancerole_charactername_text")
	role = models.ForeignKey('Role', on_delete=models.CASCADE, verbose_name="Role", blank=True, null=True, help_text='''Represents additional information about a relationship or property. For example a Role can be used to say that a 'member' role linking some SportsTeam to a player occurred during a particular time period. Or that a Person's 'actor' role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like 'member' or 'actor'.

      <br/><br/>See also <a href="http://blog.schema.org/2014/06/introducing-role.html">blog post</a>.''', related_name="performancerole_role")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PerformanceRole'
		verbose_name_plural = 'PerformanceRole'


class VisualArtwork(models.Model):

	depthDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Depth", blank=True, null=True, help_text='''The depth of the item.''', related_name="visualartwork_depth_distance")
	depthQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Depth", blank=True, null=True, help_text='''The depth of the item.''', related_name="visualartwork_depth_quantitativevalue")
	artMediumURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Artmedium", blank=True, null=True, help_text='''The material used. (e.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype, Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.)''', related_name="visualartwork_artmedium_url")
	artMediumText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Artmedium", blank=True, null=True, help_text='''The material used. (e.g. Oil, Watercolour, Acrylic, Linoprint, Marble, Cyanotype, Digital, Lithograph, DryPoint, Intaglio, Pastel, Woodcut, Pencil, Mixed Media, etc.)''', related_name="visualartwork_artmedium_text")
	artformURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Artform", blank=True, null=True, help_text='''e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc.''', related_name="visualartwork_artform_url")
	artformText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Artform", blank=True, null=True, help_text='''e.g. Painting, Drawing, Sculpture, Print, Photograph, Assemblage, Collage, etc.''', related_name="visualartwork_artform_text")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="visualartwork_creativework")
	widthQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Width", blank=True, null=True, help_text='''The width of the item.''', related_name="visualartwork_width_quantitativevalue")
	widthDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Width", blank=True, null=True, help_text='''The width of the item.''', related_name="visualartwork_width_distance")
	artEditionInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Artedition", blank=True, null=True, help_text='''The number of copies when multiple copies of a piece of artwork are produced - e.g. for a limited edition of 20 prints, 'artEdition' refers to the total number of copies (in this example "20").''', related_name="visualartwork_artedition_integer")
	artEditionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Artedition", blank=True, null=True, help_text='''The number of copies when multiple copies of a piece of artwork are produced - e.g. for a limited edition of 20 prints, 'artEdition' refers to the total number of copies (in this example "20").''', related_name="visualartwork_artedition_text")
	artworkSurfaceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Artworksurface", blank=True, null=True, help_text='''The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc.''', related_name="visualartwork_artworksurface_text")
	artworkSurfaceURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Artworksurface", blank=True, null=True, help_text='''The supporting materials for the artwork, e.g. Canvas, Paper, Wood, Board, etc.''', related_name="visualartwork_artworksurface_url")
	heightQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Height", blank=True, null=True, help_text='''The height of the item.''', related_name="visualartwork_height_quantitativevalue")
	heightDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Height", blank=True, null=True, help_text='''The height of the item.''', related_name="visualartwork_height_distance")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'VisualArtwork'
		verbose_name_plural = 'VisualArtwork'


class ShareAction(models.Model):

	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="Communicateaction", blank=True, null=True, help_text='''The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.''', related_name="shareaction_communicateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ShareAction'
		verbose_name_plural = 'ShareAction'


class LendAction(models.Model):

	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="Transferaction", blank=True, null=True, help_text='''The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.''', related_name="lendaction_transferaction")
	borrowerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Borrower", blank=True, null=True, help_text='''A sub property of participant. The person that borrows the object being lent.''', related_name="lendaction_borrower_person")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LendAction'
		verbose_name_plural = 'LendAction'


class Text(models.Model):

	value = models.TextField(blank=True, null=True, verbose_name="Value", help_text='''Data type: Text.''')

	def __str__(self):
		return str(self.value)

	class Meta:
		verbose_name = 'Text'
		verbose_name_plural = 'Text'


class NoteDigitalDocument(models.Model):

	digitalDocument = models.ForeignKey('DigitalDocument', on_delete=models.CASCADE, verbose_name="Digitaldocument", blank=True, null=True, help_text='''An electronic file or document.''', related_name="notedigitaldocument_digitaldocument")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'NoteDigitalDocument'
		verbose_name_plural = 'NoteDigitalDocument'


class Book(models.Model):

	numberOfPagesInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofpages", blank=True, null=True, help_text='''The number of pages in the book.''', related_name="book_numberofpages_integer")
	illustratorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Illustrator", blank=True, null=True, help_text='''The illustrator of the book.''', related_name="book_illustrator_person")
	bookEditionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Bookedition", blank=True, null=True, help_text='''The edition of the book.''', related_name="book_bookedition_text")
	bookFormatBookFormatType = models.ForeignKey('BookFormatType', on_delete=models.CASCADE, verbose_name="Bookformat", blank=True, null=True, help_text='''The format of the book.''', related_name="book_bookformat_bookformattype")
	isbnText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isbn", blank=True, null=True, help_text='''The ISBN of the book.''', related_name="book_isbn_text")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="book_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Book'
		verbose_name_plural = 'Book'


class Attorney(models.Model):

	legalService = models.ForeignKey('LegalService', on_delete=models.CASCADE, verbose_name="Legalservice", blank=True, null=True, help_text='''A LegalService is a business that provides legally-oriented services, advice and representation, e.g. law firms.
        <br><br>
        As a <a href="/LocalBusiness">LocalBusiness</a> it can be
        described as a <a href="/provider">provider</a> of one or more
        <a href="/Service">Service(s)</a>.
      ''', related_name="attorney_legalservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Attorney'
		verbose_name_plural = 'Attorney'


class RecyclingCenter(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="recyclingcenter_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RecyclingCenter'
		verbose_name_plural = 'RecyclingCenter'


class ComputerStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="computerstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ComputerStore'
		verbose_name_plural = 'ComputerStore'


class Brewery(models.Model):

	foodEstablishment = models.ForeignKey('FoodEstablishment', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A food-related business.''', related_name="brewery_foodestablishment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Brewery'
		verbose_name_plural = 'Brewery'


class ReceiveAction(models.Model):

	senderAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Sender", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the sending end of the action.''', related_name="receiveaction_sender_audience")
	senderOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Sender", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the sending end of the action.''', related_name="receiveaction_sender_organization")
	senderPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Sender", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the sending end of the action.''', related_name="receiveaction_sender_person")
	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="Transferaction", blank=True, null=True, help_text='''The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.''', related_name="receiveaction_transferaction")
	deliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Deliverymethod", blank=True, null=True, help_text='''A sub property of instrument. The method of delivery.''', related_name="receiveaction_deliverymethod_deliverymethod")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReceiveAction'
		verbose_name_plural = 'ReceiveAction'


class Winery(models.Model):

	foodEstablishment = models.ForeignKey('FoodEstablishment', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A food-related business.''', related_name="winery_foodestablishment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Winery'
		verbose_name_plural = 'Winery'


class BikeStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="bikestore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BikeStore'
		verbose_name_plural = 'BikeStore'


class TipAction(models.Model):

	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="Tradeaction", blank=True, null=True, help_text='''The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.''', related_name="tipaction_tradeaction")
	recipientPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="tipaction_recipient_person")
	recipientAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="tipaction_recipient_audience")
	recipientOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="tipaction_recipient_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TipAction'
		verbose_name_plural = 'TipAction'


class TravelAction(models.Model):

	distanceDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Distance", blank=True, null=True, help_text='''The distance travelled, e.g. exercising or travelling.''', related_name="travelaction_distance_distance")
	moveAction = models.ForeignKey('MoveAction', on_delete=models.CASCADE, verbose_name="Moveaction", blank=True, null=True, help_text='''The act of an agent relocating to a place.<p>Related actions:</p><ul><li><a href="http://schema.org/TransferAction">TransferAction</a>: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object</li></ul>.''', related_name="travelaction_moveaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TravelAction'
		verbose_name_plural = 'TravelAction'


class QAPage(models.Model):

	webPage = models.ForeignKey('WebPage', on_delete=models.CASCADE, verbose_name="Webpage", blank=True, null=True, help_text='''A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.''', related_name="qapage_webpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'QAPage'
		verbose_name_plural = 'QAPage'


class Museum(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="museum_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Museum'
		verbose_name_plural = 'Museum'


class StadiumOrArena(models.Model):

	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sports location, such as a playing field.''', related_name="stadiumorarena_sportsactivitylocation")
	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="stadiumorarena_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'StadiumOrArena'
		verbose_name_plural = 'StadiumOrArena'


class ConsumeAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="consumeaction_action")
	expectsAcceptanceOfOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Expectsacceptanceof", blank=True, null=True, help_text='''An Offer which must be accepted before the user can perform the Action. For example, the user may need to buy a movie before being able to watch it.''', related_name="consumeaction_expectsacceptanceof_offer")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ConsumeAction'
		verbose_name_plural = 'ConsumeAction'


class MusicAlbum(models.Model):

	albumReleaseTypeMusicAlbumReleaseType = models.ForeignKey('MusicAlbumReleaseType', on_delete=models.CASCADE, verbose_name="Albumreleasetype", blank=True, null=True, help_text='''The kind of release which this album is: single, EP or album.''', related_name="musicalbum_albumreleasetype_musicalbumreleasetype")
	albumProductionTypeMusicAlbumProductionType = models.ForeignKey('MusicAlbumProductionType', on_delete=models.CASCADE, verbose_name="Albumproductiontype", blank=True, null=True, help_text='''Classification of the album by it's type of content: soundtrack, live album, studio album, etc.''', related_name="musicalbum_albumproductiontype_musicalbumproductiontype")
	albumReleaseMusicRelease = models.ForeignKey('MusicRelease', on_delete=models.CASCADE, verbose_name="Albumrelease", blank=True, null=True, help_text='''A release of this album.''', related_name="musicalbum_albumrelease_musicrelease")
	musicPlaylist = models.ForeignKey('MusicPlaylist', on_delete=models.CASCADE, verbose_name="Musicplaylist", blank=True, null=True, help_text='''A collection of music tracks in playlist form.''', related_name="musicalbum_musicplaylist")
	byArtistMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Byartist", blank=True, null=True, help_text='''The artist that performed this album or recording.''', related_name="musicalbum_byartist_musicgroup")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicAlbum'
		verbose_name_plural = 'MusicAlbum'


class Boolean(models.Model):

	value = models.NullBooleanField(blank=True, null=True, verbose_name="Value", help_text='''Boolean: True or False.''')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Boolean'
		verbose_name_plural = 'Boolean'


class RadioEpisode(models.Model):

	episode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", blank=True, null=True, help_text='''A media episode (e.g. TV, radio, video game) which can be part of a series or season.''', related_name="radioepisode_episode")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RadioEpisode'
		verbose_name_plural = 'RadioEpisode'


class Reservation(models.Model):

	priceCurrencyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricecurrency", blank=True, null=True, help_text='''The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.''', related_name="reservation_pricecurrency_text")
	bookingTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Bookingtime", blank=True, null=True, help_text='''The date and time the reservation was booked.''', related_name="reservation_bookingtime_datetime")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="reservation_intangible")
	totalPriceNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Totalprice", blank=True, null=True, help_text='''The total price for the reservation or ticket, including applicable taxes, shipping, etc.''', related_name="reservation_totalprice_number")
	totalPricePriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Totalprice", blank=True, null=True, help_text='''The total price for the reservation or ticket, including applicable taxes, shipping, etc.''', related_name="reservation_totalprice_pricespecification")
	totalPriceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Totalprice", blank=True, null=True, help_text='''The total price for the reservation or ticket, including applicable taxes, shipping, etc.''', related_name="reservation_totalprice_text")
	brokerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Broker", blank=True, null=True, help_text='''An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.''', related_name="reservation_broker_person")
	brokerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Broker", blank=True, null=True, help_text='''An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.''', related_name="reservation_broker_organization")
	modifiedTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Modifiedtime", blank=True, null=True, help_text='''The date and time the reservation was modified.''', related_name="reservation_modifiedtime_datetime")
	reservedTicketTicket = models.ForeignKey('Ticket', on_delete=models.CASCADE, verbose_name="Reservedticket", blank=True, null=True, help_text='''A ticket associated with the reservation.''', related_name="reservation_reservedticket_ticket")
	reservationStatusReservationStatusType = models.ForeignKey('ReservationStatusType', on_delete=models.CASCADE, verbose_name="Reservationstatus", blank=True, null=True, help_text='''The current status of the reservation.''', related_name="reservation_reservationstatus_reservationstatustype")
	programMembershipUsedProgramMembership = models.ForeignKey('ProgramMembership', on_delete=models.CASCADE, verbose_name="Programmembershipused", blank=True, null=True, help_text='''Any membership in a frequent flyer, hotel loyalty program, etc. being applied to the reservation.''', related_name="reservation_programmembershipused_programmembership")
	providerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="reservation_provider_organization")
	providerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="reservation_provider_person")
	reservationForThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Reservationfor", blank=True, null=True, help_text='''The thing -- flight, event, restaurant,etc. being reserved.''', related_name="reservation_reservationfor_thing")
	reservationIdText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Reservationid", blank=True, null=True, help_text='''A unique identifier for the reservation.''', related_name="reservation_reservationid_text")
	underNamePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Undername", blank=True, null=True, help_text='''The person or organization the reservation or ticket is for.''', related_name="reservation_undername_person")
	underNameOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Undername", blank=True, null=True, help_text='''The person or organization the reservation or ticket is for.''', related_name="reservation_undername_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Reservation'
		verbose_name_plural = 'Reservation'


class Article(models.Model):

	pageStartText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pagestart", blank=True, null=True, help_text='''The page on which the work starts; for example "135" or "xiii".''', related_name="article_pagestart_text")
	pageStartInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Pagestart", blank=True, null=True, help_text='''The page on which the work starts; for example "135" or "xiii".''', related_name="article_pagestart_integer")
	pageEndInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Pageend", blank=True, null=True, help_text='''The page on which the work ends; for example "138" or "xvi".''', related_name="article_pageend_integer")
	pageEndText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pageend", blank=True, null=True, help_text='''The page on which the work ends; for example "138" or "xvi".''', related_name="article_pageend_text")
	articleSectionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Articlesection", blank=True, null=True, help_text='''Articles may belong to one or more 'sections' in a magazine or newspaper, such as Sports, Lifestyle, etc.''', related_name="article_articlesection_text")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="article_creativework")
	articleBodyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Articlebody", blank=True, null=True, help_text='''The actual body of the article.''', related_name="article_articlebody_text")
	wordCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Wordcount", blank=True, null=True, help_text='''The number of words in the text of the Article.''', related_name="article_wordcount_integer")
	paginationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pagination", blank=True, null=True, help_text='''Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".''', related_name="article_pagination_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Article'
		verbose_name_plural = 'Article'


class BedAndBreakfast(models.Model):

	lodgingBusiness = models.ForeignKey('LodgingBusiness', on_delete=models.CASCADE, verbose_name="Lodgingbusiness", blank=True, null=True, help_text='''A lodging business, such as a motel, hotel, or inn.''', related_name="bedandbreakfast_lodgingbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BedAndBreakfast'
		verbose_name_plural = 'BedAndBreakfast'


class PoliceStation(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="policestation_civicstructure")
	emergencyService = models.ForeignKey('EmergencyService', on_delete=models.CASCADE, verbose_name="Emergencyservice", blank=True, null=True, help_text='''An emergency service, such as a fire station or ER.''', related_name="policestation_emergencyservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PoliceStation'
		verbose_name_plural = 'PoliceStation'


class Enumeration(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="enumeration_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Enumeration'
		verbose_name_plural = 'Enumeration'


class GolfCourse(models.Model):

	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sports location, such as a playing field.''', related_name="golfcourse_sportsactivitylocation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GolfCourse'
		verbose_name_plural = 'GolfCourse'


class ViewAction(models.Model):

	consumeAction = models.ForeignKey('ConsumeAction', on_delete=models.CASCADE, verbose_name="Consumeaction", blank=True, null=True, help_text='''The act of ingesting information/resources/food.''', related_name="viewaction_consumeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ViewAction'
		verbose_name_plural = 'ViewAction'


class DigitalDocumentPermissionType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="digitaldocumentpermissiontype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DigitalDocumentPermissionType'
		verbose_name_plural = 'DigitalDocumentPermissionType'


class ImageObject(models.Model):

	exifDataText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Exifdata", blank=True, null=True, help_text='''exif data for this object.''', related_name="imageobject_exifdata_text")
	exifDataPropertyValue = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Exifdata", blank=True, null=True, help_text='''exif data for this object.''', related_name="imageobject_exifdata_propertyvalue")
	thumbnailImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Thumbnail", blank=True, null=True, help_text='''Thumbnail image for an image or video.''', related_name="imageobject_thumbnail_imageobject")
	mediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="Mediaobject", blank=True, null=True, help_text='''An image, video, or audio object embedded in a web page. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).''', related_name="imageobject_mediaobject")
	representativeOfPageBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Representativeofpage", blank=True, null=True, help_text='''Indicates whether this image is representative of the content of the page.''', related_name="imageobject_representativeofpage_boolean")
	captionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Caption", blank=True, null=True, help_text='''The caption for this object.''', related_name="imageobject_caption_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ImageObject'
		verbose_name_plural = 'ImageObject'


class Quantity(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="quantity_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Quantity'
		verbose_name_plural = 'Quantity'


class Rating(models.Model):

	bestRatingNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Bestrating", blank=True, null=True, help_text='''The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.''', related_name="rating_bestrating_number")
	bestRatingText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Bestrating", blank=True, null=True, help_text='''The highest value allowed in this rating system. If bestRating is omitted, 5 is assumed.''', related_name="rating_bestrating_text")
	ratingValueText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Ratingvalue", blank=True, null=True, help_text='''The rating for the content.''', related_name="rating_ratingvalue_text")
	worstRatingNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Worstrating", blank=True, null=True, help_text='''The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.''', related_name="rating_worstrating_number")
	worstRatingText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Worstrating", blank=True, null=True, help_text='''The lowest value allowed in this rating system. If worstRating is omitted, 1 is assumed.''', related_name="rating_worstrating_text")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="rating_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Rating'
		verbose_name_plural = 'Rating'


class OrderItem(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="orderitem_intangible")
	orderItemStatusOrderStatus = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, verbose_name="Orderitemstatus", blank=True, null=True, help_text='''The current status of the order item.''', related_name="orderitem_orderitemstatus_orderstatus")
	orderQuantityNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Orderquantity", blank=True, null=True, help_text='''The number of the item ordered. If the property is not set, assume the quantity is one.''', related_name="orderitem_orderquantity_number")
	orderDeliveryParcelDelivery = models.ForeignKey('ParcelDelivery', on_delete=models.CASCADE, verbose_name="Orderdelivery", blank=True, null=True, help_text='''The delivery of the parcel related to this order or order item.''', related_name="orderitem_orderdelivery_parceldelivery")
	orderedItemOrderItem = models.ForeignKey('OrderItem', on_delete=models.CASCADE, verbose_name="Ordereditem", blank=True, null=True, help_text='''The item ordered.''', related_name="orderitem_ordereditem_orderitem")
	orderedItemProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Ordereditem", blank=True, null=True, help_text='''The item ordered.''', related_name="orderitem_ordereditem_product")
	orderItemNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Orderitemnumber", blank=True, null=True, help_text='''The identifier of the order item.''', related_name="orderitem_orderitemnumber_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OrderItem'
		verbose_name_plural = 'OrderItem'


class AnimalShelter(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="animalshelter_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AnimalShelter'
		verbose_name_plural = 'AnimalShelter'


class InteractAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="interactaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'InteractAction'
		verbose_name_plural = 'InteractAction'


class CollegeOrUniversity(models.Model):

	educationalOrganization = models.ForeignKey('EducationalOrganization', on_delete=models.CASCADE, verbose_name="Educationalorganization", blank=True, null=True, help_text='''An educational organization.''', related_name="collegeoruniversity_educationalorganization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CollegeOrUniversity'
		verbose_name_plural = 'CollegeOrUniversity'


class Integer(models.Model):

	number = models.IntegerField(blank=True, null=True, verbose_name="Number", help_text='''Data type: Number.''')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Integer'
		verbose_name_plural = 'Integer'


class DownloadAction(models.Model):

	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="Transferaction", blank=True, null=True, help_text='''The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.''', related_name="downloadaction_transferaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DownloadAction'
		verbose_name_plural = 'DownloadAction'


class WPAdBlock(models.Model):

	webPageElement = models.ForeignKey('WebPageElement', on_delete=models.CASCADE, verbose_name="Webpageelement", blank=True, null=True, help_text='''A web page element, like a table or an image.''', related_name="wpadblock_webpageelement")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WPAdBlock'
		verbose_name_plural = 'WPAdBlock'


class CheckOutAction(models.Model):

	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="Communicateaction", blank=True, null=True, help_text='''The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.''', related_name="checkoutaction_communicateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CheckOutAction'
		verbose_name_plural = 'CheckOutAction'


class Review(models.Model):

	reviewBodyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Reviewbody", blank=True, null=True, help_text='''The actual body of the review.''', related_name="review_reviewbody_text")
	reviewRatingRating = models.ForeignKey('Rating', on_delete=models.CASCADE, verbose_name="Reviewrating", blank=True, null=True, help_text='''The rating given in this review. Note that reviews can themselves be rated. The <code>reviewRating</code> applies to rating given by the review. The <code>aggregateRating</code> property applies to the review itself, as a creative work.''', related_name="review_reviewrating_rating")
	itemReviewedThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Itemreviewed", blank=True, null=True, help_text='''The item that is being reviewed/rated.''', related_name="review_itemreviewed_thing")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="review_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Review'
		verbose_name_plural = 'Review'


class AgreeAction(models.Model):

	reactAction = models.ForeignKey('ReactAction', on_delete=models.CASCADE, verbose_name="Reactaction", blank=True, null=True, help_text='''The act of responding instinctively and emotionally to an object, expressing a sentiment.''', related_name="agreeaction_reactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AgreeAction'
		verbose_name_plural = 'AgreeAction'


class WarrantyPromise(models.Model):

	durationOfWarrantyQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Durationofwarranty", blank=True, null=True, help_text='''The duration of the warranty promise. Common unitCode values are ANN for year, MON for months, or DAY for days.''', related_name="warrantypromise_durationofwarranty_quantitativevalue")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="warrantypromise_structuredvalue")
	warrantyScopeWarrantyScope = models.ForeignKey('WarrantyScope', on_delete=models.CASCADE, verbose_name="Warrantyscope", blank=True, null=True, help_text='''The scope of the warranty promise.''', related_name="warrantypromise_warrantyscope_warrantyscope")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WarrantyPromise'
		verbose_name_plural = 'WarrantyPromise'


class MovieClip(models.Model):

	clip = models.ForeignKey('Clip', on_delete=models.CASCADE, verbose_name="Clip", blank=True, null=True, help_text='''A short TV or radio program or a segment/part of a program.''', related_name="movieclip_clip")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MovieClip'
		verbose_name_plural = 'MovieClip'


class CommentAction(models.Model):

	resultCommentComment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Resultcomment", blank=True, null=True, help_text='''A sub property of result. The Comment created or sent as a result of this action.''', related_name="commentaction_resultcomment_comment")
	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="Communicateaction", blank=True, null=True, help_text='''The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.''', related_name="commentaction_communicateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CommentAction'
		verbose_name_plural = 'CommentAction'


class FoodEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="foodevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FoodEvent'
		verbose_name_plural = 'FoodEvent'


class SelfStorage(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="selfstorage_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SelfStorage'
		verbose_name_plural = 'SelfStorage'


class ShoeStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="shoestore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ShoeStore'
		verbose_name_plural = 'ShoeStore'


class AutomotiveBusiness(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="automotivebusiness_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AutomotiveBusiness'
		verbose_name_plural = 'AutomotiveBusiness'


class Order(models.Model):

	orderDeliveryParcelDelivery = models.ForeignKey('ParcelDelivery', on_delete=models.CASCADE, verbose_name="Orderdelivery", blank=True, null=True, help_text='''The delivery of the parcel related to this order or order item.''', related_name="order_orderdelivery_parceldelivery")
	discountCurrencyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Discountcurrency", blank=True, null=True, help_text='''The currency (in 3-letter ISO 4217 format) of the discount.''', related_name="order_discountcurrency_text")
	brokerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Broker", blank=True, null=True, help_text='''An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.''', related_name="order_broker_person")
	brokerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Broker", blank=True, null=True, help_text='''An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.''', related_name="order_broker_organization")
	discountCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Discountcode", blank=True, null=True, help_text='''Code used to redeem a discount.''', related_name="order_discountcode_text")
	paymentMethodPaymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Paymentmethod", blank=True, null=True, help_text='''The name of the credit card or other method of payment for the order.''', related_name="order_paymentmethod_paymentmethod")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="order_intangible")
	billingAddressPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Billingaddress", blank=True, null=True, help_text='''The billing address for the order.''', related_name="order_billingaddress_postaladdress")
	paymentMethodIdText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Paymentmethodid", blank=True, null=True, help_text='''An identifier for the method of payment used (e.g. the last 4 digits of the credit card).''', related_name="order_paymentmethodid_text")
	orderStatusOrderStatus = models.ForeignKey('OrderStatus', on_delete=models.CASCADE, verbose_name="Orderstatus", blank=True, null=True, help_text='''The current status of the order.''', related_name="order_orderstatus_orderstatus")
	paymentUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Paymenturl", blank=True, null=True, help_text='''The URL for sending a payment.''', related_name="order_paymenturl_url")
	orderedItemOrderItem = models.ForeignKey('OrderItem', on_delete=models.CASCADE, verbose_name="Ordereditem", blank=True, null=True, help_text='''The item ordered.''', related_name="order_ordereditem_orderitem")
	orderedItemProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Ordereditem", blank=True, null=True, help_text='''The item ordered.''', related_name="order_ordereditem_product")
	sellerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="order_seller_organization")
	sellerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="order_seller_person")
	customerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Customer", blank=True, null=True, help_text='''Party placing the order or paying the invoice.''', related_name="order_customer_organization")
	customerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Customer", blank=True, null=True, help_text='''Party placing the order or paying the invoice.''', related_name="order_customer_person")
	acceptedOfferOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Acceptedoffer", blank=True, null=True, help_text='''The offer(s) -- e.g., product, quantity and price combinations -- included in the order.''', related_name="order_acceptedoffer_offer")
	paymentDueDateDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Paymentduedate", blank=True, null=True, help_text='''The date that payment is due.''', related_name="order_paymentduedate_datetime")
	confirmationNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Confirmationnumber", blank=True, null=True, help_text='''A number that confirms the given order or payment has been received.''', related_name="order_confirmationnumber_text")
	orderNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Ordernumber", blank=True, null=True, help_text='''The identifier of the transaction.''', related_name="order_ordernumber_text")
	orderDateDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Orderdate", blank=True, null=True, help_text='''Date order was placed.''', related_name="order_orderdate_datetime")
	partOfInvoiceInvoice = models.ForeignKey('Invoice', on_delete=models.CASCADE, verbose_name="Partofinvoice", blank=True, null=True, help_text='''The order is being paid as part of the referenced Invoice.''', related_name="order_partofinvoice_invoice")
	isGiftBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Isgift", blank=True, null=True, help_text='''Was the offer accepted as a gift for someone other than the buyer.''', related_name="order_isgift_boolean")
	discountNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Discount", blank=True, null=True, help_text='''Any discount applied (to an Order).''', related_name="order_discount_number")
	discountText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Discount", blank=True, null=True, help_text='''Any discount applied (to an Order).''', related_name="order_discount_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Order'
		verbose_name_plural = 'Order'


class WPHeader(models.Model):

	webPageElement = models.ForeignKey('WebPageElement', on_delete=models.CASCADE, verbose_name="Webpageelement", blank=True, null=True, help_text='''A web page element, like a table or an image.''', related_name="wpheader_webpageelement")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WPHeader'
		verbose_name_plural = 'WPHeader'


class LikeAction(models.Model):

	reactAction = models.ForeignKey('ReactAction', on_delete=models.CASCADE, verbose_name="Reactaction", blank=True, null=True, help_text='''The act of responding instinctively and emotionally to an object, expressing a sentiment.''', related_name="likeaction_reactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LikeAction'
		verbose_name_plural = 'LikeAction'


class CableOrSatelliteService(models.Model):

	service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Service", blank=True, null=True, help_text='''A service provided by an organization, e.g. delivery service, print services, etc.''', related_name="cableorsatelliteservice_service")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CableOrSatelliteService'
		verbose_name_plural = 'CableOrSatelliteService'


class ChildrensEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="childrensevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ChildrensEvent'
		verbose_name_plural = 'ChildrensEvent'


class Vehicle(models.Model):

	vehicleConfigurationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehicleconfiguration", blank=True, null=True, help_text='''A short text indicating the configuration of the vehicle, e.g. '5dr hatchback ST 2.5 MT 225 hp' or 'limited edition'.''', related_name="vehicle_vehicleconfiguration_text")
	driveWheelConfigurationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Drivewheelconfiguration", blank=True, null=True, help_text='''The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle's engine via the drivetrain.''', related_name="vehicle_drivewheelconfiguration_text")
	driveWheelConfigurationDriveWheelConfigurationValue = models.ForeignKey('DriveWheelConfigurationValue', on_delete=models.CASCADE, verbose_name="Drivewheelconfiguration", blank=True, null=True, help_text='''The drive wheel configuration, i.e. which roadwheels will receive torque from the vehicle's engine via the drivetrain.''', related_name="vehicle_drivewheelconfiguration_drivewheelconfigurationvalue")
	vehicleInteriorColorText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehicleinteriorcolor", blank=True, null=True, help_text='''The color or color combination of the interior of the vehicle.''', related_name="vehicle_vehicleinteriorcolor_text")
	numberOfDoorsNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Numberofdoors", blank=True, null=True, help_text='''The number of doors.<br />
Typical unit code(s): C62''', related_name="vehicle_numberofdoors_number")
	numberOfDoorsQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofdoors", blank=True, null=True, help_text='''The number of doors.<br />
Typical unit code(s): C62''', related_name="vehicle_numberofdoors_quantitativevalue")
	vehicleTransmissionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehicletransmission", blank=True, null=True, help_text='''The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) ("gearbox" for cars).''', related_name="vehicle_vehicletransmission_text")
	vehicleTransmissionURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Vehicletransmission", blank=True, null=True, help_text='''The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) ("gearbox" for cars).''', related_name="vehicle_vehicletransmission_url")
	vehicleTransmissionQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Vehicletransmission", blank=True, null=True, help_text='''The type of component used for transmitting the power from a rotating power source to the wheels or other relevant component(s) ("gearbox" for cars).''', related_name="vehicle_vehicletransmission_qualitativevalue")
	vehicleSeatingCapacityQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Vehicleseatingcapacity", blank=True, null=True, help_text='''The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.<br />
Typical unit code(s): C62 for persons.''', related_name="vehicle_vehicleseatingcapacity_quantitativevalue")
	vehicleSeatingCapacityNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Vehicleseatingcapacity", blank=True, null=True, help_text='''The number of passengers that can be seated in the vehicle, both in terms of the physical space available, and in terms of limitations set by law.<br />
Typical unit code(s): C62 for persons.''', related_name="vehicle_vehicleseatingcapacity_number")
	cargoVolumeQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Cargovolume", blank=True, null=True, help_text='''The available volume for cargo or luggage. For automobiles, this is usually the trunk volume.<br />
Typical unit code(s): LTR for liters, FTQ for cubic foot/feet<br />

Note: You can use <a href="minValue">minValue</a> and <a href="maxValue">maxValue</a> to indicate ranges.''', related_name="vehicle_cargovolume_quantitativevalue")
	knownVehicleDamagesText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Knownvehicledamages", blank=True, null=True, help_text='''A textual description of known damages, both repaired and unrepaired.''', related_name="vehicle_knownvehicledamages_text")
	vehicleEngineEngineSpecification = models.ForeignKey('EngineSpecification', on_delete=models.CASCADE, verbose_name="Vehicleengine", blank=True, null=True, help_text='''Information about the engine or engines of the vehicle.''', related_name="vehicle_vehicleengine_enginespecification")
	dateVehicleFirstRegisteredDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Datevehiclefirstregistered", blank=True, null=True, help_text='''The date of the first registration of the vehicle with the respective public authorities.''', related_name="vehicle_datevehiclefirstregistered_date")
	vehicleIdentificationNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehicleidentificationnumber", blank=True, null=True, help_text='''The Vehicle Identification Number (VIN) is a unique serial number used by the automotive industry to identify individual motor vehicles.''', related_name="vehicle_vehicleidentificationnumber_text")
	productionDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Productiondate", blank=True, null=True, help_text='''The date of production of the item, e.g. vehicle.''', related_name="vehicle_productiondate_date")
	vehicleModelDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Vehiclemodeldate", blank=True, null=True, help_text='''The release date of a vehicle model (often used to differentiate versions of the same make and model).''', related_name="vehicle_vehiclemodeldate_date")
	numberOfForwardGearsNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Numberofforwardgears", blank=True, null=True, help_text='''The total number of forward gears available for the transmission system of the vehicle.<br />
Typical unit code(s): C62''', related_name="vehicle_numberofforwardgears_number")
	numberOfForwardGearsQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofforwardgears", blank=True, null=True, help_text='''The total number of forward gears available for the transmission system of the vehicle.<br />
Typical unit code(s): C62''', related_name="vehicle_numberofforwardgears_quantitativevalue")
	fuelConsumptionQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Fuelconsumption", blank=True, null=True, help_text='''The amount of fuel consumed for traveling a particular distance or temporal duration with the given vehicle (e.g. liters per 100 km).<br />
Note 1: There are unfortunately no standard unit codes for liters per 100 km.<br />
Use <a href="unitText">unitText</a> to indicate the unit of measurement, e.g. L/100 km.
Note 2: There are two ways of indicating the fuel consumption, <a href="fuelConsumption">fuelConsumption</a> (e.g. 8 liters per 100 km) and <a href="fuelEfficiency">fuelEfficiency</a> (e.g. 30 miles per gallon). They are reciprocal.<br />
Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use <a href="valueReference">valueReference</a> to link the value for the fuel consumption to another value.''', related_name="vehicle_fuelconsumption_quantitativevalue")
	numberOfAirbagsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Numberofairbags", blank=True, null=True, help_text='''The number or type of airbags in the vehicle.''', related_name="vehicle_numberofairbags_text")
	numberOfAirbagsNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Numberofairbags", blank=True, null=True, help_text='''The number or type of airbags in the vehicle.''', related_name="vehicle_numberofairbags_number")
	purchaseDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Purchasedate", blank=True, null=True, help_text='''The date the item e.g. vehicle was purchased by the current owner.''', related_name="vehicle_purchasedate_date")
	numberOfPreviousOwnersQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofpreviousowners", blank=True, null=True, help_text='''The number of owners of the vehicle, including the current one.<br />
Typical unit code(s): C62''', related_name="vehicle_numberofpreviousowners_quantitativevalue")
	numberOfPreviousOwnersNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Numberofpreviousowners", blank=True, null=True, help_text='''The number of owners of the vehicle, including the current one.<br />
Typical unit code(s): C62''', related_name="vehicle_numberofpreviousowners_number")
	product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product", blank=True, null=True, help_text='''Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.''', related_name="vehicle_product")
	mileageFromOdometerQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Mileagefromodometer", blank=True, null=True, help_text='''The total distance travelled by the particular vehicle since its initial production, as read from its odometer.<br />
Typical unit code(s): KMT for kilometers, SMI for statute miles''', related_name="vehicle_mileagefromodometer_quantitativevalue")
	fuelEfficiencyQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Fuelefficiency", blank=True, null=True, help_text='''The distance traveled per unit of fuel used; most commonly miles per gallon (mpg) or kilometers per liter (km/L).<br />
Note 1: There are unfortunately no standard unit codes for miles per gallon or kilometers per liter.<br />
Use <a href="unitText">unitText</a> to indicate the unit of measurement, e.g. mpg or km/L.
Note 2: There are two ways of indicating the fuel consumption, <a href="fuelConsumption">fuelConsumption</a> (e.g. 8 liters per 100 km) and <a href="fuelEfficiency">fuelEfficiency</a> (e.g. 30 miles per gallon). They are reciprocal.<br />
Note 3: Often, the absolute value is useful only when related to driving speed ("at 80 km/h") or usage pattern ("city traffic"). You can use <a href="valueReference">valueReference</a> to link the value for the fuel economy to another value.''', related_name="vehicle_fuelefficiency_quantitativevalue")
	fuelTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Fueltype", blank=True, null=True, help_text='''The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.''', related_name="vehicle_fueltype_text")
	fuelTypeQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Fueltype", blank=True, null=True, help_text='''The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.''', related_name="vehicle_fueltype_qualitativevalue")
	fuelTypeURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Fueltype", blank=True, null=True, help_text='''The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.''', related_name="vehicle_fueltype_url")
	steeringPositionSteeringPositionValue = models.ForeignKey('SteeringPositionValue', on_delete=models.CASCADE, verbose_name="Steeringposition", blank=True, null=True, help_text='''The position of the steering wheel or similar device (mostly for cars).''', related_name="vehicle_steeringposition_steeringpositionvalue")
	numberOfAxlesQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofaxles", blank=True, null=True, help_text='''The number of axles.<br />
Typical unit code(s): C62''', related_name="vehicle_numberofaxles_quantitativevalue")
	numberOfAxlesNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Numberofaxles", blank=True, null=True, help_text='''The number of axles.<br />
Typical unit code(s): C62''', related_name="vehicle_numberofaxles_number")
	vehicleSpecialUsageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehiclespecialusage", blank=True, null=True, help_text='''Indicates whether the vehicle has been used for special purposes, like commercial rental, driving school, or as a taxi. The legislation in many countries requires this information to be revealed when offering a car for sale.''', related_name="vehicle_vehiclespecialusage_text")
	vehicleInteriorTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vehicleinteriortype", blank=True, null=True, help_text='''The type or material of the interior of the vehicle (e.g. synthetic fabric, leather, wood, etc.). While most interior types are characterized by the material used, an interior type can also be based on vehicle usage or target audience.''', related_name="vehicle_vehicleinteriortype_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Vehicle'
		verbose_name_plural = 'Vehicle'


class SkiResort(models.Model):

	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sports location, such as a playing field.''', related_name="skiresort_sportsactivitylocation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SkiResort'
		verbose_name_plural = 'SkiResort'


class NGO(models.Model):

	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", blank=True, null=True, help_text='''An organization such as a school, NGO, corporation, club, etc.''', related_name="ngo_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'NGO'
		verbose_name_plural = 'NGO'


class OutletStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="outletstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OutletStore'
		verbose_name_plural = 'OutletStore'


class AccountingService(models.Model):

	financialService = models.ForeignKey('FinancialService', on_delete=models.CASCADE, verbose_name="Financialservice", blank=True, null=True, help_text='''Financial services business.''', related_name="accountingservice_financialservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AccountingService'
		verbose_name_plural = 'AccountingService'


class Organization(models.Model):

	memberPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Member", blank=True, null=True, help_text='''A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.''', related_name="organization_member_person")
	memberOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Member", blank=True, null=True, help_text='''A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.''', related_name="organization_member_organization")
	memberOfOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Memberof", blank=True, null=True, help_text='''An Organization (or ProgramMembership) to which this Person or Organization belongs.''', related_name="organization_memberof_organization")
	memberOfProgramMembership = models.ForeignKey('ProgramMembership', on_delete=models.CASCADE, verbose_name="Memberof", blank=True, null=True, help_text='''An Organization (or ProgramMembership) to which this Person or Organization belongs.''', related_name="organization_memberof_programmembership")
	awardText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", blank=True, null=True, help_text='''An award won by or for this item.''', related_name="organization_award_text")
	taxIDText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Taxid", blank=True, null=True, help_text='''The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.''', related_name="organization_taxid_text")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", blank=True, null=True, help_text='''The most generic type of item.''', related_name="organization_thing")
	dunsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Duns", blank=True, null=True, help_text='''The Dun & Bradstreet DUNS number for identifying an organization or business person.''', related_name="organization_duns_text")
	isicV4Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isicv4", blank=True, null=True, help_text='''The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.''', related_name="organization_isicv4_text")
	leiCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Leicode", blank=True, null=True, help_text='''An organization identifier that uniquely identifies a legal entity as defined in ISO 17442.''', related_name="organization_leicode_text")
	eventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''Upcoming or past event associated with this place, organization, or action.''', related_name="organization_event_event")
	reviewReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", blank=True, null=True, help_text='''A review of the item.''', related_name="organization_review_review")
	numberOfEmployeesQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofemployees", blank=True, null=True, help_text='''The number of employees in an organization e.g. business.''', related_name="organization_numberofemployees_quantitativevalue")
	departmentOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Department", blank=True, null=True, help_text='''A relationship between an organization and a department of that organization, also described as an organization (allowing different urls, logos, opening hours). For example: a store with a pharmacy, or a bakery with a cafe.''', related_name="organization_department_organization")
	brandBrand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name="Brand", blank=True, null=True, help_text='''The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.''', related_name="organization_brand_brand")
	brandOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Brand", blank=True, null=True, help_text='''The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.''', related_name="organization_brand_organization")
	areaServedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="organization_areaserved_text")
	areaServedAdministrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="organization_areaserved_administrativearea")
	areaServedPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="organization_areaserved_place")
	areaServedGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="organization_areaserved_geoshape")
	parentOrganizationOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Parentorganization", blank=True, null=True, help_text='''The larger organization that this local business is a branch of, if any.''', related_name="organization_parentorganization_organization")
	addressPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="organization_address_postaladdress")
	addressText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="organization_address_text")
	contactPointContactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Contactpoint", blank=True, null=True, help_text='''A contact point for a person or organization.''', related_name="organization_contactpoint_contactpoint")
	subOrganizationOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Suborganization", blank=True, null=True, help_text='''A relationship between two organizations where the first includes the second, e.g., as a subsidiary. See also: the more specific 'department' property.''', related_name="organization_suborganization_organization")
	foundingDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Foundingdate", blank=True, null=True, help_text='''The date that this organization was founded.''', related_name="organization_foundingdate_date")
	alumniPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Alumni", blank=True, null=True, help_text='''Alumni of an organization.''', related_name="organization_alumni_person")
	vatIDText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vatid", blank=True, null=True, help_text='''The Value-added Tax ID of the organization or person.''', related_name="organization_vatid_text")
	seeksDemand = models.ForeignKey('Demand', on_delete=models.CASCADE, verbose_name="Seeks", blank=True, null=True, help_text='''A pointer to products or services sought by the organization or person (demand).''', related_name="organization_seeks_demand")
	sponsorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Sponsor", blank=True, null=True, help_text='''A person or organization that supports a thing through a pledge, promise, or financial contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.''', related_name="organization_sponsor_person")
	sponsorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Sponsor", blank=True, null=True, help_text='''A person or organization that supports a thing through a pledge, promise, or financial contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.''', related_name="organization_sponsor_organization")
	emailText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Email", blank=True, null=True, help_text='''Email address.''', related_name="organization_email_text")
	faxNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Faxnumber", blank=True, null=True, help_text='''The fax number.''', related_name="organization_faxnumber_text")
	locationPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Location", blank=True, null=True, help_text='''The location of for example where the event is happening, an organization is located, or where an action takes place.''', related_name="organization_location_postaladdress")
	locationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Location", blank=True, null=True, help_text='''The location of for example where the event is happening, an organization is located, or where an action takes place.''', related_name="organization_location_place")
	locationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Location", blank=True, null=True, help_text='''The location of for example where the event is happening, an organization is located, or where an action takes place.''', related_name="organization_location_text")
	hasPOSPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Haspos", blank=True, null=True, help_text='''Points-of-Sales operated by the organization or person.''', related_name="organization_haspos_place")
	hasOfferCatalogOfferCatalog = models.ForeignKey('OfferCatalog', on_delete=models.CASCADE, verbose_name="Hasoffercatalog", blank=True, null=True, help_text='''Indicates an OfferCatalog listing for this Organization, Person, or Service.''', related_name="organization_hasoffercatalog_offercatalog")
	telephoneText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Telephone", blank=True, null=True, help_text='''The telephone number.''', related_name="organization_telephone_text")
	aggregateRatingAggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", blank=True, null=True, help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="organization_aggregaterating_aggregaterating")
	founderPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Founder", blank=True, null=True, help_text='''A person who founded this organization.''', related_name="organization_founder_person")
	employeePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Employee", blank=True, null=True, help_text='''Someone working for this organization.''', related_name="organization_employee_person")
	logoURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="organization_logo_url")
	logoImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="organization_logo_imageobject")
	ownsOwnershipInfo = models.ForeignKey('OwnershipInfo', on_delete=models.CASCADE, verbose_name="Owns", blank=True, null=True, help_text='''Products owned by the organization or person.''', related_name="organization_owns_ownershipinfo")
	ownsProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Owns", blank=True, null=True, help_text='''Products owned by the organization or person.''', related_name="organization_owns_product")
	legalNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Legalname", blank=True, null=True, help_text='''The official name of the organization, e.g. the registered company name.''', related_name="organization_legalname_text")
	naicsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Naics", blank=True, null=True, help_text='''The North American Industry Classification System (NAICS) code for a particular organization or business person.''', related_name="organization_naics_text")
	dissolutionDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Dissolutiondate", blank=True, null=True, help_text='''The date that this organization was dissolved.''', related_name="organization_dissolutiondate_date")
	foundingLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Foundinglocation", blank=True, null=True, help_text='''The place where the Organization was founded.''', related_name="organization_foundinglocation_place")
	makesOfferOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Makesoffer", blank=True, null=True, help_text='''A pointer to products or services offered by the organization or person.''', related_name="organization_makesoffer_offer")
	globalLocationNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Globallocationnumber", blank=True, null=True, help_text='''The <a href="http://www.gs1.org/gln">Global Location Number</a> (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.''', related_name="organization_globallocationnumber_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Organization'
		verbose_name_plural = 'Organization'


class Sculpture(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="sculpture_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Sculpture'
		verbose_name_plural = 'Sculpture'


class RoofingContractor(models.Model):

	homeAndConstructionBusiness = models.ForeignKey('HomeAndConstructionBusiness', on_delete=models.CASCADE, verbose_name="Homeandconstructionbusiness", blank=True, null=True, help_text='''A construction business.
        <br><br>
        A HomeAndConstructionBusiness is a LocalBusiness that provides services around homes and buildings.
          <br><br>
          As a <a href="/LocalBusiness">LocalBusiness</a> it can be
          described as a <a href="/provider">provider</a> of one or more
          <a href="/Service">Service(s)</a>.
      ''', related_name="roofingcontractor_homeandconstructionbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RoofingContractor'
		verbose_name_plural = 'RoofingContractor'


class ElectronicsStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="electronicsstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ElectronicsStore'
		verbose_name_plural = 'ElectronicsStore'


class DryCleaningOrLaundry(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="drycleaningorlaundry_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DryCleaningOrLaundry'
		verbose_name_plural = 'DryCleaningOrLaundry'


class AcceptAction(models.Model):

	allocateAction = models.ForeignKey('AllocateAction', on_delete=models.CASCADE, verbose_name="Allocateaction", blank=True, null=True, help_text='''The act of organizing tasks/objects/events by associating resources to it.''', related_name="acceptaction_allocateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AcceptAction'
		verbose_name_plural = 'AcceptAction'


class BusinessAudience(models.Model):

	yearlyRevenueQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Yearlyrevenue", blank=True, null=True, help_text='''The size of the business in annual revenue.''', related_name="businessaudience_yearlyrevenue_quantitativevalue")
	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", blank=True, null=True, help_text='''Intended audience for an item, i.e. the group for whom the item was created.''', related_name="businessaudience_audience")
	numberOfEmployeesQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofemployees", blank=True, null=True, help_text='''The number of employees in an organization e.g. business.''', related_name="businessaudience_numberofemployees_quantitativevalue")
	yearsInOperationQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Yearsinoperation", blank=True, null=True, help_text='''The age of the business.''', related_name="businessaudience_yearsinoperation_quantitativevalue")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BusinessAudience'
		verbose_name_plural = 'BusinessAudience'


class Electrician(models.Model):

	homeAndConstructionBusiness = models.ForeignKey('HomeAndConstructionBusiness', on_delete=models.CASCADE, verbose_name="Homeandconstructionbusiness", blank=True, null=True, help_text='''A construction business.
        <br><br>
        A HomeAndConstructionBusiness is a LocalBusiness that provides services around homes and buildings.
          <br><br>
          As a <a href="/LocalBusiness">LocalBusiness</a> it can be
          described as a <a href="/provider">provider</a> of one or more
          <a href="/Service">Service(s)</a>.
      ''', related_name="electrician_homeandconstructionbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Electrician'
		verbose_name_plural = 'Electrician'


class GovernmentBuilding(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="governmentbuilding_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GovernmentBuilding'
		verbose_name_plural = 'GovernmentBuilding'


class Conversation(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="conversation_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Conversation'
		verbose_name_plural = 'Conversation'


class MotorcycleDealer(models.Model):

	automotiveBusiness = models.ForeignKey('AutomotiveBusiness', on_delete=models.CASCADE, verbose_name="Automotivebusiness", blank=True, null=True, help_text='''Car repair, sales, or parts.''', related_name="motorcycledealer_automotivebusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MotorcycleDealer'
		verbose_name_plural = 'MotorcycleDealer'


class SellAction(models.Model):

	buyerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Buyer", blank=True, null=True, help_text='''A sub property of participant. The participant/person/organization that bought the object.''', related_name="sellaction_buyer_person")
	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="Tradeaction", blank=True, null=True, help_text='''The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.''', related_name="sellaction_tradeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SellAction'
		verbose_name_plural = 'SellAction'


class CheckoutPage(models.Model):

	webPage = models.ForeignKey('WebPage', on_delete=models.CASCADE, verbose_name="Webpage", blank=True, null=True, help_text='''A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.''', related_name="checkoutpage_webpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CheckoutPage'
		verbose_name_plural = 'CheckoutPage'


class BeautySalon(models.Model):

	healthAndBeautyBusiness = models.ForeignKey('HealthAndBeautyBusiness', on_delete=models.CASCADE, verbose_name="Healthandbeautybusiness", blank=True, null=True, help_text='''Health and beauty.''', related_name="beautysalon_healthandbeautybusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BeautySalon'
		verbose_name_plural = 'BeautySalon'


class Specialty(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="specialty_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Specialty'
		verbose_name_plural = 'Specialty'


class Map(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="map_creativework")
	mapTypeMapCategoryType = models.ForeignKey('MapCategoryType', on_delete=models.CASCADE, verbose_name="Maptype", blank=True, null=True, help_text='''Indicates the kind of Map, from the MapCategoryType Enumeration.''', related_name="map_maptype_mapcategorytype")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Map'
		verbose_name_plural = 'Map'


class PeopleAudience(models.Model):

	suggestedMaxAgeNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Suggestedmaxage", blank=True, null=True, help_text='''Maximal age recommended for viewing content.''', related_name="peopleaudience_suggestedmaxage_number")
	requiredMinAgeInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Requiredminage", blank=True, null=True, help_text='''Audiences defined by a person's minimum age.''', related_name="peopleaudience_requiredminage_integer")
	suggestedMinAgeNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Suggestedminage", blank=True, null=True, help_text='''Minimal age recommended for viewing content.''', related_name="peopleaudience_suggestedminage_number")
	requiredMaxAgeInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Requiredmaxage", blank=True, null=True, help_text='''Audiences defined by a person's maximum age.''', related_name="peopleaudience_requiredmaxage_integer")
	suggestedGenderText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Suggestedgender", blank=True, null=True, help_text='''The gender of the person or audience.''', related_name="peopleaudience_suggestedgender_text")
	requiredGenderText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Requiredgender", blank=True, null=True, help_text='''Audiences defined by a person's gender.''', related_name="peopleaudience_requiredgender_text")
	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", blank=True, null=True, help_text='''Intended audience for an item, i.e. the group for whom the item was created.''', related_name="peopleaudience_audience")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PeopleAudience'
		verbose_name_plural = 'PeopleAudience'


class WinAction(models.Model):

	achieveAction = models.ForeignKey('AchieveAction', on_delete=models.CASCADE, verbose_name="Achieveaction", blank=True, null=True, help_text='''The act of accomplishing something via previous efforts. It is an instantaneous action rather than an ongoing process.''', related_name="winaction_achieveaction")
	loserPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Loser", blank=True, null=True, help_text='''A sub property of participant. The loser of the action.''', related_name="winaction_loser_person")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WinAction'
		verbose_name_plural = 'WinAction'


class GeoShape(models.Model):

	postalCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Postalcode", blank=True, null=True, help_text='''The postal code. For example, 94043.''', related_name="geoshape_postalcode_text")
	elevationNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Elevation", blank=True, null=True, help_text='''The elevation of a location (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).''', related_name="geoshape_elevation_number")
	elevationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Elevation", blank=True, null=True, help_text='''The elevation of a location (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).''', related_name="geoshape_elevation_text")
	lineText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Line", blank=True, null=True, help_text='''A line is a point-to-point path consisting of two or more points. A line is expressed as a series of two or more point objects separated by space.''', related_name="geoshape_line_text")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="geoshape_structuredvalue")
	addressCountryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Addresscountry", blank=True, null=True, help_text='''The country. For example, USA. You can also provide the two-letter <a href='http://en.wikipedia.org/wiki/ISO_3166-1'>ISO 3166-1 alpha-2 country code</a>.''', related_name="geoshape_addresscountry_text")
	addressCountryCountry = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Addresscountry", blank=True, null=True, help_text='''The country. For example, USA. You can also provide the two-letter <a href='http://en.wikipedia.org/wiki/ISO_3166-1'>ISO 3166-1 alpha-2 country code</a>.''', related_name="geoshape_addresscountry_country")
	addressPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="geoshape_address_postaladdress")
	addressText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="geoshape_address_text")
	polygonText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Polygon", blank=True, null=True, help_text='''A polygon is the area enclosed by a point-to-point path for which the starting and ending points are the same. A polygon is expressed as a series of four or more space delimited points where the first and final points are identical.''', related_name="geoshape_polygon_text")
	boxText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Box", blank=True, null=True, help_text='''A box is the area enclosed by the rectangle formed by two points. The first point is the lower corner, the second point is the upper corner. A box is expressed as two points separated by a space character.''', related_name="geoshape_box_text")
	circleText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Circle", blank=True, null=True, help_text='''A circle is the circular region of a specified radius centered at a specified latitude and longitude. A circle is expressed as a pair followed by a radius in meters.''', related_name="geoshape_circle_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GeoShape'
		verbose_name_plural = 'GeoShape'


class AssessAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="assessaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AssessAction'
		verbose_name_plural = 'AssessAction'


class Audience(models.Model):

	audienceTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Audiencetype", blank=True, null=True, help_text='''The target group associated with a given audience (e.g. veterans, car owners, musicians, etc.).''', related_name="audience_audiencetype_text")
	geographicAreaAdministrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Geographicarea", blank=True, null=True, help_text='''The geographic area associated with the audience.''', related_name="audience_geographicarea_administrativearea")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="audience_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Audience'
		verbose_name_plural = 'Audience'


class Store(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="store_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Store'
		verbose_name_plural = 'Store'


class FurnitureStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="furniturestore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FurnitureStore'
		verbose_name_plural = 'FurnitureStore'


class DigitalDocument(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="digitaldocument_creativework")
	hasDigitalDocumentPermissionDigitalDocumentPermission = models.ForeignKey('DigitalDocumentPermission', on_delete=models.CASCADE, verbose_name="Hasdigitaldocumentpermission", blank=True, null=True, help_text='''A permission related to the access to this document (e.g. permission to read or write an electronic document). For a public document, specify a grantee with an Audience with audienceType equal to "public".''', related_name="digitaldocument_hasdigitaldocumentpermission_digitaldocumentpermission")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DigitalDocument'
		verbose_name_plural = 'DigitalDocument'


class FindAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="findaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FindAction'
		verbose_name_plural = 'FindAction'


class PublicationVolume(models.Model):

	pageStartText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pagestart", blank=True, null=True, help_text='''The page on which the work starts; for example "135" or "xiii".''', related_name="publicationvolume_pagestart_text")
	pageStartInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Pagestart", blank=True, null=True, help_text='''The page on which the work starts; for example "135" or "xiii".''', related_name="publicationvolume_pagestart_integer")
	pageEndInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Pageend", blank=True, null=True, help_text='''The page on which the work ends; for example "138" or "xvi".''', related_name="publicationvolume_pageend_integer")
	pageEndText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pageend", blank=True, null=True, help_text='''The page on which the work ends; for example "138" or "xvi".''', related_name="publicationvolume_pageend_text")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="publicationvolume_creativework")
	volumeNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Volumenumber", blank=True, null=True, help_text='''Identifies the volume of publication or multi-part work; for example, "iii" or "2".''', related_name="publicationvolume_volumenumber_text")
	volumeNumberInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Volumenumber", blank=True, null=True, help_text='''Identifies the volume of publication or multi-part work; for example, "iii" or "2".''', related_name="publicationvolume_volumenumber_integer")
	paginationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pagination", blank=True, null=True, help_text='''Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".''', related_name="publicationvolume_pagination_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PublicationVolume'
		verbose_name_plural = 'PublicationVolume'


class MusicVenue(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="musicvenue_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicVenue'
		verbose_name_plural = 'MusicVenue'


class MovieRentalStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="movierentalstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MovieRentalStore'
		verbose_name_plural = 'MovieRentalStore'


class Invoice(models.Model):

	referencesOrderOrder = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name="Referencesorder", blank=True, null=True, help_text='''The Order(s) related to this Invoice. One or more Orders may be combined into a single Invoice.''', related_name="invoice_referencesorder_order")
	brokerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Broker", blank=True, null=True, help_text='''An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.''', related_name="invoice_broker_person")
	brokerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Broker", blank=True, null=True, help_text='''An entity that arranges for an exchange between a buyer and a seller.  In most cases a broker never acquires or releases ownership of a product or service involved in an exchange.  If it is not clear whether an entity is a broker, seller, or buyer, the latter two terms are preferred.''', related_name="invoice_broker_organization")
	minimumPaymentDuePriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Minimumpaymentdue", blank=True, null=True, help_text='''The minimum payment required at this time.''', related_name="invoice_minimumpaymentdue_pricespecification")
	minimumPaymentDueMonetaryAmount = models.ForeignKey('MonetaryAmount', on_delete=models.CASCADE, verbose_name="Minimumpaymentdue", blank=True, null=True, help_text='''The minimum payment required at this time.''', related_name="invoice_minimumpaymentdue_monetaryamount")
	scheduledPaymentDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Scheduledpaymentdate", blank=True, null=True, help_text='''The date the invoice is scheduled to be paid.''', related_name="invoice_scheduledpaymentdate_date")
	paymentMethodPaymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Paymentmethod", blank=True, null=True, help_text='''The name of the credit card or other method of payment for the order.''', related_name="invoice_paymentmethod_paymentmethod")
	paymentMethodIdText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Paymentmethodid", blank=True, null=True, help_text='''An identifier for the method of payment used (e.g. the last 4 digits of the credit card).''', related_name="invoice_paymentmethodid_text")
	totalPaymentDuePriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Totalpaymentdue", blank=True, null=True, help_text='''The total amount due.''', related_name="invoice_totalpaymentdue_pricespecification")
	totalPaymentDueMonetaryAmount = models.ForeignKey('MonetaryAmount', on_delete=models.CASCADE, verbose_name="Totalpaymentdue", blank=True, null=True, help_text='''The total amount due.''', related_name="invoice_totalpaymentdue_monetaryamount")
	customerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Customer", blank=True, null=True, help_text='''Party placing the order or paying the invoice.''', related_name="invoice_customer_organization")
	customerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Customer", blank=True, null=True, help_text='''Party placing the order or paying the invoice.''', related_name="invoice_customer_person")
	paymentStatusText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Paymentstatus", blank=True, null=True, help_text='''The status of payment; whether the invoice has been paid or not.''', related_name="invoice_paymentstatus_text")
	paymentDueDateDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Paymentduedate", blank=True, null=True, help_text='''The date that payment is due.''', related_name="invoice_paymentduedate_datetime")
	accountIdText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accountid", blank=True, null=True, help_text='''The identifier for the account the payment will be applied to.''', related_name="invoice_accountid_text")
	providerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="invoice_provider_organization")
	providerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="invoice_provider_person")
	confirmationNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Confirmationnumber", blank=True, null=True, help_text='''A number that confirms the given order or payment has been received.''', related_name="invoice_confirmationnumber_text")
	billingPeriodDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Billingperiod", blank=True, null=True, help_text='''The time interval used to compute the invoice.''', related_name="invoice_billingperiod_duration")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="invoice_intangible")
	categoryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Category", blank=True, null=True, help_text='''A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.''', related_name="invoice_category_text")
	categoryThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Category", blank=True, null=True, help_text='''A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.''', related_name="invoice_category_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Invoice'
		verbose_name_plural = 'Invoice'


class Event(models.Model):

	workFeaturedCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Workfeatured", blank=True, null=True, help_text='''A work featured in some event, e.g. exhibited in an ExhibitionEvent.
       Specific subproperties are available for workPerformed (e.g. a play), or a workPresented (a Movie at a ScreeningEvent).''', related_name="event_workfeatured_creativework")
	contributorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Contributor", blank=True, null=True, help_text='''A secondary contributor to the CreativeWork or Event.''', related_name="event_contributor_person")
	contributorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Contributor", blank=True, null=True, help_text='''A secondary contributor to the CreativeWork or Event.''', related_name="event_contributor_organization")
	composerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Composer", blank=True, null=True, help_text='''The person or organization who wrote a composition, or who is the composer of a work performed at some event.''', related_name="event_composer_person")
	composerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Composer", blank=True, null=True, help_text='''The person or organization who wrote a composition, or who is the composer of a work performed at some event.''', related_name="event_composer_organization")
	performerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Performer", blank=True, null=True, help_text='''A performer at the event&#x2014;for example, a presenter, musician, musical group or actor.''', related_name="event_performer_organization")
	performerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Performer", blank=True, null=True, help_text='''A performer at the event&#x2014;for example, a presenter, musician, musical group or actor.''', related_name="event_performer_person")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="event_director_person")
	eventStatusEventStatusType = models.ForeignKey('EventStatusType', on_delete=models.CASCADE, verbose_name="Eventstatus", blank=True, null=True, help_text='''An eventStatus of an event represents its status; particularly useful when an event is cancelled or rescheduled.''', related_name="event_eventstatus_eventstatustype")
	superEventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Superevent", blank=True, null=True, help_text='''An event that this event is a part of. For example, a collection of individual music performances might each have a music festival as their superEvent.''', related_name="event_superevent_event")
	translatorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Translator", blank=True, null=True, help_text='''Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.''', related_name="event_translator_person")
	translatorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Translator", blank=True, null=True, help_text='''Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.''', related_name="event_translator_organization")
	offersOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", blank=True, null=True, help_text='''An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="event_offers_offer")
	reviewReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", blank=True, null=True, help_text='''A review of the item.''', related_name="event_review_review")
	durationDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", blank=True, null=True, help_text='''The duration of the item (movie, audio recording, event, etc.) in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>.''', related_name="event_duration_duration")
	subEventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Subevent", blank=True, null=True, help_text='''An Event that is part of this event. For example, a conference event includes many presentations, each of which is a subEvent of the conference.''', related_name="event_subevent_event")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="event_actor_person")
	attendeeOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Attendee", blank=True, null=True, help_text='''A person or organization attending the event.''', related_name="event_attendee_organization")
	attendeePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Attendee", blank=True, null=True, help_text='''A person or organization attending the event.''', related_name="event_attendee_person")
	typicalAgeRangeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Typicalagerange", blank=True, null=True, help_text='''The typical expected age range, e.g. '7-9', '11-'.''', related_name="event_typicalagerange_text")
	doorTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Doortime", blank=True, null=True, help_text='''The time admission will commence.''', related_name="event_doortime_datetime")
	sponsorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Sponsor", blank=True, null=True, help_text='''A person or organization that supports a thing through a pledge, promise, or financial contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.''', related_name="event_sponsor_person")
	sponsorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Sponsor", blank=True, null=True, help_text='''A person or organization that supports a thing through a pledge, promise, or financial contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.''', related_name="event_sponsor_organization")
	locationPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Location", blank=True, null=True, help_text='''The location of for example where the event is happening, an organization is located, or where an action takes place.''', related_name="event_location_postaladdress")
	locationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Location", blank=True, null=True, help_text='''The location of for example where the event is happening, an organization is located, or where an action takes place.''', related_name="event_location_place")
	locationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Location", blank=True, null=True, help_text='''The location of for example where the event is happening, an organization is located, or where an action takes place.''', related_name="event_location_text")
	recordedInCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Recordedin", blank=True, null=True, help_text='''The CreativeWork that captured all or part of this Event.''', related_name="event_recordedin_creativework")
	organizerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Organizer", blank=True, null=True, help_text='''An organizer of an Event.''', related_name="event_organizer_person")
	organizerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organizer", blank=True, null=True, help_text='''An organizer of an Event.''', related_name="event_organizer_organization")
	aggregateRatingAggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", blank=True, null=True, help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="event_aggregaterating_aggregaterating")
	startDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", blank=True, null=True, help_text='''The start date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="event_startdate_date")
	previousStartDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Previousstartdate", blank=True, null=True, help_text='''Used in conjunction with eventStatus for rescheduled or cancelled events. This property contains the previously scheduled start date. For rescheduled events, the startDate property should be used for the newly scheduled start date. In the (rare) case of an event that has been postponed and rescheduled multiple times, this field may be repeated.''', related_name="event_previousstartdate_date")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", blank=True, null=True, help_text='''The most generic type of item.''', related_name="event_thing")
	workPerformedCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Workperformed", blank=True, null=True, help_text='''A work performed in some event, for example a play performed in a TheaterEvent.''', related_name="event_workperformed_creativework")
	endDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", blank=True, null=True, help_text='''The end date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="event_enddate_date")
	inLanguageLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Inlanguage", blank=True, null=True, help_text='''The language of the content or performance or used in an action. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[availableLanguage]].''', related_name="event_inlanguage_language")
	inLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Inlanguage", blank=True, null=True, help_text='''The language of the content or performance or used in an action. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[availableLanguage]].''', related_name="event_inlanguage_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Event'
		verbose_name_plural = 'Event'


class OpeningHoursSpecification(models.Model):

	opensTime = models.ForeignKey('Time', on_delete=models.CASCADE, verbose_name="Opens", blank=True, null=True, help_text='''The opening hour of the place or service on the given day(s) of the week.''', related_name="openinghoursspecification_opens_time")
	dayOfWeekDayOfWeek = models.ForeignKey('DayOfWeek', on_delete=models.CASCADE, verbose_name="Dayofweek", blank=True, null=True, help_text='''The day of the week for which these opening hours are valid.''', related_name="openinghoursspecification_dayofweek_dayofweek")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="openinghoursspecification_structuredvalue")
	validFromDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", blank=True, null=True, help_text='''The date when the item becomes valid.''', related_name="openinghoursspecification_validfrom_datetime")
	closesTime = models.ForeignKey('Time', on_delete=models.CASCADE, verbose_name="Closes", blank=True, null=True, help_text='''The closing hour of the place or service on the given day(s) of the week.''', related_name="openinghoursspecification_closes_time")
	validThroughDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", blank=True, null=True, help_text='''The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.''', related_name="openinghoursspecification_validthrough_datetime")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OpeningHoursSpecification'
		verbose_name_plural = 'OpeningHoursSpecification'


class LandmarksOrHistoricalBuildings(models.Model):

	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", blank=True, null=True, help_text='''Entities that have a somewhat fixed, physical extension.''', related_name="landmarksorhistoricalbuildings_place")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LandmarksOrHistoricalBuildings'
		verbose_name_plural = 'LandmarksOrHistoricalBuildings'


class UserPlays(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserPlays'
		verbose_name_plural = 'UserPlays'


class CollectionPage(models.Model):

	webPage = models.ForeignKey('WebPage', on_delete=models.CASCADE, verbose_name="Webpage", blank=True, null=True, help_text='''A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.''', related_name="collectionpage_webpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CollectionPage'
		verbose_name_plural = 'CollectionPage'


class Mountain(models.Model):

	landform = models.ForeignKey('Landform', on_delete=models.CASCADE, verbose_name="Landform", blank=True, null=True, help_text='''A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.''', related_name="mountain_landform")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Mountain'
		verbose_name_plural = 'Mountain'


class CivicStructure(models.Model):

	openingHoursText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Openinghours", blank=True, null=True, help_text='''The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.<br />- Days are specified using the following two-letter combinations: <code>Mo</code>, <code>Tu</code>, <code>We</code>, <code>Th</code>, <code>Fr</code>, <code>Sa</code>, <code>Su</code>.<br />- Times are specified using 24:00 time. For example, 3pm is specified as <code>15:00</code>. <br />- Here is an example: <code>&lt;span itemprop=&quot;openingHours&quot; content=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/span&gt;</code>. <br />- If a business is open 7 days a week, then it can be specified as <code>&lt;span itemprop=&quot;openingHours&quot; content=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/span&gt;</code>.''', related_name="civicstructure_openinghours_text")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", blank=True, null=True, help_text='''Entities that have a somewhat fixed, physical extension.''', related_name="civicstructure_place")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CivicStructure'
		verbose_name_plural = 'CivicStructure'


class MarryAction(models.Model):

	interactAction = models.ForeignKey('InteractAction', on_delete=models.CASCADE, verbose_name="Interactaction", blank=True, null=True, help_text='''The act of interacting with another person or organization.''', related_name="marryaction_interactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MarryAction'
		verbose_name_plural = 'MarryAction'


class Waterfall(models.Model):

	bodyOfWater = models.ForeignKey('BodyOfWater', on_delete=models.CASCADE, verbose_name="Bodyofwater", blank=True, null=True, help_text='''A body of water, such as a sea, ocean, or lake.''', related_name="waterfall_bodyofwater")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Waterfall'
		verbose_name_plural = 'Waterfall'


class PublicationEvent(models.Model):

	isAccessibleForFreeBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Isaccessibleforfree", blank=True, null=True, help_text='''A flag to signal that the publication is accessible for free.''', related_name="publicationevent_isaccessibleforfree_boolean")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="publicationevent_event")
	publishedOnBroadcastService = models.ForeignKey('BroadcastService', on_delete=models.CASCADE, verbose_name="Publishedon", blank=True, null=True, help_text='''A broadcast service associated with the publication event.''', related_name="publicationevent_publishedon_broadcastservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PublicationEvent'
		verbose_name_plural = 'PublicationEvent'


class AmusementPark(models.Model):

	entertainmentBusiness = models.ForeignKey('EntertainmentBusiness', on_delete=models.CASCADE, verbose_name="Entertainmentbusiness", blank=True, null=True, help_text='''A business providing entertainment.''', related_name="amusementpark_entertainmentbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AmusementPark'
		verbose_name_plural = 'AmusementPark'


class Taxi(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Taxi'
		verbose_name_plural = 'Taxi'


class SiteNavigationElement(models.Model):

	webPageElement = models.ForeignKey('WebPageElement', on_delete=models.CASCADE, verbose_name="Webpageelement", blank=True, null=True, help_text='''A web page element, like a table or an image.''', related_name="sitenavigationelement_webpageelement")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SiteNavigationElement'
		verbose_name_plural = 'SiteNavigationElement'


class ComedyClub(models.Model):

	entertainmentBusiness = models.ForeignKey('EntertainmentBusiness', on_delete=models.CASCADE, verbose_name="Entertainmentbusiness", blank=True, null=True, help_text='''A business providing entertainment.''', related_name="comedyclub_entertainmentbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ComedyClub'
		verbose_name_plural = 'ComedyClub'


class Florist(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="florist_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Florist'
		verbose_name_plural = 'Florist'


class EmployeeRole(models.Model):

	baseSalaryNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Basesalary", blank=True, null=True, help_text='''The base salary of the job or of an employee in an EmployeeRole.''', related_name="employeerole_basesalary_number")
	baseSalaryMonetaryAmount = models.ForeignKey('MonetaryAmount', on_delete=models.CASCADE, verbose_name="Basesalary", blank=True, null=True, help_text='''The base salary of the job or of an employee in an EmployeeRole.''', related_name="employeerole_basesalary_monetaryamount")
	baseSalaryPriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Basesalary", blank=True, null=True, help_text='''The base salary of the job or of an employee in an EmployeeRole.''', related_name="employeerole_basesalary_pricespecification")
	organizationRole = models.ForeignKey('OrganizationRole', on_delete=models.CASCADE, verbose_name="Organizationrole", blank=True, null=True, help_text='''A subclass of Role used to describe roles within organizations.''', related_name="employeerole_organizationrole")
	salaryCurrencyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Salarycurrency", blank=True, null=True, help_text='''The currency (coded using ISO 4217, http://en.wikipedia.org/wiki/ISO_4217 ) used for the main salary information in this job posting or for this employee.''', related_name="employeerole_salarycurrency_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EmployeeRole'
		verbose_name_plural = 'EmployeeRole'


class WarrantyScope(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="warrantyscope_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WarrantyScope'
		verbose_name_plural = 'WarrantyScope'


class DanceGroup(models.Model):

	performingGroup = models.ForeignKey('PerformingGroup', on_delete=models.CASCADE, verbose_name="Performinggroup", blank=True, null=True, help_text='''A performance group, such as a band, an orchestra, or a circus.''', related_name="dancegroup_performinggroup")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DanceGroup'
		verbose_name_plural = 'DanceGroup'


class TelevisionStation(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="televisionstation_localbusiness")
	videoFormatText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Videoformat", blank=True, null=True, help_text='''The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).''', related_name="televisionstation_videoformat_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TelevisionStation'
		verbose_name_plural = 'TelevisionStation'


class Hotel(models.Model):

	lodgingBusiness = models.ForeignKey('LodgingBusiness', on_delete=models.CASCADE, verbose_name="Lodgingbusiness", blank=True, null=True, help_text='''A lodging business, such as a motel, hotel, or inn.''', related_name="hotel_lodgingbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Hotel'
		verbose_name_plural = 'Hotel'


class ReservationStatusType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="reservationstatustype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReservationStatusType'
		verbose_name_plural = 'ReservationStatusType'


class BusStop(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="busstop_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BusStop'
		verbose_name_plural = 'BusStop'


class ContactPage(models.Model):

	webPage = models.ForeignKey('WebPage', on_delete=models.CASCADE, verbose_name="Webpage", blank=True, null=True, help_text='''A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.''', related_name="contactpage_webpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ContactPage'
		verbose_name_plural = 'ContactPage'


class VideoGallery(models.Model):

	collectionPage = models.ForeignKey('CollectionPage', on_delete=models.CASCADE, verbose_name="Collectionpage", blank=True, null=True, help_text='''Web page type: Collection page.''', related_name="videogallery_collectionpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'VideoGallery'
		verbose_name_plural = 'VideoGallery'


class RegisterAction(models.Model):

	interactAction = models.ForeignKey('InteractAction', on_delete=models.CASCADE, verbose_name="Interactaction", blank=True, null=True, help_text='''The act of interacting with another person or organization.''', related_name="registeraction_interactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RegisterAction'
		verbose_name_plural = 'RegisterAction'


class LockerDelivery(models.Model):

	deliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Deliverymethod", blank=True, null=True, help_text='''A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.
<br />
    Commonly used values:<br />
<br />
    http://purl.org/goodrelations/v1#DeliveryModeDirectDownload <br />
    http://purl.org/goodrelations/v1#DeliveryModeFreight <br />
    http://purl.org/goodrelations/v1#DeliveryModeMail <br />
    http://purl.org/goodrelations/v1#DeliveryModeOwnFleet <br />
    http://purl.org/goodrelations/v1#DeliveryModePickUp <br />
    http://purl.org/goodrelations/v1#DHL <br />
    http://purl.org/goodrelations/v1#FederalExpress <br />
    http://purl.org/goodrelations/v1#UPS <br />
        ''', related_name="lockerdelivery_deliverymethod")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LockerDelivery'
		verbose_name_plural = 'LockerDelivery'


class RealEstateAgent(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="realestateagent_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RealEstateAgent'
		verbose_name_plural = 'RealEstateAgent'


class GeoCircle(models.Model):

	geoMidpointGeoCoordinates = models.ForeignKey('GeoCoordinates', on_delete=models.CASCADE, verbose_name="Geomidpoint", blank=True, null=True, help_text='''Indicates the GeoCoordinates at the centre of a GeoShape e.g. GeoCircle.''', related_name="geocircle_geomidpoint_geocoordinates")
	geoRadiusText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Georadius", blank=True, null=True, help_text='''Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise via Distance notation).''', related_name="geocircle_georadius_text")
	geoRadiusDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Georadius", blank=True, null=True, help_text='''Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise via Distance notation).''', related_name="geocircle_georadius_distance")
	geoRadiusNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Georadius", blank=True, null=True, help_text='''Indicates the approximate radius of a GeoCircle (metres unless indicated otherwise via Distance notation).''', related_name="geocircle_georadius_number")
	geoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Geoshape", blank=True, null=True, help_text='''The geographic shape of a place. A GeoShape can be described using several properties whose values are based on latitude/longitude pairs. Either whitespace or commas can be used to separate latitude and longitude; whitespace should be used when writing a list of several such points.''', related_name="geocircle_geoshape")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GeoCircle'
		verbose_name_plural = 'GeoCircle'


class Zoo(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="zoo_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Zoo'
		verbose_name_plural = 'Zoo'


class SubscribeAction(models.Model):

	interactAction = models.ForeignKey('InteractAction', on_delete=models.CASCADE, verbose_name="Interactaction", blank=True, null=True, help_text='''The act of interacting with another person or organization.''', related_name="subscribeaction_interactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SubscribeAction'
		verbose_name_plural = 'SubscribeAction'


class AggregateOffer(models.Model):

	offer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offer", blank=True, null=True, help_text='''An offer to transfer some rights to an item or to provide a service&#x2014;for example, an offer to sell tickets to an event, to rent the DVD of a movie, to stream a TV show over the internet, to repair a motorcycle, or to loan a book.
      <br/><br/>
      For <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GTIN</a>-related fields, see
      <a href="http://www.gs1.org/barcodes/support/check_digit_calculator">Check Digit calculator</a>
      and <a href="http://www.gs1us.org/resources/standards/gtin-validation-guide">validation guide</a>
      from <a href="http://www.gs1.org/">GS1</a>.''', related_name="aggregateoffer_offer")
	offersOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", blank=True, null=True, help_text='''An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="aggregateoffer_offers_offer")
	highPriceNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Highprice", blank=True, null=True, help_text='''The highest price of all offers available.''', related_name="aggregateoffer_highprice_number")
	highPriceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Highprice", blank=True, null=True, help_text='''The highest price of all offers available.''', related_name="aggregateoffer_highprice_text")
	lowPriceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Lowprice", blank=True, null=True, help_text='''The lowest price of all offers available.''', related_name="aggregateoffer_lowprice_text")
	lowPriceNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Lowprice", blank=True, null=True, help_text='''The lowest price of all offers available.''', related_name="aggregateoffer_lowprice_number")
	offerCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Offercount", blank=True, null=True, help_text='''The number of offers for the product.''', related_name="aggregateoffer_offercount_integer")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AggregateOffer'
		verbose_name_plural = 'AggregateOffer'


class AutoWash(models.Model):

	automotiveBusiness = models.ForeignKey('AutomotiveBusiness', on_delete=models.CASCADE, verbose_name="Automotivebusiness", blank=True, null=True, help_text='''Car repair, sales, or parts.''', related_name="autowash_automotivebusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AutoWash'
		verbose_name_plural = 'AutoWash'


class Library(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="library_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Library'
		verbose_name_plural = 'Library'


class ToyStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="toystore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ToyStore'
		verbose_name_plural = 'ToyStore'


class CatholicChurch(models.Model):

	placeOfWorship = models.ForeignKey('PlaceOfWorship', on_delete=models.CASCADE, verbose_name="Placeofworship", blank=True, null=True, help_text='''Place of worship, such as a church, synagogue, or mosque.''', related_name="catholicchurch_placeofworship")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CatholicChurch'
		verbose_name_plural = 'CatholicChurch'


class Number(models.Model):

	value = models.IntegerField(blank=True, null=True, verbose_name="Value", help_text='''Data type: Number.''')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Number'
		verbose_name_plural = 'Number'


class HealthAndBeautyBusiness(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="healthandbeautybusiness_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HealthAndBeautyBusiness'
		verbose_name_plural = 'HealthAndBeautyBusiness'


class LegalService(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="legalservice_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LegalService'
		verbose_name_plural = 'LegalService'


class Bakery(models.Model):

	foodEstablishment = models.ForeignKey('FoodEstablishment', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A food-related business.''', related_name="bakery_foodestablishment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Bakery'
		verbose_name_plural = 'Bakery'


class WantAction(models.Model):

	reactAction = models.ForeignKey('ReactAction', on_delete=models.CASCADE, verbose_name="Reactaction", blank=True, null=True, help_text='''The act of responding instinctively and emotionally to an object, expressing a sentiment.''', related_name="wantaction_reactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WantAction'
		verbose_name_plural = 'WantAction'


class CreativeWork(models.Model):

	# contributorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Contributor", blank=True, null=True, help_text='''A secondary contributor to the CreativeWork or Event.''', related_name="creativework_contributor_person")
	# contributorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Contributor", blank=True, null=True, help_text='''A secondary contributor to the CreativeWork or Event.''', related_name="creativework_contributor_organization")
	# keywordsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Keywords", blank=True, null=True, help_text='''Keywords or tags used to describe this content. Multiple entries in a keywords list are typically delimited by commas.''', related_name="creativework_keywords_text")
	# audienceAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", blank=True, null=True, help_text='''An intended audience, i.e. a group for whom something was created.''', related_name="creativework_audience_audience")
	# timeRequiredDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Timerequired", blank=True, null=True, help_text='''Approximate or typical time it takes to work with or through this learning resource for the typical intended target audience, e.g. 'P30M', 'P1H25M'.''', related_name="creativework_timerequired_duration")
	# publicationPublicationEvent = models.ForeignKey('PublicationEvent', on_delete=models.CASCADE, verbose_name="Publication", blank=True, null=True, help_text='''A publication event associated with the item.''', related_name="creativework_publication_publicationevent")
	# awardText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", blank=True, null=True, help_text='''An award won by or for this item.''', related_name="creativework_award_text")
	# headlineText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Headline", blank=True, null=True, help_text='''Headline of the article.''', related_name="creativework_headline_text")
	# fileFormatText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Fileformat", blank=True, null=True, help_text='''Media type (aka MIME format, see <a href="http://www.iana.org/assignments/media-types/media-types.xhtml">IANA site</a>) of the content e.g. application/zip of a SoftwareApplication binary. In cases where a CreativeWork has several media type representations, 'encoding' can be used to indicate each MediaObject alongside particular fileFormat information.''', related_name="creativework_fileformat_text")
	# interactionStatisticInteractionCounter = models.ForeignKey('InteractionCounter', on_delete=models.CASCADE, verbose_name="Interactionstatistic", blank=True, null=True, help_text='''The number of interactions for the CreativeWork using the WebSite or SoftwareApplication. The most specific child type of InteractionCounter should be used.''', related_name="creativework_interactionstatistic_interactioncounter")
	# recordedAtEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Recordedat", blank=True, null=True, help_text='''The Event where the CreativeWork was recorded. The CreativeWork may capture all or part of the event.''', related_name="creativework_recordedat_event")
	# isPartOfCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Ispartof", blank=True, null=True, help_text='''Indicates a CreativeWork that this CreativeWork is (in some sense) part of.''', related_name="creativework_ispartof_creativework")
	# contentLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Contentlocation", blank=True, null=True, help_text='''The location depicted or described in the content. For example, the location in a photograph or painting.''', related_name="creativework_contentlocation_place")
	# exampleOfWorkCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Exampleofwork", blank=True, null=True, help_text='''A creative work that this work is an example/instance/realization/derivation of.''', related_name="creativework_exampleofwork_creativework")
	# accessibilityFeatureText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accessibilityfeature", blank=True, null=True, help_text='''Content features of the resource, such as accessible media, alternatives and supported enhancements for accessibility (<a href="http://www.w3.org/wiki/WebSchemas/Accessibility">WebSchemas wiki lists possible values</a>).''', related_name="creativework_accessibilityfeature_text")
	# dateCreatedDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datecreated", blank=True, null=True, help_text='''The date on which the CreativeWork was created or the item was added to a DataFeed.''', related_name="creativework_datecreated_datetime")
	# dateCreatedDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Datecreated", blank=True, null=True, help_text='''The date on which the CreativeWork was created or the item was added to a DataFeed.''', related_name="creativework_datecreated_date")
	# releasedEventPublicationEvent = models.ForeignKey('PublicationEvent', on_delete=models.CASCADE, verbose_name="Releasedevent", blank=True, null=True, help_text='''The place and time the release was issued, expressed as a PublicationEvent.''', related_name="creativework_releasedevent_publicationevent")
	# publisherOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Publisher", blank=True, null=True, help_text='''The publisher of the creative work.''', related_name="creativework_publisher_organization")
	# accountablePersonPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Accountableperson", blank=True, null=True, help_text='''Specifies the Person that is legally accountable for the CreativeWork.''', related_name="creativework_accountableperson_person")
	# accessibilityControlText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accessibilitycontrol", blank=True, null=True, help_text='''Identifies input methods that are sufficient to fully control the described resource (<a href="http://www.w3.org/wiki/WebSchemas/Accessibility">WebSchemas wiki lists possible values</a>).''', related_name="creativework_accessibilitycontrol_text")
	# isFamilyFriendlyBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Isfamilyfriendly", blank=True, null=True, help_text='''Indicates whether this content is family friendly.''', related_name="creativework_isfamilyfriendly_boolean")
	# encodingMediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="Encoding", blank=True, null=True, help_text='''A media object that encodes this CreativeWork. This property is a synonym for associatedMedia.''', related_name="creativework_encoding_mediaobject")
	# alternativeHeadlineText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Alternativeheadline", blank=True, null=True, help_text='''A secondary title of the CreativeWork.''', related_name="creativework_alternativeheadline_text")
	# creatorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Creator", blank=True, null=True, help_text='''The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.''', related_name="creativework_creator_person")
	# creatorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Creator", blank=True, null=True, help_text='''The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.''', related_name="creativework_creator_organization")
	# hasPartCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Haspart", blank=True, null=True, help_text='''Indicates a CreativeWork that is (in some sense) a part of this CreativeWork.''', related_name="creativework_haspart_creativework")
	# licenseCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="License", blank=True, null=True, help_text='''A license document that applies to this content, typically indicated by URL.''', related_name="creativework_license_creativework")
	# licenseURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="License", blank=True, null=True, help_text='''A license document that applies to this content, typically indicated by URL.''', related_name="creativework_license_url")
	# translatorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Translator", blank=True, null=True, help_text='''Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.''', related_name="creativework_translator_person")
	# translatorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Translator", blank=True, null=True, help_text='''Organization or person who adapts a creative work to different languages, regional differences and technical requirements of a target market, or that translates during some event.''', related_name="creativework_translator_organization")
	# offersOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", blank=True, null=True, help_text='''An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="creativework_offers_offer")
	# publishingPrinciplesURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Publishingprinciples", blank=True, null=True, help_text='''Link to page describing the editorial principles of the organization primarily responsible for the creation of the CreativeWork.''', related_name="creativework_publishingprinciples_url")
	# schemaVersionURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Schemaversion", blank=True, null=True, help_text='''Indicates (by URL or string) a particular version of a schema used in some CreativeWork. For example, a document could declare a schemaVersion using an URL such as http://schema.org/version/2.0/ if precise indication of schema version was required by some application. ''', related_name="creativework_schemaversion_url")
	# schemaVersionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Schemaversion", blank=True, null=True, help_text='''Indicates (by URL or string) a particular version of a schema used in some CreativeWork. For example, a document could declare a schemaVersion using an URL such as http://schema.org/version/2.0/ if precise indication of schema version was required by some application. ''', related_name="creativework_schemaversion_text")
	# reviewReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", blank=True, null=True, help_text='''A review of the item.''', related_name="creativework_review_review")
	# thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", blank=True, null=True, help_text='''The most generic type of item.''', related_name="creativework_thing")
	# positionInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Position", blank=True, null=True, help_text='''The position of an item in a series or sequence of items.''', related_name="creativework_position_integer")
	# positionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Position", blank=True, null=True, help_text='''The position of an item in a series or sequence of items.''', related_name="creativework_position_text")
	# genreText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Genre", blank=True, null=True, help_text='''Genre of the creative work or group.''', related_name="creativework_genre_text")
	# characterPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Character", blank=True, null=True, help_text='''Fictional person connected with a creative work.''', related_name="creativework_character_person")
	# commentCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Commentcount", blank=True, null=True, help_text='''The number of comments this CreativeWork (e.g. Article, Question or Answer) has received. This is most applicable to works published in Web sites with commenting system; additional comments may exist elsewhere.''', related_name="creativework_commentcount_integer")
	# contentRatingText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Contentrating", blank=True, null=True, help_text='''Official rating of a piece of content&#x2014;for example,'MPAA PG-13'.''', related_name="creativework_contentrating_text")
	# producerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Producer", blank=True, null=True, help_text='''The person or organization who produced the work (e.g. music album, movie, tv/radio series etc.).''', related_name="creativework_producer_person")
	# producerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Producer", blank=True, null=True, help_text='''The person or organization who produced the work (e.g. music album, movie, tv/radio series etc.).''', related_name="creativework_producer_organization")
	# editorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Editor", blank=True, null=True, help_text='''Specifies the Person who edited the CreativeWork.''', related_name="creativework_editor_person")
	# locationCreatedPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Locationcreated", blank=True, null=True, help_text='''The location where the CreativeWork was created, which may not be the same as the location depicted in the CreativeWork.''', related_name="creativework_locationcreated_place")
	# aboutThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="About", blank=True, null=True, help_text='''The subject matter of the content.''', related_name="creativework_about_thing")
	# audioAudioObject = models.ForeignKey('AudioObject', on_delete=models.CASCADE, verbose_name="Audio", blank=True, null=True, help_text='''An embedded audio object.''', related_name="creativework_audio_audioobject")
	# thumbnailUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Thumbnailurl", blank=True, null=True, help_text='''A thumbnail image relevant to the Thing.''', related_name="creativework_thumbnailurl_url")
	# typicalAgeRangeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Typicalagerange", blank=True, null=True, help_text='''The typical expected age range, e.g. '7-9', '11-'.''', related_name="creativework_typicalagerange_text")
	# textText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Text", blank=True, null=True, help_text='''The textual content of this CreativeWork.''', related_name="creativework_text_text")
	# interactivityTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Interactivitytype", blank=True, null=True, help_text='''The predominant mode of learning supported by the learning resource. Acceptable values are 'active', 'expositive', or 'mixed'.''', related_name="creativework_interactivitytype_text")
	# authorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Author", blank=True, null=True, help_text='''The author of this content. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.''', related_name="creativework_author_organization")
	# authorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Author", blank=True, null=True, help_text='''The author of this content. Please note that author is special in that HTML 5 provides a special mechanism for indicating authorship via the rel tag. That is equivalent to this and may be used interchangeably.''', related_name="creativework_author_person")
	# accessibilityHazardText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accessibilityhazard", blank=True, null=True, help_text='''A characteristic of the described resource that is physiologically dangerous to some users. Related to WCAG 2.0 guideline 2.3 (<a href="http://www.w3.org/wiki/WebSchemas/Accessibility">WebSchemas wiki lists possible values</a>).''', related_name="creativework_accessibilityhazard_text")
	# sourceOrganizationOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Sourceorganization", blank=True, null=True, help_text='''The Organization on whose behalf the creator was working.''', related_name="creativework_sourceorganization_organization")
	# providerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="creativework_provider_organization")
	# providerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="creativework_provider_person")
	# learningResourceTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Learningresourcetype", blank=True, null=True, help_text='''The predominant type or kind characterizing the learning resource. For example, 'presentation', 'handout'.''', related_name="creativework_learningresourcetype_text")
	# copyrightHolderOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Copyrightholder", blank=True, null=True, help_text='''The party holding the legal copyright to the CreativeWork.''', related_name="creativework_copyrightholder_organization")
	# copyrightHolderPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Copyrightholder", blank=True, null=True, help_text='''The party holding the legal copyright to the CreativeWork.''', related_name="creativework_copyrightholder_person")
	# accessibilityAPIText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Accessibilityapi", blank=True, null=True, help_text='''Indicates that the resource is compatible with the referenced accessibility API (<a href="http://www.w3.org/wiki/WebSchemas/Accessibility">WebSchemas wiki lists possible values</a>).''', related_name="creativework_accessibilityapi_text")
	# commentComment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Comment", blank=True, null=True, help_text='''Comments, typically from users.''', related_name="creativework_comment_comment")
	# isBasedOnURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Isbasedon", blank=True, null=True, help_text='''A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.''', related_name="creativework_isbasedon_url")
	# isBasedOnProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Isbasedon", blank=True, null=True, help_text='''A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.''', related_name="creativework_isbasedon_product")
	# isBasedOnCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Isbasedon", blank=True, null=True, help_text='''A resource that was used in the creation of this resource. This term can be repeated for multiple sources. For example, http://example.com/great-multiplication-intro.html.''', related_name="creativework_isbasedon_creativework")
	# datePublishedDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Datepublished", blank=True, null=True, help_text='''Date of first broadcast/publication.''', related_name="creativework_datepublished_date")
	# aggregateRatingAggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", blank=True, null=True, help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="creativework_aggregaterating_aggregaterating")
	# educationalAlignmentAlignmentObject = models.ForeignKey('AlignmentObject', on_delete=models.CASCADE, verbose_name="Educationalalignment", blank=True, null=True, help_text='''An alignment to an established educational framework.''', related_name="creativework_educationalalignment_alignmentobject")
	# videoVideoObject = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Video", blank=True, null=True, help_text='''An embedded video object.''', related_name="creativework_video_videoobject")
	# versionNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Version", blank=True, null=True, help_text='''The version of the CreativeWork embodied by a specified resource.''', related_name="creativework_version_number")
	# mainEntityThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Mainentity", blank=True, null=True, help_text='''Indicates the primary entity described in some page or other CreativeWork.''', related_name="creativework_mainentity_thing")
	# associatedMediaMediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="Associatedmedia", blank=True, null=True, help_text='''A media object that encodes this CreativeWork. This property is a synonym for encoding.''', related_name="creativework_associatedmedia_mediaobject")
	# workExampleCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Workexample", blank=True, null=True, help_text='''Example/instance/realization/derivation of the concept of this creative work. eg. The paperback edition, first edition, or eBook.''', related_name="creativework_workexample_creativework")
	# copyrightYearNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Copyrightyear", blank=True, null=True, help_text='''The year during which the claimed copyright for the CreativeWork was first asserted.''', related_name="creativework_copyrightyear_number")
	# mentionsThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Mentions", blank=True, null=True, help_text='''Indicates that the CreativeWork contains a reference to, but is not necessarily about a concept.''', related_name="creativework_mentions_thing")
	# citationCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Citation", blank=True, null=True, help_text='''A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.''', related_name="creativework_citation_creativework")
	# citationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Citation", blank=True, null=True, help_text='''A citation or reference to another creative work, such as another publication, web page, scholarly article, etc.''', related_name="creativework_citation_text")
	# discussionUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Discussionurl", blank=True, null=True, help_text='''A link to the page containing the comments of the CreativeWork.''', related_name="creativework_discussionurl_url")
	# dateModifiedDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datemodified", blank=True, null=True, help_text='''The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.''', related_name="creativework_datemodified_datetime")
	# dateModifiedDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Datemodified", blank=True, null=True, help_text='''The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.''', related_name="creativework_datemodified_date")
	# inLanguageLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Inlanguage", blank=True, null=True, help_text='''The language of the content or performance or used in an action. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[availableLanguage]].''', related_name="creativework_inlanguage_language")
	# inLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Inlanguage", blank=True, null=True, help_text='''The language of the content or performance or used in an action. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[availableLanguage]].''', related_name="creativework_inlanguage_text")
	# educationalUseText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Educationaluse", blank=True, null=True, help_text='''The purpose of a work in the context of education; for example, 'assignment', 'group work'.''', related_name="creativework_educationaluse_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CreativeWork'
		verbose_name_plural = 'CreativeWork'


class MovingCompany(models.Model):

	homeAndConstructionBusiness = models.ForeignKey('HomeAndConstructionBusiness', on_delete=models.CASCADE, verbose_name="Homeandconstructionbusiness", blank=True, null=True, help_text='''A construction business.
        <br><br>
        A HomeAndConstructionBusiness is a LocalBusiness that provides services around homes and buildings.
          <br><br>
          As a <a href="/LocalBusiness">LocalBusiness</a> it can be
          described as a <a href="/provider">provider</a> of one or more
          <a href="/Service">Service(s)</a>.
      ''', related_name="movingcompany_homeandconstructionbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MovingCompany'
		verbose_name_plural = 'MovingCompany'


class AutoBodyShop(models.Model):

	automotiveBusiness = models.ForeignKey('AutomotiveBusiness', on_delete=models.CASCADE, verbose_name="Automotivebusiness", blank=True, null=True, help_text='''Car repair, sales, or parts.''', related_name="autobodyshop_automotivebusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AutoBodyShop'
		verbose_name_plural = 'AutoBodyShop'


class Answer(models.Model):

	comment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Comment", blank=True, null=True, help_text='''A comment on an item - for example, a comment on a blog post. The comment's content is expressed via the "text" property, and its topic via "about", properties shared with all CreativeWorks.''', related_name="answer_comment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Answer'
		verbose_name_plural = 'Answer'


class AssignAction(models.Model):

	allocateAction = models.ForeignKey('AllocateAction', on_delete=models.CASCADE, verbose_name="Allocateaction", blank=True, null=True, help_text='''The act of organizing tasks/objects/events by associating resources to it.''', related_name="assignaction_allocateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AssignAction'
		verbose_name_plural = 'AssignAction'


class UnitPriceSpecification(models.Model):

	billingIncrementNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Billingincrement", blank=True, null=True, help_text='''This property specifies the minimal quantity and rounding increment that will be the basis for the billing. The unit of measurement is specified by the unitCode property.''', related_name="unitpricespecification_billingincrement_number")
	priceTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricetype", blank=True, null=True, help_text='''A short text or acronym indicating multiple price specifications for the same offer, e.g. SRP for the suggested retail price or INVOICE for the invoice price, mostly used in the car industry.''', related_name="unitpricespecification_pricetype_text")
	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", blank=True, null=True, help_text='''A structured value representing a price or price range. Typically, only the subclasses of this type are used for markup. It is recommended to use [[MonetaryAmount]] to describe independent amounts of money such as a salary, credit card limits, etc.''', related_name="unitpricespecification_pricespecification")
	unitCodeURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Unitcode", blank=True, null=True, help_text='''The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.''', related_name="unitpricespecification_unitcode_url")
	unitCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unitcode", blank=True, null=True, help_text='''The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.''', related_name="unitpricespecification_unitcode_text")
	referenceQuantityQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Referencequantity", blank=True, null=True, help_text='''The reference quantity for which a certain price applies, e.g. 1 EUR per 4 kWh of electricity. This property is a replacement for unitOfMeasurement for the advanced cases where the price does not relate to a standard unit.''', related_name="unitpricespecification_referencequantity_quantitativevalue")
	unitTextText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unittext", blank=True, null=True, help_text='''A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
<a href='unitCode'>unitCode</a>.''', related_name="unitpricespecification_unittext_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UnitPriceSpecification'
		verbose_name_plural = 'UnitPriceSpecification'


class FinancialProduct(models.Model):

	feesAndCommissionsSpecificationURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Feesandcommissionsspecification", blank=True, null=True, help_text='''Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.''', related_name="financialproduct_feesandcommissionsspecification_url")
	feesAndCommissionsSpecificationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Feesandcommissionsspecification", blank=True, null=True, help_text='''Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.''', related_name="financialproduct_feesandcommissionsspecification_text")
	annualPercentageRateQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Annualpercentagerate", blank=True, null=True, help_text='''The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction.''', related_name="financialproduct_annualpercentagerate_quantitativevalue")
	annualPercentageRateNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Annualpercentagerate", blank=True, null=True, help_text='''The annual rate that is charged for borrowing (or made by investing), expressed as a single percentage number that represents the actual yearly cost of funds over the term of a loan. This includes any fees or additional costs associated with the transaction.''', related_name="financialproduct_annualpercentagerate_number")
	interestRateQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Interestrate", blank=True, null=True, help_text='''The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate.''', related_name="financialproduct_interestrate_quantitativevalue")
	interestRateNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Interestrate", blank=True, null=True, help_text='''The interest rate, charged or paid, applicable to the financial product. Note: This is different from the calculated annualPercentageRate.''', related_name="financialproduct_interestrate_number")
	service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Service", blank=True, null=True, help_text='''A service provided by an organization, e.g. delivery service, print services, etc.''', related_name="financialproduct_service")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FinancialProduct'
		verbose_name_plural = 'FinancialProduct'


class MusicRecording(models.Model):

	isrcCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isrccode", blank=True, null=True, help_text='''The International Standard Recording Code for the recording.''', related_name="musicrecording_isrccode_text")
	recordingOfMusicComposition = models.ForeignKey('MusicComposition', on_delete=models.CASCADE, verbose_name="Recordingof", blank=True, null=True, help_text='''The composition this track is a recording of.''', related_name="musicrecording_recordingof_musiccomposition")
	inAlbumMusicAlbum = models.ForeignKey('MusicAlbum', on_delete=models.CASCADE, verbose_name="Inalbum", blank=True, null=True, help_text='''The album to which this recording belongs.''', related_name="musicrecording_inalbum_musicalbum")
	inPlaylistMusicPlaylist = models.ForeignKey('MusicPlaylist', on_delete=models.CASCADE, verbose_name="Inplaylist", blank=True, null=True, help_text='''The playlist to which this recording belongs.''', related_name="musicrecording_inplaylist_musicplaylist")
	durationDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", blank=True, null=True, help_text='''The duration of the item (movie, audio recording, event, etc.) in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>.''', related_name="musicrecording_duration_duration")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="musicrecording_creativework")
	byArtistMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Byartist", blank=True, null=True, help_text='''The artist that performed this album or recording.''', related_name="musicrecording_byartist_musicgroup")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicRecording'
		verbose_name_plural = 'MusicRecording'


class HardwareStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="hardwarestore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HardwareStore'
		verbose_name_plural = 'HardwareStore'


class EducationalAudience(models.Model):

	audience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", blank=True, null=True, help_text='''Intended audience for an item, i.e. the group for whom the item was created.''', related_name="educationalaudience_audience")
	educationalRoleText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Educationalrole", blank=True, null=True, help_text='''An educationalRole of an EducationalAudience.''', related_name="educationalaudience_educationalrole_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EducationalAudience'
		verbose_name_plural = 'EducationalAudience'


class MoveAction(models.Model):

	fromLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Fromlocation", blank=True, null=True, help_text='''A sub property of location. The original location of the object or the agent before the action.''', related_name="moveaction_fromlocation_place")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="moveaction_action")
	toLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Tolocation", blank=True, null=True, help_text='''A sub property of location. The final location of the object or the agent after the action.''', related_name="moveaction_tolocation_place")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MoveAction'
		verbose_name_plural = 'MoveAction'


class BoardingPolicyType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="boardingpolicytype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BoardingPolicyType'
		verbose_name_plural = 'BoardingPolicyType'


class BusTrip(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="bustrip_intangible")
	busNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Busnumber", blank=True, null=True, help_text='''The unique identifier for the bus.''', related_name="bustrip_busnumber_text")
	departureBusStopBusStop = models.ForeignKey('BusStop', on_delete=models.CASCADE, verbose_name="Departurebusstop", blank=True, null=True, help_text='''The stop or station from which the bus departs.''', related_name="bustrip_departurebusstop_busstop")
	departureBusStopBusStation = models.ForeignKey('BusStation', on_delete=models.CASCADE, verbose_name="Departurebusstop", blank=True, null=True, help_text='''The stop or station from which the bus departs.''', related_name="bustrip_departurebusstop_busstation")
	departureTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Departuretime", blank=True, null=True, help_text='''The expected departure time.''', related_name="bustrip_departuretime_datetime")
	arrivalTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Arrivaltime", blank=True, null=True, help_text='''The expected arrival time.''', related_name="bustrip_arrivaltime_datetime")
	providerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="bustrip_provider_organization")
	providerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="bustrip_provider_person")
	arrivalBusStopBusStop = models.ForeignKey('BusStop', on_delete=models.CASCADE, verbose_name="Arrivalbusstop", blank=True, null=True, help_text='''The stop or station from which the bus arrives.''', related_name="bustrip_arrivalbusstop_busstop")
	arrivalBusStopBusStation = models.ForeignKey('BusStation', on_delete=models.CASCADE, verbose_name="Arrivalbusstop", blank=True, null=True, help_text='''The stop or station from which the bus arrives.''', related_name="bustrip_arrivalbusstop_busstation")
	busNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Busname", blank=True, null=True, help_text='''The name of the bus (e.g. Bolt Express).''', related_name="bustrip_busname_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BusTrip'
		verbose_name_plural = 'BusTrip'


class TravelAgency(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="travelagency_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TravelAgency'
		verbose_name_plural = 'TravelAgency'


class FoodEstablishmentReservation(models.Model):

	startTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Starttime", blank=True, null=True, help_text='''The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from *January* to December.

Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.''', related_name="foodestablishmentreservation_starttime_datetime")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", blank=True, null=True, help_text='''Describes a reservation for travel, dining or an event. Some reservations require tickets.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use http://schema.org/Offer.''', related_name="foodestablishmentreservation_reservation")
	partySizeQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Partysize", blank=True, null=True, help_text='''Number of people the reservation should accommodate.''', related_name="foodestablishmentreservation_partysize_quantitativevalue")
	partySizeInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Partysize", blank=True, null=True, help_text='''Number of people the reservation should accommodate.''', related_name="foodestablishmentreservation_partysize_integer")
	endTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Endtime", blank=True, null=True, help_text='''The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to *December*.

Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.''', related_name="foodestablishmentreservation_endtime_datetime")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FoodEstablishmentReservation'
		verbose_name_plural = 'FoodEstablishmentReservation'


class ShoppingCenter(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="shoppingcenter_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ShoppingCenter'
		verbose_name_plural = 'ShoppingCenter'


class OrderAction(models.Model):

	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="Tradeaction", blank=True, null=True, help_text='''The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.''', related_name="orderaction_tradeaction")
	deliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Deliverymethod", blank=True, null=True, help_text='''A sub property of instrument. The method of delivery.''', related_name="orderaction_deliverymethod_deliverymethod")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OrderAction'
		verbose_name_plural = 'OrderAction'


class RsvpResponseType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="rsvpresponsetype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RsvpResponseType'
		verbose_name_plural = 'RsvpResponseType'


class PaymentStatusType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="paymentstatustype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PaymentStatusType'
		verbose_name_plural = 'PaymentStatusType'


class WriteAction(models.Model):

	createAction = models.ForeignKey('CreateAction', on_delete=models.CASCADE, verbose_name="Createaction", blank=True, null=True, help_text='''The act of deliberately creating/producing/generating/building a result out of the agent.''', related_name="writeaction_createaction")
	inLanguageLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Inlanguage", blank=True, null=True, help_text='''The language of the content or performance or used in an action. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[availableLanguage]].''', related_name="writeaction_inlanguage_language")
	inLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Inlanguage", blank=True, null=True, help_text='''The language of the content or performance or used in an action. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[availableLanguage]].''', related_name="writeaction_inlanguage_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WriteAction'
		verbose_name_plural = 'WriteAction'


class RadioSeries(models.Model):

	musicByMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="radioseries_musicby_musicgroup")
	musicByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="radioseries_musicby_person")
	trailerVideoObject = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", blank=True, null=True, help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="radioseries_trailer_videoobject")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="radioseries_director_person")
	episodeEpisode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", blank=True, null=True, help_text='''An episode of a tv, radio or game media within a series or season.''', related_name="radioseries_episode_episode")
	creativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Creativeworkseries", blank=True, null=True, help_text='''
          A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind.
          CreativeWorkSeries are usually organized into some order, often chronological. Unlike <a href="/ItemList">ItemList</a> which
          is a general purpose data structure for lists of things, the emphasis with
          CreativeWorkSeries is on published materials (written e.g. books and periodicals,
          or media such as tv, radio and games).

          <br/><br/>

          Specific subtypes are available for describing <a href="/TVSeries">TVSeries</a>, <a href="/RadioSeries">RadioSeries</a>,
          <a href="/MovieSeries">MovieSeries</a>,
          <a href="/BookSeries">BookSeries</a>,
          <a href="/Periodical">Periodical</a>
          and <a href="/VideoGameSeries">VideoGameSeries</a>. In each case,
          the <a href="/hasPart">hasPart</a> / <a href="/isPartOf">isPartOf</a> properties
          can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely
          just to organize these more specific and practical subtypes.

          <br/><br/>

          It is common for properties applicable to an item from the series to be usefully applied to the containing group.
          Schema.org attempts to anticipate some of these cases, but publishers should be free to apply
          properties of the series parts to the series as a whole wherever they seem appropriate.''', related_name="radioseries_creativeworkseries")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="radioseries_actor_person")
	containsSeasonCreativeWorkSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Containsseason", blank=True, null=True, help_text='''A season that is part of the media series.''', related_name="radioseries_containsseason_creativeworkseason")
	numberOfSeasonsInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofseasons", blank=True, null=True, help_text='''The number of seasons in this series.''', related_name="radioseries_numberofseasons_integer")
	productionCompanyOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", blank=True, null=True, help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="radioseries_productioncompany_organization")
	numberOfEpisodesInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofepisodes", blank=True, null=True, help_text='''The number of episodes in this season or series.''', related_name="radioseries_numberofepisodes_integer")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RadioSeries'
		verbose_name_plural = 'RadioSeries'


class DataFeed(models.Model):

	dataset = models.ForeignKey('Dataset', on_delete=models.CASCADE, verbose_name="Dataset", blank=True, null=True, help_text='''A body of structured information describing some topic(s) of interest.''', related_name="datafeed_dataset")
	dataFeedElementText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Datafeedelement", blank=True, null=True, help_text='''An item within in a data feed. Data feeds may have many elements.''', related_name="datafeed_datafeedelement_text")
	dataFeedElementThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Datafeedelement", blank=True, null=True, help_text='''An item within in a data feed. Data feeds may have many elements.''', related_name="datafeed_datafeedelement_thing")
	dataFeedElementDataFeedItem = models.ForeignKey('DataFeedItem', on_delete=models.CASCADE, verbose_name="Datafeedelement", blank=True, null=True, help_text='''An item within in a data feed. Data feeds may have many elements.''', related_name="datafeed_datafeedelement_datafeeditem")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DataFeed'
		verbose_name_plural = 'DataFeed'


class HobbyShop(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="hobbyshop_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HobbyShop'
		verbose_name_plural = 'HobbyShop'


class APIReference(models.Model):

	techArticle = models.ForeignKey('TechArticle', on_delete=models.CASCADE, verbose_name="Techarticle", blank=True, null=True, help_text='''A technical article - Example: How-to (task) topics, step-by-step, procedural troubleshooting, specifications, etc.''', related_name="apireference_techarticle")
	executableLibraryNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Executablelibraryname", blank=True, null=True, help_text='''Library file name e.g., mscorlib.dll, system.web.dll.''', related_name="apireference_executablelibraryname_text")
	assemblyVersionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Assemblyversion", blank=True, null=True, help_text='''Associated product/technology version. e.g., .NET Framework 4.5.''', related_name="apireference_assemblyversion_text")
	programmingModelText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Programmingmodel", blank=True, null=True, help_text='''Indicates whether API is managed or unmanaged.''', related_name="apireference_programmingmodel_text")
	targetPlatformText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Targetplatform", blank=True, null=True, help_text='''Type of app development: phone, Metro style, desktop, XBox, etc.''', related_name="apireference_targetplatform_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'APIReference'
		verbose_name_plural = 'APIReference'


class NightClub(models.Model):

	entertainmentBusiness = models.ForeignKey('EntertainmentBusiness', on_delete=models.CASCADE, verbose_name="Entertainmentbusiness", blank=True, null=True, help_text='''A business providing entertainment.''', related_name="nightclub_entertainmentbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'NightClub'
		verbose_name_plural = 'NightClub'


class PaymentChargeSpecification(models.Model):

	appliesToDeliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Appliestodeliverymethod", blank=True, null=True, help_text='''The delivery method(s) to which the delivery charge or payment charge specification applies.''', related_name="paymentchargespecification_appliestodeliverymethod_deliverymethod")
	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", blank=True, null=True, help_text='''A structured value representing a price or price range. Typically, only the subclasses of this type are used for markup. It is recommended to use [[MonetaryAmount]] to describe independent amounts of money such as a salary, credit card limits, etc.''', related_name="paymentchargespecification_pricespecification")
	appliesToPaymentMethodPaymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Appliestopaymentmethod", blank=True, null=True, help_text='''The payment method(s) to which the payment charge specification applies.''', related_name="paymentchargespecification_appliestopaymentmethod_paymentmethod")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PaymentChargeSpecification'
		verbose_name_plural = 'PaymentChargeSpecification'


class WholesaleStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="wholesalestore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WholesaleStore'
		verbose_name_plural = 'WholesaleStore'


class Beach(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="beach_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Beach'
		verbose_name_plural = 'Beach'


class Comment(models.Model):

	upvoteCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Upvotecount", blank=True, null=True, help_text='''The number of upvotes this question, answer or comment has received from the community.''', related_name="comment_upvotecount_integer")
	downvoteCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Downvotecount", blank=True, null=True, help_text='''The number of downvotes this question, answer or comment has received from the community.''', related_name="comment_downvotecount_integer")
	parentItemQuestion = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name="Parentitem", blank=True, null=True, help_text='''The parent of a question, answer or item in general.''', related_name="comment_parentitem_question")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="comment_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Comment'
		verbose_name_plural = 'Comment'


class DatedMoneySpecification(models.Model):

	amountMonetaryAmount = models.ForeignKey('MonetaryAmount', on_delete=models.CASCADE, verbose_name="Amount", blank=True, null=True, help_text='''The amount of money.''', related_name="datedmoneyspecification_amount_monetaryamount")
	amountNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Amount", blank=True, null=True, help_text='''The amount of money.''', related_name="datedmoneyspecification_amount_number")
	startDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", blank=True, null=True, help_text='''The start date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="datedmoneyspecification_startdate_date")
	currencyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Currency", blank=True, null=True, help_text='''The currency in which the monetary amount is expressed (in 3-letter <a href='http://en.wikipedia.org/wiki/ISO_4217'">ISO 4217</a> format).''', related_name="datedmoneyspecification_currency_text")
	endDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", blank=True, null=True, help_text='''The end date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="datedmoneyspecification_enddate_date")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DatedMoneySpecification'
		verbose_name_plural = 'DatedMoneySpecification'


class EndorseAction(models.Model):

	endorseeOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Endorsee", blank=True, null=True, help_text='''A sub property of participant. The person/organization being supported.''', related_name="endorseaction_endorsee_organization")
	endorseePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Endorsee", blank=True, null=True, help_text='''A sub property of participant. The person/organization being supported.''', related_name="endorseaction_endorsee_person")
	reactAction = models.ForeignKey('ReactAction', on_delete=models.CASCADE, verbose_name="Reactaction", blank=True, null=True, help_text='''The act of responding instinctively and emotionally to an object, expressing a sentiment.''', related_name="endorseaction_reactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EndorseAction'
		verbose_name_plural = 'EndorseAction'


class BookmarkAction(models.Model):

	organizeAction = models.ForeignKey('OrganizeAction', on_delete=models.CASCADE, verbose_name="Organizeaction", blank=True, null=True, help_text='''The act of manipulating/administering/supervising/controlling one or more objects.''', related_name="bookmarkaction_organizeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BookmarkAction'
		verbose_name_plural = 'BookmarkAction'


class TaxiReservation(models.Model):

	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", blank=True, null=True, help_text='''Describes a reservation for travel, dining or an event. Some reservations require tickets.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use http://schema.org/Offer.''', related_name="taxireservation_reservation")
	pickupLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Pickuplocation", blank=True, null=True, help_text='''Where a taxi will pick up a passenger or a rental car can be picked up.''', related_name="taxireservation_pickuplocation_place")
	pickupTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Pickuptime", blank=True, null=True, help_text='''When a taxi will pickup a passenger or a rental car can be picked up.''', related_name="taxireservation_pickuptime_datetime")
	partySizeQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Partysize", blank=True, null=True, help_text='''Number of people the reservation should accommodate.''', related_name="taxireservation_partysize_quantitativevalue")
	partySizeInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Partysize", blank=True, null=True, help_text='''Number of people the reservation should accommodate.''', related_name="taxireservation_partysize_integer")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TaxiReservation'
		verbose_name_plural = 'TaxiReservation'


class Pharmacy(models.Model):

	medicalOrganization = models.ForeignKey('MedicalOrganization', on_delete=models.CASCADE, verbose_name="Medicalorganization", blank=True, null=True, help_text='''A medical organization (physical or not), such as hospital, institution or clinic.''', related_name="pharmacy_medicalorganization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Pharmacy'
		verbose_name_plural = 'Pharmacy'


class UserInteraction(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserInteraction'
		verbose_name_plural = 'UserInteraction'


class OrderStatus(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="orderstatus_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OrderStatus'
		verbose_name_plural = 'OrderStatus'


class ItemAvailability(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="itemavailability_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ItemAvailability'
		verbose_name_plural = 'ItemAvailability'


class FoodEstablishment(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="foodestablishment_localbusiness")
	acceptsReservationsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Acceptsreservations", blank=True, null=True, help_text='''Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings <code>Yes</code> or <code>No</code>.''', related_name="foodestablishment_acceptsreservations_text")
	acceptsReservationsBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Acceptsreservations", blank=True, null=True, help_text='''Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings <code>Yes</code> or <code>No</code>.''', related_name="foodestablishment_acceptsreservations_boolean")
	acceptsReservationsURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Acceptsreservations", blank=True, null=True, help_text='''Indicates whether a FoodEstablishment accepts reservations. Values can be Boolean, an URL at which reservations can be made or (for backwards compatibility) the strings <code>Yes</code> or <code>No</code>.''', related_name="foodestablishment_acceptsreservations_url")
	servesCuisineText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Servescuisine", blank=True, null=True, help_text='''The cuisine of the restaurant.''', related_name="foodestablishment_servescuisine_text")
	menuText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Menu", blank=True, null=True, help_text='''Either the actual menu or a URL of the menu.''', related_name="foodestablishment_menu_text")
	menuURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Menu", blank=True, null=True, help_text='''Either the actual menu or a URL of the menu.''', related_name="foodestablishment_menu_url")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FoodEstablishment'
		verbose_name_plural = 'FoodEstablishment'


class ParkingFacility(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="parkingfacility_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ParkingFacility'
		verbose_name_plural = 'ParkingFacility'


class ConvenienceStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="conveniencestore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ConvenienceStore'
		verbose_name_plural = 'ConvenienceStore'


class MusicAlbumReleaseType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="musicalbumreleasetype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicAlbumReleaseType'
		verbose_name_plural = 'MusicAlbumReleaseType'


class DisagreeAction(models.Model):

	reactAction = models.ForeignKey('ReactAction', on_delete=models.CASCADE, verbose_name="Reactaction", blank=True, null=True, help_text='''The act of responding instinctively and emotionally to an object, expressing a sentiment.''', related_name="disagreeaction_reactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DisagreeAction'
		verbose_name_plural = 'DisagreeAction'


class GovernmentPermit(models.Model):

	permit = models.ForeignKey('Permit', on_delete=models.CASCADE, verbose_name="Permit", blank=True, null=True, help_text='''A permit issued by an organization, e.g. a parking pass.''', related_name="governmentpermit_permit")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GovernmentPermit'
		verbose_name_plural = 'GovernmentPermit'


class LocalBusiness(models.Model):

	openingHoursText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Openinghours", blank=True, null=True, help_text='''The general opening hours for a business. Opening hours can be specified as a weekly time range, starting with days, then times per day. Multiple days can be listed with commas ',' separating each day. Day or time ranges are specified using a hyphen '-'.<br />- Days are specified using the following two-letter combinations: <code>Mo</code>, <code>Tu</code>, <code>We</code>, <code>Th</code>, <code>Fr</code>, <code>Sa</code>, <code>Su</code>.<br />- Times are specified using 24:00 time. For example, 3pm is specified as <code>15:00</code>. <br />- Here is an example: <code>&lt;span itemprop=&quot;openingHours&quot; content=&quot;Tu,Th 16:00-20:00&quot;&gt;Tuesdays and Thursdays 4-8pm&lt;/span&gt;</code>. <br />- If a business is open 7 days a week, then it can be specified as <code>&lt;span itemprop=&quot;openingHours&quot; content=&quot;Mo-Su&quot;&gt;Monday through Sunday, all day&lt;/span&gt;</code>.''', related_name="localbusiness_openinghours_text")
	paymentAcceptedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Paymentaccepted", blank=True, null=True, help_text='''Cash, credit card, etc.''', related_name="localbusiness_paymentaccepted_text")
	priceRangeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricerange", blank=True, null=True, help_text='''The price range of the business, for example <code>$$$</code>.''', related_name="localbusiness_pricerange_text")
	currenciesAcceptedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Currenciesaccepted", blank=True, null=True, help_text='''The currency accepted (in <a href='http://en.wikipedia.org/wiki/ISO_4217'>ISO 4217 currency format</a>).''', related_name="localbusiness_currenciesaccepted_text")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", blank=True, null=True, help_text='''An organization such as a school, NGO, corporation, club, etc.''', related_name="localbusiness_organization")
	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", blank=True, null=True, help_text='''Entities that have a somewhat fixed, physical extension.''', related_name="localbusiness_place")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LocalBusiness'
		verbose_name_plural = 'LocalBusiness'


class OrganizationRole(models.Model):

	numberedPositionNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Numberedposition", blank=True, null=True, help_text='''A number associated with a role in an organization, for example, the number on an athlete's jersey.''', related_name="organizationrole_numberedposition_number")
	role = models.ForeignKey('Role', on_delete=models.CASCADE, verbose_name="Role", blank=True, null=True, help_text='''Represents additional information about a relationship or property. For example a Role can be used to say that a 'member' role linking some SportsTeam to a player occurred during a particular time period. Or that a Person's 'actor' role in a Movie was for some particular characterName. Such properties can be attached to a Role entity, which is then associated with the main entities using ordinary properties like 'member' or 'actor'.

      <br/><br/>See also <a href="http://blog.schema.org/2014/06/introducing-role.html">blog post</a>.''', related_name="organizationrole_role")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OrganizationRole'
		verbose_name_plural = 'OrganizationRole'


class DislikeAction(models.Model):

	reactAction = models.ForeignKey('ReactAction', on_delete=models.CASCADE, verbose_name="Reactaction", blank=True, null=True, help_text='''The act of responding instinctively and emotionally to an object, expressing a sentiment.''', related_name="dislikeaction_reactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DislikeAction'
		verbose_name_plural = 'DislikeAction'


class SaleEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="saleevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SaleEvent'
		verbose_name_plural = 'SaleEvent'


class BorrowAction(models.Model):

	lenderPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Lender", blank=True, null=True, help_text='''A sub property of participant. The person that lends the object being borrowed.''', related_name="borrowaction_lender_person")
	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="Transferaction", blank=True, null=True, help_text='''The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.''', related_name="borrowaction_transferaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BorrowAction'
		verbose_name_plural = 'BorrowAction'


class Embassy(models.Model):

	governmentBuilding = models.ForeignKey('GovernmentBuilding', on_delete=models.CASCADE, verbose_name="Governmentbuilding", blank=True, null=True, help_text='''A government building.''', related_name="embassy_governmentbuilding")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Embassy'
		verbose_name_plural = 'Embassy'


class BroadcastChannel(models.Model):

	providesBroadcastServiceBroadcastService = models.ForeignKey('BroadcastService', on_delete=models.CASCADE, verbose_name="Providesbroadcastservice", blank=True, null=True, help_text='''The BroadcastService offered on this channel.''', related_name="broadcastchannel_providesbroadcastservice_broadcastservice")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="broadcastchannel_intangible")
	broadcastChannelIdText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Broadcastchannelid", blank=True, null=True, help_text='''The unique address by which the BroadcastService can be identified in a provider lineup. In US, this is typically a number.''', related_name="broadcastchannel_broadcastchannelid_text")
	inBroadcastLineupCableOrSatelliteService = models.ForeignKey('CableOrSatelliteService', on_delete=models.CASCADE, verbose_name="Inbroadcastlineup", blank=True, null=True, help_text='''The CableOrSatelliteService offering the channel.''', related_name="broadcastchannel_inbroadcastlineup_cableorsatelliteservice")
	broadcastServiceTierText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Broadcastservicetier", blank=True, null=True, help_text='''The type of service required to have access to the channel (e.g. Standard or Premium).''', related_name="broadcastchannel_broadcastservicetier_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BroadcastChannel'
		verbose_name_plural = 'BroadcastChannel'


class TaxiService(models.Model):

	service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Service", blank=True, null=True, help_text='''A service provided by an organization, e.g. delivery service, print services, etc.''', related_name="taxiservice_service")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TaxiService'
		verbose_name_plural = 'TaxiService'


class Landform(models.Model):

	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", blank=True, null=True, help_text='''Entities that have a somewhat fixed, physical extension.''', related_name="landform_place")

	def __str__(self):
		return str(self.place.thing.nameText.value)

	class Meta:
		verbose_name = 'Landform'
		verbose_name_plural = 'Landform'


class EmergencyService(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="emergencyservice_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EmergencyService'
		verbose_name_plural = 'EmergencyService'


class TrainStation(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="trainstation_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TrainStation'
		verbose_name_plural = 'TrainStation'


class NailSalon(models.Model):

	healthAndBeautyBusiness = models.ForeignKey('HealthAndBeautyBusiness', on_delete=models.CASCADE, verbose_name="Healthandbeautybusiness", blank=True, null=True, help_text='''Health and beauty.''', related_name="nailsalon_healthandbeautybusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'NailSalon'
		verbose_name_plural = 'NailSalon'


class ItemList(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="itemlist_intangible")
	itemListOrderItemListOrderType = models.ForeignKey('ItemListOrderType', on_delete=models.CASCADE, verbose_name="Itemlistorder", blank=True, null=True, help_text='''Type of ordering (e.g. Ascending, Descending, Unordered).''', related_name="itemlist_itemlistorder_itemlistordertype")
	itemListOrderText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Itemlistorder", blank=True, null=True, help_text='''Type of ordering (e.g. Ascending, Descending, Unordered).''', related_name="itemlist_itemlistorder_text")
	numberOfItemsInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofitems", blank=True, null=True, help_text='''The number of items in an ItemList. Note that some descriptions might not fully describe all items in a list (e.g., multi-page pagination); in such cases, the numberOfItems would be for the entire list.''', related_name="itemlist_numberofitems_integer")
	itemListElementThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Itemlistelement", blank=True, null=True, help_text='''For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.
    <br/><br/>
    Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.
    <br/><br/>
    Note: The order of elements in your mark-up is not sufficient for indicating the order or elements.  Use ListItem with a 'position' property in such cases.''', related_name="itemlist_itemlistelement_thing")
	itemListElementListItem = models.ForeignKey('ListItem', on_delete=models.CASCADE, verbose_name="Itemlistelement", blank=True, null=True, help_text='''For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.
    <br/><br/>
    Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.
    <br/><br/>
    Note: The order of elements in your mark-up is not sufficient for indicating the order or elements.  Use ListItem with a 'position' property in such cases.''', related_name="itemlist_itemlistelement_listitem")
	itemListElementText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Itemlistelement", blank=True, null=True, help_text='''For itemListElement values, you can use simple strings (e.g. "Peter", "Paul", "Mary"), existing entities, or use ListItem.
    <br/><br/>
    Text values are best if the elements in the list are plain strings. Existing entities are best for a simple, unordered list of existing things in your data. ListItem is used with ordered lists when you want to provide additional context about the element in that list or when the same item might be in different places in different lists.
    <br/><br/>
    Note: The order of elements in your mark-up is not sufficient for indicating the order or elements.  Use ListItem with a 'position' property in such cases.''', related_name="itemlist_itemlistelement_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ItemList'
		verbose_name_plural = 'ItemList'


class SearchResultsPage(models.Model):

	webPage = models.ForeignKey('WebPage', on_delete=models.CASCADE, verbose_name="Webpage", blank=True, null=True, help_text='''A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.''', related_name="searchresultspage_webpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SearchResultsPage'
		verbose_name_plural = 'SearchResultsPage'


class BroadcastService(models.Model):

	service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Service", blank=True, null=True, help_text='''A service provided by an organization, e.g. delivery service, print services, etc.''', related_name="broadcastservice_service")
	broadcastTimezoneText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Broadcasttimezone", blank=True, null=True, help_text='''The timezone in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 format</a> for which the service bases its broadcasts.''', related_name="broadcastservice_broadcasttimezone_text")
	broadcastDisplayNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Broadcastdisplayname", blank=True, null=True, help_text='''The name displayed in the channel guide. For many US affiliates, it is the network name.''', related_name="broadcastservice_broadcastdisplayname_text")
	broadcastAffiliateOfOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Broadcastaffiliateof", blank=True, null=True, help_text='''The media network(s) whose content is broadcast on this station.''', related_name="broadcastservice_broadcastaffiliateof_organization")
	parentServiceBroadcastService = models.ForeignKey('BroadcastService', on_delete=models.CASCADE, verbose_name="Parentservice", blank=True, null=True, help_text='''A broadcast service to which the broadcast service may belong to such as regional variations of a national channel.''', related_name="broadcastservice_parentservice_broadcastservice")
	broadcasterOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Broadcaster", blank=True, null=True, help_text='''The organization owning or operating the broadcast service.''', related_name="broadcastservice_broadcaster_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BroadcastService'
		verbose_name_plural = 'BroadcastService'


class OrganizeAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="organizeaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OrganizeAction'
		verbose_name_plural = 'OrganizeAction'


class PlanAction(models.Model):

	organizeAction = models.ForeignKey('OrganizeAction', on_delete=models.CASCADE, verbose_name="Organizeaction", blank=True, null=True, help_text='''The act of manipulating/administering/supervising/controlling one or more objects.''', related_name="planaction_organizeaction")
	scheduledTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Scheduledtime", blank=True, null=True, help_text='''The time the object is scheduled to.''', related_name="planaction_scheduledtime_datetime")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PlanAction'
		verbose_name_plural = 'PlanAction'


class ServiceChannel(models.Model):

	providesServiceService = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Providesservice", blank=True, null=True, help_text='''The service provided by this channel.''', related_name="servicechannel_providesservice_service")
	availableLanguageLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Availablelanguage", blank=True, null=True, help_text='''A language someone may use with the item. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[inLanguage]].''', related_name="servicechannel_availablelanguage_language")
	availableLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Availablelanguage", blank=True, null=True, help_text='''A language someone may use with the item. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[inLanguage]].''', related_name="servicechannel_availablelanguage_text")
	serviceUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Serviceurl", blank=True, null=True, help_text='''The website to access the service.''', related_name="servicechannel_serviceurl_url")
	servicePhoneContactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Servicephone", blank=True, null=True, help_text='''The phone number to use to access the service.''', related_name="servicechannel_servicephone_contactpoint")
	processingTimeDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Processingtime", blank=True, null=True, help_text='''Estimated processing time for the service using this channel.''', related_name="servicechannel_processingtime_duration")
	servicePostalAddressPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Servicepostaladdress", blank=True, null=True, help_text='''The address for accessing the service by mail.''', related_name="servicechannel_servicepostaladdress_postaladdress")
	serviceSmsNumberContactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Servicesmsnumber", blank=True, null=True, help_text='''The number to access the service by text message.''', related_name="servicechannel_servicesmsnumber_contactpoint")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="servicechannel_intangible")
	serviceLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Servicelocation", blank=True, null=True, help_text='''The location (e.g. civic structure, local business, etc.) where a person can go to access the service.''', related_name="servicechannel_servicelocation_place")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ServiceChannel'
		verbose_name_plural = 'ServiceChannel'


class ContactPoint(models.Model):

	productSupportedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Productsupported", blank=True, null=True, help_text='''The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").''', related_name="contactpoint_productsupported_text")
	productSupportedProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Productsupported", blank=True, null=True, help_text='''The product or service this support contact point is related to (such as product support for a particular product line). This can be a specific product or product line (e.g. "iPhone") or a general category of products or services (e.g. "smartphones").''', related_name="contactpoint_productsupported_product")
	availableLanguageLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Availablelanguage", blank=True, null=True, help_text='''A language someone may use with the item. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[inLanguage]].''', related_name="contactpoint_availablelanguage_language")
	availableLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Availablelanguage", blank=True, null=True, help_text='''A language someone may use with the item. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[inLanguage]].''', related_name="contactpoint_availablelanguage_text")
	contactTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Contacttype", blank=True, null=True, help_text='''A person or organization can have different contact points, for different purposes. For example, a sales contact point, a PR contact point and so on. This property is used to specify the kind of contact point.''', related_name="contactpoint_contacttype_text")
	areaServedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="contactpoint_areaserved_text")
	areaServedAdministrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="contactpoint_areaserved_administrativearea")
	areaServedPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="contactpoint_areaserved_place")
	areaServedGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="contactpoint_areaserved_geoshape")
	hoursAvailableOpeningHoursSpecification = models.ForeignKey('OpeningHoursSpecification', on_delete=models.CASCADE, verbose_name="Hoursavailable", blank=True, null=True, help_text='''The hours during which this service or contact is available.''', related_name="contactpoint_hoursavailable_openinghoursspecification")
	emailText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Email", blank=True, null=True, help_text='''Email address.''', related_name="contactpoint_email_text")
	faxNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Faxnumber", blank=True, null=True, help_text='''The fax number.''', related_name="contactpoint_faxnumber_text")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="contactpoint_structuredvalue")
	telephoneText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Telephone", blank=True, null=True, help_text='''The telephone number.''', related_name="contactpoint_telephone_text")
	contactOptionContactPointOption = models.ForeignKey('ContactPointOption', on_delete=models.CASCADE, verbose_name="Contactoption", blank=True, null=True, help_text='''An option available on this contact point (e.g. a toll-free number or support for hearing-impaired callers).''', related_name="contactpoint_contactoption_contactpointoption")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ContactPoint'
		verbose_name_plural = 'ContactPoint'


class MovieTheater(models.Model):

	entertainmentBusiness = models.ForeignKey('EntertainmentBusiness', on_delete=models.CASCADE, verbose_name="Entertainmentbusiness", blank=True, null=True, help_text='''A business providing entertainment.''', related_name="movietheater_entertainmentbusiness")
	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="movietheater_civicstructure")
	screenCountNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Screencount", blank=True, null=True, help_text='''The number of screens in the movie theater.''', related_name="movietheater_screencount_number")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MovieTheater'
		verbose_name_plural = 'MovieTheater'


class Crematorium(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="crematorium_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Crematorium'
		verbose_name_plural = 'Crematorium'


class TVSeries(models.Model):

	musicByMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="tvseries_musicby_musicgroup")
	musicByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="tvseries_musicby_person")
	trailerVideoObject = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", blank=True, null=True, help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="tvseries_trailer_videoobject")
	creativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Creativeworkseries", blank=True, null=True, help_text='''
          A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind.
          CreativeWorkSeries are usually organized into some order, often chronological. Unlike <a href="/ItemList">ItemList</a> which
          is a general purpose data structure for lists of things, the emphasis with
          CreativeWorkSeries is on published materials (written e.g. books and periodicals,
          or media such as tv, radio and games).

          <br/><br/>

          Specific subtypes are available for describing <a href="/TVSeries">TVSeries</a>, <a href="/RadioSeries">RadioSeries</a>,
          <a href="/MovieSeries">MovieSeries</a>,
          <a href="/BookSeries">BookSeries</a>,
          <a href="/Periodical">Periodical</a>
          and <a href="/VideoGameSeries">VideoGameSeries</a>. In each case,
          the <a href="/hasPart">hasPart</a> / <a href="/isPartOf">isPartOf</a> properties
          can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely
          just to organize these more specific and practical subtypes.

          <br/><br/>

          It is common for properties applicable to an item from the series to be usefully applied to the containing group.
          Schema.org attempts to anticipate some of these cases, but publishers should be free to apply
          properties of the series parts to the series as a whole wherever they seem appropriate.''', related_name="tvseries_creativeworkseries")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="tvseries_creativework")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="tvseries_director_person")
	countryOfOriginCountry = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Countryoforigin", blank=True, null=True, help_text='''The country of the principal offices of the production company or individual responsible for the movie or program.''', related_name="tvseries_countryoforigin_country")
	episodeEpisode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", blank=True, null=True, help_text='''An episode of a tv, radio or game media within a series or season.''', related_name="tvseries_episode_episode")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="tvseries_actor_person")
	containsSeasonCreativeWorkSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Containsseason", blank=True, null=True, help_text='''A season that is part of the media series.''', related_name="tvseries_containsseason_creativeworkseason")
	numberOfSeasonsInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofseasons", blank=True, null=True, help_text='''The number of seasons in this series.''', related_name="tvseries_numberofseasons_integer")
	productionCompanyOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", blank=True, null=True, help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="tvseries_productioncompany_organization")
	numberOfEpisodesInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofepisodes", blank=True, null=True, help_text='''The number of episodes in this season or series.''', related_name="tvseries_numberofepisodes_integer")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TVSeries'
		verbose_name_plural = 'TVSeries'


class GovernmentOrganization(models.Model):

	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", blank=True, null=True, help_text='''An organization such as a school, NGO, corporation, club, etc.''', related_name="governmentorganization_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GovernmentOrganization'
		verbose_name_plural = 'GovernmentOrganization'


class ExerciseAction(models.Model):

	exerciseCoursePlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Exercisecourse", blank=True, null=True, help_text='''A sub property of location. The course where this action was taken.''', related_name="exerciseaction_exercisecourse_place")
	opponentPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Opponent", blank=True, null=True, help_text='''A sub property of participant. The opponent on this action.''', related_name="exerciseaction_opponent_person")
	fromLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Fromlocation", blank=True, null=True, help_text='''A sub property of location. The original location of the object or the agent before the action.''', related_name="exerciseaction_fromlocation_place")
	toLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Tolocation", blank=True, null=True, help_text='''A sub property of location. The final location of the object or the agent after the action.''', related_name="exerciseaction_tolocation_place")
	distanceDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Distance", blank=True, null=True, help_text='''The distance travelled, e.g. exercising or travelling.''', related_name="exerciseaction_distance_distance")
	sportsActivityLocationSportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sub property of location. The sports activity location where this action occurred.''', related_name="exerciseaction_sportsactivitylocation_sportsactivitylocation")
	sportsEventSportsEvent = models.ForeignKey('SportsEvent', on_delete=models.CASCADE, verbose_name="Sportsevent", blank=True, null=True, help_text='''A sub property of location. The sports event where this action occurred.''', related_name="exerciseaction_sportsevent_sportsevent")
	playAction = models.ForeignKey('PlayAction', on_delete=models.CASCADE, verbose_name="Playaction", blank=True, null=True, help_text='''The act of playing/exercising/training/performing for enjoyment, leisure, recreation, Competition or exercise.<p>Related actions:</p><ul><li><a href="http://schema.org/ListenAction">ListenAction</a>: Unlike ListenAction (which is under ConsumeAction), PlayAction refers to performing for an audience or at an event, rather than consuming music.</li><li><a href="http://schema.org/WatchAction">WatchAction</a>: Unlike WatchAction (which is under ConsumeAction), PlayAction refers to showing/displaying for an audience or at an event, rather than consuming visual content</li></ul>.''', related_name="exerciseaction_playaction")
	sportsTeamSportsTeam = models.ForeignKey('SportsTeam', on_delete=models.CASCADE, verbose_name="Sportsteam", blank=True, null=True, help_text='''A sub property of participant. The sports team that participated on this action.''', related_name="exerciseaction_sportsteam_sportsteam")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ExerciseAction'
		verbose_name_plural = 'ExerciseAction'


class Festival(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="festival_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Festival'
		verbose_name_plural = 'Festival'


class FastFoodRestaurant(models.Model):

	foodEstablishment = models.ForeignKey('FoodEstablishment', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A food-related business.''', related_name="fastfoodrestaurant_foodestablishment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FastFoodRestaurant'
		verbose_name_plural = 'FastFoodRestaurant'


class CookAction(models.Model):

	createAction = models.ForeignKey('CreateAction', on_delete=models.CASCADE, verbose_name="Createaction", blank=True, null=True, help_text='''The act of deliberately creating/producing/generating/building a result out of the agent.''', related_name="cookaction_createaction")
	foodEstablishmentFoodEstablishment = models.ForeignKey('FoodEstablishment', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A sub property of location. The specific food establishment where the action occurred.''', related_name="cookaction_foodestablishment_foodestablishment")
	foodEstablishmentPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A sub property of location. The specific food establishment where the action occurred.''', related_name="cookaction_foodestablishment_place")
	recipeRecipe = models.ForeignKey('Recipe', on_delete=models.CASCADE, verbose_name="Recipe", blank=True, null=True, help_text='''A sub property of instrument. The recipe/instructions used to perform the action.''', related_name="cookaction_recipe_recipe")
	foodEventFoodEvent = models.ForeignKey('FoodEvent', on_delete=models.CASCADE, verbose_name="Foodevent", blank=True, null=True, help_text='''A sub property of location. The specific food event where the action occurred.''', related_name="cookaction_foodevent_foodevent")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CookAction'
		verbose_name_plural = 'CookAction'


class LodgingBusiness(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="lodgingbusiness_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LodgingBusiness'
		verbose_name_plural = 'LodgingBusiness'


class DayOfWeek(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="dayofweek_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DayOfWeek'
		verbose_name_plural = 'DayOfWeek'


class ChooseAction(models.Model):

	actionOptionThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Actionoption", blank=True, null=True, help_text='''A sub property of object. The options subject to this action.''', related_name="chooseaction_actionoption_thing")
	actionOptionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Actionoption", blank=True, null=True, help_text='''A sub property of object. The options subject to this action.''', related_name="chooseaction_actionoption_text")
	assessAction = models.ForeignKey('AssessAction', on_delete=models.CASCADE, verbose_name="Assessaction", blank=True, null=True, help_text='''The act of forming one's opinion, reaction or sentiment.''', related_name="chooseaction_assessaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ChooseAction'
		verbose_name_plural = 'ChooseAction'


class MedicalOrganization(models.Model):

	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", blank=True, null=True, help_text='''An organization such as a school, NGO, corporation, club, etc.''', related_name="medicalorganization_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MedicalOrganization'
		verbose_name_plural = 'MedicalOrganization'


class DeliveryChargeSpecification(models.Model):

	priceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", blank=True, null=True, help_text='''A structured value representing a price or price range. Typically, only the subclasses of this type are used for markup. It is recommended to use [[MonetaryAmount]] to describe independent amounts of money such as a salary, credit card limits, etc.''', related_name="deliverychargespecification_pricespecification")
	appliesToDeliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Appliestodeliverymethod", blank=True, null=True, help_text='''The delivery method(s) to which the delivery charge or payment charge specification applies.''', related_name="deliverychargespecification_appliestodeliverymethod_deliverymethod")
	areaServedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="deliverychargespecification_areaserved_text")
	areaServedAdministrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="deliverychargespecification_areaserved_administrativearea")
	areaServedPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="deliverychargespecification_areaserved_place")
	areaServedGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="deliverychargespecification_areaserved_geoshape")
	ineligibleRegionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Ineligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.
      <br><br> See also <a href="/eligibleRegion">eligibleRegion</a>.
      ''', related_name="deliverychargespecification_ineligibleregion_text")
	ineligibleRegionGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Ineligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.
      <br><br> See also <a href="/eligibleRegion">eligibleRegion</a>.
      ''', related_name="deliverychargespecification_ineligibleregion_geoshape")
	ineligibleRegionPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Ineligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.
      <br><br> See also <a href="/eligibleRegion">eligibleRegion</a>.
      ''', related_name="deliverychargespecification_ineligibleregion_place")
	eligibleRegionPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Eligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.
      <br><br> See also <a href="/ineligibleRegion">ineligibleRegion</a>.
    ''', related_name="deliverychargespecification_eligibleregion_place")
	eligibleRegionGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Eligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.
      <br><br> See also <a href="/ineligibleRegion">ineligibleRegion</a>.
    ''', related_name="deliverychargespecification_eligibleregion_geoshape")
	eligibleRegionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Eligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.
      <br><br> See also <a href="/ineligibleRegion">ineligibleRegion</a>.
    ''', related_name="deliverychargespecification_eligibleregion_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DeliveryChargeSpecification'
		verbose_name_plural = 'DeliveryChargeSpecification'


class CreativeWorkSeason(models.Model):

	trailerVideoObject = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", blank=True, null=True, help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="creativeworkseason_trailer_videoobject")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="creativeworkseason_director_person")
	episodeEpisode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", blank=True, null=True, help_text='''An episode of a tv, radio or game media within a series or season.''', related_name="creativeworkseason_episode_episode")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="creativeworkseason_actor_person")
	seasonNumberInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Seasonnumber", blank=True, null=True, help_text='''Position of the season within an ordered group of seasons.''', related_name="creativeworkseason_seasonnumber_integer")
	seasonNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Seasonnumber", blank=True, null=True, help_text='''Position of the season within an ordered group of seasons.''', related_name="creativeworkseason_seasonnumber_text")
	startDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", blank=True, null=True, help_text='''The start date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="creativeworkseason_startdate_date")
	productionCompanyOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", blank=True, null=True, help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="creativeworkseason_productioncompany_organization")
	numberOfEpisodesInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofepisodes", blank=True, null=True, help_text='''The number of episodes in this season or series.''', related_name="creativeworkseason_numberofepisodes_integer")
	partOfSeriesCreativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Partofseries", blank=True, null=True, help_text='''The series to which this episode or season belongs.''', related_name="creativeworkseason_partofseries_creativeworkseries")
	endDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", blank=True, null=True, help_text='''The end date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="creativeworkseason_enddate_date")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="creativeworkseason_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CreativeWorkSeason'
		verbose_name_plural = 'CreativeWorkSeason'


class SomeProducts(models.Model):

	inventoryLevelQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Inventorylevel", blank=True, null=True, help_text='''The current approximate inventory level for the item or items.''', related_name="someproducts_inventorylevel_quantitativevalue")
	product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product", blank=True, null=True, help_text='''Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.''', related_name="someproducts_product")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SomeProducts'
		verbose_name_plural = 'SomeProducts'


class DepartmentStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="departmentstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DepartmentStore'
		verbose_name_plural = 'DepartmentStore'


class Question(models.Model):

	acceptedAnswerAnswer = models.ForeignKey('Answer', on_delete=models.CASCADE, verbose_name="Acceptedanswer", blank=True, null=True, help_text='''The answer that has been accepted as best, typically on a Question/Answer site. Sites vary in their selection mechanisms, e.g. drawing on community opinion and/or the view of the Question author.''', related_name="question_acceptedanswer_answer")
	upvoteCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Upvotecount", blank=True, null=True, help_text='''The number of upvotes this question, answer or comment has received from the community.''', related_name="question_upvotecount_integer")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="question_creativework")
	answerCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Answercount", blank=True, null=True, help_text='''The number of answers this question has received.''', related_name="question_answercount_integer")
	suggestedAnswerAnswer = models.ForeignKey('Answer', on_delete=models.CASCADE, verbose_name="Suggestedanswer", blank=True, null=True, help_text='''An answer (possibly one of several, possibly incorrect) to a Question, e.g. on a Question/Answer site.''', related_name="question_suggestedanswer_answer")
	downvoteCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Downvotecount", blank=True, null=True, help_text='''The number of downvotes this question, answer or comment has received from the community.''', related_name="question_downvotecount_integer")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Question'
		verbose_name_plural = 'Question'


class TypeAndQuantityNode(models.Model):

	businessFunctionBusinessFunction = models.ForeignKey('BusinessFunction', on_delete=models.CASCADE, verbose_name="Businessfunction", blank=True, null=True, help_text='''The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.''', related_name="typeandquantitynode_businessfunction_businessfunction")
	unitCodeURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Unitcode", blank=True, null=True, help_text='''The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.''', related_name="typeandquantitynode_unitcode_url")
	unitCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unitcode", blank=True, null=True, help_text='''The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.''', related_name="typeandquantitynode_unitcode_text")
	unitTextText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unittext", blank=True, null=True, help_text='''A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
<a href='unitCode'>unitCode</a>.''', related_name="typeandquantitynode_unittext_text")
	typeOfGoodProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Typeofgood", blank=True, null=True, help_text='''The product that this structured value is referring to.''', related_name="typeandquantitynode_typeofgood_product")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="typeandquantitynode_structuredvalue")
	amountOfThisGoodNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Amountofthisgood", blank=True, null=True, help_text='''The quantity of the goods included in the offer.''', related_name="typeandquantitynode_amountofthisgood_number")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TypeAndQuantityNode'
		verbose_name_plural = 'TypeAndQuantityNode'


class InteractionCounter(models.Model):

	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="interactioncounter_structuredvalue")
	interactionServiceSoftwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Interactionservice", blank=True, null=True, help_text='''The WebSite or SoftwareApplication where the interactions took place.''', related_name="interactioncounter_interactionservice_softwareapplication")
	interactionServiceWebSite = models.ForeignKey('WebSite', on_delete=models.CASCADE, verbose_name="Interactionservice", blank=True, null=True, help_text='''The WebSite or SoftwareApplication where the interactions took place.''', related_name="interactioncounter_interactionservice_website")
	userInteractionCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Userinteractioncount", blank=True, null=True, help_text='''The number of interactions for the CreativeWork using the WebSite or SoftwareApplication.''', related_name="interactioncounter_userinteractioncount_integer")
	interactionTypeAction = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Interactiontype", blank=True, null=True, help_text='''The Action representing the type of interaction. For up votes, +1s, etc. use <a href="/LikeAction";>LikeAction</a>. For down votes use <a href="/DislikeAction">DislikeAction</a>. Otherwise, use the most specific Action.''', related_name="interactioncounter_interactiontype_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'InteractionCounter'
		verbose_name_plural = 'InteractionCounter'


class SportingGoodsStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="sportinggoodsstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SportingGoodsStore'
		verbose_name_plural = 'SportingGoodsStore'


class HousePainter(models.Model):

	homeAndConstructionBusiness = models.ForeignKey('HomeAndConstructionBusiness', on_delete=models.CASCADE, verbose_name="Homeandconstructionbusiness", blank=True, null=True, help_text='''A construction business.
        <br><br>
        A HomeAndConstructionBusiness is a LocalBusiness that provides services around homes and buildings.
          <br><br>
          As a <a href="/LocalBusiness">LocalBusiness</a> it can be
          described as a <a href="/provider">provider</a> of one or more
          <a href="/Service">Service(s)</a>.
      ''', related_name="housepainter_homeandconstructionbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HousePainter'
		verbose_name_plural = 'HousePainter'


class InsertAction(models.Model):

	addAction = models.ForeignKey('AddAction', on_delete=models.CASCADE, verbose_name="Addaction", blank=True, null=True, help_text='''The act of editing by adding an object to a collection.''', related_name="insertaction_addaction")
	toLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Tolocation", blank=True, null=True, help_text='''A sub property of location. The final location of the object or the agent after the action.''', related_name="insertaction_tolocation_place")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'InsertAction'
		verbose_name_plural = 'InsertAction'


class OnDemandEvent(models.Model):

	publicationEvent = models.ForeignKey('PublicationEvent', on_delete=models.CASCADE, verbose_name="Publicationevent", blank=True, null=True, help_text='''A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media.''', related_name="ondemandevent_publicationevent")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OnDemandEvent'
		verbose_name_plural = 'OnDemandEvent'


class Date(models.Model):

	value = models.DateField(blank=True, null=True, verbose_name="Value", help_text='''A date value in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>.''')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Date'
		verbose_name_plural = 'Date'


class DriveWheelConfigurationValue(models.Model):

	qualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Qualitativevalue", blank=True, null=True, help_text='''A predefined value for a product characteristic, e.g. the power cord plug type "US" or the garment sizes "S", "M", "L", and "XL".''', related_name="drivewheelconfigurationvalue_qualitativevalue")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DriveWheelConfigurationValue'
		verbose_name_plural = 'DriveWheelConfigurationValue'


class AggregateRating(models.Model):

	reviewCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Reviewcount", blank=True, null=True, help_text='''The count of total number of reviews.''', related_name="aggregaterating_reviewcount_integer")
	rating = models.ForeignKey('Rating', on_delete=models.CASCADE, verbose_name="Rating", blank=True, null=True, help_text='''A rating is an evaluation on a numeric scale, such as 1 to 5 stars.''', related_name="aggregaterating_rating")
	itemReviewedThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Itemreviewed", blank=True, null=True, help_text='''The item that is being reviewed/rated.''', related_name="aggregaterating_itemreviewed_thing")
	ratingCountInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Ratingcount", blank=True, null=True, help_text='''The count of total number of ratings.''', related_name="aggregaterating_ratingcount_integer")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AggregateRating'
		verbose_name_plural = 'AggregateRating'


class Season(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Season'
		verbose_name_plural = 'Season'


class HairSalon(models.Model):

	healthAndBeautyBusiness = models.ForeignKey('HealthAndBeautyBusiness', on_delete=models.CASCADE, verbose_name="Healthandbeautybusiness", blank=True, null=True, help_text='''Health and beauty.''', related_name="hairsalon_healthandbeautybusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HairSalon'
		verbose_name_plural = 'HairSalon'


class WearAction(models.Model):

	useAction = models.ForeignKey('UseAction', on_delete=models.CASCADE, verbose_name="Useaction", blank=True, null=True, help_text='''The act of applying an object to its intended purpose.''', related_name="wearaction_useaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WearAction'
		verbose_name_plural = 'WearAction'


class ListItem(models.Model):

	positionInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Position", blank=True, null=True, help_text='''The position of an item in a series or sequence of items.''', related_name="listitem_position_integer")
	positionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Position", blank=True, null=True, help_text='''The position of an item in a series or sequence of items.''', related_name="listitem_position_text")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="listitem_intangible")
	previousItemListItem = models.ForeignKey('ListItem', on_delete=models.CASCADE, verbose_name="Previousitem", blank=True, null=True, help_text='''A link to the ListItem that preceeds the current one.''', related_name="listitem_previousitem_listitem")
	nextItemListItem = models.ForeignKey('ListItem', on_delete=models.CASCADE, verbose_name="Nextitem", blank=True, null=True, help_text='''A link to the ListItem that follows the current one.''', related_name="listitem_nextitem_listitem")
	itemThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Item", blank=True, null=True, help_text='''An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists')’.''', related_name="listitem_item_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ListItem'
		verbose_name_plural = 'ListItem'


class VideoGame(models.Model):

	musicByMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="videogame_musicby_musicgroup")
	musicByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="videogame_musicby_person")
	trailerVideoObject = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", blank=True, null=True, help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="videogame_trailer_videoobject")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="videogame_director_person")
	gameServerGameServer = models.ForeignKey('GameServer', on_delete=models.CASCADE, verbose_name="Gameserver", blank=True, null=True, help_text='''The server on which  it is possible to play the game.''', related_name="videogame_gameserver_gameserver")
	cheatCodeCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Cheatcode", blank=True, null=True, help_text='''Cheat codes to the game.''', related_name="videogame_cheatcode_creativework")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="videogame_actor_person")
	gameTipCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Gametip", blank=True, null=True, help_text='''Links to tips, tactics, etc.''', related_name="videogame_gametip_creativework")
	playModeGamePlayMode = models.ForeignKey('GamePlayMode', on_delete=models.CASCADE, verbose_name="Playmode", blank=True, null=True, help_text='''Indicates whether this game is multi-player, co-op or single-player.  The game can be marked as multi-player, co-op and single-player at the same time.''', related_name="videogame_playmode_gameplaymode")
	softwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Softwareapplication", blank=True, null=True, help_text='''A software application.''', related_name="videogame_softwareapplication")
	game = models.ForeignKey('Game', on_delete=models.CASCADE, verbose_name="Game", blank=True, null=True, help_text='''The Game type represents things which are games. These are typically rule-governed recreational activities, e.g. role-playing games in which players assume the role of characters in a fictional setting.''', related_name="videogame_game")
	gamePlatformThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Gameplatform", blank=True, null=True, help_text='''The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.''', related_name="videogame_gameplatform_thing")
	gamePlatformText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gameplatform", blank=True, null=True, help_text='''The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.''', related_name="videogame_gameplatform_text")
	gamePlatformURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Gameplatform", blank=True, null=True, help_text='''The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.''', related_name="videogame_gameplatform_url")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'VideoGame'
		verbose_name_plural = 'VideoGame'


class PawnShop(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="pawnshop_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PawnShop'
		verbose_name_plural = 'PawnShop'


class DiscussionForumPosting(models.Model):

	socialMediaPosting = models.ForeignKey('SocialMediaPosting', on_delete=models.CASCADE, verbose_name="Socialmediaposting", blank=True, null=True, help_text='''A post to a social media platform, including blog posts, tweets, Facebook posts, etc.''', related_name="discussionforumposting_socialmediaposting")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DiscussionForumPosting'
		verbose_name_plural = 'DiscussionForumPosting'


class IgnoreAction(models.Model):

	assessAction = models.ForeignKey('AssessAction', on_delete=models.CASCADE, verbose_name="Assessaction", blank=True, null=True, help_text='''The act of forming one's opinion, reaction or sentiment.''', related_name="ignoreaction_assessaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'IgnoreAction'
		verbose_name_plural = 'IgnoreAction'


class PayAction(models.Model):

	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="Tradeaction", blank=True, null=True, help_text='''The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.''', related_name="payaction_tradeaction")
	recipientPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="payaction_recipient_person")
	recipientAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="payaction_recipient_audience")
	recipientOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="payaction_recipient_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PayAction'
		verbose_name_plural = 'PayAction'


class PerformAction(models.Model):

	playAction = models.ForeignKey('PlayAction', on_delete=models.CASCADE, verbose_name="Playaction", blank=True, null=True, help_text='''The act of playing/exercising/training/performing for enjoyment, leisure, recreation, Competition or exercise.<p>Related actions:</p><ul><li><a href="http://schema.org/ListenAction">ListenAction</a>: Unlike ListenAction (which is under ConsumeAction), PlayAction refers to performing for an audience or at an event, rather than consuming music.</li><li><a href="http://schema.org/WatchAction">WatchAction</a>: Unlike WatchAction (which is under ConsumeAction), PlayAction refers to showing/displaying for an audience or at an event, rather than consuming visual content</li></ul>.''', related_name="performaction_playaction")
	entertainmentBusinessEntertainmentBusiness = models.ForeignKey('EntertainmentBusiness', on_delete=models.CASCADE, verbose_name="Entertainmentbusiness", blank=True, null=True, help_text='''A sub property of location. The entertainment business where the action occurred.''', related_name="performaction_entertainmentbusiness_entertainmentbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PerformAction'
		verbose_name_plural = 'PerformAction'


class JewelryStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="jewelrystore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'JewelryStore'
		verbose_name_plural = 'JewelryStore'


class Canal(models.Model):

	bodyOfWater = models.ForeignKey('BodyOfWater', on_delete=models.CASCADE, verbose_name="Bodyofwater", blank=True, null=True, help_text='''A body of water, such as a sea, ocean, or lake.''', related_name="canal_bodyofwater")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Canal'
		verbose_name_plural = 'Canal'


class Car(models.Model):

	vehicle = models.ForeignKey('Vehicle', on_delete=models.CASCADE, verbose_name="Vehicle", blank=True, null=True, help_text='''A vehicle is a device that is designed or used to transport people or cargo over land, water, air, or through space.''', related_name="car_vehicle")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Car'
		verbose_name_plural = 'Car'


class Game(models.Model):

	gameLocationURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Gamelocation", blank=True, null=True, help_text='''Real or fictional location of the game (or part of game).''', related_name="game_gamelocation_url")
	gameLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Gamelocation", blank=True, null=True, help_text='''Real or fictional location of the game (or part of game).''', related_name="game_gamelocation_place")
	gameLocationPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Gamelocation", blank=True, null=True, help_text='''Real or fictional location of the game (or part of game).''', related_name="game_gamelocation_postaladdress")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="game_creativework")
	questThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Quest", blank=True, null=True, help_text='''The task that a player-controlled character, or group of characters may complete in order to gain a reward.''', related_name="game_quest_thing")
	gameItemThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Gameitem", blank=True, null=True, help_text='''An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.''', related_name="game_gameitem_thing")
	numberOfPlayersQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofplayers", blank=True, null=True, help_text='''Indicate how many people can play this game (minimum, maximum, or range).''', related_name="game_numberofplayers_quantitativevalue")
	characterAttributeThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Characterattribute", blank=True, null=True, help_text='''A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).''', related_name="game_characterattribute_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Game'
		verbose_name_plural = 'Game'


class Episode(models.Model):

	musicByMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="episode_musicby_musicgroup")
	musicByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="episode_musicby_person")
	trailerVideoObject = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", blank=True, null=True, help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="episode_trailer_videoobject")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="episode_director_person")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="episode_creativework")
	partOfSeasonCreativeWorkSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Partofseason", blank=True, null=True, help_text='''The season to which this episode belongs.''', related_name="episode_partofseason_creativeworkseason")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="episode_actor_person")
	episodeNumberInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Episodenumber", blank=True, null=True, help_text='''Position of the episode within an ordered group of episodes.''', related_name="episode_episodenumber_integer")
	episodeNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Episodenumber", blank=True, null=True, help_text='''Position of the episode within an ordered group of episodes.''', related_name="episode_episodenumber_text")
	productionCompanyOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", blank=True, null=True, help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="episode_productioncompany_organization")
	partOfSeriesCreativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Partofseries", blank=True, null=True, help_text='''The series to which this episode or season belongs.''', related_name="episode_partofseries_creativeworkseries")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Episode'
		verbose_name_plural = 'Episode'


class LegislativeBuilding(models.Model):

	governmentBuilding = models.ForeignKey('GovernmentBuilding', on_delete=models.CASCADE, verbose_name="Governmentbuilding", blank=True, null=True, help_text='''A government building.''', related_name="legislativebuilding_governmentbuilding")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LegislativeBuilding'
		verbose_name_plural = 'LegislativeBuilding'


class IceCreamShop(models.Model):

	foodEstablishment = models.ForeignKey('FoodEstablishment', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A food-related business.''', related_name="icecreamshop_foodestablishment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'IceCreamShop'
		verbose_name_plural = 'IceCreamShop'


class SuspendAction(models.Model):

	controlAction = models.ForeignKey('ControlAction', on_delete=models.CASCADE, verbose_name="Controlaction", blank=True, null=True, help_text='''An agent controls a device or application.''', related_name="suspendaction_controlaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SuspendAction'
		verbose_name_plural = 'SuspendAction'


class ReadAction(models.Model):

	consumeAction = models.ForeignKey('ConsumeAction', on_delete=models.CASCADE, verbose_name="Consumeaction", blank=True, null=True, help_text='''The act of ingesting information/resources/food.''', related_name="readaction_consumeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReadAction'
		verbose_name_plural = 'ReadAction'


class Cemetery(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="cemetery_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Cemetery'
		verbose_name_plural = 'Cemetery'


class PerformingArtsTheater(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="performingartstheater_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PerformingArtsTheater'
		verbose_name_plural = 'PerformingArtsTheater'


class BowlingAlley(models.Model):

	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sports location, such as a playing field.''', related_name="bowlingalley_sportsactivitylocation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BowlingAlley'
		verbose_name_plural = 'BowlingAlley'


class GatedResidenceCommunity(models.Model):

	residence = models.ForeignKey('Residence', on_delete=models.CASCADE, verbose_name="Residence", blank=True, null=True, help_text='''The place where a person lives.''', related_name="gatedresidencecommunity_residence")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GatedResidenceCommunity'
		verbose_name_plural = 'GatedResidenceCommunity'


class TransferAction(models.Model):

	fromLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Fromlocation", blank=True, null=True, help_text='''A sub property of location. The original location of the object or the agent before the action.''', related_name="transferaction_fromlocation_place")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="transferaction_action")
	toLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Tolocation", blank=True, null=True, help_text='''A sub property of location. The final location of the object or the agent after the action.''', related_name="transferaction_tolocation_place")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TransferAction'
		verbose_name_plural = 'TransferAction'


class UserTweets(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserTweets'
		verbose_name_plural = 'UserTweets'


class SportsEvent(models.Model):

	awayTeamSportsTeam = models.ForeignKey('SportsTeam', on_delete=models.CASCADE, verbose_name="Awayteam", blank=True, null=True, help_text='''The away team in a sports event.''', related_name="sportsevent_awayteam_sportsteam")
	awayTeamPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Awayteam", blank=True, null=True, help_text='''The away team in a sports event.''', related_name="sportsevent_awayteam_person")
	competitorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Competitor", blank=True, null=True, help_text='''A competitor in a sports event.''', related_name="sportsevent_competitor_person")
	competitorSportsTeam = models.ForeignKey('SportsTeam', on_delete=models.CASCADE, verbose_name="Competitor", blank=True, null=True, help_text='''A competitor in a sports event.''', related_name="sportsevent_competitor_sportsteam")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="sportsevent_event")
	homeTeamPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Hometeam", blank=True, null=True, help_text='''The home team in a sports event.''', related_name="sportsevent_hometeam_person")
	homeTeamSportsTeam = models.ForeignKey('SportsTeam', on_delete=models.CASCADE, verbose_name="Hometeam", blank=True, null=True, help_text='''The home team in a sports event.''', related_name="sportsevent_hometeam_sportsteam")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SportsEvent'
		verbose_name_plural = 'SportsEvent'


class OfficeEquipmentStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="officeequipmentstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OfficeEquipmentStore'
		verbose_name_plural = 'OfficeEquipmentStore'


class Reservoir(models.Model):

	bodyOfWater = models.ForeignKey('BodyOfWater', on_delete=models.CASCADE, verbose_name="Bodyofwater", blank=True, null=True, help_text='''A body of water, such as a sea, ocean, or lake.''', related_name="reservoir_bodyofwater")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Reservoir'
		verbose_name_plural = 'Reservoir'


class School(models.Model):

	educationalOrganization = models.ForeignKey('EducationalOrganization', on_delete=models.CASCADE, verbose_name="Educationalorganization", blank=True, null=True, help_text='''An educational organization.''', related_name="school_educationalorganization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'School'
		verbose_name_plural = 'School'


class Notary(models.Model):

	legalService = models.ForeignKey('LegalService', on_delete=models.CASCADE, verbose_name="Legalservice", blank=True, null=True, help_text='''A LegalService is a business that provides legally-oriented services, advice and representation, e.g. law firms.
        <br><br>
        As a <a href="/LocalBusiness">LocalBusiness</a> it can be
        described as a <a href="/provider">provider</a> of one or more
        <a href="/Service">Service(s)</a>.
      ''', related_name="notary_legalservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Notary'
		verbose_name_plural = 'Notary'


class GovernmentService(models.Model):

	serviceOperatorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Serviceoperator", blank=True, null=True, help_text='''The operating organization, if different from the provider.  This enables the representation of services that are provided by an organization, but operated by another organization like a subcontractor.''', related_name="governmentservice_serviceoperator_organization")
	service = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Service", blank=True, null=True, help_text='''A service provided by an organization, e.g. delivery service, print services, etc.''', related_name="governmentservice_service")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GovernmentService'
		verbose_name_plural = 'GovernmentService'


class PostalAddress(models.Model):

	postalCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Postalcode", blank=True, null=True, help_text='''The postal code. For example, 94043.''', related_name="postaladdress_postalcode_text")
	postOfficeBoxNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Postofficeboxnumber", blank=True, null=True, help_text='''The post office box number for PO box addresses.''', related_name="postaladdress_postofficeboxnumber_text")
	contactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Contactpoint", blank=True, null=True, help_text='''A contact point&#x2014;for example, a Customer Complaints department.''', related_name="postaladdress_contactpoint")
	addressLocalityText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Addresslocality", blank=True, null=True, help_text='''The locality. For example, Mountain View.''', related_name="postaladdress_addresslocality_text")
	addressCountryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Addresscountry", blank=True, null=True, help_text='''The country. For example, USA. You can also provide the two-letter <a href='http://en.wikipedia.org/wiki/ISO_3166-1'>ISO 3166-1 alpha-2 country code</a>.''', related_name="postaladdress_addresscountry_text")
	addressCountryCountry = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Addresscountry", blank=True, null=True, help_text='''The country. For example, USA. You can also provide the two-letter <a href='http://en.wikipedia.org/wiki/ISO_3166-1'>ISO 3166-1 alpha-2 country code</a>.''', related_name="postaladdress_addresscountry_country")
	streetAddressText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Streetaddress", blank=True, null=True, help_text='''The street address. For example, 1600 Amphitheatre Pkwy.''', related_name="postaladdress_streetaddress_text")
	addressRegionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Addressregion", blank=True, null=True, help_text='''The region. For example, CA.''', related_name="postaladdress_addressregion_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PostalAddress'
		verbose_name_plural = 'PostalAddress'


class QuoteAction(models.Model):

	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="Tradeaction", blank=True, null=True, help_text='''The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.''', related_name="quoteaction_tradeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'QuoteAction'
		verbose_name_plural = 'QuoteAction'


class ApplyAction(models.Model):

	organizeAction = models.ForeignKey('OrganizeAction', on_delete=models.CASCADE, verbose_name="Organizeaction", blank=True, null=True, help_text='''The act of manipulating/administering/supervising/controlling one or more objects.''', related_name="applyaction_organizeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ApplyAction'
		verbose_name_plural = 'ApplyAction'


class GenderType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="gendertype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GenderType'
		verbose_name_plural = 'GenderType'


class UserPlusOnes(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserPlusOnes'
		verbose_name_plural = 'UserPlusOnes'


class Duration(models.Model):

	quantity = models.ForeignKey('Quantity', on_delete=models.CASCADE, verbose_name="Quantity", blank=True, null=True, help_text='''Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 Kg' or '4 milligrams'.''', related_name="duration_quantity")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Duration'
		verbose_name_plural = 'Duration'


class PaintAction(models.Model):

	createAction = models.ForeignKey('CreateAction', on_delete=models.CASCADE, verbose_name="Createaction", blank=True, null=True, help_text='''The act of deliberately creating/producing/generating/building a result out of the agent.''', related_name="paintaction_createaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PaintAction'
		verbose_name_plural = 'PaintAction'


class Time(models.Model):

	value = models.TimeField(blank=True, null=True, verbose_name="Value", help_text='''A point in time recurring on multiple days in the form hh:mm:ss[Z|(+|-)hh:mm] (see <a href="http://www.w3.org/TR/xmlschema-2/#time">XML schema for details</a>).''')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Time'
		verbose_name_plural = 'Time'


class GeneralContractor(models.Model):

	homeAndConstructionBusiness = models.ForeignKey('HomeAndConstructionBusiness', on_delete=models.CASCADE, verbose_name="Homeandconstructionbusiness", blank=True, null=True, help_text='''A construction business.
        <br><br>
        A HomeAndConstructionBusiness is a LocalBusiness that provides services around homes and buildings.
          <br><br>
          As a <a href="/LocalBusiness">LocalBusiness</a> it can be
          described as a <a href="/provider">provider</a> of one or more
          <a href="/Service">Service(s)</a>.
      ''', related_name="generalcontractor_homeandconstructionbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GeneralContractor'
		verbose_name_plural = 'GeneralContractor'


class ProfessionalService(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="professionalservice_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ProfessionalService'
		verbose_name_plural = 'ProfessionalService'


class SearchAction(models.Model):

	queryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Query", blank=True, null=True, help_text='''A sub property of instrument. The query used on this action.''', related_name="searchaction_query_text")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="searchaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SearchAction'
		verbose_name_plural = 'SearchAction'


class Courthouse(models.Model):

	governmentBuilding = models.ForeignKey('GovernmentBuilding', on_delete=models.CASCADE, verbose_name="Governmentbuilding", blank=True, null=True, help_text='''A government building.''', related_name="courthouse_governmentbuilding")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Courthouse'
		verbose_name_plural = 'Courthouse'


class CreditCard(models.Model):

	loanOrCredit = models.ForeignKey('LoanOrCredit', on_delete=models.CASCADE, verbose_name="Loanorcredit", blank=True, null=True, help_text='''A financial product for the loaning of an amount of money under agreed terms and charges.''', related_name="creditcard_loanorcredit")
	paymentCard = models.ForeignKey('PaymentCard', on_delete=models.CASCADE, verbose_name="Paymentcard", blank=True, null=True, help_text='''A payment method using a credit, debit, store or other card to associate the payment with an account.''', related_name="creditcard_paymentcard")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CreditCard'
		verbose_name_plural = 'CreditCard'


class ExerciseGym(models.Model):

	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sports location, such as a playing field.''', related_name="exercisegym_sportsactivitylocation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ExerciseGym'
		verbose_name_plural = 'ExerciseGym'


class OfferCatalog(models.Model):

	itemList = models.ForeignKey('ItemList', on_delete=models.CASCADE, verbose_name="Itemlist", blank=True, null=True, help_text='''A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.''', related_name="offercatalog_itemlist")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OfferCatalog'
		verbose_name_plural = 'OfferCatalog'


class TouristAttraction(models.Model):

	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", blank=True, null=True, help_text='''Entities that have a somewhat fixed, physical extension.''', related_name="touristattraction_place")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TouristAttraction'
		verbose_name_plural = 'TouristAttraction'


class ReviewAction(models.Model):

	resultReviewReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Resultreview", blank=True, null=True, help_text='''A sub property of result. The review that resulted in the performing of the action.''', related_name="reviewaction_resultreview_review")
	assessAction = models.ForeignKey('AssessAction', on_delete=models.CASCADE, verbose_name="Assessaction", blank=True, null=True, help_text='''The act of forming one's opinion, reaction or sentiment.''', related_name="reviewaction_assessaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReviewAction'
		verbose_name_plural = 'ReviewAction'


class ItemListOrderType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="itemlistordertype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ItemListOrderType'
		verbose_name_plural = 'ItemListOrderType'


class SportsTeam(models.Model):

	sportsOrganization = models.ForeignKey('SportsOrganization', on_delete=models.CASCADE, verbose_name="Sportsorganization", blank=True, null=True, help_text='''Represents the collection of all sports organizations, including sports teams, governing bodies, and sports associations.''', related_name="sportsteam_sportsorganization")
	athletePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Athlete", blank=True, null=True, help_text='''A person that acts as performing member of a sports team; a player as opposed to a coach.''', related_name="sportsteam_athlete_person")
	coachPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Coach", blank=True, null=True, help_text='''A person that acts in a coaching role for a sports team.''', related_name="sportsteam_coach_person")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SportsTeam'
		verbose_name_plural = 'SportsTeam'


class Barcode(models.Model):

	imageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Imageobject", blank=True, null=True, help_text='''An image file.''', related_name="barcode_imageobject")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Barcode'
		verbose_name_plural = 'Barcode'


class Permit(models.Model):

	validFromDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", blank=True, null=True, help_text='''The date when the item becomes valid.''', related_name="permit_validfrom_datetime")
	validUntilDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Validuntil", blank=True, null=True, help_text='''The date when the item is no longer valid.''', related_name="permit_validuntil_date")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="permit_intangible")
	validInAdministrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Validin", blank=True, null=True, help_text='''The geographic area where the permit is valid.''', related_name="permit_validin_administrativearea")
	issuedByOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Issuedby", blank=True, null=True, help_text='''The organization issuing the ticket or permit.''', related_name="permit_issuedby_organization")
	issuedThroughService = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Issuedthrough", blank=True, null=True, help_text='''The service through with the permit was granted.''', related_name="permit_issuedthrough_service")
	permitAudienceAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Permitaudience", blank=True, null=True, help_text='''The target audience for this permit.''', related_name="permit_permitaudience_audience")
	validForDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Validfor", blank=True, null=True, help_text='''The time validity of the permit.''', related_name="permit_validfor_duration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Permit'
		verbose_name_plural = 'Permit'


class CancelAction(models.Model):

	planAction = models.ForeignKey('PlanAction', on_delete=models.CASCADE, verbose_name="Planaction", blank=True, null=True, help_text='''The act of planning the execution of an event/task/action/reservation/plan to a future date.''', related_name="cancelaction_planaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CancelAction'
		verbose_name_plural = 'CancelAction'


class Painting(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="painting_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Painting'
		verbose_name_plural = 'Painting'


class RejectAction(models.Model):

	allocateAction = models.ForeignKey('AllocateAction', on_delete=models.CASCADE, verbose_name="Allocateaction", blank=True, null=True, help_text='''The act of organizing tasks/objects/events by associating resources to it.''', related_name="rejectaction_allocateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RejectAction'
		verbose_name_plural = 'RejectAction'


class TVSeason(models.Model):

	countryOfOriginCountry = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Countryoforigin", blank=True, null=True, help_text='''The country of the principal offices of the production company or individual responsible for the movie or program.''', related_name="tvseason_countryoforigin_country")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="tvseason_creativework")
	creativeWorkSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Creativeworkseason", blank=True, null=True, help_text='''A media season e.g. tv, radio, video game etc.''', related_name="tvseason_creativeworkseason")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TVSeason'
		verbose_name_plural = 'TVSeason'


class BuddhistTemple(models.Model):

	placeOfWorship = models.ForeignKey('PlaceOfWorship', on_delete=models.CASCADE, verbose_name="Placeofworship", blank=True, null=True, help_text='''Place of worship, such as a church, synagogue, or mosque.''', related_name="buddhisttemple_placeofworship")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BuddhistTemple'
		verbose_name_plural = 'BuddhistTemple'


class Playground(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="playground_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Playground'
		verbose_name_plural = 'Playground'


class VideoGameClip(models.Model):

	clip = models.ForeignKey('Clip', on_delete=models.CASCADE, verbose_name="Clip", blank=True, null=True, help_text='''A short TV or radio program or a segment/part of a program.''', related_name="videogameclip_clip")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'VideoGameClip'
		verbose_name_plural = 'VideoGameClip'


class Seat(models.Model):

	seatingTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Seatingtype", blank=True, null=True, help_text='''The type/class of the seat.''', related_name="seat_seatingtype_text")
	seatingTypeQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Seatingtype", blank=True, null=True, help_text='''The type/class of the seat.''', related_name="seat_seatingtype_qualitativevalue")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="seat_intangible")
	seatSectionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Seatsection", blank=True, null=True, help_text='''The section location of the reserved seat (e.g. Orchestra).''', related_name="seat_seatsection_text")
	seatNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Seatnumber", blank=True, null=True, help_text='''The location of the reserved seat (e.g., 27).''', related_name="seat_seatnumber_text")
	seatRowText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Seatrow", blank=True, null=True, help_text='''The row location of the reserved seat (e.g., B).''', related_name="seat_seatrow_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Seat'
		verbose_name_plural = 'Seat'


class BuyAction(models.Model):

	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="Tradeaction", blank=True, null=True, help_text='''The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.''', related_name="buyaction_tradeaction")
	sellerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="buyaction_seller_organization")
	sellerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="buyaction_seller_person")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BuyAction'
		verbose_name_plural = 'BuyAction'


class Movie(models.Model):

	musicByMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="movie_musicby_musicgroup")
	musicByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="movie_musicby_person")
	trailerVideoObject = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", blank=True, null=True, help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="movie_trailer_videoobject")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="movie_director_person")
	subtitleLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Subtitlelanguage", blank=True, null=True, help_text='''Languages in which subtitles/captions are available, in <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard format.</a>''', related_name="movie_subtitlelanguage_text")
	subtitleLanguageLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Subtitlelanguage", blank=True, null=True, help_text='''Languages in which subtitles/captions are available, in <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard format.</a>''', related_name="movie_subtitlelanguage_language")
	countryOfOriginCountry = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Countryoforigin", blank=True, null=True, help_text='''The country of the principal offices of the production company or individual responsible for the movie or program.''', related_name="movie_countryoforigin_country")
	durationDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", blank=True, null=True, help_text='''The duration of the item (movie, audio recording, event, etc.) in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>.''', related_name="movie_duration_duration")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="movie_actor_person")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="movie_creativework")
	productionCompanyOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", blank=True, null=True, help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="movie_productioncompany_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Movie'
		verbose_name_plural = 'Movie'


class RentAction(models.Model):

	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="Tradeaction", blank=True, null=True, help_text='''The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.''', related_name="rentaction_tradeaction")
	realEstateAgentRealEstateAgent = models.ForeignKey('RealEstateAgent', on_delete=models.CASCADE, verbose_name="Realestateagent", blank=True, null=True, help_text='''A sub property of participant. The real estate agent involved in the action.''', related_name="rentaction_realestateagent_realestateagent")
	landlordOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Landlord", blank=True, null=True, help_text='''A sub property of participant. The owner of the real estate property.''', related_name="rentaction_landlord_organization")
	landlordPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Landlord", blank=True, null=True, help_text='''A sub property of participant. The owner of the real estate property.''', related_name="rentaction_landlord_person")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RentAction'
		verbose_name_plural = 'RentAction'


class Series(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="series_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Series'
		verbose_name_plural = 'Series'


class Corporation(models.Model):

	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", blank=True, null=True, help_text='''An organization such as a school, NGO, corporation, club, etc.''', related_name="corporation_organization")
	tickerSymbolText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Tickersymbol", blank=True, null=True, help_text='''The exchange traded instrument associated with a Corporation object. The tickerSymbol is expressed as an exchange and an instrument name separated by a space character. For the exchange component of the tickerSymbol attribute, we reccommend using the controlled vocaulary of Market Identifier Codes (MIC) specified in ISO15022.''', related_name="corporation_tickersymbol_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Corporation'
		verbose_name_plural = 'Corporation'


class Offer(models.Model):

	advanceBookingRequirementQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Advancebookingrequirement", blank=True, null=True, help_text='''The amount of time that is required between accepting the offer and the actual usage of the resource or service.''', related_name="offer_advancebookingrequirement_quantitativevalue")
	priceCurrencyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricecurrency", blank=True, null=True, help_text='''The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.''', related_name="offer_pricecurrency_text")
	availableDeliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Availabledeliverymethod", blank=True, null=True, help_text='''The delivery method(s) available for this offer.''', related_name="offer_availabledeliverymethod_deliverymethod")
	priceSpecificationPriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", blank=True, null=True, help_text='''One or more detailed price specifications, indicating the unit price and delivery or payment charges.''', related_name="offer_pricespecification_pricespecification")
	validFromDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", blank=True, null=True, help_text='''The date when the item becomes valid.''', related_name="offer_validfrom_datetime")
	businessFunctionBusinessFunction = models.ForeignKey('BusinessFunction', on_delete=models.CASCADE, verbose_name="Businessfunction", blank=True, null=True, help_text='''The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.''', related_name="offer_businessfunction_businessfunction")
	itemOfferedProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Itemoffered", blank=True, null=True, help_text='''The item being offered.''', related_name="offer_itemoffered_product")
	itemOfferedService = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Itemoffered", blank=True, null=True, help_text='''The item being offered.''', related_name="offer_itemoffered_service")
	includesObjectTypeAndQuantityNode = models.ForeignKey('TypeAndQuantityNode', on_delete=models.CASCADE, verbose_name="Includesobject", blank=True, null=True, help_text='''This links to a node or nodes indicating the exact quantity of the products included in the offer.''', related_name="offer_includesobject_typeandquantitynode")
	gtin14Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin14", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-14.aspx">GTIN-14</a> code of the product, or the product to which the offer refers. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="offer_gtin14_text")
	gtin13Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin13", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-13.aspx">GTIN-13</a> code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="offer_gtin13_text")
	gtin12Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin12", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-12.aspx">GTIN-12</a> code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="offer_gtin12_text")
	availableAtOrFromPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Availableatorfrom", blank=True, null=True, help_text='''The place(s) from which the offer can be obtained (e.g. store locations).''', related_name="offer_availableatorfrom_place")
	warrantyWarrantyPromise = models.ForeignKey('WarrantyPromise', on_delete=models.CASCADE, verbose_name="Warranty", blank=True, null=True, help_text='''The warranty promise(s) included in the offer.''', related_name="offer_warranty_warrantypromise")
	inventoryLevelQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Inventorylevel", blank=True, null=True, help_text='''The current approximate inventory level for the item or items.''', related_name="offer_inventorylevel_quantitativevalue")
	offeredByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Offeredby", blank=True, null=True, help_text='''A pointer to the organization or person making the offer.''', related_name="offer_offeredby_person")
	offeredByOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Offeredby", blank=True, null=True, help_text='''A pointer to the organization or person making the offer.''', related_name="offer_offeredby_organization")
	availabilityStartsDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availabilitystarts", blank=True, null=True, help_text='''The beginning of the availability of the product or service included in the offer.''', related_name="offer_availabilitystarts_datetime")
	eligibleDurationQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligibleduration", blank=True, null=True, help_text='''The duration for which the given offer is valid.''', related_name="offer_eligibleduration_quantitativevalue")
	reviewReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", blank=True, null=True, help_text='''A review of the item.''', related_name="offer_review_review")
	eligibleTransactionVolumePriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Eligibletransactionvolume", blank=True, null=True, help_text='''The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.''', related_name="offer_eligibletransactionvolume_pricespecification")
	mpnText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mpn", blank=True, null=True, help_text='''The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.''', related_name="offer_mpn_text")
	areaServedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="offer_areaserved_text")
	areaServedAdministrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="offer_areaserved_administrativearea")
	areaServedPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="offer_areaserved_place")
	areaServedGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="offer_areaserved_geoshape")
	serialNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Serialnumber", blank=True, null=True, help_text='''The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.''', related_name="offer_serialnumber_text")
	sellerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="offer_seller_organization")
	sellerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="offer_seller_person")
	acceptedPaymentMethodLoanOrCredit = models.ForeignKey('LoanOrCredit', on_delete=models.CASCADE, verbose_name="Acceptedpaymentmethod", blank=True, null=True, help_text='''The payment method(s) accepted by seller for this offer.''', related_name="offer_acceptedpaymentmethod_loanorcredit")
	acceptedPaymentMethodPaymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Acceptedpaymentmethod", blank=True, null=True, help_text='''The payment method(s) accepted by seller for this offer.''', related_name="offer_acceptedpaymentmethod_paymentmethod")
	validThroughDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", blank=True, null=True, help_text='''The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.''', related_name="offer_validthrough_datetime")
	availabilityItemAvailability = models.ForeignKey('ItemAvailability', on_delete=models.CASCADE, verbose_name="Availability", blank=True, null=True, help_text='''The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.''', related_name="offer_availability_itemavailability")
	skuText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Sku", blank=True, null=True, help_text='''The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.''', related_name="offer_sku_text")
	gtin8Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin8", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-8.aspx">GTIN-8</a> code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="offer_gtin8_text")
	priceValidUntilDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Pricevaliduntil", blank=True, null=True, help_text='''The date after which the price is no longer available.''', related_name="offer_pricevaliduntil_date")
	priceNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Price", blank=True, null=True, help_text='''The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.
<br />
<br />
      Usage guidelines:
<br />
<ul>
<li>Use the <a href="/priceCurrency">priceCurrency</a> property (with <a href="http://en.wikipedia.org/wiki/ISO_4217#Active_codes">ISO 4217 codes</a> e.g. "USD") instead of
      including <a href="http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign">ambiguous symbols</a> such as '$' in the value.
</li>
<li>
      Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
</li>
<li>
      Note that both <a href="http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute">RDFa</a> and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values
      alongside more human-friendly formatting.
</li>
<li>
      Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols.
</li>
</ul>
      ''', related_name="offer_price_number")
	priceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Price", blank=True, null=True, help_text='''The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.
<br />
<br />
      Usage guidelines:
<br />
<ul>
<li>Use the <a href="/priceCurrency">priceCurrency</a> property (with <a href="http://en.wikipedia.org/wiki/ISO_4217#Active_codes">ISO 4217 codes</a> e.g. "USD") instead of
      including <a href="http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign">ambiguous symbols</a> such as '$' in the value.
</li>
<li>
      Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
</li>
<li>
      Note that both <a href="http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute">RDFa</a> and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values
      alongside more human-friendly formatting.
</li>
<li>
      Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols.
</li>
</ul>
      ''', related_name="offer_price_text")
	deliveryLeadTimeQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Deliveryleadtime", blank=True, null=True, help_text='''The typical delay between the receipt of the order and the goods leaving the warehouse.''', related_name="offer_deliveryleadtime_quantitativevalue")
	eligibleQuantityQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligiblequantity", blank=True, null=True, help_text='''The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.''', related_name="offer_eligiblequantity_quantitativevalue")
	ineligibleRegionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Ineligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.
      <br><br> See also <a href="/eligibleRegion">eligibleRegion</a>.
      ''', related_name="offer_ineligibleregion_text")
	ineligibleRegionGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Ineligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.
      <br><br> See also <a href="/eligibleRegion">eligibleRegion</a>.
      ''', related_name="offer_ineligibleregion_geoshape")
	ineligibleRegionPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Ineligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.
      <br><br> See also <a href="/eligibleRegion">eligibleRegion</a>.
      ''', related_name="offer_ineligibleregion_place")
	itemConditionOfferItemCondition = models.ForeignKey('OfferItemCondition', on_delete=models.CASCADE, verbose_name="Itemcondition", blank=True, null=True, help_text='''A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.''', related_name="offer_itemcondition_offeritemcondition")
	eligibleRegionPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Eligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.
      <br><br> See also <a href="/ineligibleRegion">ineligibleRegion</a>.
    ''', related_name="offer_eligibleregion_place")
	eligibleRegionGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Eligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.
      <br><br> See also <a href="/ineligibleRegion">ineligibleRegion</a>.
    ''', related_name="offer_eligibleregion_geoshape")
	eligibleRegionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Eligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.
      <br><br> See also <a href="/ineligibleRegion">ineligibleRegion</a>.
    ''', related_name="offer_eligibleregion_text")
	aggregateRatingAggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", blank=True, null=True, help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="offer_aggregaterating_aggregaterating")
	eligibleCustomerTypeBusinessEntityType = models.ForeignKey('BusinessEntityType', on_delete=models.CASCADE, verbose_name="Eligiblecustomertype", blank=True, null=True, help_text='''The type(s) of customers for which the given offer is valid.''', related_name="offer_eligiblecustomertype_businessentitytype")
	availabilityEndsDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availabilityends", blank=True, null=True, help_text='''The end of the availability of the product or service included in the offer.''', related_name="offer_availabilityends_datetime")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="offer_intangible")
	addOnOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Addon", blank=True, null=True, help_text='''An additional offer that can only be obtained in combination with the first base offer (e.g. supplements and extensions that are available for a surcharge).''', related_name="offer_addon_offer")
	categoryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Category", blank=True, null=True, help_text='''A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.''', related_name="offer_category_text")
	categoryThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Category", blank=True, null=True, help_text='''A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.''', related_name="offer_category_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Offer'
		verbose_name_plural = 'Offer'


class GameServer(models.Model):

	gameVideoGame = models.ForeignKey('VideoGame', on_delete=models.CASCADE, verbose_name="Game", blank=True, null=True, help_text='''Video game which is played on this server.''', related_name="gameserver_game_videogame")
	playersOnlineInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Playersonline", blank=True, null=True, help_text='''Number of players on the server.''', related_name="gameserver_playersonline_integer")
	serverStatusGameServerStatus = models.ForeignKey('GameServerStatus', on_delete=models.CASCADE, verbose_name="Serverstatus", blank=True, null=True, help_text='''Status of a game server.''', related_name="gameserver_serverstatus_gameserverstatus")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="gameserver_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GameServer'
		verbose_name_plural = 'GameServer'


class ExhibitionEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="exhibitionevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ExhibitionEvent'
		verbose_name_plural = 'ExhibitionEvent'


class InsuranceAgency(models.Model):

	financialService = models.ForeignKey('FinancialService', on_delete=models.CASCADE, verbose_name="Financialservice", blank=True, null=True, help_text='''Financial services business.''', related_name="insuranceagency_financialservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'InsuranceAgency'
		verbose_name_plural = 'InsuranceAgency'


class Airline(models.Model):

	iataCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Iatacode", blank=True, null=True, help_text='''IATA identifier for an airline or airport.''', related_name="airline_iatacode_text")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", blank=True, null=True, help_text='''An organization such as a school, NGO, corporation, club, etc.''', related_name="airline_organization")
	boardingPolicyBoardingPolicyType = models.ForeignKey('BoardingPolicyType', on_delete=models.CASCADE, verbose_name="Boardingpolicy", blank=True, null=True, help_text='''The type of boarding policy used by the airline (e.g. zone-based or group-based).''', related_name="airline_boardingpolicy_boardingpolicytype")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Airline'
		verbose_name_plural = 'Airline'


class Hospital(models.Model):

	medicalOrganization = models.ForeignKey('MedicalOrganization', on_delete=models.CASCADE, verbose_name="Medicalorganization", blank=True, null=True, help_text='''A medical organization (physical or not), such as hospital, institution or clinic.''', related_name="hospital_medicalorganization")
	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="hospital_civicstructure")
	emergencyService = models.ForeignKey('EmergencyService', on_delete=models.CASCADE, verbose_name="Emergencyservice", blank=True, null=True, help_text='''An emergency service, such as a fire station or ER.''', related_name="hospital_emergencyservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Hospital'
		verbose_name_plural = 'Hospital'


class InstallAction(models.Model):

	consumeAction = models.ForeignKey('ConsumeAction', on_delete=models.CASCADE, verbose_name="Consumeaction", blank=True, null=True, help_text='''The act of ingesting information/resources/food.''', related_name="installaction_consumeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'InstallAction'
		verbose_name_plural = 'InstallAction'


class QuantitativeValue(models.Model):

	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="quantitativevalue_structuredvalue")
	additionalPropertyPropertyValue = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Additionalproperty", blank=True, null=True, help_text='''A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. <br /><br />

Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
''', related_name="quantitativevalue_additionalproperty_propertyvalue")
	unitCodeURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Unitcode", blank=True, null=True, help_text='''The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.''', related_name="quantitativevalue_unitcode_url")
	unitCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unitcode", blank=True, null=True, help_text='''The unit of measurement given using the UN/CEFACT Common Code (3 characters) or a URL. Other codes than the UN/CEFACT Common Code may be used with a prefix followed by a colon.''', related_name="quantitativevalue_unitcode_text")
	minValueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Minvalue", blank=True, null=True, help_text='''The lower value of some characteristic or property.''', related_name="quantitativevalue_minvalue_number")
	unitTextText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Unittext", blank=True, null=True, help_text='''A string or text indicating the unit of measurement. Useful if you cannot provide a standard unit code for
<a href='unitCode'>unitCode</a>.''', related_name="quantitativevalue_unittext_text")
	valueReferencePropertyValue = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="quantitativevalue_valuereference_propertyvalue")
	valueReferenceEnumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="quantitativevalue_valuereference_enumeration")
	valueReferenceStructuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="quantitativevalue_valuereference_structuredvalue")
	valueReferenceQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="quantitativevalue_valuereference_quantitativevalue")
	valueReferenceQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="quantitativevalue_valuereference_qualitativevalue")
	valueStructuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="quantitativevalue_value_structuredvalue")
	valueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="quantitativevalue_value_number")
	valueBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="quantitativevalue_value_boolean")
	valueText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="quantitativevalue_value_text")
	maxValueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Maxvalue", blank=True, null=True, help_text='''The upper value of some characteristic or property.''', related_name="quantitativevalue_maxvalue_number")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'QuantitativeValue'
		verbose_name_plural = 'QuantitativeValue'


class GeoCoordinates(models.Model):

	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="geocoordinates_structuredvalue")
	latitudeNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Latitude", blank=True, null=True, help_text='''The latitude of a location. For example <code>37.42242</code> (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).''', related_name="geocoordinates_latitude_number")
	latitudeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Latitude", blank=True, null=True, help_text='''The latitude of a location. For example <code>37.42242</code> (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).''', related_name="geocoordinates_latitude_text")
	postalCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Postalcode", blank=True, null=True, help_text='''The postal code. For example, 94043.''', related_name="geocoordinates_postalcode_text")
	elevationNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Elevation", blank=True, null=True, help_text='''The elevation of a location (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).''', related_name="geocoordinates_elevation_number")
	elevationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Elevation", blank=True, null=True, help_text='''The elevation of a location (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).''', related_name="geocoordinates_elevation_text")
	longitudeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Longitude", blank=True, null=True, help_text='''The longitude of a location. For example <code>-122.08585</code> (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).''', related_name="geocoordinates_longitude_text")
	longitudeNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Longitude", blank=True, null=True, help_text='''The longitude of a location. For example <code>-122.08585</code> (<a href="https://en.wikipedia.org/wiki/World_Geodetic_System">WGS 84</a>).''', related_name="geocoordinates_longitude_number")
	addressCountryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Addresscountry", blank=True, null=True, help_text='''The country. For example, USA. You can also provide the two-letter <a href='http://en.wikipedia.org/wiki/ISO_3166-1'>ISO 3166-1 alpha-2 country code</a>.''', related_name="geocoordinates_addresscountry_text")
	addressCountryCountry = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Addresscountry", blank=True, null=True, help_text='''The country. For example, USA. You can also provide the two-letter <a href='http://en.wikipedia.org/wiki/ISO_3166-1'>ISO 3166-1 alpha-2 country code</a>.''', related_name="geocoordinates_addresscountry_country")
	addressPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="geocoordinates_address_postaladdress")
	addressText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="geocoordinates_address_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GeoCoordinates'
		verbose_name_plural = 'GeoCoordinates'


class Bridge(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="bridge_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Bridge'
		verbose_name_plural = 'Bridge'


class Energy(models.Model):

	quantity = models.ForeignKey('Quantity', on_delete=models.CASCADE, verbose_name="Quantity", blank=True, null=True, help_text='''Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 Kg' or '4 milligrams'.''', related_name="energy_quantity")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Energy'
		verbose_name_plural = 'Energy'


class DigitalDocumentPermission(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="digitaldocumentpermission_intangible")
	permissionTypeDigitalDocumentPermissionType = models.ForeignKey('DigitalDocumentPermissionType', on_delete=models.CASCADE, verbose_name="Permissiontype", blank=True, null=True, help_text='''The type of permission granted the person, organization, or audience.''', related_name="digitaldocumentpermission_permissiontype_digitaldocumentpermissiontype")
	granteePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Grantee", blank=True, null=True, help_text='''The person, organization, contact point, or audience that has been granted this permission.''', related_name="digitaldocumentpermission_grantee_person")
	granteeContactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Grantee", blank=True, null=True, help_text='''The person, organization, contact point, or audience that has been granted this permission.''', related_name="digitaldocumentpermission_grantee_contactpoint")
	granteeOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Grantee", blank=True, null=True, help_text='''The person, organization, contact point, or audience that has been granted this permission.''', related_name="digitaldocumentpermission_grantee_organization")
	granteeAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Grantee", blank=True, null=True, help_text='''The person, organization, contact point, or audience that has been granted this permission.''', related_name="digitaldocumentpermission_grantee_audience")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DigitalDocumentPermission'
		verbose_name_plural = 'DigitalDocumentPermission'


class BroadcastEvent(models.Model):

	broadcastOfEventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Broadcastofevent", blank=True, null=True, help_text='''The event being broadcast such as a sporting event or awards ceremony.''', related_name="broadcastevent_broadcastofevent_event")
	isLiveBroadcastBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Islivebroadcast", blank=True, null=True, help_text='''True is the broadcast is of a live event.''', related_name="broadcastevent_islivebroadcast_boolean")
	publicationEvent = models.ForeignKey('PublicationEvent', on_delete=models.CASCADE, verbose_name="Publicationevent", blank=True, null=True, help_text='''A PublicationEvent corresponds indifferently to the event of publication for a CreativeWork of any type e.g. a broadcast event, an on-demand event, a book/journal publication via a variety of delivery media.''', related_name="broadcastevent_publicationevent")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BroadcastEvent'
		verbose_name_plural = 'BroadcastEvent'


class ReactAction(models.Model):

	assessAction = models.ForeignKey('AssessAction', on_delete=models.CASCADE, verbose_name="Assessaction", blank=True, null=True, help_text='''The act of forming one's opinion, reaction or sentiment.''', related_name="reactaction_assessaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReactAction'
		verbose_name_plural = 'ReactAction'


class Synagogue(models.Model):

	placeOfWorship = models.ForeignKey('PlaceOfWorship', on_delete=models.CASCADE, verbose_name="Placeofworship", blank=True, null=True, help_text='''Place of worship, such as a church, synagogue, or mosque.''', related_name="synagogue_placeofworship")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Synagogue'
		verbose_name_plural = 'Synagogue'


class UserCheckins(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserCheckins'
		verbose_name_plural = 'UserCheckins'


class BusReservation(models.Model):

	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", blank=True, null=True, help_text='''Describes a reservation for travel, dining or an event. Some reservations require tickets.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use http://schema.org/Offer.''', related_name="busreservation_reservation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BusReservation'
		verbose_name_plural = 'BusReservation'


class Product(models.Model):

	audienceAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", blank=True, null=True, help_text='''An intended audience, i.e. a group for whom something was created.''', related_name="product_audience_audience")
	depthDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Depth", blank=True, null=True, help_text='''The depth of the item.''', related_name="product_depth_distance")
	depthQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Depth", blank=True, null=True, help_text='''The depth of the item.''', related_name="product_depth_quantitativevalue")
	awardText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", blank=True, null=True, help_text='''An award won by or for this item.''', related_name="product_award_text")
	isAccessoryOrSparePartForProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Isaccessoryorsparepartfor", blank=True, null=True, help_text='''A pointer to another product (or multiple products) for which this product is an accessory or spare part.''', related_name="product_isaccessoryorsparepartfor_product")
	gtin14Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin14", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-14.aspx">GTIN-14</a> code of the product, or the product to which the offer refers. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="product_gtin14_text")
	gtin13Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin13", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-13.aspx">GTIN-13</a> code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="product_gtin13_text")
	gtin12Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin12", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-12.aspx">GTIN-12</a> code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="product_gtin12_text")
	additionalPropertyPropertyValue = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Additionalproperty", blank=True, null=True, help_text='''A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. <br /><br />

Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
''', related_name="product_additionalproperty_propertyvalue")
	isRelatedToService = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Isrelatedto", blank=True, null=True, help_text='''A pointer to another, somehow related product (or multiple products).''', related_name="product_isrelatedto_service")
	isRelatedToProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Isrelatedto", blank=True, null=True, help_text='''A pointer to another, somehow related product (or multiple products).''', related_name="product_isrelatedto_product")
	offersOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", blank=True, null=True, help_text='''An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="product_offers_offer")
	reviewReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", blank=True, null=True, help_text='''A review of the item.''', related_name="product_review_review")
	mpnText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mpn", blank=True, null=True, help_text='''The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.''', related_name="product_mpn_text")
	releaseDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Releasedate", blank=True, null=True, help_text='''The release date of a product or product model. This can be used to distinguish the exact variant of a product.''', related_name="product_releasedate_date")
	productionDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Productiondate", blank=True, null=True, help_text='''The date of production of the item, e.g. vehicle.''', related_name="product_productiondate_date")
	brandBrand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name="Brand", blank=True, null=True, help_text='''The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.''', related_name="product_brand_brand")
	brandOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Brand", blank=True, null=True, help_text='''The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.''', related_name="product_brand_organization")
	modelProductModel = models.ForeignKey('ProductModel', on_delete=models.CASCADE, verbose_name="Model", blank=True, null=True, help_text='''The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties.''', related_name="product_model_productmodel")
	modelText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Model", blank=True, null=True, help_text='''The model of the product. Use with the URL of a ProductModel or a textual representation of the model identifier. The URL of the ProductModel can be from an external source. It is recommended to additionally provide strong product identifiers via the gtin8/gtin13/gtin14 and mpn properties.''', related_name="product_model_text")
	colorText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Color", blank=True, null=True, help_text='''The color of the product.''', related_name="product_color_text")
	skuText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Sku", blank=True, null=True, help_text='''The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.''', related_name="product_sku_text")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", blank=True, null=True, help_text='''The most generic type of item.''', related_name="product_thing")
	gtin8Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin8", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-8.aspx">GTIN-8</a> code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="product_gtin8_text")
	purchaseDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Purchasedate", blank=True, null=True, help_text='''The date the item e.g. vehicle was purchased by the current owner.''', related_name="product_purchasedate_date")
	productIDText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Productid", blank=True, null=True, help_text='''The product identifier, such as ISBN. For example: <code>&lt;meta itemprop='productID' content='isbn:123-456-789'/&gt;</code>.''', related_name="product_productid_text")
	isConsumableForProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Isconsumablefor", blank=True, null=True, help_text='''A pointer to another product (or multiple products) for which this product is a consumable.''', related_name="product_isconsumablefor_product")
	weightQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Weight", blank=True, null=True, help_text='''The weight of the product or person.''', related_name="product_weight_quantitativevalue")
	isSimilarToService = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Issimilarto", blank=True, null=True, help_text='''A pointer to another, functionally similar product (or multiple products).''', related_name="product_issimilarto_service")
	isSimilarToProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Issimilarto", blank=True, null=True, help_text='''A pointer to another, functionally similar product (or multiple products).''', related_name="product_issimilarto_product")
	widthQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Width", blank=True, null=True, help_text='''The width of the item.''', related_name="product_width_quantitativevalue")
	widthDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Width", blank=True, null=True, help_text='''The width of the item.''', related_name="product_width_distance")
	itemConditionOfferItemCondition = models.ForeignKey('OfferItemCondition', on_delete=models.CASCADE, verbose_name="Itemcondition", blank=True, null=True, help_text='''A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.''', related_name="product_itemcondition_offeritemcondition")
	aggregateRatingAggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", blank=True, null=True, help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="product_aggregaterating_aggregaterating")
	logoURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="product_logo_url")
	logoImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="product_logo_imageobject")
	heightQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Height", blank=True, null=True, help_text='''The height of the item.''', related_name="product_height_quantitativevalue")
	heightDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Height", blank=True, null=True, help_text='''The height of the item.''', related_name="product_height_distance")
	manufacturerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Manufacturer", blank=True, null=True, help_text='''The manufacturer of the product.''', related_name="product_manufacturer_organization")
	categoryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Category", blank=True, null=True, help_text='''A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.''', related_name="product_category_text")
	categoryThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Category", blank=True, null=True, help_text='''A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.''', related_name="product_category_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Product'
		verbose_name_plural = 'Product'


class Thing(models.Model):

	nameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Name", blank=True, null=True, help_text='''The name of the item.''', related_name="thing_name_text")
	urlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Url", blank=True, null=True, help_text='''URL of the item.''', related_name="thing_url_url")
	imageURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Image", blank=True, null=True, help_text='''An image of the item. This can be a <a href="http://schema.org/URL">URL</a> or a fully described <a href="http://schema.org/ImageObject">ImageObject</a>.''', related_name="thing_image_url")
	imageImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Image", blank=True, null=True, help_text='''An image of the item. This can be a <a href="http://schema.org/URL">URL</a> or a fully described <a href="http://schema.org/ImageObject">ImageObject</a>.''', related_name="thing_image_imageobject")
	descriptionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Description", blank=True, null=True, help_text='''A description of the item.''', related_name="thing_description_text")
	disambiguatingDescriptionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Disambiguatingdescription", blank=True, null=True, help_text='''A sub property of description. A short description of the item used to disambiguate from other, similar items. Information from other properties (in particular, name) may be necessary for the description to be useful for disambiguation.''', related_name="thing_disambiguatingdescription_text")
	alternateNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Alternatename", blank=True, null=True, help_text='''An alias for the item.''', related_name="thing_alternatename_text")
	sameAsURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Sameas", blank=True, null=True, help_text='''URL of a reference Web page that unambiguously indicates the item's identity. E.g. the URL of the item's Wikipedia page, Freebase page, or official website.''', related_name="thing_sameas_url")
	additionalTypeURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Additionaltype", blank=True, null=True, help_text='''An additional type for the item, typically used for adding more specific types from external vocabularies in microdata syntax. This is a relationship between something and a class that the thing is in. In RDFa syntax, it is better to use the native RDFa syntax - the 'typeof' attribute - for multiple types. Schema.org tools may have only weaker understanding of extra types, in particular those defined externally.''', related_name="thing_additionaltype_url")
	potentialActionAction = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Potentialaction", blank=True, null=True, help_text='''Indicates a potential Action, which describes an idealized action in which this thing would play an 'object' role.''', related_name="thing_potentialaction_action")
	mainEntityOfPageURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Mainentityofpage", blank=True, null=True, help_text='''Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See <a href="/docs/datamodel.html#mainEntityBackground">background notes</a> for details.''', related_name="thing_mainentityofpage_url")
	mainEntityOfPageCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Mainentityofpage", blank=True, null=True, help_text='''Indicates a page (or other CreativeWork) for which this thing is the main entity being described. See <a href="/docs/datamodel.html#mainEntityBackground">background notes</a> for details.''', related_name="thing_mainentityofpage_creativework")

	def __str__(self):
		return str(self.nameText.value)

	class Meta:
		verbose_name = 'Thing'
		verbose_name_plural = 'Thing'


class RadioStation(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="radiostation_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RadioStation'
		verbose_name_plural = 'RadioStation'


class PostOffice(models.Model):

	governmentOffice = models.ForeignKey('GovernmentOffice', on_delete=models.CASCADE, verbose_name="Governmentoffice", blank=True, null=True, help_text='''A government office&#x2014;for example, an IRS or DMV office.''', related_name="postoffice_governmentoffice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PostOffice'
		verbose_name_plural = 'PostOffice'


class ReturnAction(models.Model):

	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="Transferaction", blank=True, null=True, help_text='''The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.''', related_name="returnaction_transferaction")
	recipientPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="returnaction_recipient_person")
	recipientAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="returnaction_recipient_audience")
	recipientOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="returnaction_recipient_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReturnAction'
		verbose_name_plural = 'ReturnAction'


class InformAction(models.Model):

	eventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''Upcoming or past event associated with this place, organization, or action.''', related_name="informaction_event_event")
	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="Communicateaction", blank=True, null=True, help_text='''The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.''', related_name="informaction_communicateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'InformAction'
		verbose_name_plural = 'InformAction'


class GasStation(models.Model):

	automotiveBusiness = models.ForeignKey('AutomotiveBusiness', on_delete=models.CASCADE, verbose_name="Automotivebusiness", blank=True, null=True, help_text='''Car repair, sales, or parts.''', related_name="gasstation_automotivebusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GasStation'
		verbose_name_plural = 'GasStation'


class AutomatedTeller(models.Model):

	financialService = models.ForeignKey('FinancialService', on_delete=models.CASCADE, verbose_name="Financialservice", blank=True, null=True, help_text='''Financial services business.''', related_name="automatedteller_financialservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AutomatedTeller'
		verbose_name_plural = 'AutomatedTeller'


class ListenAction(models.Model):

	consumeAction = models.ForeignKey('ConsumeAction', on_delete=models.CASCADE, verbose_name="Consumeaction", blank=True, null=True, help_text='''The act of ingesting information/resources/food.''', related_name="listenaction_consumeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ListenAction'
		verbose_name_plural = 'ListenAction'


class PhotographAction(models.Model):

	createAction = models.ForeignKey('CreateAction', on_delete=models.CASCADE, verbose_name="Createaction", blank=True, null=True, help_text='''The act of deliberately creating/producing/generating/building a result out of the agent.''', related_name="photographaction_createaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PhotographAction'
		verbose_name_plural = 'PhotographAction'


class Mosque(models.Model):

	placeOfWorship = models.ForeignKey('PlaceOfWorship', on_delete=models.CASCADE, verbose_name="Placeofworship", blank=True, null=True, help_text='''Place of worship, such as a church, synagogue, or mosque.''', related_name="mosque_placeofworship")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Mosque'
		verbose_name_plural = 'Mosque'


class BefriendAction(models.Model):

	interactAction = models.ForeignKey('InteractAction', on_delete=models.CASCADE, verbose_name="Interactaction", blank=True, null=True, help_text='''The act of interacting with another person or organization.''', related_name="befriendaction_interactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BefriendAction'
		verbose_name_plural = 'BefriendAction'


class ParentAudience(models.Model):

	childMinAgeNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Childminage", blank=True, null=True, help_text='''Minimal age of the child.''', related_name="parentaudience_childminage_number")
	peopleAudience = models.ForeignKey('PeopleAudience', on_delete=models.CASCADE, verbose_name="Peopleaudience", blank=True, null=True, help_text='''A set of characteristics belonging to people, e.g. who compose an item's target audience.''', related_name="parentaudience_peopleaudience")
	childMaxAgeNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Childmaxage", blank=True, null=True, help_text='''Maximal age of the child.''', related_name="parentaudience_childmaxage_number")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ParentAudience'
		verbose_name_plural = 'ParentAudience'


class AskAction(models.Model):

	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="Communicateaction", blank=True, null=True, help_text='''The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.''', related_name="askaction_communicateaction")
	questionQuestion = models.ForeignKey('Question', on_delete=models.CASCADE, verbose_name="Question", blank=True, null=True, help_text='''A sub property of object. A question.''', related_name="askaction_question_question")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AskAction'
		verbose_name_plural = 'AskAction'


class TouristInformationCenter(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="touristinformationcenter_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TouristInformationCenter'
		verbose_name_plural = 'TouristInformationCenter'


class Hostel(models.Model):

	lodgingBusiness = models.ForeignKey('LodgingBusiness', on_delete=models.CASCADE, verbose_name="Lodgingbusiness", blank=True, null=True, help_text='''A lodging business, such as a motel, hotel, or inn.''', related_name="hostel_lodgingbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Hostel'
		verbose_name_plural = 'Hostel'


class EmploymentAgency(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="employmentagency_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EmploymentAgency'
		verbose_name_plural = 'EmploymentAgency'


class LakeBodyOfWater(models.Model):

	bodyOfWater = models.ForeignKey('BodyOfWater', on_delete=models.CASCADE, verbose_name="Bodyofwater", blank=True, null=True, help_text='''A body of water, such as a sea, ocean, or lake.''', related_name="lakebodyofwater_bodyofwater")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LakeBodyOfWater'
		verbose_name_plural = 'LakeBodyOfWater'


class Action(models.Model):

	startTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Starttime", blank=True, null=True, help_text='''The startTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to start. For actions that span a period of time, when the action was performed. e.g. John wrote a book from *January* to December.

Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.''', related_name="action_starttime_datetime")
	targetEntryPoint = models.ForeignKey('EntryPoint', on_delete=models.CASCADE, verbose_name="Target", blank=True, null=True, help_text='''Indicates a target EntryPoint for an Action.''', related_name="action_target_entrypoint")
	participantOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Participant", blank=True, null=True, help_text='''Other co-agents that participated in the action indirectly. e.g. John wrote a book with *Steve*.''', related_name="action_participant_organization")
	participantPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Participant", blank=True, null=True, help_text='''Other co-agents that participated in the action indirectly. e.g. John wrote a book with *Steve*.''', related_name="action_participant_person")
	instrumentThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Instrument", blank=True, null=True, help_text='''The object that helped the agent perform the action. e.g. John wrote a book with *a pen*.''', related_name="action_instrument_thing")
	agentOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Agent", blank=True, null=True, help_text='''The direct performer or driver of the action (animate or inanimate). e.g. *John* wrote a book.''', related_name="action_agent_organization")
	agentPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Agent", blank=True, null=True, help_text='''The direct performer or driver of the action (animate or inanimate). e.g. *John* wrote a book.''', related_name="action_agent_person")
	objectThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Object", blank=True, null=True, help_text='''The object upon the action is carried out, whose state is kept intact or changed. Also known as the semantic roles patient, affected or undergoer (which change their state) or theme (which doesn't). e.g. John read *a book*.''', related_name="action_object_thing")
	actionStatusActionStatusType = models.ForeignKey('ActionStatusType', on_delete=models.CASCADE, verbose_name="Actionstatus", blank=True, null=True, help_text='''Indicates the current disposition of the Action.''', related_name="action_actionstatus_actionstatustype")
	resultThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Result", blank=True, null=True, help_text='''The result produced in the action. e.g. John wrote *a book*.''', related_name="action_result_thing")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", blank=True, null=True, help_text='''The most generic type of item.''', related_name="action_thing")
	locationPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Location", blank=True, null=True, help_text='''The location of for example where the event is happening, an organization is located, or where an action takes place.''', related_name="action_location_postaladdress")
	locationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Location", blank=True, null=True, help_text='''The location of for example where the event is happening, an organization is located, or where an action takes place.''', related_name="action_location_place")
	locationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Location", blank=True, null=True, help_text='''The location of for example where the event is happening, an organization is located, or where an action takes place.''', related_name="action_location_text")
	errorThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Error", blank=True, null=True, help_text='''For failed actions, more information on the cause of the failure.''', related_name="action_error_thing")
	endTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Endtime", blank=True, null=True, help_text='''The endTime of something. For a reserved event or service (e.g. FoodEstablishmentReservation), the time that it is expected to end. For actions that span a period of time, when the action was performed. e.g. John wrote a book from January to *December*.

Note that Event uses startDate/endDate instead of startTime/endTime, even when describing dates with times. This situation may be clarified in future revisions.''', related_name="action_endtime_datetime")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Action'
		verbose_name_plural = 'Action'


class HealthClub(models.Model):

	healthAndBeautyBusiness = models.ForeignKey('HealthAndBeautyBusiness', on_delete=models.CASCADE, verbose_name="Healthandbeautybusiness", blank=True, null=True, help_text='''Health and beauty.''', related_name="healthclub_healthandbeautybusiness")
	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sports location, such as a playing field.''', related_name="healthclub_sportsactivitylocation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HealthClub'
		verbose_name_plural = 'HealthClub'


class PublicationIssue(models.Model):

	pageStartText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pagestart", blank=True, null=True, help_text='''The page on which the work starts; for example "135" or "xiii".''', related_name="publicationissue_pagestart_text")
	pageStartInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Pagestart", blank=True, null=True, help_text='''The page on which the work starts; for example "135" or "xiii".''', related_name="publicationissue_pagestart_integer")
	pageEndInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Pageend", blank=True, null=True, help_text='''The page on which the work ends; for example "138" or "xvi".''', related_name="publicationissue_pageend_integer")
	pageEndText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pageend", blank=True, null=True, help_text='''The page on which the work ends; for example "138" or "xvi".''', related_name="publicationissue_pageend_text")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="publicationissue_creativework")
	paginationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pagination", blank=True, null=True, help_text='''Any description of pages that is not separated into pageStart and pageEnd; for example, "1-6, 9, 55" or "10-12, 46-49".''', related_name="publicationissue_pagination_text")
	issueNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Issuenumber", blank=True, null=True, help_text='''Identifies the issue of publication; for example, "iii" or "2".''', related_name="publicationissue_issuenumber_text")
	issueNumberInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Issuenumber", blank=True, null=True, help_text='''Identifies the issue of publication; for example, "iii" or "2".''', related_name="publicationissue_issuenumber_integer")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PublicationIssue'
		verbose_name_plural = 'PublicationIssue'


class UserDownloads(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserDownloads'
		verbose_name_plural = 'UserDownloads'


class Periodical(models.Model):

	creativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Creativeworkseries", blank=True, null=True, help_text='''
          A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind.
          CreativeWorkSeries are usually organized into some order, often chronological. Unlike <a href="/ItemList">ItemList</a> which
          is a general purpose data structure for lists of things, the emphasis with
          CreativeWorkSeries is on published materials (written e.g. books and periodicals,
          or media such as tv, radio and games).

          <br/><br/>

          Specific subtypes are available for describing <a href="/TVSeries">TVSeries</a>, <a href="/RadioSeries">RadioSeries</a>,
          <a href="/MovieSeries">MovieSeries</a>,
          <a href="/BookSeries">BookSeries</a>,
          <a href="/Periodical">Periodical</a>
          and <a href="/VideoGameSeries">VideoGameSeries</a>. In each case,
          the <a href="/hasPart">hasPart</a> / <a href="/isPartOf">isPartOf</a> properties
          can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely
          just to organize these more specific and practical subtypes.

          <br/><br/>

          It is common for properties applicable to an item from the series to be usefully applied to the containing group.
          Schema.org attempts to anticipate some of these cases, but publishers should be free to apply
          properties of the series parts to the series as a whole wherever they seem appropriate.''', related_name="periodical_creativeworkseries")
	issnText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Issn", blank=True, null=True, help_text='''The International Standard Serial Number (ISSN) that identifies this periodical. You can repeat this property to (for example) identify different formats of this periodical.''', related_name="periodical_issn_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Periodical'
		verbose_name_plural = 'Periodical'


class Demand(models.Model):

	advanceBookingRequirementQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Advancebookingrequirement", blank=True, null=True, help_text='''The amount of time that is required between accepting the offer and the actual usage of the resource or service.''', related_name="demand_advancebookingrequirement_quantitativevalue")
	availableDeliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Availabledeliverymethod", blank=True, null=True, help_text='''The delivery method(s) available for this offer.''', related_name="demand_availabledeliverymethod_deliverymethod")
	priceSpecificationPriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", blank=True, null=True, help_text='''One or more detailed price specifications, indicating the unit price and delivery or payment charges.''', related_name="demand_pricespecification_pricespecification")
	validFromDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", blank=True, null=True, help_text='''The date when the item becomes valid.''', related_name="demand_validfrom_datetime")
	businessFunctionBusinessFunction = models.ForeignKey('BusinessFunction', on_delete=models.CASCADE, verbose_name="Businessfunction", blank=True, null=True, help_text='''The business function (e.g. sell, lease, repair, dispose) of the offer or component of a bundle (TypeAndQuantityNode). The default is http://purl.org/goodrelations/v1#Sell.''', related_name="demand_businessfunction_businessfunction")
	itemOfferedProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Itemoffered", blank=True, null=True, help_text='''The item being offered.''', related_name="demand_itemoffered_product")
	itemOfferedService = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Itemoffered", blank=True, null=True, help_text='''The item being offered.''', related_name="demand_itemoffered_service")
	includesObjectTypeAndQuantityNode = models.ForeignKey('TypeAndQuantityNode', on_delete=models.CASCADE, verbose_name="Includesobject", blank=True, null=True, help_text='''This links to a node or nodes indicating the exact quantity of the products included in the offer.''', related_name="demand_includesobject_typeandquantitynode")
	gtin14Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin14", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-14.aspx">GTIN-14</a> code of the product, or the product to which the offer refers. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="demand_gtin14_text")
	gtin13Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin13", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-13.aspx">GTIN-13</a> code of the product, or the product to which the offer refers. This is equivalent to 13-digit ISBN codes and EAN UCC-13. Former 12-digit UPC codes can be converted into a GTIN-13 code by simply adding a preceeding zero. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="demand_gtin13_text")
	gtin12Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin12", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-12.aspx">GTIN-12</a> code of the product, or the product to which the offer refers. The GTIN-12 is the 12-digit GS1 Identification Key composed of a U.P.C. Company Prefix, Item Reference, and Check Digit used to identify trade items. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="demand_gtin12_text")
	availableAtOrFromPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Availableatorfrom", blank=True, null=True, help_text='''The place(s) from which the offer can be obtained (e.g. store locations).''', related_name="demand_availableatorfrom_place")
	warrantyWarrantyPromise = models.ForeignKey('WarrantyPromise', on_delete=models.CASCADE, verbose_name="Warranty", blank=True, null=True, help_text='''The warranty promise(s) included in the offer.''', related_name="demand_warranty_warrantypromise")
	inventoryLevelQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Inventorylevel", blank=True, null=True, help_text='''The current approximate inventory level for the item or items.''', related_name="demand_inventorylevel_quantitativevalue")
	availabilityStartsDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availabilitystarts", blank=True, null=True, help_text='''The beginning of the availability of the product or service included in the offer.''', related_name="demand_availabilitystarts_datetime")
	eligibleDurationQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligibleduration", blank=True, null=True, help_text='''The duration for which the given offer is valid.''', related_name="demand_eligibleduration_quantitativevalue")
	eligibleTransactionVolumePriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Eligibletransactionvolume", blank=True, null=True, help_text='''The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.''', related_name="demand_eligibletransactionvolume_pricespecification")
	mpnText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Mpn", blank=True, null=True, help_text='''The Manufacturer Part Number (MPN) of the product, or the product to which the offer refers.''', related_name="demand_mpn_text")
	areaServedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="demand_areaserved_text")
	areaServedAdministrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="demand_areaserved_administrativearea")
	areaServedPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="demand_areaserved_place")
	areaServedGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="demand_areaserved_geoshape")
	serialNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Serialnumber", blank=True, null=True, help_text='''The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.''', related_name="demand_serialnumber_text")
	sellerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="demand_seller_organization")
	sellerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Seller", blank=True, null=True, help_text='''An entity which offers (sells / leases / lends / loans) the services / goods.  A seller may also be a provider.''', related_name="demand_seller_person")
	acceptedPaymentMethodLoanOrCredit = models.ForeignKey('LoanOrCredit', on_delete=models.CASCADE, verbose_name="Acceptedpaymentmethod", blank=True, null=True, help_text='''The payment method(s) accepted by seller for this offer.''', related_name="demand_acceptedpaymentmethod_loanorcredit")
	acceptedPaymentMethodPaymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Acceptedpaymentmethod", blank=True, null=True, help_text='''The payment method(s) accepted by seller for this offer.''', related_name="demand_acceptedpaymentmethod_paymentmethod")
	validThroughDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", blank=True, null=True, help_text='''The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.''', related_name="demand_validthrough_datetime")
	availabilityItemAvailability = models.ForeignKey('ItemAvailability', on_delete=models.CASCADE, verbose_name="Availability", blank=True, null=True, help_text='''The availability of this item&#x2014;for example In stock, Out of stock, Pre-order, etc.''', related_name="demand_availability_itemavailability")
	skuText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Sku", blank=True, null=True, help_text='''The Stock Keeping Unit (SKU), i.e. a merchant-specific identifier for a product or service, or the product to which the offer refers.''', related_name="demand_sku_text")
	gtin8Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gtin8", blank=True, null=True, help_text='''The <a href="http://ocp.gs1.org/sites/glossary/en-gb/Pages/GTIN-8.aspx">GTIN-8</a> code of the product, or the product to which the offer refers. This code is also known as EAN/UCC-8 or 8-digit EAN. See <a href="http://www.gs1.org/barcodes/technical/idkeys/gtin">GS1 GTIN Summary</a> for more details.''', related_name="demand_gtin8_text")
	deliveryLeadTimeQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Deliveryleadtime", blank=True, null=True, help_text='''The typical delay between the receipt of the order and the goods leaving the warehouse.''', related_name="demand_deliveryleadtime_quantitativevalue")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="demand_intangible")
	eligibleQuantityQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligiblequantity", blank=True, null=True, help_text='''The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.''', related_name="demand_eligiblequantity_quantitativevalue")
	ineligibleRegionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Ineligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.
      <br><br> See also <a href="/eligibleRegion">eligibleRegion</a>.
      ''', related_name="demand_ineligibleregion_text")
	ineligibleRegionGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Ineligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.
      <br><br> See also <a href="/eligibleRegion">eligibleRegion</a>.
      ''', related_name="demand_ineligibleregion_geoshape")
	ineligibleRegionPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Ineligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is not valid, e.g. a region where the transaction is not allowed.
      <br><br> See also <a href="/eligibleRegion">eligibleRegion</a>.
      ''', related_name="demand_ineligibleregion_place")
	itemConditionOfferItemCondition = models.ForeignKey('OfferItemCondition', on_delete=models.CASCADE, verbose_name="Itemcondition", blank=True, null=True, help_text='''A predefined value from OfferItemCondition or a textual description of the condition of the product or service, or the products or services included in the offer.''', related_name="demand_itemcondition_offeritemcondition")
	eligibleRegionPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Eligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.
      <br><br> See also <a href="/ineligibleRegion">ineligibleRegion</a>.
    ''', related_name="demand_eligibleregion_place")
	eligibleRegionGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Eligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.
      <br><br> See also <a href="/ineligibleRegion">ineligibleRegion</a>.
    ''', related_name="demand_eligibleregion_geoshape")
	eligibleRegionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Eligibleregion", blank=True, null=True, help_text='''The ISO 3166-1 (ISO 3166-1 alpha-2) or ISO 3166-2 code, the place, or the GeoShape for the geo-political region(s) for which the offer or delivery charge specification is valid.
      <br><br> See also <a href="/ineligibleRegion">ineligibleRegion</a>.
    ''', related_name="demand_eligibleregion_text")
	eligibleCustomerTypeBusinessEntityType = models.ForeignKey('BusinessEntityType', on_delete=models.CASCADE, verbose_name="Eligiblecustomertype", blank=True, null=True, help_text='''The type(s) of customers for which the given offer is valid.''', related_name="demand_eligiblecustomertype_businessentitytype")
	availabilityEndsDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Availabilityends", blank=True, null=True, help_text='''The end of the availability of the product or service included in the offer.''', related_name="demand_availabilityends_datetime")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Demand'
		verbose_name_plural = 'Demand'


class BookStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="bookstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BookStore'
		verbose_name_plural = 'BookStore'


class StructuredValue(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="structuredvalue_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'StructuredValue'
		verbose_name_plural = 'StructuredValue'


class PaymentService(models.Model):

	financialProduct = models.ForeignKey('FinancialProduct', on_delete=models.CASCADE, verbose_name="Financialproduct", blank=True, null=True, help_text='''A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.''', related_name="paymentservice_financialproduct")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PaymentService'
		verbose_name_plural = 'PaymentService'


class MusicAlbumProductionType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="musicalbumproductiontype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicAlbumProductionType'
		verbose_name_plural = 'MusicAlbumProductionType'


class GiveAction(models.Model):

	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="Transferaction", blank=True, null=True, help_text='''The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.''', related_name="giveaction_transferaction")
	recipientPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="giveaction_recipient_person")
	recipientAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="giveaction_recipient_audience")
	recipientOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="giveaction_recipient_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GiveAction'
		verbose_name_plural = 'GiveAction'


class IndividualProduct(models.Model):

	product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product", blank=True, null=True, help_text='''Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.''', related_name="individualproduct_product")
	serialNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Serialnumber", blank=True, null=True, help_text='''The serial number or any alphanumeric identifier of a particular product. When attached to an offer, it is a shortcut for the serial number of the product included in the offer.''', related_name="individualproduct_serialnumber_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'IndividualProduct'
		verbose_name_plural = 'IndividualProduct'


class SportsOrganization(models.Model):

	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", blank=True, null=True, help_text='''An organization such as a school, NGO, corporation, club, etc.''', related_name="sportsorganization_organization")
	sportText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Sport", blank=True, null=True, help_text='''A type of sport (e.g. Baseball).''', related_name="sportsorganization_sport_text")
	sportURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Sport", blank=True, null=True, help_text='''A type of sport (e.g. Baseball).''', related_name="sportsorganization_sport_url")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SportsOrganization'
		verbose_name_plural = 'SportsOrganization'


class SendAction(models.Model):

	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="Transferaction", blank=True, null=True, help_text='''The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.''', related_name="sendaction_transferaction")
	deliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Deliverymethod", blank=True, null=True, help_text='''A sub property of instrument. The method of delivery.''', related_name="sendaction_deliverymethod_deliverymethod")
	recipientPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="sendaction_recipient_person")
	recipientAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="sendaction_recipient_audience")
	recipientOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="sendaction_recipient_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SendAction'
		verbose_name_plural = 'SendAction'


class GameServerStatus(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="gameserverstatus_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GameServerStatus'
		verbose_name_plural = 'GameServerStatus'


class UserBlocks(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserBlocks'
		verbose_name_plural = 'UserBlocks'


class ParcelDelivery(models.Model):

	partOfOrderOrder = models.ForeignKey('Order', on_delete=models.CASCADE, verbose_name="Partoforder", blank=True, null=True, help_text='''The overall order the items in this delivery were included in.''', related_name="parceldelivery_partoforder_order")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="parceldelivery_intangible")
	expectedArrivalFromDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Expectedarrivalfrom", blank=True, null=True, help_text='''The earliest date the package may arrive.''', related_name="parceldelivery_expectedarrivalfrom_datetime")
	trackingUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Trackingurl", blank=True, null=True, help_text='''Tracking url for the parcel delivery.''', related_name="parceldelivery_trackingurl_url")
	originAddressPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Originaddress", blank=True, null=True, help_text='''Shipper's address.''', related_name="parceldelivery_originaddress_postaladdress")
	itemShippedProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Itemshipped", blank=True, null=True, help_text='''Item(s) being shipped.''', related_name="parceldelivery_itemshipped_product")
	deliveryAddressPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Deliveryaddress", blank=True, null=True, help_text='''Destination address.''', related_name="parceldelivery_deliveryaddress_postaladdress")
	deliveryStatusDeliveryEvent = models.ForeignKey('DeliveryEvent', on_delete=models.CASCADE, verbose_name="Deliverystatus", blank=True, null=True, help_text='''New entry added as the package passes through each leg of its journey (from shipment to final delivery).''', related_name="parceldelivery_deliverystatus_deliveryevent")
	expectedArrivalUntilDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Expectedarrivaluntil", blank=True, null=True, help_text='''The latest date the package may arrive.''', related_name="parceldelivery_expectedarrivaluntil_datetime")
	providerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="parceldelivery_provider_organization")
	providerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="parceldelivery_provider_person")
	trackingNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Trackingnumber", blank=True, null=True, help_text='''Shipper tracking number.''', related_name="parceldelivery_trackingnumber_text")
	hasDeliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Hasdeliverymethod", blank=True, null=True, help_text='''Method used for delivery or shipping.''', related_name="parceldelivery_hasdeliverymethod_deliverymethod")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ParcelDelivery'
		verbose_name_plural = 'ParcelDelivery'


class RadioClip(models.Model):

	clip = models.ForeignKey('Clip', on_delete=models.CASCADE, verbose_name="Clip", blank=True, null=True, help_text='''A short TV or radio program or a segment/part of a program.''', related_name="radioclip_clip")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RadioClip'
		verbose_name_plural = 'RadioClip'


class DeleteAction(models.Model):

	updateAction = models.ForeignKey('UpdateAction', on_delete=models.CASCADE, verbose_name="Updateaction", blank=True, null=True, help_text='''The act of managing by changing/editing the state of the object.''', related_name="deleteaction_updateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DeleteAction'
		verbose_name_plural = 'DeleteAction'


class PlaceOfWorship(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="placeofworship_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PlaceOfWorship'
		verbose_name_plural = 'PlaceOfWorship'


class Plumber(models.Model):

	homeAndConstructionBusiness = models.ForeignKey('HomeAndConstructionBusiness', on_delete=models.CASCADE, verbose_name="Homeandconstructionbusiness", blank=True, null=True, help_text='''A construction business.
        <br><br>
        A HomeAndConstructionBusiness is a LocalBusiness that provides services around homes and buildings.
          <br><br>
          As a <a href="/LocalBusiness">LocalBusiness</a> it can be
          described as a <a href="/provider">provider</a> of one or more
          <a href="/Service">Service(s)</a>.
      ''', related_name="plumber_homeandconstructionbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Plumber'
		verbose_name_plural = 'Plumber'


class BankOrCreditUnion(models.Model):

	financialService = models.ForeignKey('FinancialService', on_delete=models.CASCADE, verbose_name="Financialservice", blank=True, null=True, help_text='''Financial services business.''', related_name="bankorcreditunion_financialservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BankOrCreditUnion'
		verbose_name_plural = 'BankOrCreditUnion'


class MusicEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="musicevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicEvent'
		verbose_name_plural = 'MusicEvent'


class Intangible(models.Model):

	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", blank=True, null=True, help_text='''The most generic type of item.''', related_name="intangible_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Intangible'
		verbose_name_plural = 'Intangible'


class FilmAction(models.Model):

	createAction = models.ForeignKey('CreateAction', on_delete=models.CASCADE, verbose_name="Createaction", blank=True, null=True, help_text='''The act of deliberately creating/producing/generating/building a result out of the agent.''', related_name="filmaction_createaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FilmAction'
		verbose_name_plural = 'FilmAction'


class Airport(models.Model):

	iataCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Iatacode", blank=True, null=True, help_text='''IATA identifier for an airline or airport.''', related_name="airport_iatacode_text")
	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="airport_civicstructure")
	icaoCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Icaocode", blank=True, null=True, help_text='''ICAO identifier for an airport.''', related_name="airport_icaocode_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Airport'
		verbose_name_plural = 'Airport'


class Role(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="role_intangible")
	roleNameURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Rolename", blank=True, null=True, help_text='''A role played, performed or filled by a person or organization. For example, the team of creators for a comic book might fill the roles named 'inker', 'penciller', and 'letterer'; or an athlete in a SportsTeam might play in the position named 'Quarterback'.''', related_name="role_rolename_url")
	roleNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Rolename", blank=True, null=True, help_text='''A role played, performed or filled by a person or organization. For example, the team of creators for a comic book might fill the roles named 'inker', 'penciller', and 'letterer'; or an athlete in a SportsTeam might play in the position named 'Quarterback'.''', related_name="role_rolename_text")
	startDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", blank=True, null=True, help_text='''The start date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="role_startdate_date")
	endDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", blank=True, null=True, help_text='''The end date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="role_enddate_date")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Role'
		verbose_name_plural = 'Role'


class Ticket(models.Model):

	priceCurrencyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricecurrency", blank=True, null=True, help_text='''The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.''', related_name="ticket_pricecurrency_text")
	totalPriceNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Totalprice", blank=True, null=True, help_text='''The total price for the reservation or ticket, including applicable taxes, shipping, etc.''', related_name="ticket_totalprice_number")
	totalPricePriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Totalprice", blank=True, null=True, help_text='''The total price for the reservation or ticket, including applicable taxes, shipping, etc.''', related_name="ticket_totalprice_pricespecification")
	totalPriceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Totalprice", blank=True, null=True, help_text='''The total price for the reservation or ticket, including applicable taxes, shipping, etc.''', related_name="ticket_totalprice_text")
	dateIssuedDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Dateissued", blank=True, null=True, help_text='''The date the ticket was issued.''', related_name="ticket_dateissued_datetime")
	ticketTokenURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Tickettoken", blank=True, null=True, help_text='''Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance.''', related_name="ticket_tickettoken_url")
	ticketTokenText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Tickettoken", blank=True, null=True, help_text='''Reference to an asset (e.g., Barcode, QR code image or PDF) usable for entrance.''', related_name="ticket_tickettoken_text")
	ticketNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Ticketnumber", blank=True, null=True, help_text='''The unique identifier for the ticket.''', related_name="ticket_ticketnumber_text")
	issuedByOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Issuedby", blank=True, null=True, help_text='''The organization issuing the ticket or permit.''', related_name="ticket_issuedby_organization")
	ticketedSeatSeat = models.ForeignKey('Seat', on_delete=models.CASCADE, verbose_name="Ticketedseat", blank=True, null=True, help_text='''The seat associated with the ticket.''', related_name="ticket_ticketedseat_seat")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="ticket_intangible")
	underNamePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Undername", blank=True, null=True, help_text='''The person or organization the reservation or ticket is for.''', related_name="ticket_undername_person")
	underNameOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Undername", blank=True, null=True, help_text='''The person or organization the reservation or ticket is for.''', related_name="ticket_undername_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Ticket'
		verbose_name_plural = 'Ticket'


class TaxiStand(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="taxistand_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TaxiStand'
		verbose_name_plural = 'TaxiStand'


class PaymentMethod(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="paymentmethod_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PaymentMethod'
		verbose_name_plural = 'PaymentMethod'


class ReserveAction(models.Model):

	planAction = models.ForeignKey('PlanAction', on_delete=models.CASCADE, verbose_name="Planaction", blank=True, null=True, help_text='''The act of planning the execution of an event/task/action/reservation/plan to a future date.''', related_name="reserveaction_planaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReserveAction'
		verbose_name_plural = 'ReserveAction'


class ParcelService(models.Model):

	deliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Deliverymethod", blank=True, null=True, help_text='''A delivery method is a standardized procedure for transferring the product or service to the destination of fulfillment chosen by the customer. Delivery methods are characterized by the means of transportation used, and by the organization or group that is the contracting party for the sending organization or person.
<br />
    Commonly used values:<br />
<br />
    http://purl.org/goodrelations/v1#DeliveryModeDirectDownload <br />
    http://purl.org/goodrelations/v1#DeliveryModeFreight <br />
    http://purl.org/goodrelations/v1#DeliveryModeMail <br />
    http://purl.org/goodrelations/v1#DeliveryModeOwnFleet <br />
    http://purl.org/goodrelations/v1#DeliveryModePickUp <br />
    http://purl.org/goodrelations/v1#DHL <br />
    http://purl.org/goodrelations/v1#FederalExpress <br />
    http://purl.org/goodrelations/v1#UPS <br />
        ''', related_name="parcelservice_deliverymethod")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ParcelService'
		verbose_name_plural = 'ParcelService'


class RestrictedDiet(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="restricteddiet_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RestrictedDiet'
		verbose_name_plural = 'RestrictedDiet'


class TelevisionChannel(models.Model):

	broadcastChannel = models.ForeignKey('BroadcastChannel', on_delete=models.CASCADE, verbose_name="Broadcastchannel", blank=True, null=True, help_text='''A unique instance of a BroadcastService on a CableOrSatelliteService lineup.''', related_name="televisionchannel_broadcastchannel")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TelevisionChannel'
		verbose_name_plural = 'TelevisionChannel'


class AdultEntertainment(models.Model):

	entertainmentBusiness = models.ForeignKey('EntertainmentBusiness', on_delete=models.CASCADE, verbose_name="Entertainmentbusiness", blank=True, null=True, help_text='''A business providing entertainment.''', related_name="adultentertainment_entertainmentbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AdultEntertainment'
		verbose_name_plural = 'AdultEntertainment'


class ChildCare(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="childcare_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ChildCare'
		verbose_name_plural = 'ChildCare'


class MusicReleaseFormatType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="musicreleaseformattype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicReleaseFormatType'
		verbose_name_plural = 'MusicReleaseFormatType'


class DepositAccount(models.Model):

	investmentOrDeposit = models.ForeignKey('InvestmentOrDeposit', on_delete=models.CASCADE, verbose_name="Investmentordeposit", blank=True, null=True, help_text='''A type of financial product that typically requires the client to transfer funds to a financial service in return for potential beneficial financial return.''', related_name="depositaccount_investmentordeposit")
	bankAccount = models.ForeignKey('BankAccount', on_delete=models.CASCADE, verbose_name="Bankaccount", blank=True, null=True, help_text='''A product or service offered by a bank whereby one may deposit, withdraw or transfer money and in some cases be paid interest.''', related_name="depositaccount_bankaccount")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DepositAccount'
		verbose_name_plural = 'DepositAccount'


class DeliveryMethod(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="deliverymethod_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DeliveryMethod'
		verbose_name_plural = 'DeliveryMethod'


class EventStatusType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="eventstatustype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EventStatusType'
		verbose_name_plural = 'EventStatusType'


class BarOrPub(models.Model):

	foodEstablishment = models.ForeignKey('FoodEstablishment', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A food-related business.''', related_name="barorpub_foodestablishment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BarOrPub'
		verbose_name_plural = 'BarOrPub'


class OfferItemCondition(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="offeritemcondition_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OfferItemCondition'
		verbose_name_plural = 'OfferItemCondition'


class SportsClub(models.Model):

	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sports location, such as a playing field.''', related_name="sportsclub_sportsactivitylocation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SportsClub'
		verbose_name_plural = 'SportsClub'


class Language(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="language_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Language'
		verbose_name_plural = 'Language'


class LoanOrCredit(models.Model):

	amountMonetaryAmount = models.ForeignKey('MonetaryAmount', on_delete=models.CASCADE, verbose_name="Amount", blank=True, null=True, help_text='''The amount of money.''', related_name="loanorcredit_amount_monetaryamount")
	amountNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Amount", blank=True, null=True, help_text='''The amount of money.''', related_name="loanorcredit_amount_number")
	financialProduct = models.ForeignKey('FinancialProduct', on_delete=models.CASCADE, verbose_name="Financialproduct", blank=True, null=True, help_text='''A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.''', related_name="loanorcredit_financialproduct")
	requiredCollateralThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Requiredcollateral", blank=True, null=True, help_text='''Assets required to secure loan or credit repayments. It may take form of third party pledge, goods, financial instruments (cash, securities, etc.)''', related_name="loanorcredit_requiredcollateral_thing")
	requiredCollateralText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Requiredcollateral", blank=True, null=True, help_text='''Assets required to secure loan or credit repayments. It may take form of third party pledge, goods, financial instruments (cash, securities, etc.)''', related_name="loanorcredit_requiredcollateral_text")
	loanTermQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Loanterm", blank=True, null=True, help_text='''The duration of the loan or credit agreement.''', related_name="loanorcredit_loanterm_quantitativevalue")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LoanOrCredit'
		verbose_name_plural = 'LoanOrCredit'


class BankAccount(models.Model):

	financialProduct = models.ForeignKey('FinancialProduct', on_delete=models.CASCADE, verbose_name="Financialproduct", blank=True, null=True, help_text='''A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.''', related_name="bankaccount_financialproduct")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BankAccount'
		verbose_name_plural = 'BankAccount'


class WebPage(models.Model):

	breadcrumbBreadcrumbList = models.ForeignKey('BreadcrumbList', on_delete=models.CASCADE, verbose_name="Breadcrumb", blank=True, null=True, help_text='''A set of links that can help a user understand and navigate a website hierarchy.''', related_name="webpage_breadcrumb_breadcrumblist")
	breadcrumbText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Breadcrumb", blank=True, null=True, help_text='''A set of links that can help a user understand and navigate a website hierarchy.''', related_name="webpage_breadcrumb_text")
	relatedLinkURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Relatedlink", blank=True, null=True, help_text='''A link related to this web page, for example to other related web pages.''', related_name="webpage_relatedlink_url")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="webpage_creativework")
	primaryImageOfPageImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Primaryimageofpage", blank=True, null=True, help_text='''Indicates the main image on the page.''', related_name="webpage_primaryimageofpage_imageobject")
	specialtySpecialty = models.ForeignKey('Specialty', on_delete=models.CASCADE, verbose_name="Specialty", blank=True, null=True, help_text='''One of the domain specialities to which this web page's content applies.''', related_name="webpage_specialty_specialty")
	significantLinkURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Significantlink", blank=True, null=True, help_text='''One of the more significant URLs on the page. Typically, these are the non-navigation links that are clicked on the most.''', related_name="webpage_significantlink_url")
	mainContentOfPageWebPageElement = models.ForeignKey('WebPageElement', on_delete=models.CASCADE, verbose_name="Maincontentofpage", blank=True, null=True, help_text='''Indicates if this web page element is the main subject of the page.''', related_name="webpage_maincontentofpage_webpageelement")
	reviewedByOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Reviewedby", blank=True, null=True, help_text='''People or organizations that have reviewed the content on this web page for accuracy and/or completeness.''', related_name="webpage_reviewedby_organization")
	reviewedByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Reviewedby", blank=True, null=True, help_text='''People or organizations that have reviewed the content on this web page for accuracy and/or completeness.''', related_name="webpage_reviewedby_person")
	lastReviewedDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Lastreviewed", blank=True, null=True, help_text='''Date on which the content on this web page was last reviewed for accuracy and/or completeness.''', related_name="webpage_lastreviewed_date")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WebPage'
		verbose_name_plural = 'WebPage'


class ConfirmAction(models.Model):

	informAction = models.ForeignKey('InformAction', on_delete=models.CASCADE, verbose_name="Informaction", blank=True, null=True, help_text='''The act of notifying someone of information pertinent to them, with no expectation of a response.''', related_name="confirmaction_informaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ConfirmAction'
		verbose_name_plural = 'ConfirmAction'


class ProductModel(models.Model):

	product = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Product", blank=True, null=True, help_text='''Any offered product or service. For example: a pair of shoes; a concert ticket; the rental of a car; a haircut; or an episode of a TV show streamed online.''', related_name="productmodel_product")
	isVariantOfProductModel = models.ForeignKey('ProductModel', on_delete=models.CASCADE, verbose_name="Isvariantof", blank=True, null=True, help_text='''A pointer to a base product from which this product is a variant. It is safe to infer that the variant inherits all product features from the base model, unless defined locally. This is not transitive.''', related_name="productmodel_isvariantof_productmodel")
	successorOfProductModel = models.ForeignKey('ProductModel', on_delete=models.CASCADE, verbose_name="Successorof", blank=True, null=True, help_text='''A pointer from a newer variant of a product  to its previous, often discontinued predecessor.''', related_name="productmodel_successorof_productmodel")
	predecessorOfProductModel = models.ForeignKey('ProductModel', on_delete=models.CASCADE, verbose_name="Predecessorof", blank=True, null=True, help_text='''A pointer from a previous, often discontinued variant of the product to its newer variant.''', related_name="productmodel_predecessorof_productmodel")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ProductModel'
		verbose_name_plural = 'ProductModel'


class FlightReservation(models.Model):

	boardingGroupText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Boardinggroup", blank=True, null=True, help_text='''The airline-specific indicator of boarding order / preference.''', related_name="flightreservation_boardinggroup_text")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", blank=True, null=True, help_text='''Describes a reservation for travel, dining or an event. Some reservations require tickets.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use http://schema.org/Offer.''', related_name="flightreservation_reservation")
	securityScreeningText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Securityscreening", blank=True, null=True, help_text='''The type of security screening the passenger is subject to.''', related_name="flightreservation_securityscreening_text")
	passengerPriorityStatusText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Passengerprioritystatus", blank=True, null=True, help_text='''The priority status assigned to a passenger for security or boarding (e.g. FastTrack or Priority).''', related_name="flightreservation_passengerprioritystatus_text")
	passengerPriorityStatusQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Passengerprioritystatus", blank=True, null=True, help_text='''The priority status assigned to a passenger for security or boarding (e.g. FastTrack or Priority).''', related_name="flightreservation_passengerprioritystatus_qualitativevalue")
	passengerSequenceNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Passengersequencenumber", blank=True, null=True, help_text='''The passenger's sequence number as assigned by the airline.''', related_name="flightreservation_passengersequencenumber_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FlightReservation'
		verbose_name_plural = 'FlightReservation'


class VoteAction(models.Model):

	candidatePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Candidate", blank=True, null=True, help_text='''A sub property of object. The candidate subject of this action.''', related_name="voteaction_candidate_person")
	chooseAction = models.ForeignKey('ChooseAction', on_delete=models.CASCADE, verbose_name="Chooseaction", blank=True, null=True, help_text='''The act of expressing a preference from a set of options or a large or unbounded set of choices/options.''', related_name="voteaction_chooseaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'VoteAction'
		verbose_name_plural = 'VoteAction'


class Service(models.Model):

	audienceAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", blank=True, null=True, help_text='''An intended audience, i.e. a group for whom something was created.''', related_name="service_audience_audience")
	awardText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", blank=True, null=True, help_text='''An award won by or for this item.''', related_name="service_award_text")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="service_intangible")
	isRelatedToService = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Isrelatedto", blank=True, null=True, help_text='''A pointer to another, somehow related product (or multiple products).''', related_name="service_isrelatedto_service")
	isRelatedToProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Isrelatedto", blank=True, null=True, help_text='''A pointer to another, somehow related product (or multiple products).''', related_name="service_isrelatedto_product")
	providerMobilityText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Providermobility", blank=True, null=True, help_text='''Indicates the mobility of a provided service (e.g. 'static', 'dynamic').''', related_name="service_providermobility_text")
	offersOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Offers", blank=True, null=True, help_text='''An offer to provide this item&#x2014;for example, an offer to sell a product, rent the DVD of a movie, perform a service, or give away tickets to an event.''', related_name="service_offers_offer")
	reviewReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", blank=True, null=True, help_text='''A review of the item.''', related_name="service_review_review")
	brandBrand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name="Brand", blank=True, null=True, help_text='''The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.''', related_name="service_brand_brand")
	brandOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Brand", blank=True, null=True, help_text='''The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.''', related_name="service_brand_organization")
	areaServedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="service_areaserved_text")
	areaServedAdministrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="service_areaserved_administrativearea")
	areaServedPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="service_areaserved_place")
	areaServedGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Areaserved", blank=True, null=True, help_text='''The geographic area where a service or offered item is provided.''', related_name="service_areaserved_geoshape")
	hoursAvailableOpeningHoursSpecification = models.ForeignKey('OpeningHoursSpecification', on_delete=models.CASCADE, verbose_name="Hoursavailable", blank=True, null=True, help_text='''The hours during which this service or contact is available.''', related_name="service_hoursavailable_openinghoursspecification")
	availableChannelServiceChannel = models.ForeignKey('ServiceChannel', on_delete=models.CASCADE, verbose_name="Availablechannel", blank=True, null=True, help_text='''A means of accessing the service (e.g. a phone bank, a web site, a location, etc.).''', related_name="service_availablechannel_servicechannel")
	isSimilarToService = models.ForeignKey('Service', on_delete=models.CASCADE, verbose_name="Issimilarto", blank=True, null=True, help_text='''A pointer to another, functionally similar product (or multiple products).''', related_name="service_issimilarto_service")
	isSimilarToProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Issimilarto", blank=True, null=True, help_text='''A pointer to another, functionally similar product (or multiple products).''', related_name="service_issimilarto_product")
	providerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="service_provider_organization")
	providerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="service_provider_person")
	hasOfferCatalogOfferCatalog = models.ForeignKey('OfferCatalog', on_delete=models.CASCADE, verbose_name="Hasoffercatalog", blank=True, null=True, help_text='''Indicates an OfferCatalog listing for this Organization, Person, or Service.''', related_name="service_hasoffercatalog_offercatalog")
	aggregateRatingAggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", blank=True, null=True, help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="service_aggregaterating_aggregaterating")
	serviceOutputThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Serviceoutput", blank=True, null=True, help_text='''The tangible thing generated by the service, e.g. a passport, permit, etc.''', related_name="service_serviceoutput_thing")
	logoURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="service_logo_url")
	logoImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="service_logo_imageobject")
	serviceTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Servicetype", blank=True, null=True, help_text='''The type of service being offered, e.g. veterans' benefits, emergency relief, etc.''', related_name="service_servicetype_text")
	categoryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Category", blank=True, null=True, help_text='''A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.''', related_name="service_category_text")
	categoryThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Category", blank=True, null=True, help_text='''A category for the item. Greater signs or slashes can be used to informally indicate a category hierarchy.''', related_name="service_category_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Service'
		verbose_name_plural = 'Service'


class CityHall(models.Model):

	governmentBuilding = models.ForeignKey('GovernmentBuilding', on_delete=models.CASCADE, verbose_name="Governmentbuilding", blank=True, null=True, help_text='''A government building.''', related_name="cityhall_governmentbuilding")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CityHall'
		verbose_name_plural = 'CityHall'


class TVEpisode(models.Model):

	episode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", blank=True, null=True, help_text='''A media episode (e.g. TV, radio, video game) which can be part of a series or season.''', related_name="tvepisode_episode")
	subtitleLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Subtitlelanguage", blank=True, null=True, help_text='''Languages in which subtitles/captions are available, in <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard format.</a>''', related_name="tvepisode_subtitlelanguage_text")
	subtitleLanguageLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Subtitlelanguage", blank=True, null=True, help_text='''Languages in which subtitles/captions are available, in <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard format.</a>''', related_name="tvepisode_subtitlelanguage_language")
	countryOfOriginCountry = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Countryoforigin", blank=True, null=True, help_text='''The country of the principal offices of the production company or individual responsible for the movie or program.''', related_name="tvepisode_countryoforigin_country")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TVEpisode'
		verbose_name_plural = 'TVEpisode'


class BookSeries(models.Model):

	creativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Creativeworkseries", blank=True, null=True, help_text='''
          A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind.
          CreativeWorkSeries are usually organized into some order, often chronological. Unlike <a href="/ItemList">ItemList</a> which
          is a general purpose data structure for lists of things, the emphasis with
          CreativeWorkSeries is on published materials (written e.g. books and periodicals,
          or media such as tv, radio and games).

          <br/><br/>

          Specific subtypes are available for describing <a href="/TVSeries">TVSeries</a>, <a href="/RadioSeries">RadioSeries</a>,
          <a href="/MovieSeries">MovieSeries</a>,
          <a href="/BookSeries">BookSeries</a>,
          <a href="/Periodical">Periodical</a>
          and <a href="/VideoGameSeries">VideoGameSeries</a>. In each case,
          the <a href="/hasPart">hasPart</a> / <a href="/isPartOf">isPartOf</a> properties
          can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely
          just to organize these more specific and practical subtypes.

          <br/><br/>

          It is common for properties applicable to an item from the series to be usefully applied to the containing group.
          Schema.org attempts to anticipate some of these cases, but publishers should be free to apply
          properties of the series parts to the series as a whole wherever they seem appropriate.''', related_name="bookseries_creativeworkseries")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BookSeries'
		verbose_name_plural = 'BookSeries'


class LiquorStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="liquorstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LiquorStore'
		verbose_name_plural = 'LiquorStore'


class BlogPosting(models.Model):

	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", blank=True, null=True, help_text='''An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.

      <br/><br/>See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.''', related_name="blogposting_article")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BlogPosting'
		verbose_name_plural = 'BlogPosting'


class QualitativeValue(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="qualitativevalue_enumeration")
	greaterOrEqualQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Greaterorequal", blank=True, null=True, help_text='''This ordering relation for qualitative values indicates that the subject is greater than or equal to the object.''', related_name="qualitativevalue_greaterorequal_qualitativevalue")
	additionalPropertyPropertyValue = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Additionalproperty", blank=True, null=True, help_text='''A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. <br /><br />

Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
''', related_name="qualitativevalue_additionalproperty_propertyvalue")
	nonEqualQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Nonequal", blank=True, null=True, help_text='''This ordering relation for qualitative values indicates that the subject is not equal to the object.''', related_name="qualitativevalue_nonequal_qualitativevalue")
	lesserQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Lesser", blank=True, null=True, help_text='''This ordering relation for qualitative values indicates that the subject is lesser than the object.''', related_name="qualitativevalue_lesser_qualitativevalue")
	lesserOrEqualQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Lesserorequal", blank=True, null=True, help_text='''This ordering relation for qualitative values indicates that the subject is lesser than or equal to the object.''', related_name="qualitativevalue_lesserorequal_qualitativevalue")
	equalQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Equal", blank=True, null=True, help_text='''This ordering relation for qualitative values indicates that the subject is equal to the object.''', related_name="qualitativevalue_equal_qualitativevalue")
	greaterQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Greater", blank=True, null=True, help_text='''This ordering relation for qualitative values indicates that the subject is greater than the object.''', related_name="qualitativevalue_greater_qualitativevalue")
	valueReferencePropertyValue = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="qualitativevalue_valuereference_propertyvalue")
	valueReferenceEnumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="qualitativevalue_valuereference_enumeration")
	valueReferenceStructuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="qualitativevalue_valuereference_structuredvalue")
	valueReferenceQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="qualitativevalue_valuereference_quantitativevalue")
	valueReferenceQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Valuereference", blank=True, null=True, help_text='''A pointer to a secondary value that provides additional information on the original value, e.g. a reference temperature.''', related_name="qualitativevalue_valuereference_qualitativevalue")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'QualitativeValue'
		verbose_name_plural = 'QualitativeValue'


class UserComments(models.Model):

	commentTextText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Commenttext", blank=True, null=True, help_text='''The text of the UserComment.''', related_name="usercomments_commenttext_text")
	discussesCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Discusses", blank=True, null=True, help_text='''Specifies the CreativeWork associated with the UserComment.''', related_name="usercomments_discusses_creativework")
	replyToUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Replytourl", blank=True, null=True, help_text='''The URL at which a reply may be posted to the specified UserComment.''', related_name="usercomments_replytourl_url")
	creatorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Creator", blank=True, null=True, help_text='''The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.''', related_name="usercomments_creator_person")
	creatorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Creator", blank=True, null=True, help_text='''The creator/author of this CreativeWork. This is the same as the Author property for CreativeWork.''', related_name="usercomments_creator_organization")
	commentTimeDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Commenttime", blank=True, null=True, help_text='''The time at which the UserComment was made.''', related_name="usercomments_commenttime_date")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserComments'
		verbose_name_plural = 'UserComments'


class CreateAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="createaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CreateAction'
		verbose_name_plural = 'CreateAction'


class DeactivateAction(models.Model):

	controlAction = models.ForeignKey('ControlAction', on_delete=models.CASCADE, verbose_name="Controlaction", blank=True, null=True, help_text='''An agent controls a device or application.''', related_name="deactivateaction_controlaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DeactivateAction'
		verbose_name_plural = 'DeactivateAction'


class TennisComplex(models.Model):

	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sports location, such as a playing field.''', related_name="tenniscomplex_sportsactivitylocation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TennisComplex'
		verbose_name_plural = 'TennisComplex'


class InvestmentOrDeposit(models.Model):

	amountMonetaryAmount = models.ForeignKey('MonetaryAmount', on_delete=models.CASCADE, verbose_name="Amount", blank=True, null=True, help_text='''The amount of money.''', related_name="investmentordeposit_amount_monetaryamount")
	amountNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Amount", blank=True, null=True, help_text='''The amount of money.''', related_name="investmentordeposit_amount_number")
	financialProduct = models.ForeignKey('FinancialProduct', on_delete=models.CASCADE, verbose_name="Financialproduct", blank=True, null=True, help_text='''A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.''', related_name="investmentordeposit_financialproduct")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'InvestmentOrDeposit'
		verbose_name_plural = 'InvestmentOrDeposit'


class Recipe(models.Model):

	cookingMethodText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Cookingmethod", blank=True, null=True, help_text='''The method of cooking, such as Frying, Steaming, ...''', related_name="recipe_cookingmethod_text")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="recipe_creativework")
	recipeCuisineText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recipecuisine", blank=True, null=True, help_text='''The cuisine of the recipe (for example, French or Ethiopian).''', related_name="recipe_recipecuisine_text")
	suitableForDietRestrictedDiet = models.ForeignKey('RestrictedDiet', on_delete=models.CASCADE, verbose_name="Suitablefordiet", blank=True, null=True, help_text='''Indicates a dietary restriction or guideline for which this recipe is suitable, e.g. diabetic, halal etc.''', related_name="recipe_suitablefordiet_restricteddiet")
	recipeInstructionsItemList = models.ForeignKey('ItemList', on_delete=models.CASCADE, verbose_name="Recipeinstructions", blank=True, null=True, help_text='''A step or instruction involved in making the recipe.''', related_name="recipe_recipeinstructions_itemlist")
	recipeInstructionsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recipeinstructions", blank=True, null=True, help_text='''A step or instruction involved in making the recipe.''', related_name="recipe_recipeinstructions_text")
	cookTimeDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Cooktime", blank=True, null=True, help_text='''The time it takes to actually cook the dish, in ISO 8601 duration format.''', related_name="recipe_cooktime_duration")
	recipeYieldText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recipeyield", blank=True, null=True, help_text='''The quantity produced by the recipe (for example, number of people served, number of servings, etc).''', related_name="recipe_recipeyield_text")
	prepTimeDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Preptime", blank=True, null=True, help_text='''The length of time it takes to prepare the recipe, in ISO 8601 duration format.''', related_name="recipe_preptime_duration")
	totalTimeDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Totaltime", blank=True, null=True, help_text='''The total time it takes to prepare and cook the recipe, in ISO 8601 duration format.''', related_name="recipe_totaltime_duration")
	nutritionNutritionInformation = models.ForeignKey('NutritionInformation', on_delete=models.CASCADE, verbose_name="Nutrition", blank=True, null=True, help_text='''Nutrition information about the recipe.''', related_name="recipe_nutrition_nutritioninformation")
	recipeCategoryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recipecategory", blank=True, null=True, help_text='''The category of the recipe—for example, appetizer, entree, etc.''', related_name="recipe_recipecategory_text")
	recipeIngredientText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Recipeingredient", blank=True, null=True, help_text='''A single ingredient used in the recipe, e.g. sugar, flour or garlic.''', related_name="recipe_recipeingredient_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Recipe'
		verbose_name_plural = 'Recipe'


class BookFormatType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="bookformattype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BookFormatType'
		verbose_name_plural = 'BookFormatType'


class MonetaryAmount(models.Model):

	validFromDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", blank=True, null=True, help_text='''The date when the item becomes valid.''', related_name="monetaryamount_validfrom_datetime")
	minValueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Minvalue", blank=True, null=True, help_text='''The lower value of some characteristic or property.''', related_name="monetaryamount_minvalue_number")
	validThroughDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", blank=True, null=True, help_text='''The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.''', related_name="monetaryamount_validthrough_datetime")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="monetaryamount_structuredvalue")
	valueStructuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="monetaryamount_value_structuredvalue")
	valueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="monetaryamount_value_number")
	valueBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="monetaryamount_value_boolean")
	valueText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Value", blank=True, null=True, help_text='''The value of the quantitative value or property value node.<br/>
	For QuantitativeValue and MonetaryValue, the recommended type for values is 'Number'. <br/>
	For PropertyValue, it can be 'Text;', 'Number', 'Boolean', or 'StructuredValue'.''', related_name="monetaryamount_value_text")
	maxValueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Maxvalue", blank=True, null=True, help_text='''The upper value of some characteristic or property.''', related_name="monetaryamount_maxvalue_number")
	currencyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Currency", blank=True, null=True, help_text='''The currency in which the monetary amount is expressed (in 3-letter <a href='http://en.wikipedia.org/wiki/ISO_4217'">ISO 4217</a> format).''', related_name="monetaryamount_currency_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MonetaryAmount'
		verbose_name_plural = 'MonetaryAmount'


class BusStation(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="busstation_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BusStation'
		verbose_name_plural = 'BusStation'


class SoftwareApplication(models.Model):

	storageRequirementsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Storagerequirements", blank=True, null=True, help_text='''Storage requirements (free space required).''', related_name="softwareapplication_storagerequirements_text")
	storageRequirementsURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Storagerequirements", blank=True, null=True, help_text='''Storage requirements (free space required).''', related_name="softwareapplication_storagerequirements_url")
	installUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Installurl", blank=True, null=True, help_text='''URL at which the app may be installed, if different from the URL of the item.''', related_name="softwareapplication_installurl_url")
	countriesSupportedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Countriessupported", blank=True, null=True, help_text='''Countries for which the application is supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.''', related_name="softwareapplication_countriessupported_text")
	softwareVersionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Softwareversion", blank=True, null=True, help_text='''Version of the software instance.''', related_name="softwareapplication_softwareversion_text")
	supportingDataDataFeed = models.ForeignKey('DataFeed', on_delete=models.CASCADE, verbose_name="Supportingdata", blank=True, null=True, help_text='''Supporting data for a SoftwareApplication.''', related_name="softwareapplication_supportingdata_datafeed")
	memoryRequirementsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Memoryrequirements", blank=True, null=True, help_text='''Minimum memory requirements.''', related_name="softwareapplication_memoryrequirements_text")
	memoryRequirementsURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Memoryrequirements", blank=True, null=True, help_text='''Minimum memory requirements.''', related_name="softwareapplication_memoryrequirements_url")
	softwareAddOnSoftwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Softwareaddon", blank=True, null=True, help_text='''Additional content for a software application.''', related_name="softwareapplication_softwareaddon_softwareapplication")
	applicationSubCategoryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Applicationsubcategory", blank=True, null=True, help_text='''Subcategory of the application, e.g. "Arcade Game".''', related_name="softwareapplication_applicationsubcategory_text")
	applicationSubCategoryURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Applicationsubcategory", blank=True, null=True, help_text='''Subcategory of the application, e.g. "Arcade Game".''', related_name="softwareapplication_applicationsubcategory_url")
	featureListText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Featurelist", blank=True, null=True, help_text='''Features or modules provided by this application (and possibly required by other applications).''', related_name="softwareapplication_featurelist_text")
	featureListURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Featurelist", blank=True, null=True, help_text='''Features or modules provided by this application (and possibly required by other applications).''', related_name="softwareapplication_featurelist_url")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="softwareapplication_creativework")
	softwareHelpCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Softwarehelp", blank=True, null=True, help_text='''Software application help.''', related_name="softwareapplication_softwarehelp_creativework")
	screenshotImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Screenshot", blank=True, null=True, help_text='''A link to a screenshot image of the app.''', related_name="softwareapplication_screenshot_imageobject")
	screenshotURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Screenshot", blank=True, null=True, help_text='''A link to a screenshot image of the app.''', related_name="softwareapplication_screenshot_url")
	permissionsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Permissions", blank=True, null=True, help_text='''Permission(s) required to run the app (for example, a mobile app may require full internet access or may run only on wifi).''', related_name="softwareapplication_permissions_text")
	applicationCategoryURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Applicationcategory", blank=True, null=True, help_text='''Type of software application, e.g. "Game, Multimedia".''', related_name="softwareapplication_applicationcategory_url")
	applicationCategoryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Applicationcategory", blank=True, null=True, help_text='''Type of software application, e.g. "Game, Multimedia".''', related_name="softwareapplication_applicationcategory_text")
	releaseNotesURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Releasenotes", blank=True, null=True, help_text='''Description of what changed in this version.''', related_name="softwareapplication_releasenotes_url")
	releaseNotesText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Releasenotes", blank=True, null=True, help_text='''Description of what changed in this version.''', related_name="softwareapplication_releasenotes_text")
	operatingSystemText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Operatingsystem", blank=True, null=True, help_text='''Operating systems supported (Windows 7, OSX 10.6, Android 1.6).''', related_name="softwareapplication_operatingsystem_text")
	processorRequirementsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Processorrequirements", blank=True, null=True, help_text='''Processor architecture required to run the application (e.g. IA64).''', related_name="softwareapplication_processorrequirements_text")
	countriesNotSupportedText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Countriesnotsupported", blank=True, null=True, help_text='''Countries for which the application is not supported. You can also provide the two-letter ISO 3166-1 alpha-2 country code.''', related_name="softwareapplication_countriesnotsupported_text")
	availableOnDeviceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Availableondevice", blank=True, null=True, help_text='''Device required to run the application. Used in cases where a specific make/model is required to run the application.''', related_name="softwareapplication_availableondevice_text")
	softwareRequirementsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Softwarerequirements", blank=True, null=True, help_text='''Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (Examples: DirectX, Java or .NET runtime).''', related_name="softwareapplication_softwarerequirements_text")
	softwareRequirementsURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Softwarerequirements", blank=True, null=True, help_text='''Component dependency requirements for application. This includes runtime environments and shared libraries that are not included in the application distribution package, but required to run the application (Examples: DirectX, Java or .NET runtime).''', related_name="softwareapplication_softwarerequirements_url")
	fileSizeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Filesize", blank=True, null=True, help_text='''Size of the application / package (e.g. 18MB). In the absence of a unit (MB, KB etc.), KB will be assumed.''', related_name="softwareapplication_filesize_text")
	applicationSuiteText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Applicationsuite", blank=True, null=True, help_text='''The name of the application suite to which the application belongs (e.g. Excel belongs to Office).''', related_name="softwareapplication_applicationsuite_text")
	downloadUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Downloadurl", blank=True, null=True, help_text='''If the file can be downloaded, URL to download the binary.''', related_name="softwareapplication_downloadurl_url")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SoftwareApplication'
		verbose_name_plural = 'SoftwareApplication'


class CheckAction(models.Model):

	findAction = models.ForeignKey('FindAction', on_delete=models.CASCADE, verbose_name="Findaction", blank=True, null=True, help_text='''The act of finding an object.<p>Related actions:</p><ul><li><a href="http://schema.org/SearchAction">SearchAction</a>: FindAction is generally lead by a SearchAction, but not necessarily</li></ul>.''', related_name="checkaction_findaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CheckAction'
		verbose_name_plural = 'CheckAction'


class PetStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="petstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PetStore'
		verbose_name_plural = 'PetStore'


class EmailMessage(models.Model):

	message = models.ForeignKey('Message', on_delete=models.CASCADE, verbose_name="Message", blank=True, null=True, help_text='''A single message from a sender to one or more organizations or people.''', related_name="emailmessage_message")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EmailMessage'
		verbose_name_plural = 'EmailMessage'


class EventVenue(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="eventvenue_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EventVenue'
		verbose_name_plural = 'EventVenue'


class DepartAction(models.Model):

	moveAction = models.ForeignKey('MoveAction', on_delete=models.CASCADE, verbose_name="Moveaction", blank=True, null=True, help_text='''The act of an agent relocating to a place.<p>Related actions:</p><ul><li><a href="http://schema.org/TransferAction">TransferAction</a>: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object</li></ul>.''', related_name="departaction_moveaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DepartAction'
		verbose_name_plural = 'DepartAction'


class InternetCafe(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="internetcafe_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'InternetCafe'
		verbose_name_plural = 'InternetCafe'


class ProgramMembership(models.Model):

	memberPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Member", blank=True, null=True, help_text='''A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.''', related_name="programmembership_member_person")
	memberOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Member", blank=True, null=True, help_text='''A member of an Organization or a ProgramMembership. Organizations can be members of organizations; ProgramMembership is typically for individuals.''', related_name="programmembership_member_organization")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="programmembership_intangible")
	programNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Programname", blank=True, null=True, help_text='''The program providing the membership.''', related_name="programmembership_programname_text")
	hostingOrganizationOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Hostingorganization", blank=True, null=True, help_text='''The organization (airline, travelers' club, etc.) the membership is made with.''', related_name="programmembership_hostingorganization_organization")
	membershipNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Membershipnumber", blank=True, null=True, help_text='''A unique identifier for the membership.''', related_name="programmembership_membershipnumber_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ProgramMembership'
		verbose_name_plural = 'ProgramMembership'


class PrependAction(models.Model):

	insertAction = models.ForeignKey('InsertAction', on_delete=models.CASCADE, verbose_name="Insertaction", blank=True, null=True, help_text='''The act of adding at a specific location in an ordered collection.''', related_name="prependaction_insertaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PrependAction'
		verbose_name_plural = 'PrependAction'


class SoftwareSourceCode(models.Model):

	runtimePlatformText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Runtimeplatform", blank=True, null=True, help_text='''Runtime platform or script interpreter dependencies (Example - Java v1, Python2.3, .Net Framework 3.0).''', related_name="softwaresourcecode_runtimeplatform_text")
	codeRepositoryURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Coderepository", blank=True, null=True, help_text='''Link to the repository where the un-compiled, human readable code and related code is located (SVN, github, CodePlex).''', related_name="softwaresourcecode_coderepository_url")
	targetProductSoftwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Targetproduct", blank=True, null=True, help_text='''Target Operating System / Product to which the code applies.  If applies to several versions, just the product name can be used.''', related_name="softwaresourcecode_targetproduct_softwareapplication")
	codeSampleTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Codesampletype", blank=True, null=True, help_text='''Full (compile ready) solution, code snippet, inline code, scripts, template.''', related_name="softwaresourcecode_codesampletype_text")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="softwaresourcecode_creativework")
	programmingLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Programminglanguage", blank=True, null=True, help_text='''The computer programming language.''', related_name="softwaresourcecode_programminglanguage_text")
	programmingLanguageComputerLanguage = models.ForeignKey('ComputerLanguage', on_delete=models.CASCADE, verbose_name="Programminglanguage", blank=True, null=True, help_text='''The computer programming language.''', related_name="softwaresourcecode_programminglanguage_computerlanguage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SoftwareSourceCode'
		verbose_name_plural = 'SoftwareSourceCode'


class AudioObject(models.Model):

	mediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="Mediaobject", blank=True, null=True, help_text='''An image, video, or audio object embedded in a web page. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).''', related_name="audioobject_mediaobject")
	transcriptText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Transcript", blank=True, null=True, help_text='''If this MediaObject is an AudioObject or VideoObject, the transcript of that object.''', related_name="audioobject_transcript_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AudioObject'
		verbose_name_plural = 'AudioObject'


class EngineSpecification(models.Model):

	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="enginespecification_structuredvalue")
	fuelTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Fueltype", blank=True, null=True, help_text='''The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.''', related_name="enginespecification_fueltype_text")
	fuelTypeQualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Fueltype", blank=True, null=True, help_text='''The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.''', related_name="enginespecification_fueltype_qualitativevalue")
	fuelTypeURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Fueltype", blank=True, null=True, help_text='''The type of fuel suitable for the engine or engines of the vehicle. If the vehicle has only one engine, this property can be attached directly to the vehicle.''', related_name="enginespecification_fueltype_url")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EngineSpecification'
		verbose_name_plural = 'EngineSpecification'


class SeaBodyOfWater(models.Model):

	bodyOfWater = models.ForeignKey('BodyOfWater', on_delete=models.CASCADE, verbose_name="Bodyofwater", blank=True, null=True, help_text='''A body of water, such as a sea, ocean, or lake.''', related_name="seabodyofwater_bodyofwater")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SeaBodyOfWater'
		verbose_name_plural = 'SeaBodyOfWater'


class ScheduleAction(models.Model):

	planAction = models.ForeignKey('PlanAction', on_delete=models.CASCADE, verbose_name="Planaction", blank=True, null=True, help_text='''The act of planning the execution of an event/task/action/reservation/plan to a future date.''', related_name="scheduleaction_planaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ScheduleAction'
		verbose_name_plural = 'ScheduleAction'


class TakeAction(models.Model):

	transferAction = models.ForeignKey('TransferAction', on_delete=models.CASCADE, verbose_name="Transferaction", blank=True, null=True, help_text='''The act of transferring/moving (abstract or concrete) animate or inanimate objects from one place to another.''', related_name="takeaction_transferaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TakeAction'
		verbose_name_plural = 'TakeAction'


class SteeringPositionValue(models.Model):

	qualitativeValue = models.ForeignKey('QualitativeValue', on_delete=models.CASCADE, verbose_name="Qualitativevalue", blank=True, null=True, help_text='''A predefined value for a product characteristic, e.g. the power cord plug type "US" or the garment sizes "S", "M", "L", and "XL".''', related_name="steeringpositionvalue_qualitativevalue")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SteeringPositionValue'
		verbose_name_plural = 'SteeringPositionValue'


class SportsActivityLocation(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="sportsactivitylocation_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SportsActivityLocation'
		verbose_name_plural = 'SportsActivityLocation'


class AutoPartsStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="autopartsstore_store")
	automotiveBusiness = models.ForeignKey('AutomotiveBusiness', on_delete=models.CASCADE, verbose_name="Automotivebusiness", blank=True, null=True, help_text='''Car repair, sales, or parts.''', related_name="autopartsstore_automotivebusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AutoPartsStore'
		verbose_name_plural = 'AutoPartsStore'


class ActivateAction(models.Model):

	controlAction = models.ForeignKey('ControlAction', on_delete=models.CASCADE, verbose_name="Controlaction", blank=True, null=True, help_text='''An agent controls a device or application.''', related_name="activateaction_controlaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ActivateAction'
		verbose_name_plural = 'ActivateAction'


class Dataset(models.Model):

	spatialPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Spatial", blank=True, null=True, help_text='''The range of spatial applicability of a dataset, e.g. for a dataset of New York weather, the state of New York.''', related_name="dataset_spatial_place")
	includedInDataCatalogDataCatalog = models.ForeignKey('DataCatalog', on_delete=models.CASCADE, verbose_name="Includedindatacatalog", blank=True, null=True, help_text='''A data catalog which contains this dataset.''', related_name="dataset_includedindatacatalog_datacatalog")
	datasetTimeIntervalDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datasettimeinterval", blank=True, null=True, help_text='''The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the year 2011 (in ISO 8601 time interval format).''', related_name="dataset_datasettimeinterval_datetime")
	distributionDataDownload = models.ForeignKey('DataDownload', on_delete=models.CASCADE, verbose_name="Distribution", blank=True, null=True, help_text='''A downloadable form of this dataset, at a specific location, in a specific format.''', related_name="dataset_distribution_datadownload")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="dataset_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Dataset'
		verbose_name_plural = 'Dataset'


class HVACBusiness(models.Model):

	homeAndConstructionBusiness = models.ForeignKey('HomeAndConstructionBusiness', on_delete=models.CASCADE, verbose_name="Homeandconstructionbusiness", blank=True, null=True, help_text='''A construction business.
        <br><br>
        A HomeAndConstructionBusiness is a LocalBusiness that provides services around homes and buildings.
          <br><br>
          As a <a href="/LocalBusiness">LocalBusiness</a> it can be
          described as a <a href="/provider">provider</a> of one or more
          <a href="/Service">Service(s)</a>.
      ''', related_name="hvacbusiness_homeandconstructionbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HVACBusiness'
		verbose_name_plural = 'HVACBusiness'


class UseAction(models.Model):

	consumeAction = models.ForeignKey('ConsumeAction', on_delete=models.CASCADE, verbose_name="Consumeaction", blank=True, null=True, help_text='''The act of ingesting information/resources/food.''', related_name="useaction_consumeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UseAction'
		verbose_name_plural = 'UseAction'


class RadioSeason(models.Model):

	creativeWorkSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Creativeworkseason", blank=True, null=True, help_text='''A media season e.g. tv, radio, video game etc.''', related_name="radioseason_creativeworkseason")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RadioSeason'
		verbose_name_plural = 'RadioSeason'


class DaySpa(models.Model):

	healthAndBeautyBusiness = models.ForeignKey('HealthAndBeautyBusiness', on_delete=models.CASCADE, verbose_name="Healthandbeautybusiness", blank=True, null=True, help_text='''Health and beauty.''', related_name="dayspa_healthandbeautybusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DaySpa'
		verbose_name_plural = 'DaySpa'


class UnRegisterAction(models.Model):

	interactAction = models.ForeignKey('InteractAction', on_delete=models.CASCADE, verbose_name="Interactaction", blank=True, null=True, help_text='''The act of interacting with another person or organization.''', related_name="unregisteraction_interactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UnRegisterAction'
		verbose_name_plural = 'UnRegisterAction'


class CafeOrCoffeeShop(models.Model):

	foodEstablishment = models.ForeignKey('FoodEstablishment', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A food-related business.''', related_name="cafeorcoffeeshop_foodestablishment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CafeOrCoffeeShop'
		verbose_name_plural = 'CafeOrCoffeeShop'


class Float(models.Model):

	number = models.FloatField(blank=True, null=True, verbose_name="Number", help_text='''Data type: Number.''')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Float'
		verbose_name_plural = 'Float'


class TradeAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="tradeaction_action")
	priceSpecificationPriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Pricespecification", blank=True, null=True, help_text='''One or more detailed price specifications, indicating the unit price and delivery or payment charges.''', related_name="tradeaction_pricespecification_pricespecification")
	priceNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Price", blank=True, null=True, help_text='''The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.
<br />
<br />
      Usage guidelines:
<br />
<ul>
<li>Use the <a href="/priceCurrency">priceCurrency</a> property (with <a href="http://en.wikipedia.org/wiki/ISO_4217#Active_codes">ISO 4217 codes</a> e.g. "USD") instead of
      including <a href="http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign">ambiguous symbols</a> such as '$' in the value.
</li>
<li>
      Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
</li>
<li>
      Note that both <a href="http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute">RDFa</a> and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values
      alongside more human-friendly formatting.
</li>
<li>
      Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols.
</li>
</ul>
      ''', related_name="tradeaction_price_number")
	priceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Price", blank=True, null=True, help_text='''The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.
<br />
<br />
      Usage guidelines:
<br />
<ul>
<li>Use the <a href="/priceCurrency">priceCurrency</a> property (with <a href="http://en.wikipedia.org/wiki/ISO_4217#Active_codes">ISO 4217 codes</a> e.g. "USD") instead of
      including <a href="http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign">ambiguous symbols</a> such as '$' in the value.
</li>
<li>
      Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
</li>
<li>
      Note that both <a href="http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute">RDFa</a> and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values
      alongside more human-friendly formatting.
</li>
<li>
      Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols.
</li>
</ul>
      ''', related_name="tradeaction_price_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TradeAction'
		verbose_name_plural = 'TradeAction'


class GovernmentOffice(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="governmentoffice_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GovernmentOffice'
		verbose_name_plural = 'GovernmentOffice'


class AddAction(models.Model):

	updateAction = models.ForeignKey('UpdateAction', on_delete=models.CASCADE, verbose_name="Updateaction", blank=True, null=True, help_text='''The act of managing by changing/editing the state of the object.''', related_name="addaction_updateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AddAction'
		verbose_name_plural = 'AddAction'


class AuthorizeAction(models.Model):

	allocateAction = models.ForeignKey('AllocateAction', on_delete=models.CASCADE, verbose_name="Allocateaction", blank=True, null=True, help_text='''The act of organizing tasks/objects/events by associating resources to it.''', related_name="authorizeaction_allocateaction")
	recipientPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="authorizeaction_recipient_person")
	recipientAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="authorizeaction_recipient_audience")
	recipientOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="authorizeaction_recipient_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AuthorizeAction'
		verbose_name_plural = 'AuthorizeAction'


class UpdateAction(models.Model):

	targetCollectionThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Targetcollection", blank=True, null=True, help_text='''A sub property of object. The collection target of the action.''', related_name="updateaction_targetcollection_thing")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="updateaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UpdateAction'
		verbose_name_plural = 'UpdateAction'


class WebApplication(models.Model):

	softwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Softwareapplication", blank=True, null=True, help_text='''A software application.''', related_name="webapplication_softwareapplication")
	browserRequirementsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Browserrequirements", blank=True, null=True, help_text='''Specifies browser requirements in human-readable text. For example,"requires HTML5 support".''', related_name="webapplication_browserrequirements_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WebApplication'
		verbose_name_plural = 'WebApplication'


class Volcano(models.Model):

	landform = models.ForeignKey('Landform', on_delete=models.CASCADE, verbose_name="Landform", blank=True, null=True, help_text='''A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.''', related_name="volcano_landform")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Volcano'
		verbose_name_plural = 'Volcano'


class ImageGallery(models.Model):

	collectionPage = models.ForeignKey('CollectionPage', on_delete=models.CASCADE, verbose_name="Collectionpage", blank=True, null=True, help_text='''Web page type: Collection page.''', related_name="imagegallery_collectionpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ImageGallery'
		verbose_name_plural = 'ImageGallery'


class BreadcrumbList(models.Model):

	itemList = models.ForeignKey('ItemList', on_delete=models.CASCADE, verbose_name="Itemlist", blank=True, null=True, help_text='''A list of items of any sort&#x2014;for example, Top 10 Movies About Weathermen, or Top 100 Party Songs. Not to be confused with HTML lists, which are often used only for formatting.''', related_name="breadcrumblist_itemlist")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BreadcrumbList'
		verbose_name_plural = 'BreadcrumbList'


class ResumeAction(models.Model):

	controlAction = models.ForeignKey('ControlAction', on_delete=models.CASCADE, verbose_name="Controlaction", blank=True, null=True, help_text='''An agent controls a device or application.''', related_name="resumeaction_controlaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ResumeAction'
		verbose_name_plural = 'ResumeAction'


class Table(models.Model):

	webPageElement = models.ForeignKey('WebPageElement', on_delete=models.CASCADE, verbose_name="Webpageelement", blank=True, null=True, help_text='''A web page element, like a table or an image.''', related_name="table_webpageelement")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Table'
		verbose_name_plural = 'Table'


class AchieveAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="achieveaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AchieveAction'
		verbose_name_plural = 'AchieveAction'


class BusinessEntityType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="businessentitytype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BusinessEntityType'
		verbose_name_plural = 'BusinessEntityType'


class NutritionInformation(models.Model):

	caloriesEnergy = models.ForeignKey('Energy', on_delete=models.CASCADE, verbose_name="Calories", blank=True, null=True, help_text='''The number of calories.''', related_name="nutritioninformation_calories_energy")
	fiberContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Fibercontent", blank=True, null=True, help_text='''The number of grams of fiber.''', related_name="nutritioninformation_fibercontent_mass")
	sugarContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Sugarcontent", blank=True, null=True, help_text='''The number of grams of sugar.''', related_name="nutritioninformation_sugarcontent_mass")
	proteinContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Proteincontent", blank=True, null=True, help_text='''The number of grams of protein.''', related_name="nutritioninformation_proteincontent_mass")
	fatContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Fatcontent", blank=True, null=True, help_text='''The number of grams of fat.''', related_name="nutritioninformation_fatcontent_mass")
	transFatContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Transfatcontent", blank=True, null=True, help_text='''The number of grams of trans fat.''', related_name="nutritioninformation_transfatcontent_mass")
	carbohydrateContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Carbohydratecontent", blank=True, null=True, help_text='''The number of grams of carbohydrates.''', related_name="nutritioninformation_carbohydratecontent_mass")
	unsaturatedFatContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Unsaturatedfatcontent", blank=True, null=True, help_text='''The number of grams of unsaturated fat.''', related_name="nutritioninformation_unsaturatedfatcontent_mass")
	saturatedFatContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Saturatedfatcontent", blank=True, null=True, help_text='''The number of grams of saturated fat.''', related_name="nutritioninformation_saturatedfatcontent_mass")
	cholesterolContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Cholesterolcontent", blank=True, null=True, help_text='''The number of milligrams of cholesterol.''', related_name="nutritioninformation_cholesterolcontent_mass")
	sodiumContentMass = models.ForeignKey('Mass', on_delete=models.CASCADE, verbose_name="Sodiumcontent", blank=True, null=True, help_text='''The number of milligrams of sodium.''', related_name="nutritioninformation_sodiumcontent_mass")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="nutritioninformation_structuredvalue")
	servingSizeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Servingsize", blank=True, null=True, help_text='''The serving size, in terms of the number of volume or mass.''', related_name="nutritioninformation_servingsize_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'NutritionInformation'
		verbose_name_plural = 'NutritionInformation'


class MusicGroup(models.Model):

	performingGroup = models.ForeignKey('PerformingGroup', on_delete=models.CASCADE, verbose_name="Performinggroup", blank=True, null=True, help_text='''A performance group, such as a band, an orchestra, or a circus.''', related_name="musicgroup_performinggroup")
	genreText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Genre", blank=True, null=True, help_text='''Genre of the creative work or group.''', related_name="musicgroup_genre_text")
	trackItemList = models.ForeignKey('ItemList', on_delete=models.CASCADE, verbose_name="Track", blank=True, null=True, help_text='''A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.''', related_name="musicgroup_track_itemlist")
	trackMusicRecording = models.ForeignKey('MusicRecording', on_delete=models.CASCADE, verbose_name="Track", blank=True, null=True, help_text='''A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.''', related_name="musicgroup_track_musicrecording")
	albumMusicAlbum = models.ForeignKey('MusicAlbum', on_delete=models.CASCADE, verbose_name="Album", blank=True, null=True, help_text='''A music album.''', related_name="musicgroup_album_musicalbum")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicGroup'
		verbose_name_plural = 'MusicGroup'


class City(models.Model):

	administrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Administrativearea", blank=True, null=True, help_text='''A geographical region, typically under the jurisdiction of a particular government.''', related_name="city_administrativearea")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'City'
		verbose_name_plural = 'City'


class ScreeningEvent(models.Model):

	subtitleLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Subtitlelanguage", blank=True, null=True, help_text='''Languages in which subtitles/captions are available, in <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard format.</a>''', related_name="screeningevent_subtitlelanguage_text")
	subtitleLanguageLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Subtitlelanguage", blank=True, null=True, help_text='''Languages in which subtitles/captions are available, in <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard format.</a>''', related_name="screeningevent_subtitlelanguage_language")
	videoFormatText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Videoformat", blank=True, null=True, help_text='''The type of screening or video broadcast used (e.g. IMAX, 3D, SD, HD, etc.).''', related_name="screeningevent_videoformat_text")
	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="screeningevent_event")
	workPresentedMovie = models.ForeignKey('Movie', on_delete=models.CASCADE, verbose_name="Workpresented", blank=True, null=True, help_text='''The movie presented during this event.''', related_name="screeningevent_workpresented_movie")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ScreeningEvent'
		verbose_name_plural = 'ScreeningEvent'


class HighSchool(models.Model):

	educationalOrganization = models.ForeignKey('EducationalOrganization', on_delete=models.CASCADE, verbose_name="Educationalorganization", blank=True, null=True, help_text='''An educational organization.''', related_name="highschool_educationalorganization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HighSchool'
		verbose_name_plural = 'HighSchool'


class DataDownload(models.Model):

	mediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="Mediaobject", blank=True, null=True, help_text='''An image, video, or audio object embedded in a web page. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).''', related_name="datadownload_mediaobject")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DataDownload'
		verbose_name_plural = 'DataDownload'


class Distance(models.Model):

	quantity = models.ForeignKey('Quantity', on_delete=models.CASCADE, verbose_name="Quantity", blank=True, null=True, help_text='''Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 Kg' or '4 milligrams'.''', related_name="distance_quantity")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Distance'
		verbose_name_plural = 'Distance'


class Person(models.Model):

	birthPlacePlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Birthplace", blank=True, null=True, help_text='''The place where the person was born.''', related_name="person_birthplace_place")
	relatedToPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Relatedto", blank=True, null=True, help_text='''The most generic familial relation.''', related_name="person_relatedto_person")
	alumniOfEducationalOrganization = models.ForeignKey('EducationalOrganization', on_delete=models.CASCADE, verbose_name="Alumniof", blank=True, null=True, help_text='''An organization that the person is an alumni of.''', related_name="person_alumniof_educationalorganization")
	alumniOfOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Alumniof", blank=True, null=True, help_text='''An organization that the person is an alumni of.''', related_name="person_alumniof_organization")
	memberOfOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Memberof", blank=True, null=True, help_text='''An Organization (or ProgramMembership) to which this Person or Organization belongs.''', related_name="person_memberof_organization")
	memberOfProgramMembership = models.ForeignKey('ProgramMembership', on_delete=models.CASCADE, verbose_name="Memberof", blank=True, null=True, help_text='''An Organization (or ProgramMembership) to which this Person or Organization belongs.''', related_name="person_memberof_programmembership")
	awardText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Award", blank=True, null=True, help_text='''An award won by or for this item.''', related_name="person_award_text")
	childrenPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Children", blank=True, null=True, help_text='''A child of the person.''', related_name="person_children_person")
	taxIDText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Taxid", blank=True, null=True, help_text='''The Tax / Fiscal ID of the organization or person, e.g. the TIN in the US or the CIF/NIF in Spain.''', related_name="person_taxid_text")
	dunsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Duns", blank=True, null=True, help_text='''The Dun & Bradstreet DUNS number for identifying an organization or business person.''', related_name="person_duns_text")
	isicV4Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isicv4", blank=True, null=True, help_text='''The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.''', related_name="person_isicv4_text")
	honorificSuffixText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Honorificsuffix", blank=True, null=True, help_text='''An honorific suffix preceding a Person's name such as M.D. /PhD/MSCSW.''', related_name="person_honorificsuffix_text")
	worksForOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Worksfor", blank=True, null=True, help_text='''Organizations that the person works for.''', related_name="person_worksfor_organization")
	followsPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Follows", blank=True, null=True, help_text='''The most generic uni-directional social relation.''', related_name="person_follows_person")
	brandBrand = models.ForeignKey('Brand', on_delete=models.CASCADE, verbose_name="Brand", blank=True, null=True, help_text='''The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.''', related_name="person_brand_brand")
	brandOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Brand", blank=True, null=True, help_text='''The brand(s) associated with a product or service, or the brand(s) maintained by an organization or business person.''', related_name="person_brand_organization")
	familyNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Familyname", blank=True, null=True, help_text='''Family name. In the U.S., the last name of an Person. This can be used along with givenName instead of the name property.''', related_name="person_familyname_text")
	homeLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Homelocation", blank=True, null=True, help_text='''A contact location for a person's residence.''', related_name="person_homelocation_place")
	homeLocationContactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Homelocation", blank=True, null=True, help_text='''A contact location for a person's residence.''', related_name="person_homelocation_contactpoint")
	jobTitleText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Jobtitle", blank=True, null=True, help_text='''The job title of the person (for example, Financial Manager).''', related_name="person_jobtitle_text")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", blank=True, null=True, help_text='''The most generic type of item.''', related_name="person_thing")
	addressPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="person_address_postaladdress")
	addressText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="person_address_text")
	deathDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Deathdate", blank=True, null=True, help_text='''Date of death.''', related_name="person_deathdate_date")
	knowsPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Knows", blank=True, null=True, help_text='''The most generic bi-directional social/work relation.''', related_name="person_knows_person")
	affiliationOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Affiliation", blank=True, null=True, help_text='''An organization that this person is affiliated with. For example, a school/university, a club, or a team.''', related_name="person_affiliation_organization")
	contactPointContactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Contactpoint", blank=True, null=True, help_text='''A contact point for a person or organization.''', related_name="person_contactpoint_contactpoint")
	performerInEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Performerin", blank=True, null=True, help_text='''Event that this person is a performer or participant in.''', related_name="person_performerin_event")
	vatIDText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Vatid", blank=True, null=True, help_text='''The Value-added Tax ID of the organization or person.''', related_name="person_vatid_text")
	genderGenderType = models.ForeignKey('GenderType', on_delete=models.CASCADE, verbose_name="Gender", blank=True, null=True, help_text='''Gender of the person. While http://schema.org/Male and http://schema.org/Female may be used, text strings are also acceptable for people who do not identify as a binary gender.''', related_name="person_gender_gendertype")
	genderText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gender", blank=True, null=True, help_text='''Gender of the person. While http://schema.org/Male and http://schema.org/Female may be used, text strings are also acceptable for people who do not identify as a binary gender.''', related_name="person_gender_text")
	seeksDemand = models.ForeignKey('Demand', on_delete=models.CASCADE, verbose_name="Seeks", blank=True, null=True, help_text='''A pointer to products or services sought by the organization or person (demand).''', related_name="person_seeks_demand")
	nationalityCountry = models.ForeignKey('Country', on_delete=models.CASCADE, verbose_name="Nationality", blank=True, null=True, help_text='''Nationality of the person.''', related_name="person_nationality_country")
	sponsorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Sponsor", blank=True, null=True, help_text='''A person or organization that supports a thing through a pledge, promise, or financial contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.''', related_name="person_sponsor_person")
	sponsorOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Sponsor", blank=True, null=True, help_text='''A person or organization that supports a thing through a pledge, promise, or financial contribution. e.g. a sponsor of a Medical Study or a corporate sponsor of an event.''', related_name="person_sponsor_organization")
	weightQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Weight", blank=True, null=True, help_text='''The weight of the product or person.''', related_name="person_weight_quantitativevalue")
	emailText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Email", blank=True, null=True, help_text='''Email address.''', related_name="person_email_text")
	givenNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Givenname", blank=True, null=True, help_text='''Given name. In the U.S., the first name of a Person. This can be used along with familyName instead of the name property.''', related_name="person_givenname_text")
	faxNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Faxnumber", blank=True, null=True, help_text='''The fax number.''', related_name="person_faxnumber_text")
	hasPOSPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Haspos", blank=True, null=True, help_text='''Points-of-Sales operated by the organization or person.''', related_name="person_haspos_place")
	siblingPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Sibling", blank=True, null=True, help_text='''A sibling of the person.''', related_name="person_sibling_person")
	hasOfferCatalogOfferCatalog = models.ForeignKey('OfferCatalog', on_delete=models.CASCADE, verbose_name="Hasoffercatalog", blank=True, null=True, help_text='''Indicates an OfferCatalog listing for this Organization, Person, or Service.''', related_name="person_hasoffercatalog_offercatalog")
	telephoneText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Telephone", blank=True, null=True, help_text='''The telephone number.''', related_name="person_telephone_text")
	deathPlacePlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Deathplace", blank=True, null=True, help_text='''The place where the person died.''', related_name="person_deathplace_place")
	additionalNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Additionalname", blank=True, null=True, help_text='''An additional name for a Person, can be used for a middle name.''', related_name="person_additionalname_text")
	colleaguePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Colleague", blank=True, null=True, help_text='''A colleague of the person.''', related_name="person_colleague_person")
	colleagueURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Colleague", blank=True, null=True, help_text='''A colleague of the person.''', related_name="person_colleague_url")
	netWorthPriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Networth", blank=True, null=True, help_text='''The total financial value of the organization or person as calculated by subtracting assets from liabilities.''', related_name="person_networth_pricespecification")
	netWorthMonetaryAmount = models.ForeignKey('MonetaryAmount', on_delete=models.CASCADE, verbose_name="Networth", blank=True, null=True, help_text='''The total financial value of the organization or person as calculated by subtracting assets from liabilities.''', related_name="person_networth_monetaryamount")
	honorificPrefixText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Honorificprefix", blank=True, null=True, help_text='''An honorific prefix preceding a Person's name such as Dr/Mrs/Mr.''', related_name="person_honorificprefix_text")
	spousePerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Spouse", blank=True, null=True, help_text='''The person's spouse.''', related_name="person_spouse_person")
	ownsOwnershipInfo = models.ForeignKey('OwnershipInfo', on_delete=models.CASCADE, verbose_name="Owns", blank=True, null=True, help_text='''Products owned by the organization or person.''', related_name="person_owns_ownershipinfo")
	ownsProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Owns", blank=True, null=True, help_text='''Products owned by the organization or person.''', related_name="person_owns_product")
	naicsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Naics", blank=True, null=True, help_text='''The North American Industry Classification System (NAICS) code for a particular organization or business person.''', related_name="person_naics_text")
	birthDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Birthdate", blank=True, null=True, help_text='''Date of birth.''', related_name="person_birthdate_date")
	workLocationContactPoint = models.ForeignKey('ContactPoint', on_delete=models.CASCADE, verbose_name="Worklocation", blank=True, null=True, help_text='''A contact location for a person's place of work.''', related_name="person_worklocation_contactpoint")
	workLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Worklocation", blank=True, null=True, help_text='''A contact location for a person's place of work.''', related_name="person_worklocation_place")
	heightQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Height", blank=True, null=True, help_text='''The height of the item.''', related_name="person_height_quantitativevalue")
	heightDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Height", blank=True, null=True, help_text='''The height of the item.''', related_name="person_height_distance")
	makesOfferOffer = models.ForeignKey('Offer', on_delete=models.CASCADE, verbose_name="Makesoffer", blank=True, null=True, help_text='''A pointer to products or services offered by the organization or person.''', related_name="person_makesoffer_offer")
	parentPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Parent", blank=True, null=True, help_text='''A parent of this person.''', related_name="person_parent_person")
	globalLocationNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Globallocationnumber", blank=True, null=True, help_text='''The <a href="http://www.gs1.org/gln">Global Location Number</a> (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.''', related_name="person_globallocationnumber_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Person'
		verbose_name_plural = 'Person'


class JobPosting(models.Model):

	baseSalaryNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Basesalary", blank=True, null=True, help_text='''The base salary of the job or of an employee in an EmployeeRole.''', related_name="jobposting_basesalary_number")
	baseSalaryMonetaryAmount = models.ForeignKey('MonetaryAmount', on_delete=models.CASCADE, verbose_name="Basesalary", blank=True, null=True, help_text='''The base salary of the job or of an employee in an EmployeeRole.''', related_name="jobposting_basesalary_monetaryamount")
	baseSalaryPriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Basesalary", blank=True, null=True, help_text='''The base salary of the job or of an employee in an EmployeeRole.''', related_name="jobposting_basesalary_pricespecification")
	jobBenefitsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Jobbenefits", blank=True, null=True, help_text='''Description of benefits associated with the job.''', related_name="jobposting_jobbenefits_text")
	experienceRequirementsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Experiencerequirements", blank=True, null=True, help_text='''Description of skills and experience needed for the position.''', related_name="jobposting_experiencerequirements_text")
	hiringOrganizationOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Hiringorganization", blank=True, null=True, help_text='''Organization offering the job position.''', related_name="jobposting_hiringorganization_organization")
	employmentTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Employmenttype", blank=True, null=True, help_text='''Type of employment (e.g. full-time, part-time, contract, temporary, seasonal, internship).''', related_name="jobposting_employmenttype_text")
	workHoursText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Workhours", blank=True, null=True, help_text='''The typical working hours for this job (e.g. 1st shift, night shift, 8am-5pm).''', related_name="jobposting_workhours_text")
	responsibilitiesText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Responsibilities", blank=True, null=True, help_text='''Responsibilities associated with this role.''', related_name="jobposting_responsibilities_text")
	skillsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Skills", blank=True, null=True, help_text='''Skills required to fulfill this role.''', related_name="jobposting_skills_text")
	qualificationsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Qualifications", blank=True, null=True, help_text='''Specific qualifications required for this role.''', related_name="jobposting_qualifications_text")
	occupationalCategoryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Occupationalcategory", blank=True, null=True, help_text='''Category or categories describing the job. Use BLS O*NET-SOC taxonomy: http://www.onetcenter.org/taxonomy.html. Ideally includes textual label and formal code, with the property repeated for each applicable value.''', related_name="jobposting_occupationalcategory_text")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="jobposting_intangible")
	validThroughDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", blank=True, null=True, help_text='''The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.''', related_name="jobposting_validthrough_datetime")
	titleText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Title", blank=True, null=True, help_text='''The title of the job.''', related_name="jobposting_title_text")
	educationRequirementsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Educationrequirements", blank=True, null=True, help_text='''Educational background needed for the position.''', related_name="jobposting_educationrequirements_text")
	specialCommitmentsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Specialcommitments", blank=True, null=True, help_text='''Any special commitments associated with this job posting. Valid entries include VeteranCommit, MilitarySpouseCommit, etc.''', related_name="jobposting_specialcommitments_text")
	incentiveCompensationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Incentivecompensation", blank=True, null=True, help_text='''Description of bonus and commission compensation aspects of the job.''', related_name="jobposting_incentivecompensation_text")
	salaryCurrencyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Salarycurrency", blank=True, null=True, help_text='''The currency (coded using ISO 4217, http://en.wikipedia.org/wiki/ISO_4217 ) used for the main salary information in this job posting or for this employee.''', related_name="jobposting_salarycurrency_text")
	jobLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Joblocation", blank=True, null=True, help_text='''A (typically single) geographic location associated with the job position.''', related_name="jobposting_joblocation_place")
	industryText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Industry", blank=True, null=True, help_text='''The industry associated with the job position.''', related_name="jobposting_industry_text")
	datePostedDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Dateposted", blank=True, null=True, help_text='''Publication date for the job posting.''', related_name="jobposting_dateposted_date")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'JobPosting'
		verbose_name_plural = 'JobPosting'


class Locksmith(models.Model):

	homeAndConstructionBusiness = models.ForeignKey('HomeAndConstructionBusiness', on_delete=models.CASCADE, verbose_name="Homeandconstructionbusiness", blank=True, null=True, help_text='''A construction business.
        <br><br>
        A HomeAndConstructionBusiness is a LocalBusiness that provides services around homes and buildings.
          <br><br>
          As a <a href="/LocalBusiness">LocalBusiness</a> it can be
          described as a <a href="/provider">provider</a> of one or more
          <a href="/Service">Service(s)</a>.
      ''', related_name="locksmith_homeandconstructionbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Locksmith'
		verbose_name_plural = 'Locksmith'


class DataFeedItem(models.Model):

	dateDeletedDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datedeleted", blank=True, null=True, help_text='''The datetime the item was removed from the DataFeed.''', related_name="datafeeditem_datedeleted_datetime")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="datafeeditem_intangible")
	dateCreatedDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datecreated", blank=True, null=True, help_text='''The date on which the CreativeWork was created or the item was added to a DataFeed.''', related_name="datafeeditem_datecreated_datetime")
	dateCreatedDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Datecreated", blank=True, null=True, help_text='''The date on which the CreativeWork was created or the item was added to a DataFeed.''', related_name="datafeeditem_datecreated_date")
	itemThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Item", blank=True, null=True, help_text='''An entity represented by an entry in a list or data feed (e.g. an 'artist' in a list of 'artists')’.''', related_name="datafeeditem_item_thing")
	dateModifiedDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Datemodified", blank=True, null=True, help_text='''The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.''', related_name="datafeeditem_datemodified_datetime")
	dateModifiedDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Datemodified", blank=True, null=True, help_text='''The date on which the CreativeWork was most recently modified or when the item's entry was modified within a DataFeed.''', related_name="datafeeditem_datemodified_date")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DataFeedItem'
		verbose_name_plural = 'DataFeedItem'


class DateTime(models.Model):

	value = models.DateTimeField(blank=True, null=True, verbose_name="Value", help_text='''A combination of date and time of day in the form [-]CCYY-MM-DDThh:mm:ss[Z|(+|-)hh:mm] (see Chapter 5.4 of ISO 8601).''')

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DateTime'
		verbose_name_plural = 'DateTime'


class DanceEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="danceevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DanceEvent'
		verbose_name_plural = 'DanceEvent'


class Motel(models.Model):

	lodgingBusiness = models.ForeignKey('LodgingBusiness', on_delete=models.CASCADE, verbose_name="Lodgingbusiness", blank=True, null=True, help_text='''A lodging business, such as a motel, hotel, or inn.''', related_name="motel_lodgingbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Motel'
		verbose_name_plural = 'Motel'


class AlignmentObject(models.Model):

	educationalFrameworkText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Educationalframework", blank=True, null=True, help_text='''The framework to which the resource being described is aligned.''', related_name="alignmentobject_educationalframework_text")
	targetNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Targetname", blank=True, null=True, help_text='''The name of a node in an established educational framework.''', related_name="alignmentobject_targetname_text")
	alignmentTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Alignmenttype", blank=True, null=True, help_text='''A category of alignment between the learning resource and the framework node. Recommended values include: 'assesses', 'teaches', 'requires', 'textComplexity', 'readingLevel', 'educationalSubject', and 'educationLevel'.''', related_name="alignmentobject_alignmenttype_text")
	targetDescriptionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Targetdescription", blank=True, null=True, help_text='''The description of a node in an established educational framework.''', related_name="alignmentobject_targetdescription_text")
	targetUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Targeturl", blank=True, null=True, help_text='''The URL of a node in an established educational framework.''', related_name="alignmentobject_targeturl_url")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="alignmentobject_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AlignmentObject'
		verbose_name_plural = 'AlignmentObject'


class Dentist(models.Model):

	professionalService = models.ForeignKey('ProfessionalService', on_delete=models.CASCADE, verbose_name="Professionalservice", blank=True, null=True, help_text='''Original definition: "provider of professional services."
        <br><br>
        The general <a href="/ProfessionalService">ProfessionalService</a> type
        for local businesses was deprecated due to confusion with <a href="/Service">Service</a>.
        For reference, the types that it included were: <a href="/Dentist">Dentist</a>,
        <a href="/AccountingService">AccountingService</a>,
        <a href="/Attorney">Attorney</a>,
        <a href="/Notary">Notary</a>, as well as types for several kinds of
        <a href="/HomeAndConstructionBusiness">HomeAndConstructionBusiness</a>:
        <a href="/Electrician">Electrician</a>,
        <a href="/GeneralContractor">GeneralContractor</a>,
        <a href="/HousePainter">HousePainter</a>,
        <a href="/Locksmith">Locksmith</a>,
        <a href="/Plumber">Plumber</a>,
        <a href="/Plumber">RoofingContractor</a>.
        <a href="/LegalService">LegalService</a> was introduced as a more
        inclusive supertype of <a href="/Attorney">Attorney</a>.

      ''', related_name="dentist_professionalservice")
	medicalOrganization = models.ForeignKey('MedicalOrganization', on_delete=models.CASCADE, verbose_name="Medicalorganization", blank=True, null=True, help_text='''A medical organization (physical or not), such as hospital, institution or clinic.''', related_name="dentist_medicalorganization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Dentist'
		verbose_name_plural = 'Dentist'


class Place(models.Model):

	additionalPropertyPropertyValue = models.ForeignKey('PropertyValue', on_delete=models.CASCADE, verbose_name="Additionalproperty", blank=True, null=True, help_text='''A property-value pair representing an additional characteristics of the entitity, e.g. a product feature or another characteristic for which there is no matching property in schema.org. <br /><br />

Note: Publishers should be aware that applications designed to use specific schema.org properties (e.g. http://schema.org/width, http://schema.org/color, http://schema.org/gtin13, ...) will typically expect such data to be provided using those properties, rather than using the generic property/value mechanism.
''', related_name="place_additionalproperty_propertyvalue")
	isicV4Text = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Isicv4", blank=True, null=True, help_text='''The International Standard of Industrial Classification of All Economic Activities (ISIC), Revision 4 code for a particular organization, business person, or place.''', related_name="place_isicv4_text")
	containsPlacePlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Containsplace", blank=True, null=True, help_text='''The basic containment relation between a place and another that it contains.''', related_name="place_containsplace_place")
	eventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''Upcoming or past event associated with this place, organization, or action.''', related_name="place_event_event")
	reviewReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", blank=True, null=True, help_text='''A review of the item.''', related_name="place_review_review")
	containedInPlacePlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Containedinplace", blank=True, null=True, help_text='''The basic containment relation between a place and one that contains it.''', related_name="place_containedinplace_place")
	photoImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Photo", blank=True, null=True, help_text='''A photograph of this place.''', related_name="place_photo_imageobject")
	photoPhotograph = models.ForeignKey('Photograph', on_delete=models.CASCADE, verbose_name="Photo", blank=True, null=True, help_text='''A photograph of this place.''', related_name="place_photo_photograph")
	addressPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="place_address_postaladdress")
	addressText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Address", blank=True, null=True, help_text='''Physical address of the item.''', related_name="place_address_text")
	geoGeoCoordinates = models.ForeignKey('GeoCoordinates', on_delete=models.CASCADE, verbose_name="Geo", blank=True, null=True, help_text='''The geo coordinates of the place.''', related_name="place_geo_geocoordinates")
	geoGeoShape = models.ForeignKey('GeoShape', on_delete=models.CASCADE, verbose_name="Geo", blank=True, null=True, help_text='''The geo coordinates of the place.''', related_name="place_geo_geoshape")
	openingHoursSpecificationOpeningHoursSpecification = models.ForeignKey('OpeningHoursSpecification', on_delete=models.CASCADE, verbose_name="Openinghoursspecification", blank=True, null=True, help_text='''The opening hours of a certain place.''', related_name="place_openinghoursspecification_openinghoursspecification")
	hasMapMap = models.ForeignKey('Map', on_delete=models.CASCADE, verbose_name="Hasmap", blank=True, null=True, help_text='''A URL to a map of the place.''', related_name="place_hasmap_map")
	hasMapURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Hasmap", blank=True, null=True, help_text='''A URL to a map of the place.''', related_name="place_hasmap_url")
	thing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Thing", blank=True, null=True, help_text='''The most generic type of item.''', related_name="place_thing")
	faxNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Faxnumber", blank=True, null=True, help_text='''The fax number.''', related_name="place_faxnumber_text")
	telephoneText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Telephone", blank=True, null=True, help_text='''The telephone number.''', related_name="place_telephone_text")
	aggregateRatingAggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", blank=True, null=True, help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="place_aggregaterating_aggregaterating")
	specialOpeningHoursSpecificationOpeningHoursSpecification = models.ForeignKey('OpeningHoursSpecification', on_delete=models.CASCADE, verbose_name="Specialopeninghoursspecification", blank=True, null=True, help_text='''The special opening hours of a certain place.
<br />
Use this to explicitly override general opening hours brought in scope by <a href="/openingHoursSpecification">openingHoursSpecification</a> or <a href="/openingHours">openingHours</a>.
      ''', related_name="place_specialopeninghoursspecification_openinghoursspecification")
	branchCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Branchcode", blank=True, null=True, help_text='''A short textual code (also called "store code") that uniquely identifies a place of business. The code is typically assigned by the parentOrganization and used in structured URLs.
<br /><br /> For example, in the URL http://www.starbucks.co.uk/store-locator/etc/detail/3047 the code "3047" is a branchCode for a particular branch.
      ''', related_name="place_branchcode_text")
	logoURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="place_logo_url")
	logoImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="place_logo_imageobject")
	globalLocationNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Globallocationnumber", blank=True, null=True, help_text='''The <a href="http://www.gs1.org/gln">Global Location Number</a> (GLN, sometimes also referred to as International Location Number or ILN) of the respective organization, person, or place. The GLN is a 13-digit number used to identify parties and physical locations.''', related_name="place_globallocationnumber_text")

	def __str__(self):
		return str(self.thing.nameText.value)

	class Meta:
		verbose_name = 'Place'
		verbose_name_plural = 'Place'


class Blog(models.Model):

	blogPostBlogPosting = models.ForeignKey('BlogPosting', on_delete=models.CASCADE, verbose_name="Blogpost", blank=True, null=True, help_text='''A posting that is part of this blog.''', related_name="blog_blogpost_blogposting")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="blog_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Blog'
		verbose_name_plural = 'Blog'


class Mass(models.Model):

	quantity = models.ForeignKey('Quantity', on_delete=models.CASCADE, verbose_name="Quantity", blank=True, null=True, help_text='''Quantities such as distance, time, mass, weight, etc. Particular instances of say Mass are entities like '3 Kg' or '4 milligrams'.''', related_name="mass_quantity")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Mass'
		verbose_name_plural = 'Mass'


class CommunicateAction(models.Model):

	interactAction = models.ForeignKey('InteractAction', on_delete=models.CASCADE, verbose_name="Interactaction", blank=True, null=True, help_text='''The act of interacting with another person or organization.''', related_name="communicateaction_interactaction")
	aboutThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="About", blank=True, null=True, help_text='''The subject matter of the content.''', related_name="communicateaction_about_thing")
	inLanguageLanguage = models.ForeignKey('Language', on_delete=models.CASCADE, verbose_name="Inlanguage", blank=True, null=True, help_text='''The language of the content or performance or used in an action. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[availableLanguage]].''', related_name="communicateaction_inlanguage_language")
	inLanguageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Inlanguage", blank=True, null=True, help_text='''The language of the content or performance or used in an action. Please use one of the language codes from the <a href='http://tools.ietf.org/html/bcp47'>IETF BCP 47 standard</a>. See also [[availableLanguage]].''', related_name="communicateaction_inlanguage_text")
	recipientPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="communicateaction_recipient_person")
	recipientAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="communicateaction_recipient_audience")
	recipientOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="communicateaction_recipient_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CommunicateAction'
		verbose_name_plural = 'CommunicateAction'


class ProfilePage(models.Model):

	webPage = models.ForeignKey('WebPage', on_delete=models.CASCADE, verbose_name="Webpage", blank=True, null=True, help_text='''A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.''', related_name="profilepage_webpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ProfilePage'
		verbose_name_plural = 'ProfilePage'


class MapCategoryType(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="mapcategorytype_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MapCategoryType'
		verbose_name_plural = 'MapCategoryType'


class MusicStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="musicstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicStore'
		verbose_name_plural = 'MusicStore'


class FinancialService(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="financialservice_localbusiness")
	feesAndCommissionsSpecificationURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Feesandcommissionsspecification", blank=True, null=True, help_text='''Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.''', related_name="financialservice_feesandcommissionsspecification_url")
	feesAndCommissionsSpecificationText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Feesandcommissionsspecification", blank=True, null=True, help_text='''Description of fees, commissions, and other terms applied either to a class of financial product, or by a financial service organization.''', related_name="financialservice_feesandcommissionsspecification_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FinancialService'
		verbose_name_plural = 'FinancialService'


class TrainTrip(models.Model):

	departureStationTrainStation = models.ForeignKey('TrainStation', on_delete=models.CASCADE, verbose_name="Departurestation", blank=True, null=True, help_text='''The station from which the train departs.''', related_name="traintrip_departurestation_trainstation")
	arrivalStationTrainStation = models.ForeignKey('TrainStation', on_delete=models.CASCADE, verbose_name="Arrivalstation", blank=True, null=True, help_text='''The station where the train trip ends.''', related_name="traintrip_arrivalstation_trainstation")
	departureTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Departuretime", blank=True, null=True, help_text='''The expected departure time.''', related_name="traintrip_departuretime_datetime")
	arrivalTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Arrivaltime", blank=True, null=True, help_text='''The expected arrival time.''', related_name="traintrip_arrivaltime_datetime")
	trainNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Trainname", blank=True, null=True, help_text='''The name of the train (e.g. The Orient Express).''', related_name="traintrip_trainname_text")
	departurePlatformText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Departureplatform", blank=True, null=True, help_text='''The platform from which the train departs.''', related_name="traintrip_departureplatform_text")
	providerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="traintrip_provider_organization")
	providerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Provider", blank=True, null=True, help_text='''The service provider, service operator, or service performer; the goods producer. Another party (a seller) may offer those services or goods on behalf of the provider. A provider may also serve as the seller.''', related_name="traintrip_provider_person")
	arrivalPlatformText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Arrivalplatform", blank=True, null=True, help_text='''The platform where the train arrives.''', related_name="traintrip_arrivalplatform_text")
	trainNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Trainnumber", blank=True, null=True, help_text='''The unique identifier for the train.''', related_name="traintrip_trainnumber_text")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="traintrip_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TrainTrip'
		verbose_name_plural = 'TrainTrip'


class AboutPage(models.Model):

	webPage = models.ForeignKey('WebPage', on_delete=models.CASCADE, verbose_name="Webpage", blank=True, null=True, help_text='''A web page. Every web page is implicitly assumed to be declared to be of type WebPage, so the various properties about that webpage, such as <code>breadcrumb</code> may be used. We recommend explicit declaration if these properties are specified, but if they are found outside of an itemscope, they will be assumed to be about the page.''', related_name="aboutpage_webpage")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AboutPage'
		verbose_name_plural = 'AboutPage'


class EntertainmentBusiness(models.Model):

	localBusiness = models.ForeignKey('LocalBusiness', on_delete=models.CASCADE, verbose_name="Localbusiness", blank=True, null=True, help_text='''A particular physical business or branch of an organization. Examples of LocalBusiness include a restaurant, a particular branch of a restaurant chain, a branch of a bank, a medical practice, a club, a bowling alley, etc.''', related_name="entertainmentbusiness_localbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EntertainmentBusiness'
		verbose_name_plural = 'EntertainmentBusiness'


class SubwayStation(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="subwaystation_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SubwayStation'
		verbose_name_plural = 'SubwayStation'


class MobileApplication(models.Model):

	softwareApplication = models.ForeignKey('SoftwareApplication', on_delete=models.CASCADE, verbose_name="Softwareapplication", blank=True, null=True, help_text='''A software application.''', related_name="mobileapplication_softwareapplication")
	carrierRequirementsText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Carrierrequirements", blank=True, null=True, help_text='''Specifies specific carrier(s) requirements for the application (e.g. an application may only work on a specific carrier network).''', related_name="mobileapplication_carrierrequirements_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MobileApplication'
		verbose_name_plural = 'MobileApplication'


class SingleFamilyResidence(models.Model):

	residence = models.ForeignKey('Residence', on_delete=models.CASCADE, verbose_name="Residence", blank=True, null=True, help_text='''The place where a person lives.''', related_name="singlefamilyresidence_residence")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SingleFamilyResidence'
		verbose_name_plural = 'SingleFamilyResidence'


class UserLikes(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserLikes'
		verbose_name_plural = 'UserLikes'


class PublicSwimmingPool(models.Model):

	sportsActivityLocation = models.ForeignKey('SportsActivityLocation', on_delete=models.CASCADE, verbose_name="Sportsactivitylocation", blank=True, null=True, help_text='''A sports location, such as a playing field.''', related_name="publicswimmingpool_sportsactivitylocation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PublicSwimmingPool'
		verbose_name_plural = 'PublicSwimmingPool'


class MusicRelease(models.Model):

	creditedToPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Creditedto", blank=True, null=True, help_text='''The group the release is credited to if different than the byArtist. For example, Red and Blue is credited to "Stefani Germanotta Band", but by Lady Gaga.''', related_name="musicrelease_creditedto_person")
	creditedToOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Creditedto", blank=True, null=True, help_text='''The group the release is credited to if different than the byArtist. For example, Red and Blue is credited to "Stefani Germanotta Band", but by Lady Gaga.''', related_name="musicrelease_creditedto_organization")
	recordLabelOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recordlabel", blank=True, null=True, help_text='''The label that issued the release.''', related_name="musicrelease_recordlabel_organization")
	musicReleaseFormatMusicReleaseFormatType = models.ForeignKey('MusicReleaseFormatType', on_delete=models.CASCADE, verbose_name="Musicreleaseformat", blank=True, null=True, help_text='''Format of this release (the type of recording media used, ie. compact disc, digital media, LP, etc.).''', related_name="musicrelease_musicreleaseformat_musicreleaseformattype")
	catalogNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Catalognumber", blank=True, null=True, help_text='''The catalog number for the release.''', related_name="musicrelease_catalognumber_text")
	durationDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", blank=True, null=True, help_text='''The duration of the item (movie, audio recording, event, etc.) in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>.''', related_name="musicrelease_duration_duration")
	musicPlaylist = models.ForeignKey('MusicPlaylist', on_delete=models.CASCADE, verbose_name="Musicplaylist", blank=True, null=True, help_text='''A collection of music tracks in playlist form.''', related_name="musicrelease_musicplaylist")
	releaseOfMusicAlbum = models.ForeignKey('MusicAlbum', on_delete=models.CASCADE, verbose_name="Releaseof", blank=True, null=True, help_text='''The album this is a release of.''', related_name="musicrelease_releaseof_musicalbum")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicRelease'
		verbose_name_plural = 'MusicRelease'


class ScholarlyArticle(models.Model):

	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", blank=True, null=True, help_text='''An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.

      <br/><br/>See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.''', related_name="scholarlyarticle_article")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ScholarlyArticle'
		verbose_name_plural = 'ScholarlyArticle'


class ArriveAction(models.Model):

	moveAction = models.ForeignKey('MoveAction', on_delete=models.CASCADE, verbose_name="Moveaction", blank=True, null=True, help_text='''The act of an agent relocating to a place.<p>Related actions:</p><ul><li><a href="http://schema.org/TransferAction">TransferAction</a>: Unlike TransferAction, the subject of the move is a living Person or Organization rather than an inanimate object</li></ul>.''', related_name="arriveaction_moveaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ArriveAction'
		verbose_name_plural = 'ArriveAction'


class AutoRepair(models.Model):

	automotiveBusiness = models.ForeignKey('AutomotiveBusiness', on_delete=models.CASCADE, verbose_name="Automotivebusiness", blank=True, null=True, help_text='''Car repair, sales, or parts.''', related_name="autorepair_automotivebusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AutoRepair'
		verbose_name_plural = 'AutoRepair'


class MediaObject(models.Model):

	expiresDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Expires", blank=True, null=True, help_text='''Date the content expires and is no longer useful or available. Useful for videos.''', related_name="mediaobject_expires_date")
	regionsAllowedPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Regionsallowed", blank=True, null=True, help_text='''The regions where the media is allowed. If not specified, then it's assumed to be allowed everywhere. Specify the countries in <a href='http://en.wikipedia.org/wiki/ISO_3166'>ISO 3166 format</a>.''', related_name="mediaobject_regionsallowed_place")
	encodingFormatText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Encodingformat", blank=True, null=True, help_text='''mp3, mpeg4, etc.''', related_name="mediaobject_encodingformat_text")
	embedUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Embedurl", blank=True, null=True, help_text='''A URL pointing to a player for a specific video. In general, this is the information in the <code>src</code> element of an <code>embed</code> tag and should not be the same as the content of the <code>loc</code> tag.''', related_name="mediaobject_embedurl_url")
	requiresSubscriptionBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Requiressubscription", blank=True, null=True, help_text='''Indicates if use of the media require a subscription  (either paid or free). Allowed values are <code>true</code> or <code>false</code> (note that an earlier version had 'yes', 'no').''', related_name="mediaobject_requiressubscription_boolean")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="mediaobject_creativework")
	playerTypeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Playertype", blank=True, null=True, help_text='''Player type required&#x2014;for example, Flash or Silverlight.''', related_name="mediaobject_playertype_text")
	durationDuration = models.ForeignKey('Duration', on_delete=models.CASCADE, verbose_name="Duration", blank=True, null=True, help_text='''The duration of the item (movie, audio recording, event, etc.) in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>.''', related_name="mediaobject_duration_duration")
	contentUrlURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Contenturl", blank=True, null=True, help_text='''Actual bytes of the media object, for example the image file or video file.''', related_name="mediaobject_contenturl_url")
	widthQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Width", blank=True, null=True, help_text='''The width of the item.''', related_name="mediaobject_width_quantitativevalue")
	widthDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Width", blank=True, null=True, help_text='''The width of the item.''', related_name="mediaobject_width_distance")
	associatedArticleNewsArticle = models.ForeignKey('NewsArticle', on_delete=models.CASCADE, verbose_name="Associatedarticle", blank=True, null=True, help_text='''A NewsArticle associated with the Media Object.''', related_name="mediaobject_associatedarticle_newsarticle")
	contentSizeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Contentsize", blank=True, null=True, help_text='''File size in (mega/kilo) bytes.''', related_name="mediaobject_contentsize_text")
	productionCompanyOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", blank=True, null=True, help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="mediaobject_productioncompany_organization")
	uploadDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Uploaddate", blank=True, null=True, help_text='''Date when this media object was uploaded to this site.''', related_name="mediaobject_uploaddate_date")
	bitrateText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Bitrate", blank=True, null=True, help_text='''The bitrate of the media object.''', related_name="mediaobject_bitrate_text")
	encodesCreativeWorkCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Encodescreativework", blank=True, null=True, help_text='''The CreativeWork encoded by this media object.''', related_name="mediaobject_encodescreativework_creativework")
	heightQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Height", blank=True, null=True, help_text='''The height of the item.''', related_name="mediaobject_height_quantitativevalue")
	heightDistance = models.ForeignKey('Distance', on_delete=models.CASCADE, verbose_name="Height", blank=True, null=True, help_text='''The height of the item.''', related_name="mediaobject_height_distance")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MediaObject'
		verbose_name_plural = 'MediaObject'


class LeaveAction(models.Model):

	interactAction = models.ForeignKey('InteractAction', on_delete=models.CASCADE, verbose_name="Interactaction", blank=True, null=True, help_text='''The act of interacting with another person or organization.''', related_name="leaveaction_interactaction")
	eventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''Upcoming or past event associated with this place, organization, or action.''', related_name="leaveaction_event_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'LeaveAction'
		verbose_name_plural = 'LeaveAction'


class PlayAction(models.Model):

	audienceAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Audience", blank=True, null=True, help_text='''An intended audience, i.e. a group for whom something was created.''', related_name="playaction_audience_audience")
	eventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''Upcoming or past event associated with this place, organization, or action.''', related_name="playaction_event_event")
	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="playaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PlayAction'
		verbose_name_plural = 'PlayAction'


class DataCatalog(models.Model):

	datasetDataset = models.ForeignKey('Dataset', on_delete=models.CASCADE, verbose_name="Dataset", blank=True, null=True, help_text='''A dataset contained in this catalog.''', related_name="datacatalog_dataset_dataset")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="datacatalog_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DataCatalog'
		verbose_name_plural = 'DataCatalog'


class AdministrativeArea(models.Model):

	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", blank=True, null=True, help_text='''Entities that have a somewhat fixed, physical extension.''', related_name="administrativearea_place")

	def __str__(self):
		return str(self.place.thing.nameText.value)

	class Meta:
		verbose_name = 'AdministrativeArea'
		verbose_name_plural = 'AdministrativeArea'


class Aquarium(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="aquarium_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Aquarium'
		verbose_name_plural = 'Aquarium'


class ControlAction(models.Model):

	action = models.ForeignKey('Action', on_delete=models.CASCADE, verbose_name="Action", blank=True, null=True, help_text='''An action performed by a direct agent and indirect participants upon a direct object. Optionally happens at a location with the help of an inanimate instrument. The execution of the action may produce a result. Specific action sub-type documentation specifies the exact expectation of each argument/role.
      <br/><br/>See also <a href="http://blog.schema.org/2014/04/announcing-schemaorg-actions.html">blog post</a>
      and <a href="http://schema.org/docs/actions.html">Actions overview document</a>.''', related_name="controlaction_action")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ControlAction'
		verbose_name_plural = 'ControlAction'


class HomeGoodsStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="homegoodsstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HomeGoodsStore'
		verbose_name_plural = 'HomeGoodsStore'


class ApartmentComplex(models.Model):

	residence = models.ForeignKey('Residence', on_delete=models.CASCADE, verbose_name="Residence", blank=True, null=True, help_text='''The place where a person lives.''', related_name="apartmentcomplex_residence")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ApartmentComplex'
		verbose_name_plural = 'ApartmentComplex'


class CreativeWorkSeries(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="creativeworkseries_creativework")
	startDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Startdate", blank=True, null=True, help_text='''The start date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="creativeworkseries_startdate_date")
	endDateDate = models.ForeignKey('Date', on_delete=models.CASCADE, verbose_name="Enddate", blank=True, null=True, help_text='''The end date and time of the item (in <a href='http://en.wikipedia.org/wiki/ISO_8601'>ISO 8601 date format</a>).''', related_name="creativeworkseries_enddate_date")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CreativeWorkSeries'
		verbose_name_plural = 'CreativeWorkSeries'


class MusicPlaylist(models.Model):

	numTracksInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numtracks", blank=True, null=True, help_text='''The number of tracks in this album or playlist.''', related_name="musicplaylist_numtracks_integer")
	trackItemList = models.ForeignKey('ItemList', on_delete=models.CASCADE, verbose_name="Track", blank=True, null=True, help_text='''A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.''', related_name="musicplaylist_track_itemlist")
	trackMusicRecording = models.ForeignKey('MusicRecording', on_delete=models.CASCADE, verbose_name="Track", blank=True, null=True, help_text='''A music recording (track)&#x2014;usually a single song. If an ItemList is given, the list should contain items of type MusicRecording.''', related_name="musicplaylist_track_musicrecording")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="musicplaylist_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicPlaylist'
		verbose_name_plural = 'MusicPlaylist'


class HinduTemple(models.Model):

	placeOfWorship = models.ForeignKey('PlaceOfWorship', on_delete=models.CASCADE, verbose_name="Placeofworship", blank=True, null=True, help_text='''Place of worship, such as a church, synagogue, or mosque.''', related_name="hindutemple_placeofworship")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'HinduTemple'
		verbose_name_plural = 'HinduTemple'


class RentalCarReservation(models.Model):

	dropoffLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Dropofflocation", blank=True, null=True, help_text='''Where a rental car can be dropped off.''', related_name="rentalcarreservation_dropofflocation_place")
	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", blank=True, null=True, help_text='''Describes a reservation for travel, dining or an event. Some reservations require tickets.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use http://schema.org/Offer.''', related_name="rentalcarreservation_reservation")
	pickupLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Pickuplocation", blank=True, null=True, help_text='''Where a taxi will pick up a passenger or a rental car can be picked up.''', related_name="rentalcarreservation_pickuplocation_place")
	pickupTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Pickuptime", blank=True, null=True, help_text='''When a taxi will pickup a passenger or a rental car can be picked up.''', related_name="rentalcarreservation_pickuptime_datetime")
	dropoffTimeDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Dropofftime", blank=True, null=True, help_text='''When a rental car can be dropped off.''', related_name="rentalcarreservation_dropofftime_datetime")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RentalCarReservation'
		verbose_name_plural = 'RentalCarReservation'


class TattooParlor(models.Model):

	healthAndBeautyBusiness = models.ForeignKey('HealthAndBeautyBusiness', on_delete=models.CASCADE, verbose_name="Healthandbeautybusiness", blank=True, null=True, help_text='''Health and beauty.''', related_name="tattooparlor_healthandbeautybusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TattooParlor'
		verbose_name_plural = 'TattooParlor'


class Church(models.Model):

	placeOfWorship = models.ForeignKey('PlaceOfWorship', on_delete=models.CASCADE, verbose_name="Placeofworship", blank=True, null=True, help_text='''Place of worship, such as a church, synagogue, or mosque.''', related_name="church_placeofworship")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Church'
		verbose_name_plural = 'Church'


class DiscoverAction(models.Model):

	findAction = models.ForeignKey('FindAction', on_delete=models.CASCADE, verbose_name="Findaction", blank=True, null=True, help_text='''The act of finding an object.<p>Related actions:</p><ul><li><a href="http://schema.org/SearchAction">SearchAction</a>: FindAction is generally lead by a SearchAction, but not necessarily</li></ul>.''', related_name="discoveraction_findaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DiscoverAction'
		verbose_name_plural = 'DiscoverAction'


class ComputerLanguage(models.Model):

	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="computerlanguage_intangible")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ComputerLanguage'
		verbose_name_plural = 'ComputerLanguage'


class Brand(models.Model):

	reviewReview = models.ForeignKey('Review', on_delete=models.CASCADE, verbose_name="Review", blank=True, null=True, help_text='''A review of the item.''', related_name="brand_review_review")
	aggregateRatingAggregateRating = models.ForeignKey('AggregateRating', on_delete=models.CASCADE, verbose_name="Aggregaterating", blank=True, null=True, help_text='''The overall rating, based on a collection of reviews or ratings, of the item.''', related_name="brand_aggregaterating_aggregaterating")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="brand_intangible")
	logoURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="brand_logo_url")
	logoImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Logo", blank=True, null=True, help_text='''An associated logo.''', related_name="brand_logo_imageobject")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Brand'
		verbose_name_plural = 'Brand'


class SocialEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="socialevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SocialEvent'
		verbose_name_plural = 'SocialEvent'


class EventReservation(models.Model):

	reservation = models.ForeignKey('Reservation', on_delete=models.CASCADE, verbose_name="Reservation", blank=True, null=True, help_text='''Describes a reservation for travel, dining or an event. Some reservations require tickets.Note: This type is for information about actual reservations, e.g. in confirmation emails or HTML pages with individual confirmations of reservations. For offers of tickets, restaurant reservations, flights, or rental cars, use http://schema.org/Offer.''', related_name="eventreservation_reservation")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EventReservation'
		verbose_name_plural = 'EventReservation'


class RiverBodyOfWater(models.Model):

	bodyOfWater = models.ForeignKey('BodyOfWater', on_delete=models.CASCADE, verbose_name="Bodyofwater", blank=True, null=True, help_text='''A body of water, such as a sea, ocean, or lake.''', related_name="riverbodyofwater_bodyofwater")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RiverBodyOfWater'
		verbose_name_plural = 'RiverBodyOfWater'


class OwnershipInfo(models.Model):

	ownedThroughDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Ownedthrough", blank=True, null=True, help_text='''The date and time of giving up ownership on the product.''', related_name="ownershipinfo_ownedthrough_datetime")
	acquiredFromPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Acquiredfrom", blank=True, null=True, help_text='''The organization or person from which the product was acquired.''', related_name="ownershipinfo_acquiredfrom_person")
	acquiredFromOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Acquiredfrom", blank=True, null=True, help_text='''The organization or person from which the product was acquired.''', related_name="ownershipinfo_acquiredfrom_organization")
	typeOfGoodProduct = models.ForeignKey('Product', on_delete=models.CASCADE, verbose_name="Typeofgood", blank=True, null=True, help_text='''The product that this structured value is referring to.''', related_name="ownershipinfo_typeofgood_product")
	ownedFromDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Ownedfrom", blank=True, null=True, help_text='''The date and time of obtaining the product.''', related_name="ownershipinfo_ownedfrom_datetime")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="ownershipinfo_structuredvalue")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OwnershipInfo'
		verbose_name_plural = 'OwnershipInfo'


class PropertyValueSpecification(models.Model):

	valueMinLengthNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Valueminlength", blank=True, null=True, help_text='''Specifies the minimum allowed range for number of characters in a literal value.''', related_name="propertyvaluespecification_valueminlength_number")
	valuePatternText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Valuepattern", blank=True, null=True, help_text='''Specifies a regular expression for testing literal values according to the HTML spec.''', related_name="propertyvaluespecification_valuepattern_text")
	readonlyValueBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Readonlyvalue", blank=True, null=True, help_text='''Whether or not a property is mutable.  Default is false. Specifying this for a property that also has a value makes it act similar to a "hidden" input in an HTML form.''', related_name="propertyvaluespecification_readonlyvalue_boolean")
	minValueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Minvalue", blank=True, null=True, help_text='''The lower value of some characteristic or property.''', related_name="propertyvaluespecification_minvalue_number")
	stepValueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Stepvalue", blank=True, null=True, help_text='''The stepValue attribute indicates the granularity that is expected (and required) of the value in a PropertyValueSpecification.''', related_name="propertyvaluespecification_stepvalue_number")
	intangible = models.ForeignKey('Intangible', on_delete=models.CASCADE, verbose_name="Intangible", blank=True, null=True, help_text='''A utility class that serves as the umbrella for a number of 'intangible' things such as quantities, structured values, etc.''', related_name="propertyvaluespecification_intangible")
	valueNameText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Valuename", blank=True, null=True, help_text='''Indicates the name of the PropertyValueSpecification to be used in URL templates and form encoding in a manner analogous to HTML's input@name.''', related_name="propertyvaluespecification_valuename_text")
	valueMaxLengthNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Valuemaxlength", blank=True, null=True, help_text='''Specifies the allowed range for number of characters in a literal value.''', related_name="propertyvaluespecification_valuemaxlength_number")
	maxValueNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Maxvalue", blank=True, null=True, help_text='''The upper value of some characteristic or property.''', related_name="propertyvaluespecification_maxvalue_number")
	valueRequiredBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Valuerequired", blank=True, null=True, help_text='''Whether the property must be filled in to complete the action.  Default is false.''', related_name="propertyvaluespecification_valuerequired_boolean")
	multipleValuesBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Multiplevalues", blank=True, null=True, help_text='''Whether multiple values are allowed for the property.  Default is false.''', related_name="propertyvaluespecification_multiplevalues_boolean")
	defaultValueText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Defaultvalue", blank=True, null=True, help_text='''The default value of the input.  For properties that expect a literal, the default is a literal value, for properties that expect an object, it's an ID reference to one of the current values.''', related_name="propertyvaluespecification_defaultvalue_text")
	defaultValueThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Defaultvalue", blank=True, null=True, help_text='''The default value of the input.  For properties that expect a literal, the default is a literal value, for properties that expect an object, it's an ID reference to one of the current values.''', related_name="propertyvaluespecification_defaultvalue_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PropertyValueSpecification'
		verbose_name_plural = 'PropertyValueSpecification'


class Physician(models.Model):

	medicalOrganization = models.ForeignKey('MedicalOrganization', on_delete=models.CASCADE, verbose_name="Medicalorganization", blank=True, null=True, help_text='''A medical organization (physical or not), such as hospital, institution or clinic.''', related_name="physician_medicalorganization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Physician'
		verbose_name_plural = 'Physician'


class GamePlayMode(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="gameplaymode_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GamePlayMode'
		verbose_name_plural = 'GamePlayMode'


class TechArticle(models.Model):

	dependenciesText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Dependencies", blank=True, null=True, help_text='''Prerequisites needed to fulfill steps in article.''', related_name="techarticle_dependencies_text")
	proficiencyLevelText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Proficiencylevel", blank=True, null=True, help_text='''Proficiency needed for this content; expected values: 'Beginner', 'Expert'.''', related_name="techarticle_proficiencylevel_text")
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", blank=True, null=True, help_text='''An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.

      <br/><br/>See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.''', related_name="techarticle_article")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TechArticle'
		verbose_name_plural = 'TechArticle'


class MovieSeries(models.Model):

	musicByMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="movieseries_musicby_musicgroup")
	musicByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="movieseries_musicby_person")
	trailerVideoObject = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", blank=True, null=True, help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="movieseries_trailer_videoobject")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="movieseries_director_person")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="movieseries_actor_person")
	creativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Creativeworkseries", blank=True, null=True, help_text='''
          A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind.
          CreativeWorkSeries are usually organized into some order, often chronological. Unlike <a href="/ItemList">ItemList</a> which
          is a general purpose data structure for lists of things, the emphasis with
          CreativeWorkSeries is on published materials (written e.g. books and periodicals,
          or media such as tv, radio and games).

          <br/><br/>

          Specific subtypes are available for describing <a href="/TVSeries">TVSeries</a>, <a href="/RadioSeries">RadioSeries</a>,
          <a href="/MovieSeries">MovieSeries</a>,
          <a href="/BookSeries">BookSeries</a>,
          <a href="/Periodical">Periodical</a>
          and <a href="/VideoGameSeries">VideoGameSeries</a>. In each case,
          the <a href="/hasPart">hasPart</a> / <a href="/isPartOf">isPartOf</a> properties
          can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely
          just to organize these more specific and practical subtypes.

          <br/><br/>

          It is common for properties applicable to an item from the series to be usefully applied to the containing group.
          Schema.org attempts to anticipate some of these cases, but publishers should be free to apply
          properties of the series parts to the series as a whole wherever they seem appropriate.''', related_name="movieseries_creativeworkseries")
	productionCompanyOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", blank=True, null=True, help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="movieseries_productioncompany_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MovieSeries'
		verbose_name_plural = 'MovieSeries'


class MusicComposition(models.Model):

	musicArrangementMusicComposition = models.ForeignKey('MusicComposition', on_delete=models.CASCADE, verbose_name="Musicarrangement", blank=True, null=True, help_text='''An arrangement derived from the composition.''', related_name="musiccomposition_musicarrangement_musiccomposition")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="musiccomposition_creativework")
	composerPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Composer", blank=True, null=True, help_text='''The person or organization who wrote a composition, or who is the composer of a work performed at some event.''', related_name="musiccomposition_composer_person")
	composerOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Composer", blank=True, null=True, help_text='''The person or organization who wrote a composition, or who is the composer of a work performed at some event.''', related_name="musiccomposition_composer_organization")
	recordedAsMusicRecording = models.ForeignKey('MusicRecording', on_delete=models.CASCADE, verbose_name="Recordedas", blank=True, null=True, help_text='''An audio recording of the work.''', related_name="musiccomposition_recordedas_musicrecording")
	musicCompositionFormText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Musiccompositionform", blank=True, null=True, help_text='''The type of composition (e.g. overture, sonata, symphony, etc.).''', related_name="musiccomposition_musiccompositionform_text")
	musicalKeyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Musicalkey", blank=True, null=True, help_text='''The key, mode, or scale this composition uses.''', related_name="musiccomposition_musicalkey_text")
	iswcCodeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Iswccode", blank=True, null=True, help_text='''The International Standard Musical Work Code for the composition.''', related_name="musiccomposition_iswccode_text")
	includedCompositionMusicComposition = models.ForeignKey('MusicComposition', on_delete=models.CASCADE, verbose_name="Includedcomposition", blank=True, null=True, help_text='''Smaller compositions included in this work (e.g. a movement in a symphony).''', related_name="musiccomposition_includedcomposition_musiccomposition")
	lyricsCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Lyrics", blank=True, null=True, help_text='''The words in the song.''', related_name="musiccomposition_lyrics_creativework")
	firstPerformanceEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Firstperformance", blank=True, null=True, help_text='''The date and place the work was first performed.''', related_name="musiccomposition_firstperformance_event")
	lyricistPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Lyricist", blank=True, null=True, help_text='''The person who wrote the words.''', related_name="musiccomposition_lyricist_person")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicComposition'
		verbose_name_plural = 'MusicComposition'


class NewsArticle(models.Model):

	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", blank=True, null=True, help_text='''An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.

      <br/><br/>See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.''', related_name="newsarticle_article")
	printPageText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Printpage", blank=True, null=True, help_text='''If this NewsArticle appears in print, this field indicates the name of the page on which the article is found. Please note that this field is intended for the exact page name (e.g. A5, B18).''', related_name="newsarticle_printpage_text")
	datelineText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Dateline", blank=True, null=True, help_text='''The location where the NewsArticle was produced.''', related_name="newsarticle_dateline_text")
	printEditionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Printedition", blank=True, null=True, help_text='''The edition of the print product in which the NewsArticle appears.''', related_name="newsarticle_printedition_text")
	printSectionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Printsection", blank=True, null=True, help_text='''If this NewsArticle appears in print, this field indicates the print section in which the article appeared.''', related_name="newsarticle_printsection_text")
	printColumnText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Printcolumn", blank=True, null=True, help_text='''The number of the column in which the NewsArticle appears in the print edition.''', related_name="newsarticle_printcolumn_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'NewsArticle'
		verbose_name_plural = 'NewsArticle'


class WebPageElement(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="webpageelement_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WebPageElement'
		verbose_name_plural = 'WebPageElement'


class SocialMediaPosting(models.Model):

	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", blank=True, null=True, help_text='''An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.

      <br/><br/>See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.''', related_name="socialmediaposting_article")
	sharedContentCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Sharedcontent", blank=True, null=True, help_text='''A CreativeWork such as an image, video, or audio clip shared as part of this posting.''', related_name="socialmediaposting_sharedcontent_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SocialMediaPosting'
		verbose_name_plural = 'SocialMediaPosting'


class DonateAction(models.Model):

	tradeAction = models.ForeignKey('TradeAction', on_delete=models.CASCADE, verbose_name="Tradeaction", blank=True, null=True, help_text='''The act of participating in an exchange of goods and services for monetary compensation. An agent trades an object, product or service with a participant in exchange for a one time or periodic payment.''', related_name="donateaction_tradeaction")
	recipientPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="donateaction_recipient_person")
	recipientAudience = models.ForeignKey('Audience', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="donateaction_recipient_audience")
	recipientOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Recipient", blank=True, null=True, help_text='''A sub property of participant. The participant who is at the receiving end of the action.''', related_name="donateaction_recipient_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DonateAction'
		verbose_name_plural = 'DonateAction'


class State(models.Model):

	administrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Administrativearea", blank=True, null=True, help_text='''A geographical region, typically under the jurisdiction of a particular government.''', related_name="state_administrativearea")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'State'
		verbose_name_plural = 'State'


class Residence(models.Model):

	place = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Place", blank=True, null=True, help_text='''Entities that have a somewhat fixed, physical extension.''', related_name="residence_place")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Residence'
		verbose_name_plural = 'Residence'


class ReplaceAction(models.Model):

	updateAction = models.ForeignKey('UpdateAction', on_delete=models.CASCADE, verbose_name="Updateaction", blank=True, null=True, help_text='''The act of managing by changing/editing the state of the object.''', related_name="replaceaction_updateaction")
	replacerThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Replacer", blank=True, null=True, help_text='''A sub property of object. The object that replaces.''', related_name="replaceaction_replacer_thing")
	replaceeThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Replacee", blank=True, null=True, help_text='''A sub property of object. The object that is being replaced.''', related_name="replaceaction_replacee_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReplaceAction'
		verbose_name_plural = 'ReplaceAction'


class TheaterEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="theaterevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TheaterEvent'
		verbose_name_plural = 'TheaterEvent'


class PaymentCard(models.Model):

	financialProduct = models.ForeignKey('FinancialProduct', on_delete=models.CASCADE, verbose_name="Financialproduct", blank=True, null=True, help_text='''A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.''', related_name="paymentcard_financialproduct")
	paymentMethod = models.ForeignKey('PaymentMethod', on_delete=models.CASCADE, verbose_name="Paymentmethod", blank=True, null=True, help_text='''A payment method is a standardized procedure for transferring the monetary amount for a purchase. Payment methods are characterized by the legal and technical structures used, and by the organization or group carrying out the transaction.
<br />
    Commonly used values:<br />
<br />
    http://purl.org/goodrelations/v1#ByBankTransferInAdvance <br />
    http://purl.org/goodrelations/v1#ByInvoice <br />
    http://purl.org/goodrelations/v1#Cash <br />
    http://purl.org/goodrelations/v1#CheckInAdvance <br />
    http://purl.org/goodrelations/v1#COD <br />
    http://purl.org/goodrelations/v1#DirectDebit <br />
    http://purl.org/goodrelations/v1#GoogleCheckout <br />
    http://purl.org/goodrelations/v1#PayPal <br />
    http://purl.org/goodrelations/v1#PaySwarm <br />
        ''', related_name="paymentcard_paymentmethod")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PaymentCard'
		verbose_name_plural = 'PaymentCard'


class MusicVideoObject(models.Model):

	mediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="Mediaobject", blank=True, null=True, help_text='''An image, video, or audio object embedded in a web page. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).''', related_name="musicvideoobject_mediaobject")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MusicVideoObject'
		verbose_name_plural = 'MusicVideoObject'


class ElementarySchool(models.Model):

	educationalOrganization = models.ForeignKey('EducationalOrganization', on_delete=models.CASCADE, verbose_name="Educationalorganization", blank=True, null=True, help_text='''An educational organization.''', related_name="elementaryschool_educationalorganization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ElementarySchool'
		verbose_name_plural = 'ElementarySchool'


class TheaterGroup(models.Model):

	performingGroup = models.ForeignKey('PerformingGroup', on_delete=models.CASCADE, verbose_name="Performinggroup", blank=True, null=True, help_text='''A performance group, such as a band, an orchestra, or a circus.''', related_name="theatergroup_performinggroup")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TheaterGroup'
		verbose_name_plural = 'TheaterGroup'


class DrinkAction(models.Model):

	consumeAction = models.ForeignKey('ConsumeAction', on_delete=models.CASCADE, verbose_name="Consumeaction", blank=True, null=True, help_text='''The act of ingesting information/resources/food.''', related_name="drinkaction_consumeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DrinkAction'
		verbose_name_plural = 'DrinkAction'


class TVClip(models.Model):

	clip = models.ForeignKey('Clip', on_delete=models.CASCADE, verbose_name="Clip", blank=True, null=True, help_text='''A short TV or radio program or a segment/part of a program.''', related_name="tvclip_clip")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TVClip'
		verbose_name_plural = 'TVClip'


class AutoDealer(models.Model):

	automotiveBusiness = models.ForeignKey('AutomotiveBusiness', on_delete=models.CASCADE, verbose_name="Automotivebusiness", blank=True, null=True, help_text='''Car repair, sales, or parts.''', related_name="autodealer_automotivebusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AutoDealer'
		verbose_name_plural = 'AutoDealer'


class PriceSpecification(models.Model):

	priceCurrencyText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Pricecurrency", blank=True, null=True, help_text='''The currency (in 3-letter ISO 4217 format) of the price or a price component, when attached to PriceSpecification and its subtypes.''', related_name="pricespecification_pricecurrency_text")
	validFromDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validfrom", blank=True, null=True, help_text='''The date when the item becomes valid.''', related_name="pricespecification_validfrom_datetime")
	minPriceNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Minprice", blank=True, null=True, help_text='''The lowest price if the price is a range.''', related_name="pricespecification_minprice_number")
	structuredValue = models.ForeignKey('StructuredValue', on_delete=models.CASCADE, verbose_name="Structuredvalue", blank=True, null=True, help_text='''Structured values are used when the value of a property has a more complex structure than simply being a textual value or a reference to another thing.''', related_name="pricespecification_structuredvalue")
	eligibleTransactionVolumePriceSpecification = models.ForeignKey('PriceSpecification', on_delete=models.CASCADE, verbose_name="Eligibletransactionvolume", blank=True, null=True, help_text='''The transaction volume, in a monetary unit, for which the offer or price specification is valid, e.g. for indicating a minimal purchasing volume, to express free shipping above a certain order volume, or to limit the acceptance of credit cards to purchases to a certain minimal amount.''', related_name="pricespecification_eligibletransactionvolume_pricespecification")
	validThroughDateTime = models.ForeignKey('DateTime', on_delete=models.CASCADE, verbose_name="Validthrough", blank=True, null=True, help_text='''The date after when the item is not valid. For example the end of an offer, salary period, or a period of opening hours.''', related_name="pricespecification_validthrough_datetime")
	priceNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Price", blank=True, null=True, help_text='''The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.
<br />
<br />
      Usage guidelines:
<br />
<ul>
<li>Use the <a href="/priceCurrency">priceCurrency</a> property (with <a href="http://en.wikipedia.org/wiki/ISO_4217#Active_codes">ISO 4217 codes</a> e.g. "USD") instead of
      including <a href="http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign">ambiguous symbols</a> such as '$' in the value.
</li>
<li>
      Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
</li>
<li>
      Note that both <a href="http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute">RDFa</a> and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values
      alongside more human-friendly formatting.
</li>
<li>
      Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols.
</li>
</ul>
      ''', related_name="pricespecification_price_number")
	priceText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Price", blank=True, null=True, help_text='''The offer price of a product, or of a price component when attached to PriceSpecification and its subtypes.
<br />
<br />
      Usage guidelines:
<br />
<ul>
<li>Use the <a href="/priceCurrency">priceCurrency</a> property (with <a href="http://en.wikipedia.org/wiki/ISO_4217#Active_codes">ISO 4217 codes</a> e.g. "USD") instead of
      including <a href="http://en.wikipedia.org/wiki/Dollar_sign#Currencies_that_use_the_dollar_or_peso_sign">ambiguous symbols</a> such as '$' in the value.
</li>
<li>
      Use '.' (Unicode 'FULL STOP' (U+002E)) rather than ',' to indicate a decimal point. Avoid using these symbols as a readability separator.
</li>
<li>
      Note that both <a href="http://www.w3.org/TR/xhtml-rdfa-primer/#using-the-content-attribute">RDFa</a> and Microdata syntax allow the use of a "content=" attribute for publishing simple machine-readable values
      alongside more human-friendly formatting.
</li>
<li>
      Use values from 0123456789 (Unicode 'DIGIT ZERO' (U+0030) to 'DIGIT NINE' (U+0039)) rather than superficially similiar Unicode symbols.
</li>
</ul>
      ''', related_name="pricespecification_price_text")
	valueAddedTaxIncludedBoolean = models.ForeignKey('Boolean', on_delete=models.CASCADE, verbose_name="Valueaddedtaxincluded", blank=True, null=True, help_text='''Specifies whether the applicable value-added tax (VAT) is included in the price specification or not.''', related_name="pricespecification_valueaddedtaxincluded_boolean")
	eligibleQuantityQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Eligiblequantity", blank=True, null=True, help_text='''The interval and unit of measurement of ordering quantities for which the offer or price specification is valid. This allows e.g. specifying that a certain freight charge is valid only for a certain quantity.''', related_name="pricespecification_eligiblequantity_quantitativevalue")
	maxPriceNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Maxprice", blank=True, null=True, help_text='''The highest price if the price is a range.''', related_name="pricespecification_maxprice_number")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'PriceSpecification'
		verbose_name_plural = 'PriceSpecification'


class RadioChannel(models.Model):

	broadcastChannel = models.ForeignKey('BroadcastChannel', on_delete=models.CASCADE, verbose_name="Broadcastchannel", blank=True, null=True, help_text='''A unique instance of a BroadcastService on a CableOrSatelliteService lineup.''', related_name="radiochannel_broadcastchannel")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RadioChannel'
		verbose_name_plural = 'RadioChannel'


class EatAction(models.Model):

	consumeAction = models.ForeignKey('ConsumeAction', on_delete=models.CASCADE, verbose_name="Consumeaction", blank=True, null=True, help_text='''The act of ingesting information/resources/food.''', related_name="eataction_consumeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EatAction'
		verbose_name_plural = 'EatAction'


class ComedyEvent(models.Model):

	event = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''An event happening at a certain time and location, such as a concert, lecture, or festival. Ticketing information may be added via the 'offers' property. Repeated events may be structured as separate Event objects.''', related_name="comedyevent_event")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ComedyEvent'
		verbose_name_plural = 'ComedyEvent'


class FireStation(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="firestation_civicstructure")
	emergencyService = models.ForeignKey('EmergencyService', on_delete=models.CASCADE, verbose_name="Emergencyservice", blank=True, null=True, help_text='''An emergency service, such as a fire station or ER.''', related_name="firestation_emergencyservice")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'FireStation'
		verbose_name_plural = 'FireStation'


class AppendAction(models.Model):

	insertAction = models.ForeignKey('InsertAction', on_delete=models.CASCADE, verbose_name="Insertaction", blank=True, null=True, help_text='''The act of adding at a specific location in an ordered collection.''', related_name="appendaction_insertaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'AppendAction'
		verbose_name_plural = 'AppendAction'


class TextDigitalDocument(models.Model):

	digitalDocument = models.ForeignKey('DigitalDocument', on_delete=models.CASCADE, verbose_name="Digitaldocument", blank=True, null=True, help_text='''An electronic file or document.''', related_name="textdigitaldocument_digitaldocument")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TextDigitalDocument'
		verbose_name_plural = 'TextDigitalDocument'


class WatchAction(models.Model):

	consumeAction = models.ForeignKey('ConsumeAction', on_delete=models.CASCADE, verbose_name="Consumeaction", blank=True, null=True, help_text='''The act of ingesting information/resources/food.''', related_name="watchaction_consumeaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WatchAction'
		verbose_name_plural = 'WatchAction'


class Continent(models.Model):

	landform = models.ForeignKey('Landform', on_delete=models.CASCADE, verbose_name="Landform", blank=True, null=True, help_text='''A landform or physical feature.  Landform elements include mountains, plains, lakes, rivers, seascape and oceanic waterbody interface features such as bays, peninsulas, seas and so forth, including sub-aqueous terrain features such as submersed mountain ranges, volcanoes, and the great ocean basins.''', related_name="continent_landform")

	def __str__(self):
		return str(self.landform.place.thing.nameText.value)

	class Meta:
		verbose_name = 'Continent'
		verbose_name_plural = 'Continent'


class GardenStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="gardenstore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GardenStore'
		verbose_name_plural = 'GardenStore'


class WPSideBar(models.Model):

	webPageElement = models.ForeignKey('WebPageElement', on_delete=models.CASCADE, verbose_name="Webpageelement", blank=True, null=True, help_text='''A web page element, like a table or an image.''', related_name="wpsidebar_webpageelement")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WPSideBar'
		verbose_name_plural = 'WPSideBar'


class TireShop(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="tireshop_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TireShop'
		verbose_name_plural = 'TireShop'


class Campground(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="campground_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Campground'
		verbose_name_plural = 'Campground'


class JoinAction(models.Model):

	eventEvent = models.ForeignKey('Event', on_delete=models.CASCADE, verbose_name="Event", blank=True, null=True, help_text='''Upcoming or past event associated with this place, organization, or action.''', related_name="joinaction_event_event")
	interactAction = models.ForeignKey('InteractAction', on_delete=models.CASCADE, verbose_name="Interactaction", blank=True, null=True, help_text='''The act of interacting with another person or organization.''', related_name="joinaction_interactaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'JoinAction'
		verbose_name_plural = 'JoinAction'


class CurrencyConversionService(models.Model):

	financialProduct = models.ForeignKey('FinancialProduct', on_delete=models.CASCADE, verbose_name="Financialproduct", blank=True, null=True, help_text='''A product provided to consumers and businesses by financial institutions such as banks, insurance companies, brokerage firms, consumer finance companies, and investment companies which comprise the financial services industry.''', related_name="currencyconversionservice_financialproduct")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CurrencyConversionService'
		verbose_name_plural = 'CurrencyConversionService'


class MiddleSchool(models.Model):

	educationalOrganization = models.ForeignKey('EducationalOrganization', on_delete=models.CASCADE, verbose_name="Educationalorganization", blank=True, null=True, help_text='''An educational organization.''', related_name="middleschool_educationalorganization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MiddleSchool'
		verbose_name_plural = 'MiddleSchool'


class RsvpAction(models.Model):

	additionalNumberOfGuestsNumber = models.ForeignKey('Number', on_delete=models.CASCADE, verbose_name="Additionalnumberofguests", blank=True, null=True, help_text='''If responding yes, the number of guests who will attend in addition to the invitee.''', related_name="rsvpaction_additionalnumberofguests_number")
	rsvpResponseRsvpResponseType = models.ForeignKey('RsvpResponseType', on_delete=models.CASCADE, verbose_name="Rsvpresponse", blank=True, null=True, help_text='''The response (yes, no, maybe) to the RSVP.''', related_name="rsvpaction_rsvpresponse_rsvpresponsetype")
	informAction = models.ForeignKey('InformAction', on_delete=models.CASCADE, verbose_name="Informaction", blank=True, null=True, help_text='''The act of notifying someone of information pertinent to them, with no expectation of a response.''', related_name="rsvpaction_informaction")
	commentComment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Comment", blank=True, null=True, help_text='''Comments, typically from users.''', related_name="rsvpaction_comment_comment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RsvpAction'
		verbose_name_plural = 'RsvpAction'


class Restaurant(models.Model):

	foodEstablishment = models.ForeignKey('FoodEstablishment', on_delete=models.CASCADE, verbose_name="Foodestablishment", blank=True, null=True, help_text='''A food-related business.''', related_name="restaurant_foodestablishment")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Restaurant'
		verbose_name_plural = 'Restaurant'


class BusinessFunction(models.Model):

	enumeration = models.ForeignKey('Enumeration', on_delete=models.CASCADE, verbose_name="Enumeration", blank=True, null=True, help_text='''Lists or enumerations—for example, a list of cuisines or music genres, etc.''', related_name="businessfunction_enumeration")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'BusinessFunction'
		verbose_name_plural = 'BusinessFunction'


class DefenceEstablishment(models.Model):

	governmentBuilding = models.ForeignKey('GovernmentBuilding', on_delete=models.CASCADE, verbose_name="Governmentbuilding", blank=True, null=True, help_text='''A government building.''', related_name="defenceestablishment_governmentbuilding")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DefenceEstablishment'
		verbose_name_plural = 'DefenceEstablishment'


class MotorcycleRepair(models.Model):

	automotiveBusiness = models.ForeignKey('AutomotiveBusiness', on_delete=models.CASCADE, verbose_name="Automotivebusiness", blank=True, null=True, help_text='''Car repair, sales, or parts.''', related_name="motorcyclerepair_automotivebusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MotorcycleRepair'
		verbose_name_plural = 'MotorcycleRepair'


class WPFooter(models.Model):

	webPageElement = models.ForeignKey('WebPageElement', on_delete=models.CASCADE, verbose_name="Webpageelement", blank=True, null=True, help_text='''A web page element, like a table or an image.''', related_name="wpfooter_webpageelement")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'WPFooter'
		verbose_name_plural = 'WPFooter'


class SpreadsheetDigitalDocument(models.Model):

	digitalDocument = models.ForeignKey('DigitalDocument', on_delete=models.CASCADE, verbose_name="Digitaldocument", blank=True, null=True, help_text='''An electronic file or document.''', related_name="spreadsheetdigitaldocument_digitaldocument")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'SpreadsheetDigitalDocument'
		verbose_name_plural = 'SpreadsheetDigitalDocument'


class VideoObject(models.Model):

	musicByMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="videoobject_musicby_musicgroup")
	musicByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="videoobject_musicby_person")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="videoobject_director_person")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="videoobject_actor_person")
	thumbnailImageObject = models.ForeignKey('ImageObject', on_delete=models.CASCADE, verbose_name="Thumbnail", blank=True, null=True, help_text='''Thumbnail image for an image or video.''', related_name="videoobject_thumbnail_imageobject")
	transcriptText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Transcript", blank=True, null=True, help_text='''If this MediaObject is an AudioObject or VideoObject, the transcript of that object.''', related_name="videoobject_transcript_text")
	videoQualityText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Videoquality", blank=True, null=True, help_text='''The quality of the video.''', related_name="videoobject_videoquality_text")
	videoFrameSizeText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Videoframesize", blank=True, null=True, help_text='''The frame size of the video.''', related_name="videoobject_videoframesize_text")
	mediaObject = models.ForeignKey('MediaObject', on_delete=models.CASCADE, verbose_name="Mediaobject", blank=True, null=True, help_text='''An image, video, or audio object embedded in a web page. Note that a creative work may have many media objects associated with it on the same web page. For example, a page about a single song (MusicRecording) may have a music video (VideoObject), and a high and low bandwidth audio stream (2 AudioObject's).''', related_name="videoobject_mediaobject")
	captionText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Caption", blank=True, null=True, help_text='''The caption for this object.''', related_name="videoobject_caption_text")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'VideoObject'
		verbose_name_plural = 'VideoObject'


class MobilePhoneStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="mobilephonestore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'MobilePhoneStore'
		verbose_name_plural = 'MobilePhoneStore'


class Photograph(models.Model):

	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="photograph_creativework")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Photograph'
		verbose_name_plural = 'Photograph'


class Report(models.Model):

	reportNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Reportnumber", blank=True, null=True, help_text='''The number or other unique designator assigned to a Report by the publishing organization.''', related_name="report_reportnumber_text")
	article = models.ForeignKey('Article', on_delete=models.CASCADE, verbose_name="Article", blank=True, null=True, help_text='''An article, such as a news article or piece of investigative report. Newspapers and magazines have articles of many different types and this is intended to cover them all.

      <br/><br/>See also <a href="http://blog.schema.org/2014/09/schemaorg-support-for-bibliographic_2.html">blog post</a>.''', related_name="report_article")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Report'
		verbose_name_plural = 'Report'


class Country(models.Model):

	administrativeArea = models.ForeignKey('AdministrativeArea', on_delete=models.CASCADE, verbose_name="Administrativearea", blank=True, null=True, help_text='''A geographical region, typically under the jurisdiction of a particular government.''', related_name="country_administrativearea")

	def __str__(self):
		return str(self.administrativeArea.place.thing.nameText.value)

	class Meta:
		verbose_name = 'Country'
		verbose_name_plural = 'Country'


class Pond(models.Model):

	bodyOfWater = models.ForeignKey('BodyOfWater', on_delete=models.CASCADE, verbose_name="Bodyofwater", blank=True, null=True, help_text='''A body of water, such as a sea, ocean, or lake.''', related_name="pond_bodyofwater")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Pond'
		verbose_name_plural = 'Pond'


class TrackAction(models.Model):

	findAction = models.ForeignKey('FindAction', on_delete=models.CASCADE, verbose_name="Findaction", blank=True, null=True, help_text='''The act of finding an object.<p>Related actions:</p><ul><li><a href="http://schema.org/SearchAction">SearchAction</a>: FindAction is generally lead by a SearchAction, but not necessarily</li></ul>.''', related_name="trackaction_findaction")
	deliveryMethodDeliveryMethod = models.ForeignKey('DeliveryMethod', on_delete=models.CASCADE, verbose_name="Deliverymethod", blank=True, null=True, help_text='''A sub property of instrument. The method of delivery.''', related_name="trackaction_deliverymethod_deliverymethod")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'TrackAction'
		verbose_name_plural = 'TrackAction'


class GroceryStore(models.Model):

	store = models.ForeignKey('Store', on_delete=models.CASCADE, verbose_name="Store", blank=True, null=True, help_text='''A retail good store.''', related_name="grocerystore_store")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'GroceryStore'
		verbose_name_plural = 'GroceryStore'


class UserPageVisits(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'UserPageVisits'
		verbose_name_plural = 'UserPageVisits'


class Park(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="park_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Park'
		verbose_name_plural = 'Park'


class EducationalOrganization(models.Model):

	alumniPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Alumni", blank=True, null=True, help_text='''Alumni of an organization.''', related_name="educationalorganization_alumni_person")
	organization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Organization", blank=True, null=True, help_text='''An organization such as a school, NGO, corporation, club, etc.''', related_name="educationalorganization_organization")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'EducationalOrganization'
		verbose_name_plural = 'EducationalOrganization'


class ReplyAction(models.Model):

	resultCommentComment = models.ForeignKey('Comment', on_delete=models.CASCADE, verbose_name="Resultcomment", blank=True, null=True, help_text='''A sub property of result. The Comment created or sent as a result of this action.''', related_name="replyaction_resultcomment_comment")
	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="Communicateaction", blank=True, null=True, help_text='''The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.''', related_name="replyaction_communicateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ReplyAction'
		verbose_name_plural = 'ReplyAction'


class Clip(models.Model):

	musicByMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="clip_musicby_musicgroup")
	musicByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="clip_musicby_person")
	clipNumberInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Clipnumber", blank=True, null=True, help_text='''Position of the clip within an ordered group of clips.''', related_name="clip_clipnumber_integer")
	clipNumberText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Clipnumber", blank=True, null=True, help_text='''Position of the clip within an ordered group of clips.''', related_name="clip_clipnumber_text")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="clip_director_person")
	partOfEpisodeEpisode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Partofepisode", blank=True, null=True, help_text='''The episode to which this clip belongs.''', related_name="clip_partofepisode_episode")
	creativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Creativework", blank=True, null=True, help_text='''The most generic kind of creative work, including books, movies, photographs, software programs, etc.''', related_name="clip_creativework")
	partOfSeasonCreativeWorkSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Partofseason", blank=True, null=True, help_text='''The season to which this episode belongs.''', related_name="clip_partofseason_creativeworkseason")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="clip_actor_person")
	partOfSeriesCreativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Partofseries", blank=True, null=True, help_text='''The series to which this episode or season belongs.''', related_name="clip_partofseries_creativeworkseries")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Clip'
		verbose_name_plural = 'Clip'


class CheckInAction(models.Model):

	communicateAction = models.ForeignKey('CommunicateAction', on_delete=models.CASCADE, verbose_name="Communicateaction", blank=True, null=True, help_text='''The act of conveying information to another person via a communication medium (instrument) such as speech, email, or telephone conversation.''', related_name="checkinaction_communicateaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'CheckInAction'
		verbose_name_plural = 'CheckInAction'


class OceanBodyOfWater(models.Model):

	bodyOfWater = models.ForeignKey('BodyOfWater', on_delete=models.CASCADE, verbose_name="Bodyofwater", blank=True, null=True, help_text='''A body of water, such as a sea, ocean, or lake.''', related_name="oceanbodyofwater_bodyofwater")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'OceanBodyOfWater'
		verbose_name_plural = 'OceanBodyOfWater'


class RVPark(models.Model):

	civicStructure = models.ForeignKey('CivicStructure', on_delete=models.CASCADE, verbose_name="Civicstructure", blank=True, null=True, help_text='''A public structure, such as a town hall or concert hall.''', related_name="rvpark_civicstructure")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'RVPark'
		verbose_name_plural = 'RVPark'


class Code(models.Model):


	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'Code'
		verbose_name_plural = 'Code'


class DrawAction(models.Model):

	createAction = models.ForeignKey('CreateAction', on_delete=models.CASCADE, verbose_name="Createaction", blank=True, null=True, help_text='''The act of deliberately creating/producing/generating/building a result out of the agent.''', related_name="drawaction_createaction")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'DrawAction'
		verbose_name_plural = 'DrawAction'


class ArtGallery(models.Model):

	entertainmentBusiness = models.ForeignKey('EntertainmentBusiness', on_delete=models.CASCADE, verbose_name="Entertainmentbusiness", blank=True, null=True, help_text='''A business providing entertainment.''', related_name="artgallery_entertainmentbusiness")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'ArtGallery'
		verbose_name_plural = 'ArtGallery'


class VideoGameSeries(models.Model):

	musicByMusicGroup = models.ForeignKey('MusicGroup', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="videogameseries_musicby_musicgroup")
	musicByPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Musicby", blank=True, null=True, help_text='''The composer of the soundtrack.''', related_name="videogameseries_musicby_person")
	gameLocationURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Gamelocation", blank=True, null=True, help_text='''Real or fictional location of the game (or part of game).''', related_name="videogameseries_gamelocation_url")
	gameLocationPlace = models.ForeignKey('Place', on_delete=models.CASCADE, verbose_name="Gamelocation", blank=True, null=True, help_text='''Real or fictional location of the game (or part of game).''', related_name="videogameseries_gamelocation_place")
	gameLocationPostalAddress = models.ForeignKey('PostalAddress', on_delete=models.CASCADE, verbose_name="Gamelocation", blank=True, null=True, help_text='''Real or fictional location of the game (or part of game).''', related_name="videogameseries_gamelocation_postaladdress")
	trailerVideoObject = models.ForeignKey('VideoObject', on_delete=models.CASCADE, verbose_name="Trailer", blank=True, null=True, help_text='''The trailer of a movie or tv/radio series, season, episode, etc.''', related_name="videogameseries_trailer_videoobject")
	directorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Director", blank=True, null=True, help_text='''A director of e.g. tv, radio, movie, video gaming etc. content, or of an event. Directors can be associated with individual items or with a series, episode, clip.''', related_name="videogameseries_director_person")
	cheatCodeCreativeWork = models.ForeignKey('CreativeWork', on_delete=models.CASCADE, verbose_name="Cheatcode", blank=True, null=True, help_text='''Cheat codes to the game.''', related_name="videogameseries_cheatcode_creativework")
	episodeEpisode = models.ForeignKey('Episode', on_delete=models.CASCADE, verbose_name="Episode", blank=True, null=True, help_text='''An episode of a tv, radio or game media within a series or season.''', related_name="videogameseries_episode_episode")
	actorPerson = models.ForeignKey('Person', on_delete=models.CASCADE, verbose_name="Actor", blank=True, null=True, help_text='''An actor, e.g. in tv, radio, movie, video games etc., or in an event. Actors can be associated with individual items or with a series, episode, clip.''', related_name="videogameseries_actor_person")
	containsSeasonCreativeWorkSeason = models.ForeignKey('CreativeWorkSeason', on_delete=models.CASCADE, verbose_name="Containsseason", blank=True, null=True, help_text='''A season that is part of the media series.''', related_name="videogameseries_containsseason_creativeworkseason")
	playModeGamePlayMode = models.ForeignKey('GamePlayMode', on_delete=models.CASCADE, verbose_name="Playmode", blank=True, null=True, help_text='''Indicates whether this game is multi-player, co-op or single-player.  The game can be marked as multi-player, co-op and single-player at the same time.''', related_name="videogameseries_playmode_gameplaymode")
	creativeWorkSeries = models.ForeignKey('CreativeWorkSeries', on_delete=models.CASCADE, verbose_name="Creativeworkseries", blank=True, null=True, help_text='''
          A CreativeWorkSeries in schema.org is a group of related items, typically but not necessarily of the same kind.
          CreativeWorkSeries are usually organized into some order, often chronological. Unlike <a href="/ItemList">ItemList</a> which
          is a general purpose data structure for lists of things, the emphasis with
          CreativeWorkSeries is on published materials (written e.g. books and periodicals,
          or media such as tv, radio and games).

          <br/><br/>

          Specific subtypes are available for describing <a href="/TVSeries">TVSeries</a>, <a href="/RadioSeries">RadioSeries</a>,
          <a href="/MovieSeries">MovieSeries</a>,
          <a href="/BookSeries">BookSeries</a>,
          <a href="/Periodical">Periodical</a>
          and <a href="/VideoGameSeries">VideoGameSeries</a>. In each case,
          the <a href="/hasPart">hasPart</a> / <a href="/isPartOf">isPartOf</a> properties
          can be used to relate the CreativeWorkSeries to its parts. The general CreativeWorkSeries type serves largely
          just to organize these more specific and practical subtypes.

          <br/><br/>

          It is common for properties applicable to an item from the series to be usefully applied to the containing group.
          Schema.org attempts to anticipate some of these cases, but publishers should be free to apply
          properties of the series parts to the series as a whole wherever they seem appropriate.''', related_name="videogameseries_creativeworkseries")
	questThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Quest", blank=True, null=True, help_text='''The task that a player-controlled character, or group of characters may complete in order to gain a reward.''', related_name="videogameseries_quest_thing")
	numberOfSeasonsInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofseasons", blank=True, null=True, help_text='''The number of seasons in this series.''', related_name="videogameseries_numberofseasons_integer")
	gamePlatformThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Gameplatform", blank=True, null=True, help_text='''The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.''', related_name="videogameseries_gameplatform_thing")
	gamePlatformText = models.ForeignKey('Text', on_delete=models.CASCADE, verbose_name="Gameplatform", blank=True, null=True, help_text='''The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.''', related_name="videogameseries_gameplatform_text")
	gamePlatformURL = models.ForeignKey('URL', on_delete=models.CASCADE, verbose_name="Gameplatform", blank=True, null=True, help_text='''The electronic systems used to play <a href="http://en.wikipedia.org/wiki/Category:Video_game_platforms">video games</a>.''', related_name="videogameseries_gameplatform_url")
	gameItemThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Gameitem", blank=True, null=True, help_text='''An item is an object within the game world that can be collected by a player or, occasionally, a non-player character.''', related_name="videogameseries_gameitem_thing")
	numberOfPlayersQuantitativeValue = models.ForeignKey('QuantitativeValue', on_delete=models.CASCADE, verbose_name="Numberofplayers", blank=True, null=True, help_text='''Indicate how many people can play this game (minimum, maximum, or range).''', related_name="videogameseries_numberofplayers_quantitativevalue")
	productionCompanyOrganization = models.ForeignKey('Organization', on_delete=models.CASCADE, verbose_name="Productioncompany", blank=True, null=True, help_text='''The production company or studio responsible for the item e.g. series, video game, episode etc.''', related_name="videogameseries_productioncompany_organization")
	numberOfEpisodesInteger = models.ForeignKey('Integer', on_delete=models.CASCADE, verbose_name="Numberofepisodes", blank=True, null=True, help_text='''The number of episodes in this season or series.''', related_name="videogameseries_numberofepisodes_integer")
	characterAttributeThing = models.ForeignKey('Thing', on_delete=models.CASCADE, verbose_name="Characterattribute", blank=True, null=True, help_text='''A piece of data that represents a particular aspect of a fictional character (skill, power, character points, advantage, disadvantage).''', related_name="videogameseries_characterattribute_thing")

	def __str__(self):
		return str(self.id)

	class Meta:
		verbose_name = 'VideoGameSeries'
		verbose_name_plural = 'VideoGameSeries'
