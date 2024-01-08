Allows providers to submit times they are available for appointments
e.g. On Friday the 13th of August, Dr. Jekyll wants to work between 8am and 3pm
Allows a client to retrieve a list of available appointment slots
Appointment slots are 15 minutes long
Allows clients to reserve an available appointment slot
Allows clients to confirm their reservation



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
    appointments: list of datetime strings in 15 minute intervals to create availability etc,
                ex:
                    2022-01-05T14:00:00
                    2022-01-05T14:15:00
                    2022-01-05T14:30:00
                    2022-01-05T14:45:00
                    in format: 'YYYY-MM-DDTHH:MM:SS', 

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
