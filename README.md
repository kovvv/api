# API DATE service

## Usage

--All requests must be sent to localhost:5000/date and have the form

json
{
    "date":"Dec 20 2018  11:40PM"
}

"Jun 28 2018 at 7:40AM" -> "%b %d %Y at %I:%M%p"

--All response will have the form

json
{
   "date": "2018-12-20 23:40:00",
   "message": "success"
}

## Running API in container

Type the following command:
docker-compose up
