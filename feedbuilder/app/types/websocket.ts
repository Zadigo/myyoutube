import type { FeedBlocks, NewFeed, VideoItem } from '.'

export interface WebsocketMessage {
  action: 'initial_feed' 
    | 'update_feed' 
    | 'add_block' 
    | 'delete_block' 
    | 'update_feed_videos'
    | 'set_current_feed'
    | 'searching'
    | 'feed_videos'
}

export interface MessageSetCurrentFeed extends WebsocketMessage {
  feed: NewFeed | undefined
}

export interface MessageReceivedFeedVideos extends WebsocketMessage {
  videos: VideoItem[]
}
