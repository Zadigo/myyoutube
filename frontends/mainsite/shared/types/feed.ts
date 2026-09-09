import type { BaseUser, BaseUserProfile } from './accounts'
import type { BaseUserChannel } from './channels'
import type { RelayNode, RelayEdge, GraphQlData } from './graphql'
import type { BaseVideo } from './video'
import type { DefaultMainCategories } from '~/constants/categories'
import type { DefaultVideoLength, DefaultUploadDate, DefaultSortBy } from '~/constants/filtering'

interface _SearchQuery {
  search: string
  category: DefaultMainCategories
  videoLength: DefaultVideoLength
  uploadDate: DefaultUploadDate
  sortBy: DefaultSortBy
}

/**
 * Search query parameters for video searches
 */
export type SearchQuery = Partial<_SearchQuery>

/**
 * Basic Fields included in a basic video type used in feed listings
 */
export type BaseVideoFields = 'id' | 'title' | 'description' | 'video' | 'views' | 'videoId' | 'createdOn'

/**
 * Simple feed video type used in feed listings
 */
export type FeedVideo<F extends BaseVideoFields = BaseVideoFields> = Pick<BaseVideo, F> & { user: Pick<BaseUser, 'id' | 'username'> & { userProfile: Pick<BaseUserProfile, 'avatar'> } } & { userChannel: Pick<BaseUserChannel, 'id' | 'name' | 'reference'> }

/**
 * Detailed video type used in video details page
 */
export type VideoDetails = BaseVideo & { user: BaseUser & { userProfile: BaseUserProfile } } & { userChannel: BaseUserChannel }


export type FeedVideoNode = RelayNode<FeedVideo>

export type FeedVideos = RelayEdge<FeedVideo>

export type Feed = GraphQlData<'allVideos', FeedVideos>
