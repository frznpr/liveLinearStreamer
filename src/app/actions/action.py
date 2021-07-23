class Action:

    async def playlist_not_found(self):
        return {'error': 'Playlist not found'}

    async def playable_video_not_found(self):
        return {'error': 'No streamable video found'}
