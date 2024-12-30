export * from './authentication'
export * from './feed'
export * from './channels'
export * from './comments'
export * from './video'
export * from './studio'

export type VideoMenuAction = 'Store' | 'Download' | 'Save' | 'Gift' | 'Donate' | 'Share' | 'Recommendations' | 'Community note' | 'Classify' | 'Fact check' | 'Report'

export interface VideoMenuItem {
    name: VideoMenuAction
    icon: string
}

export interface SessionCache {
    categories: []
}
