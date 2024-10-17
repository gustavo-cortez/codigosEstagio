from pydantic import BaseModel
from datetime import date

class HotelReservation(BaseModel):
    no_of_previous_bookings_not_canceled: int 
    no_of_children: int 
    repeated_guest: int
    no_of_special_requests: int
    no_of_adults: int
    no_of_week_nights: int
    required_car_parking_space: int
    arrival_date: date
    no_of_weekend_nights: int
    arrival_month: int
    lead_time: int
    no_of_previous_cancellations: int
    room_type_reserved_rt2: bool
    room_type_reserved_rt3: bool
    room_type_reserved_rt4: bool
    room_type_reserved_rt5: bool
    room_type_reserved_rt6: bool
    room_type_reserved_rt7: bool
    type_of_meal_plan_Meal_Plan_2: bool
    type_of_meal_plan_Not_Selected: bool
    market_segment_type_Complementary: bool
    market_segment_type_Corporate: bool
    market_segment_type_Offline: bool
    market_segment_type_Online: bool
