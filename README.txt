Have docker installed.
Run command `docker-compose up`
Will run api server on localhost:5000



API Endpoints: {'Content-Type': 'application/json'}

'/users', POST
Creates a new user
Accepts payload: 
    username,
    type, (provider or client)

'/submit_availability'
Submits availability for a provider.
Payload:
    provider_id: integer id of provider
    appointments: list of datetime strings to create availability 2022-01-05T14:30:00  'YYYY-MM-DDTHH:MM:SS':

/reserve'
Payload:
    client_id: integer id of client
    appointment_i: integer id of appointment trying to be reserve

'/confirm'
Payload:
    client_id: integer id of client
    appointment_id: integer id of reserved appointment trying to be confirmed

'/get_available_appointments'
Returns all available appointments
