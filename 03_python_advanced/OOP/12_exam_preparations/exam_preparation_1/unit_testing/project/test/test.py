from unittest import TestCase, main
from project.trip import Trip


class TestTrip(TestCase):
    def setUp(self):
        self.t1f = Trip(10000, 1, False)
        self.t2f = Trip(10000, 2, False)
        self.t3t = Trip(10000, 2, True)

    def test_init(self):
        self.assertEqual(10000, self.t1f.budget)
        self.assertEqual(1, self.t1f.travelers)
        self.assertFalse(self.t1f.is_family)
        self.assertEqual({}, self.t1f.booked_destinations_paid_amounts)

    def test_setter_travelers_when_travelers_are_less_than_one_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.t1f.travelers = 0

        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family_when_travelers_are_less_than_two_returns_false(self):
        self.assertTrue(self.t3t.is_family)

        self.t1f.is_family = True
        self.assertFalse(self.t1f.is_family)

    def test_book_a_trip_when_destination_does_not_exist_in_the_available_offers(self):
        result = self.t1f.book_a_trip('England')

        self.assertEqual('This destination is not in our offers, please choose a new one!', result)

    def test_book_a_trip_when_the_budget_is_not_enough(self):
        result = self.t2f.book_a_trip('New Zealand')

        self.assertEqual('Your budget is not enough!', result)

    def test_book_a_trip_successfully_when_family_discount_is_available(self):
        result = self.t2f.book_a_trip('Bulgaria')

        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 9000.00', result)
        self.assertEqual(9000, self.t2f.budget)
        self.assertEqual({'Bulgaria': 1000}, self.t2f.booked_destinations_paid_amounts)

    def test_book_a_trip_successfully_when_family_discount_is_not_available(self):
        result = self.t3t.book_a_trip('Bulgaria')

        self.assertEqual('Successfully booked destination Bulgaria! Your budget left is 9100.00', result)
        self.assertEqual(9100, self.t3t.budget)
        self.assertEqual({'Bulgaria': 900}, self.t3t.booked_destinations_paid_amounts)

    def test_booking_status_when_there_are_not_any_bookings(self):
        self.assertEqual('No bookings yet. Budget: 10000.00', self.t1f.booking_status())

    def test_booking_status_when_there_are_bookings_made(self):
        self.t2f.budget = 100_000
        self.t2f.book_a_trip('Brazil')
        self.t2f.book_a_trip('New Zealand')

        result = self.t2f.booking_status()
        expected = '''Booked Destination: Brazil
Paid Amount: 12400.00
Booked Destination: New Zealand
Paid Amount: 15000.00
Number of Travelers: 2
Budget Left: 72600.00'''

        self.assertEqual(expected, result)


if __name__ == '__main__':
    main()
