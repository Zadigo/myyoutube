import type { BaseUserChannel, GraphQlData } from "~/types";

export const userChannelsFixture: GraphQlData<'userChannel', BaseUserChannel> = {
  data: {
    userChannel: {
      id: '1',
      reference: 'tech-reviews',
      name: 'Tech Reviews',
      description: 'Latest reviews on tech gadgets and software.',
      banner: 'https://example.com/banners/tech-reviews.jpg',
      category: 'Technology',
      createdOn: '2023-01-15T10:00:00Z',
      isVerified: true,
      instagram: 'tech_reviews',
      facebook: 'techreviews',
      tiktok: 'tech_reviews',
      tags: [],
      subscribers: [],
      channelplaylistSet: []
    }
  }
}
