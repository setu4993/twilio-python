# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from tests import IntegrationTestCase
from tests.holodeck import Request
from twilio.base.exceptions import TwilioException
from twilio.http.response import Response


class InsightsQuestionnairesCategoryTestCase(IntegrationTestCase):

    def test_create_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.insights_questionnaires_category.create(name="name", token="token")

        values = {'Name': "name", }

        headers = {'Token': "token", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Insights/QM/Categories',
            headers=headers,
        ))
        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Insights/QM/Categories',
            data=values,
        ))

    def test_create_response(self):
        self.holodeck.mock(Response(
            201,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "category_id": "4b4e78e4-4f05-49e2-bf52-0973c5cde419",
                "name": "abc",
                "url": "https://flex-api.twilio.com/v1/Insights/QM/Categories/4b4e78e4-4f05-49e2-bf52-0973c5cde419"
            }
            '''
        ))

        actual = self.client.flex_api.v1.insights_questionnaires_category.create(name="name")

        self.assertIsNotNone(actual)

    def test_update_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.insights_questionnaires_category("category_id").update(name="name", token="token")

        values = {'Name': "name", }

        headers = {'Token': "token", }
        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Insights/QM/Categories/category_id',
            headers=headers,
        ))
        self.holodeck.assert_has_request(Request(
            'post',
            'https://flex-api.twilio.com/v1/Insights/QM/Categories/category_id',
            data=values,
        ))

    def test_update_response(self):
        self.holodeck.mock(Response(
            200,
            '''
            {
                "account_sid": "ACaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa",
                "category_id": "4b4e78e4-4f05-49e2-bf52-0973c5cde419",
                "name": "abcd",
                "url": "https://flex-api.twilio.com/v1/Insights/QM/Categories/4b4e78e4-4f05-49e2-bf52-0973c5cde419"
            }
            '''
        ))

        actual = self.client.flex_api.v1.insights_questionnaires_category("category_id").update(name="name")

        self.assertIsNotNone(actual)

    def test_delete_request(self):
        self.holodeck.mock(Response(500, ''))

        with self.assertRaises(TwilioException):
            self.client.flex_api.v1.insights_questionnaires_category("category_id").delete(token="token")

        headers = {'Token': "token", }
        self.holodeck.assert_has_request(Request(
            'delete',
            'https://flex-api.twilio.com/v1/Insights/QM/Categories/category_id',
            headers=headers,
        ))

    def test_delete_response(self):
        self.holodeck.mock(Response(
            204,
            None,
        ))

        actual = self.client.flex_api.v1.insights_questionnaires_category("category_id").delete()

        self.assertTrue(actual)