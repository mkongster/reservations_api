from .database import db
from .models import User, Appointment
from datetime import datetime, timedelta
from typing import List, Optional

MINUTE_INTERVALS = (0, 15, 30, 45)

def submit_availability(provider_id: int, appointments: List[datetime]) -> List[Appointment]:
    completed_appts = []
    for appt in appointments:
        if appt.minute in MINUTE_INTERVALS:
            new_appt = Appointment(provider_id=provider_id, slot_datetime=appt)
            db.session.add(new_appt)
            db.session.commit()
            completed_appts.append(new_appt)
    return completed_appts


def reserve(client_id: int, appointment_id: int) -> Optional[Appointment]:
    appointment = Appointment.query.get(appointment_id)
    
    if appointment:
        time_diff = appointment.slot_datetime - datetime.now()
        # must reserve at least 24 hours ahead
        if time_diff >= timedelta(days=1):
            appointment.last_reserved_by = client_id
            appointment.last_reserved_datetime = datetime.now()
            db.session.commit()
            return appointment
    return None
