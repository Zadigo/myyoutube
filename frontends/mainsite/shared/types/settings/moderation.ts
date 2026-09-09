import type { BlockingDuration } from '~/constants/settings'
import type { BaseUser } from '../accounts'
import type { BaseUserChannel } from '../channels'

export interface BlockedKeyword {
  word: string
  duration: BlockingDuration
}

export interface BlockedChannel {
  channel: BaseUserChannel
  user: BaseUser
}
