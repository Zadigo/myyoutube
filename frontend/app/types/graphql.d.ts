/**
 * Type for Relay Node structure
 * @example
 * ```ts
 * const relayNode: RelayNode<Video> = { edges: [ { node: Video }, ... ] }
 * ```
 */
type RelayNode<N> = {
  edges: Array<{ node: N }>
}

/**
 * Type for GraphQL paginated response using Relay-style pagination
 * @example
 * ```ts
 * const response = await $fetch<GraphQlResponse<'searchvideos', Video>>(...)
 * const videos: Video[] = response.data.searchvideos.edges.map(edge => edge.node)
 * ```  
 */
export type GraphQlResponse<T extends string, R = Record<string, unknown>> = {
  data: {
    [key in T]: {
      edges: Array<{ node: R }>
    }
  }
}

/**
 * Type for GraphQL single object response
 * @example
 * ```ts
 * const response = await $fetch<GraphQlSingleResponse<'getUser', User>>(...)
 * const user: User = response.data.getUser
 * ```
 */
export type GraphQlSingleResponse<T extends string, R = Record<string, unknown>> = {
  data: {
    [key in T]: R
  }
}

/**
 * Type for GraphQL edges structure using Relay-style pagination
 * @example
 * ```ts
 * const videos: GraphQlEdges<Video> = { edges: [ { node: Video }, ... ] }
 * ```
 */
export type GraphQlEdges<T> = { edges: Array<{ node: T }> }

/**
 * Type for GraphQL pagination info using Relay-style pagination
 */
export interface GraphQlPaginationInfo {
  pageInfo: {
    startCursor: string
    endCursor: string
    hasNextPage: boolean
    hasPreviousPage: boolean
  }
}

