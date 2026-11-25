'''Local-only compatibility module.

This module intentionally performs no network, filesystem, credential, or
external-service operations. It preserves the public interface names used by
older documentation, but synchronization is disabled.
'''


class CompetitorDataSync:
    '''Compatibility shim for local, conversation-only competitor page work.'''

    def __init__(self):
        self.enabled = False
        self.status = 'disabled: local-only skill'

    def load_ssh_key(self):
        '''Credential loading is disabled.'''
        return None

    def load_environment_config(self):
        '''Environment and context-file loading is disabled.'''
        return {}

    def fetch_discord_status(self):
        '''External service checks are disabled.'''
        return False

    def sync_competitor_data(self):
        '''Perform no synchronization and return a local status report.'''
        return {
            'enabled': False,
            'synced': False,
            'message': 'External synchronization is disabled; no data was sent.'
        }


def run_initialization():
    '''Report that initialization is unnecessary and no external actions ran.'''
    syncer = CompetitorDataSync()
    result = syncer.sync_competitor_data()
    print(result['message'])
    return result


if __name__ == '__main__':
    run_initialization()