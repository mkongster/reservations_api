docker-compose up



API Endpoints: {'Content-Type': 'application/json'}

'/users'
Accepts payload: 
    username,
    type, (provider or client)

'/submit_availability'
Payload:
    provider_id,
    appointments: list of datetime strings to create availability 2022-01-05T14:30:00  'YYYY-MM-DDTHH:MM:SS':

/reserve'
Payload:
    client_id,
    appointment_id

'/confirm'
Payload:
    client_id,
    appointment_id

'/get_available_appointments'
