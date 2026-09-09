import type { BlockingDuration } from '~/utils/constants'
import type { CustomUser } from '../accounts'
import type { UserChannel } from '../channels'

export interface BlockedKeyword {
  word: string
  duration: BlockingDuration
}

export interface BlockedChannel {
  channel: UserChannel
  user: CustomUser
}
