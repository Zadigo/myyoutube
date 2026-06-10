import dataclasses
from typing import Any

from channels.db import database_sync_to_async
from channels.generic.websocket import AsyncJsonWebsocketConsumer
from videos.models import Video
from django.db.models.query import QuerySet
from videos.api.serializers import VideoSerializer
from django.utils import timezone


@dataclasses.dataclass
class Block:
    position: int
    component: str
    data: dict[str, str]


@dataclasses.dataclass
class Feed:
    name: str
    blocks: list[Block] = dataclasses.field(default_factory=lambda: [])


class FeedBuilderMixin(AsyncJsonWebsocketConsumer):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.temp_feeds = []
        self.feeds = []
        self.current_feed: Feed | None = None

    def filter_source(self, source: str, limit: str, queryset: QuerySet[Video]) -> QuerySet[Video] | list:
        accepted_sources = ['Tags', 'Single user',
                            'List', 'Feed', 'Single post', 'Labels']
        accepted_duration = ['30 minutes', '3 hours',
                             '12 hours', '24 hours', '3 days', '7 days']

        if source not in accepted_sources:
            return []

        if limit not in accepted_duration:
            return []

        if source == 'Tags':
            pass

        if source == 'Single user':
            pass

        current_date = timezone.now()

        if limit == '7 days':
            return queryset.filter(created_at__gte=current_date - timezone.timedelta(days=7))

        if limit == '3 days':
            return queryset.filter(created_at__gte=current_date - timezone.timedelta(days=3))

        if limit == '24 hours':
            return queryset.filter(created_at__gte=current_date - timezone.timedelta(hours=24))

        if limit == '12 hours':
            return queryset.filter(created_at__gte=current_date - timezone.timedelta(hours=12))

        if limit == '3 hours':
            return queryset.filter(created_at__gte=current_date - timezone.timedelta(hours=3))

        if limit == '30 minutes':
            return queryset.filter(created_at__gte=current_date - timezone.timedelta(minutes=30))

    @database_sync_to_async
    def get_videos(self):
        queryset = Video.objects.filter(active=True)

        print(self.current_feed)
        if self.current_feed:
            for block in self.current_feed.blocks:
                if block.component == 'BlockSource':
                    source = block.data.get('source', 'Entire network')
                    limit = block.data.get('limit', '7 days')

                    queryset = self.filter_source(source, limit, queryset)

                # elif block.component == 'BlockRegex':
                #     regex = block.data.get('regex', '')
                #     if regex:
                #         queryset = queryset.filter(title__iregex=regex)

                # elif block.component == 'BlockSort':
                #     sort_by = block.data.get('sort_by', '')
                #     if sort_by:
                #         queryset = queryset.order_by(sort_by)

        serializer = VideoSerializer(instance=queryset, many=True)
        return serializer.data


class FeedBuilderConsumer(FeedBuilderMixin):
    async def connect(self):
        await self.accept()
        await self.send_json({
            'type': 'connected',
            'feeds': self.temp_feeds
        })

    async def disconnect(self, close_code):
        await self.close(code=close_code)

    async def send_error(self, message: str):
        await self.send_json({
            'type': 'error',
            'message': message
        })

    async def receive_json(self, content: dict[str, Any], **kwargs):
        # print(content)

        action: str | None = content.get('action', None)

        if action:
            if action == 'initial_feeds':
                pass

            if action == 'set_current_feed':
                current_feed = content.get('feed', None)
                if current_feed is not None:
                    blocks = [
                        Block(
                            position=block.get('position', 0),
                            component=block.get('component', ''),
                            data=block.get('data', {})
                        ) for block in current_feed.get('blocks', [])
                    ]

                    self.current_feed = Feed(
                        name=current_feed.get('name', 'Unnamed Feed'),
                        blocks=blocks
                    )

            if action == 'update_feed':
                pass

            if action == 'add_block':
                pass

            if action == 'delete_block':
                pass

            if action == 'update_feed_videos':
                current_feed = content.get('feed', None)
                print('update_feed_videos', current_feed)
                await self.send_json({'action': 'searching'})
                data = await self.get_videos()
                print(data)
                await self.send_json({'action': 'feed_videos', 'videos': list(data)})
        else:
            await self.send_error('Invalid action specified')
