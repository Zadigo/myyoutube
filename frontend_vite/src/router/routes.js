const routes = [
  {
    path: '/',
    component: () => import('../layouts/BaseLayout.vue'),
    children: [
      {
        path: '/',
        name: 'feed',
        meta: { requiresAuthentication: false },
        component: async () => import('../pages/FeedPage.vue')
      }
    ]
  }
]

export default routes
