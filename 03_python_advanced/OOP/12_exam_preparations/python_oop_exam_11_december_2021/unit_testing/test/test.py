from unittest import TestCase, main
from project.team import Team


class TestTeam(TestCase):

    def setUp(self):
        self.team = Team("TeamOne")

    def test_init(self):
        self.assertEqual("TeamOne", self.team.name)

    def test_name_setter_if_the_name_does_not_contain_only_letters_raises_value_error(self):
        with self.assertRaises(ValueError) as ve:
            self.team.name = "Team One 1"

        expected = "Team Name can contain only letters!"
        self.assertEqual(expected, str(ve.exception))

    def test_add_member_when_some_members_already_exist(self):
        self.team.members = {"Member 1": 18, "Member 2": 19, "Member 3": 20}

        result = self.team.add_member(**{"Member 1": 18, "Member 2": 19, "Member 3": 20})
        expected = "Successfully added: "

        self.assertEqual(expected, result)
        self.assertEqual({"Member 1": 18, "Member 2": 19, "Member 3": 20}, self.team.members)

    def test_add_member_when_adding_new_members(self):
        self.team.members = {"Member 1": 18, "Member 2": 19}

        result = self.team.add_member(**{"Member 1": 18, "Member 2": 19, "Member 3": 20})

        expected = "Successfully added: Member 3"

        self.assertEqual(expected, result)
        self.assertEqual({"Member 1": 18, "Member 2": 19, "Member 3": 20}, self.team.members)

    def test_add_dunder_with_same_members(self):
        team2 = Team("TeamTwo")

        team2.add_member(**{"M1": 20, "M2": 22})
        team2.add_member(**{"M1": 20, "M2": 22})

        new_team = self.team + team2

        self.assertEqual("TeamOneTeamTwo", new_team.name)
        self.assertEqual(2, len(new_team))
        self.assertEqual({"M1": 20, "M2": 22}, new_team.members)

    def test_remove_member_when_member_does_not_exist(self):
        self.team.add_member(**{"M1": 18, "M2": 19, "M3": 20})

        result = self.team.remove_member("M4")
        expected = "Member with name M4 does not exist"

        self.assertEqual(expected, result)
        self.assertEqual({"M1": 18, "M2": 19, "M3": 20}, self.team.members)

    def test_remove_member_successfully(self):
        self.team.add_member(**{"M1": 18, "M2": 19, "M3": 20})
        result = self.team.remove_member("M2")
        expected = "Member M2 removed"

        self.assertEqual(expected, result)
        self.assertEqual({"M1": 18, "M3": 20}, self.team.members)

    def test_greater_than_dunder_when_the_team_has_more_members_than_the_other_team(self):
        team2 = Team("TeamTwo")

        self.team.add_member(**{"M1": 18, "M2": 19, "M3": 20})
        team2.add_member(**{"M1": 18})

        result = self.team > team2

        self.assertTrue(result)

    def test_greater_than_dunder_with_equal_team_members_count(self):
        team2 = Team("TeamTwo")

        self.team.add_member(**{"M1": 18, "M2": 19, "M3": 20})
        team2.add_member(**{"M1": 18, "M2": 19, "M3": 20})

        team2.remove_member("M1")

        self.assertEqual(True, self.team > team2)
        self.assertEqual(False, self.team < team2)

    def test_len_dunder(self):
        self.team.add_member(**{"M1": 18, "M2": 19, "M3": 20})
        self.assertEqual(3, len(self.team))

        self.team.remove_member("M3")
        self.assertEqual(2, len(self.team))

        self.team.remove_member("M2")
        self.assertEqual(1, len(self.team))

        self.team.remove_member("M1")
        self.assertEqual(0, len(self.team))

    def test_add_dunder(self):
        team2 = Team("TeamTwo")
        self.team.add_member(**{"M1": 18, "M2": 19, "M3": 20})
        team2.add_member(**{"M4": 18, "M5": 19, "M6": 20})
        new_team = self.team + team2
        self.assertEqual("TeamOneTeamTwo", new_team.name)
        self.assertEqual(6, len(new_team))
        self.assertTrue(new_team > self.team)
        self.assertEqual({"M1": 18, "M2": 19, "M3": 20, "M4": 18, "M5": 19, "M6": 20}, new_team.members)

    def test_str_dunder(self):
        self.team.add_member(**{"A": 18, "B": 20, "C": 20})

        expected = """Team name: TeamOne
Member: B - 20-years old
Member: C - 20-years old
Member: A - 18-years old"""

        self.assertEqual(expected, self.team.__str__())

    def test_str_dunder_with_no_data(self):
        expected = "Team name: TeamOne"
        self.assertEqual(expected, self.team.__str__())


if __name__ == '__main__':
    main()