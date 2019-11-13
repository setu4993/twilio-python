# coding=utf-8
r"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /
"""

from twilio.base import values
from twilio.base.instance_context import InstanceContext
from twilio.base.instance_resource import InstanceResource
from twilio.base.list_resource import ListResource
from twilio.base.page import Page


class InstalledAddOnExtensionList(ListResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, installed_add_on_sid):
        """
        Initialize the InstalledAddOnExtensionList

        :param Version version: Version that contains the resource
        :param installed_add_on_sid: The SID of the InstalledAddOn resource to which this extension applies

        :returns: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionList
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionList
        """
        super(InstalledAddOnExtensionList, self).__init__(version)

        # Path Solution
        self._solution = {'installed_add_on_sid': installed_add_on_sid, }
        self._uri = '/InstalledAddOns/{installed_add_on_sid}/Extensions'.format(**self._solution)

    def stream(self, limit=None, page_size=None):
        """
        Streams InstalledAddOnExtensionInstance records from the API as a generator stream.
        This operation lazily loads records as efficiently as possible until the limit
        is reached.
        The results are returned as a generator, so this operation is memory efficient.

        :param int limit: Upper limit for the number of records to return. stream()
                          guarantees to never return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, stream() will attempt to read the
                              limit with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance]
        """
        limits = self._version.read_limits(limit, page_size)

        page = self.page(page_size=limits['page_size'], )

        return self._version.stream(page, limits['limit'], limits['page_limit'])

    def list(self, limit=None, page_size=None):
        """
        Lists InstalledAddOnExtensionInstance records from the API as a list.
        Unlike stream(), this operation is eager and will load `limit` records into
        memory before returning.

        :param int limit: Upper limit for the number of records to return. list() guarantees
                          never to return more than limit.  Default is no limit
        :param int page_size: Number of records to fetch per request, when not set will use
                              the default value of 50 records.  If no page_size is defined
                              but a limit is defined, list() will attempt to read the limit
                              with the most efficient page size, i.e. min(limit, 1000)

        :returns: Generator that will yield up to limit results
        :rtype: list[twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance]
        """
        return list(self.stream(limit=limit, page_size=page_size, ))

    def page(self, page_token=values.unset, page_number=values.unset,
             page_size=values.unset):
        """
        Retrieve a single page of InstalledAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param str page_token: PageToken provided by the API
        :param int page_number: Page Number, this value is simply for client state
        :param int page_size: Number of records to return, defaults to 50

        :returns: Page of InstalledAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionPage
        """
        params = values.of({'PageToken': page_token, 'Page': page_number, 'PageSize': page_size, })

        response = self._version.page(
            'GET',
            self._uri,
            params=params,
        )

        return InstalledAddOnExtensionPage(self._version, response, self._solution)

    def get_page(self, target_url):
        """
        Retrieve a specific page of InstalledAddOnExtensionInstance records from the API.
        Request is executed immediately

        :param str target_url: API-generated URL for the requested results page

        :returns: Page of InstalledAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionPage
        """
        response = self._version.domain.twilio.request(
            'GET',
            target_url,
        )

        return InstalledAddOnExtensionPage(self._version, response, self._solution)

    def get(self, sid):
        """
        Constructs a InstalledAddOnExtensionContext

        :param sid: The SID of the InstalledAddOn Extension resource to fetch

        :returns: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionContext
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionContext
        """
        return InstalledAddOnExtensionContext(
            self._version,
            installed_add_on_sid=self._solution['installed_add_on_sid'],
            sid=sid,
        )

    def __call__(self, sid):
        """
        Constructs a InstalledAddOnExtensionContext

        :param sid: The SID of the InstalledAddOn Extension resource to fetch

        :returns: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionContext
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionContext
        """
        return InstalledAddOnExtensionContext(
            self._version,
            installed_add_on_sid=self._solution['installed_add_on_sid'],
            sid=sid,
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.InstalledAddOnExtensionList>'


class InstalledAddOnExtensionPage(Page):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, response, solution):
        """
        Initialize the InstalledAddOnExtensionPage

        :param Version version: Version that contains the resource
        :param Response response: Response from the API
        :param installed_add_on_sid: The SID of the InstalledAddOn resource to which this extension applies

        :returns: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionPage
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionPage
        """
        super(InstalledAddOnExtensionPage, self).__init__(version, response)

        # Path Solution
        self._solution = solution

    def get_instance(self, payload):
        """
        Build an instance of InstalledAddOnExtensionInstance

        :param dict payload: Payload response from the API

        :returns: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance
        """
        return InstalledAddOnExtensionInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution['installed_add_on_sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        return '<Twilio.Preview.Marketplace.InstalledAddOnExtensionPage>'


class InstalledAddOnExtensionContext(InstanceContext):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, installed_add_on_sid, sid):
        """
        Initialize the InstalledAddOnExtensionContext

        :param Version version: Version that contains the resource
        :param installed_add_on_sid: The SID of the InstalledAddOn resource with the extension to fetch
        :param sid: The SID of the InstalledAddOn Extension resource to fetch

        :returns: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionContext
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionContext
        """
        super(InstalledAddOnExtensionContext, self).__init__(version)

        # Path Solution
        self._solution = {'installed_add_on_sid': installed_add_on_sid, 'sid': sid, }
        self._uri = '/InstalledAddOns/{installed_add_on_sid}/Extensions/{sid}'.format(**self._solution)

    def fetch(self):
        """
        Fetch a InstalledAddOnExtensionInstance

        :returns: Fetched InstalledAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance
        """
        params = values.of({})

        payload = self._version.fetch(
            'GET',
            self._uri,
            params=params,
        )

        return InstalledAddOnExtensionInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution['installed_add_on_sid'],
            sid=self._solution['sid'],
        )

    def update(self, enabled):
        """
        Update the InstalledAddOnExtensionInstance

        :param bool enabled: Whether the Extension should be invoked

        :returns: Updated InstalledAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance
        """
        data = values.of({'Enabled': enabled, })

        payload = self._version.update(
            'POST',
            self._uri,
            data=data,
        )

        return InstalledAddOnExtensionInstance(
            self._version,
            payload,
            installed_add_on_sid=self._solution['installed_add_on_sid'],
            sid=self._solution['sid'],
        )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.InstalledAddOnExtensionContext {}>'.format(context)


class InstalledAddOnExtensionInstance(InstanceResource):
    """ PLEASE NOTE that this class contains preview products that are subject
    to change. Use them with caution. If you currently do not have developer
    preview access, please contact help@twilio.com. """

    def __init__(self, version, payload, installed_add_on_sid, sid=None):
        """
        Initialize the InstalledAddOnExtensionInstance

        :returns: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance
        """
        super(InstalledAddOnExtensionInstance, self).__init__(version)

        # Marshaled Properties
        self._properties = {
            'sid': payload.get('sid'),
            'installed_add_on_sid': payload.get('installed_add_on_sid'),
            'friendly_name': payload.get('friendly_name'),
            'product_name': payload.get('product_name'),
            'unique_name': payload.get('unique_name'),
            'enabled': payload.get('enabled'),
            'url': payload.get('url'),
        }

        # Context
        self._context = None
        self._solution = {
            'installed_add_on_sid': installed_add_on_sid,
            'sid': sid or self._properties['sid'],
        }

    @property
    def _proxy(self):
        """
        Generate an instance context for the instance, the context is capable of
        performing various actions.  All instance actions are proxied to the context

        :returns: InstalledAddOnExtensionContext for this InstalledAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionContext
        """
        if self._context is None:
            self._context = InstalledAddOnExtensionContext(
                self._version,
                installed_add_on_sid=self._solution['installed_add_on_sid'],
                sid=self._solution['sid'],
            )
        return self._context

    @property
    def sid(self):
        """
        :returns: The unique string that identifies the resource
        :rtype: unicode
        """
        return self._properties['sid']

    @property
    def installed_add_on_sid(self):
        """
        :returns: The SID of the InstalledAddOn resource to which this extension applies
        :rtype: unicode
        """
        return self._properties['installed_add_on_sid']

    @property
    def friendly_name(self):
        """
        :returns: The string that you assigned to describe the resource
        :rtype: unicode
        """
        return self._properties['friendly_name']

    @property
    def product_name(self):
        """
        :returns: The name of the Extension's Product
        :rtype: unicode
        """
        return self._properties['product_name']

    @property
    def unique_name(self):
        """
        :returns: An application-defined string that uniquely identifies the resource
        :rtype: unicode
        """
        return self._properties['unique_name']

    @property
    def enabled(self):
        """
        :returns: Whether the Extension will be invoked
        :rtype: bool
        """
        return self._properties['enabled']

    @property
    def url(self):
        """
        :returns: The absolute URL of the resource
        :rtype: unicode
        """
        return self._properties['url']

    def fetch(self):
        """
        Fetch a InstalledAddOnExtensionInstance

        :returns: Fetched InstalledAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance
        """
        return self._proxy.fetch()

    def update(self, enabled):
        """
        Update the InstalledAddOnExtensionInstance

        :param bool enabled: Whether the Extension should be invoked

        :returns: Updated InstalledAddOnExtensionInstance
        :rtype: twilio.rest.preview.marketplace.installed_add_on.installed_add_on_extension.InstalledAddOnExtensionInstance
        """
        return self._proxy.update(enabled, )

    def __repr__(self):
        """
        Provide a friendly representation

        :returns: Machine friendly representation
        :rtype: str
        """
        context = ' '.join('{}={}'.format(k, v) for k, v in self._solution.items())
        return '<Twilio.Preview.Marketplace.InstalledAddOnExtensionInstance {}>'.format(context)
