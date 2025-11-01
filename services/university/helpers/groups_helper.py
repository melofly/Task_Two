from services.general.base_helper import BaseHelper


class GroupsHelper(BaseHelper):
    ENDPOINT_PREFIX = '/groups'

    ROOT_ENDPOINT = f'{ENDPOINT_PREFIX}/'
    GROUP_ID_ENDPOINT = f'{ENDPOINT_PREFIX}/{{group_id}}/'

    def post_create_group(self, json=None):
        res = self.api_utils.post(
            endpoint_url=self.ROOT_ENDPOINT,
            json=json
        )
        return res

    def get_groups(self):
        res = self.api_utils.get(
            endpoint_url=self.ROOT_ENDPOINT
        )
        return res

    def delete_groups(self, id: str):
        res = self.api_utils.delete(
            endpoint_url=self.GROUP_ID_ENDPOINT.format(group_id=id)
        )
        return res

    def get_group(self, id: str):
        res = self.api_utils.get(
            endpoint_url=self.GROUP_ID_ENDPOINT.format(group_id=id)
        )
        return res

    def put_group(self, id: str, json=None):
        res = self.api_utils.put(
            endpoint_url=self.GROUP_ID_ENDPOINT.format(group_id=id),
            json=json
        )
        return res