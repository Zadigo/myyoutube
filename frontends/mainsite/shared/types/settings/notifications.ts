type NotificationTypes = 'subscribed_channel_activity' | 'video_recommendation' | 'channel_activity' | 'replies_activity' | 'mentions' | 'repost'

export type NotificationProfile = {
    [key in NotificationTypes]: boolean
}
