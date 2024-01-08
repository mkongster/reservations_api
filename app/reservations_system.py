from .database import db
from .models import User, Appointment
from datetime import datetime, timedelta
from sqlalchemy import or_
from typing import List, Optional

MINUTE_INTERVALS = (0, 15, 30, 45)

def submit_availability(provider_id: int, appointments: List[datetime]) -> List[Appointment]:
    completed_appts = []
    for appt in appointments:
        appt = datetime.strptime(appt, '%Y-%m-%dT%H:%M:%S')
        if appt.minute in MINUTE_INTERVALS:
            new_appt = Appointment(provider_id=provider_id, slot_datetime=appt)
            db.session.add(new_appt)
            db.session.commit()
            completed_appts.append(new_appt.to_dict())
    return completed_appts


def reserve(client_id: int, appointment_id: int) -> Optional[Appointment]:
    appointment = Appointment.query.get(appointment_id)
    
    if appointment:
        time_diff = (appointment.slot_datetime - datetime.now()) >= timedelta(days=1)
        reserved_time = True if not appointment.last_reserved_datetime else \
            (datetime.now() - appointment.last_reserved_datetime) >= timedelta(minutes=30)
        # must reserve at least 24 hours ahead and someone reserved it within 30 mins
        if time_diff and reserved_time:
            appointment.last_reserved_by = client_id
            appointment.last_reserved_datetime = datetime.now()
            db.session.commit()
            return appointment.to_dict()
    return None


def confirm(client_id: int, appointment_id: int) -> Optional[Appointment]:
    appointment = Appointment.query.get(appointment_id)
    if appointment:
        correct_reservation = appointment.last_reserved_by == client_id
        correct_reservation_time = False if not appointment.last_reserved_datetime else \
            (datetime.now() - appointment.last_reserved_datetime) < timedelta(minutes=30)
        if correct_reservation and correct_reservation_time:
            appointment.client_id = client_id
            appointment.confirmed = True
            db.session.commit()
            return appointment.to_dict()
    return None


def get_available_appointments() -> List[Optional[Appointment]]:
    reservation_boundary = datetime.now() - timedelta(minutes=30)
    appointments = Appointment.query.filter(
            or_(Appointment.last_reserved_datetime == None, Appointment.last_reserved_datetime > reservation_boundary),
            Appointment.confirmed == False
        ).all()
    return [appointment.to_dict() for appointment in appointments]
