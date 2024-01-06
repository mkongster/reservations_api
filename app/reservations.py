from app.database import db
from app.models import User, Appointment
from datetime import datetime
from typing import List

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
