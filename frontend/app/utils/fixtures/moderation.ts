import type { CommunityNotes } from '~/types'
import { faker } from '@faker-js/faker'

export const communityNotesFixture: CommunityNotes = {
  data: {
    allnotes: {
      edges: [
        {
          node: {
            id: 'note1',
            title: faker.lorem.sentence({ min: 1, max: 3 }),
            description: faker.lorem.paragraph({ min: 2, max: 5 }),
            reference: 'no_zefino322fzinfo',
            createdOn: '2024-06-01T12:00:00Z',
            creatorId: 'user123',
            upvotes: faker.number.int({ min: 0, max: 100 }),
            downvotes: faker.number.int({ min: 0, max: 100 }),
            score: faker.number.int({ min: 0, max: 100 }),
            status: 'APPROVED',
            subjectCreatorId: 'Kendall Marquez',
            author: {
              id: 'user123',
              username: faker.person.fullName({ sex: 'generic' }),
            },
            noteSources: [
              {
                id: 'source1',
                url: 'https://example.com/source1',
                reference: 'Source 1 reference',
                sourceCredibility: 8,
                updatedOn: '2024-05-30T10:00:00Z',
                createdOn: '2024-05-25T09:00:00Z',
              },
              {
                id: 'source2',
                url: 'https://example.com/source2',
                reference: 'Source 2 reference',
                sourceCredibility: 7,
                updatedOn: '2024-05-28T11:00:00Z',
                createdOn: '2024-05-20T08:00:00Z',
              }
            ]
          }
        },
        {
          node: {
            id: 'note2',
            reference: 'no_zefino322fzinfo2',
            title: faker.lorem.sentence({ min: 1, max: 3 }),
            description: faker.lorem.paragraph({ min: 2, max: 5 }),
            createdOn: '2024-06-02T14:30:00Z',
            creatorId: 'user456',
            upvotes: faker.number.int({ min: 0, max: 100 }),
            downvotes: faker.number.int({ min: 0, max: 100 }),
            score: faker.number.int({ min: 0, max: 100 }),
            status: 'PENDING',
            subjectCreatorId: faker.person.fullName({ sex: 'generic' }),
            author: {
              id: 'user456',
              username: faker.person.fullName({ sex: 'generic' }),
            },
            noteSources: [
              {
                id: 'source3',
                url: 'https://example.com/source3',
                reference: 'Source 3 reference',
                sourceCredibility: 6,
                updatedOn: '2024-05-29T12:00:00Z',
                createdOn: '2024-05-22T07:00:00Z',
              }
            ]
          }
        }
      ]
    }
  }
}
