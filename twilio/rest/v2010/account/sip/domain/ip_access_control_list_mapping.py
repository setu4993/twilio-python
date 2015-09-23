# coding=utf-8
"""
This code was generated by
\ / _    _  _|   _  _
 | (_)\/(_)(_|\/| |(/_  v1.0.0
      /       /       
"""

from twilio import values
from twilio.rest import deserialize
from twilio.rest.base import InstanceContext
from twilio.rest.base import InstanceResource
from twilio.rest.base import ListResource


class IpAccessControlListMappingList(ListResource):

    def __init__(self, domain, account_sid, domain_sid):
        super(IpAccessControlListMappingList, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'domain_sid': domain_sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings.json".format(**self._instance_kwargs)

    def create(self, ip_access_control_list_sid):
        data = values.of({
            "IpAccessControlListSid": ip_access_control_list_sid,
        })
        
        return self._domain.create(
            IpAccessControlListMappingInstance,
            self._instance_kwargs,
            'POST',
            self._uri,
            data=data,
        )

    def read(self, limit=None, page_size=None, **kwargs):
        limits = self._domain.read_limits(limit, page_size)
        
        params = values.of({})
        params.update(kwargs)
        
        return self._domain.read(
            self,
            IpAccessControlListMappingInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            limits['limit'],
            limits['page_limit'],
            params=params,
        )

    def page(self, page_token=None, page_number=None, page_size=None, **kwargs):
        params = values.of({
            "PageToken": page_token,
            "Page": page_number,
            "PageSize": page_size,
        })
        params.update(kwargs)
        
        return self._domain.page(
            self,
            IpAccessControlListMappingInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )


class IpAccessControlListMappingContext(InstanceContext):

    def __init__(self, domain, account_sid, domain_sid, sid):
        super(IpAccessControlListMappingContext, self).__init__(domain)
        
        # Path Solution
        self._instance_kwargs = {
            'account_sid': account_sid,
            'domain_sid': domain_sid,
            'sid': sid,
        }
        self._uri = "/Accounts/{account_sid}/SIP/Domains/{domain_sid}/IpAccessControlListMappings/{sid}.json".format(**self._instance_kwargs)

    def fetch(self):
        params = values.of({})
        
        return self._domain.fetch(
            IpAccessControlListMappingInstance,
            self._instance_kwargs,
            'GET',
            self._uri,
            params=params,
        )

    def delete(self):
        return self._domain.delete("delete", self._uri)


class IpAccessControlListMappingInstance(InstanceResource):

    def __init__(self, domain, payload, account_sid, domain_sid, sid=None):
        super(IpAccessControlListMappingInstance, self).__init__(domain)
        
        # Marshaled Properties
        self._account_sid = payload['account_sid']
        self._api_version = payload['api_version']
        self._date_created = deserialize.iso8601_datetime(payload['date_created'])
        self._date_updated = deserialize.iso8601_datetime(payload['date_updated'])
        self._friendly_name = payload['friendly_name']
        self._sid = payload['sid']
        self._uri = payload['uri']
        
        # Context
        self._lazy_context = None
        self._context_account_sid = account_sid
        self._context_domain_sid = domain_sid
        self._context_sid = sid or self._sid

    @property
    def _context(self):
        if self._lazy_context is None:
            self._lazy_context = IpAccessControlListMappingContext(
                self._domain,
                self._context_account_sid,
                self._context_domain_sid,
                self._context_sid,
            )
        return self._lazy_context

    @property
    def account_sid(self):
        """ The account_sid """
        return self._account_sid

    @property
    def api_version(self):
        """ The api_version """
        return self._api_version

    @property
    def date_created(self):
        """ The date_created """
        return self._date_created

    @property
    def date_updated(self):
        """ The date_updated """
        return self._date_updated

    @property
    def friendly_name(self):
        """ The friendly_name """
        return self._friendly_name

    @property
    def sid(self):
        """ The sid """
        return self._sid

    @property
    def uri(self):
        """ The uri """
        return self._uri

    def fetch(self):
        self._context.fetch()

    def delete(self):
        self._context.delete()