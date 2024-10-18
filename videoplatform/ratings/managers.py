from django.db.models import QuerySet
from django.db.models.aggregates import Count
from django.db.models.query_utils import Q

from ratings.choices import RatingFor, RatingTypes


class RatingManager(QuerySet):
    @staticmethod
    def _build_details(user, video, method='video', rating_type='like'):
        """
        Base dictionnary used in order to create a new rating

        Args:
            user (obj): a valid user object
            video (obj): a valid video object represeting the current video
            method (str, optional): the item for which the rating is for. Defaults to 'video'.
            rating_type (str, optional): the type of rating like/dislike. Defaults to 'like'.

        Returns:
            dict: a dict of the values for creating a new rating
        """
        allowed_methods = ['video', 'comment', 'reply']

        details = {
            'user': user,
            'video': video
        }

        if rating_type == 'like':
            details.update({'rating_type': RatingTypes.LIKE})
        elif rating_type == 'dislike':
            details.update({'rating_type': RatingTypes.DISLIKE})
        else:
            return False

        if method in allowed_methods:
            if method == 'video':
                details.update({'rating_for': RatingFor.VIDEO})
        else:
            return False
        
        return details

    def _created_rating(self, details):
        """
        Create a new rating for the user using
        a set of details

        Parameters

            details (dict): the items to use for creatin the new rating

        Returns:
            obj: a newly created rating from the database
        """
        already_has_ratings = (
            Q(rating_type=RatingTypes.LIKE) | 
            Q(rating_type=RatingTypes.DISLIKE) & 
            Q(user=details['user'])
        )
        ratings = self.filter(already_has_ratings)
        # Since a user cannot have multiple ratings,
        # we have to check that a rating already exists
        # and if it does, just simply change
        if ratings.exists():
            try:
                return ratings.get()
            except:
                return False
        else:
            new_rating = self.create(**details)
            return new_rating

    def _compute_likes_dislikes(self, video):
        ratings = video.rating_set.all()
        return {
            'likes': ratings.filter(rating_type=RatingTypes.LIKE).count(),
            'dislikes': ratings.filter(rating_type=RatingTypes.DISLIKE).count()
        }

    def add_like(self, request, video, method):
        details = self._build_details(
            request.user,
            video,
            method=method,
            rating_type='like'
        )
        state = False
        if details:
            new_rating = self._created_rating(details)
            state = True if new_rating else False
        return state, self._compute_likes_dislikes(video=video)

    def add_dislike(self, request, video, method):
        details = self._build_details(
            request.user,
            video,
            method=method,
            rating_type='dislike'
        )
        state = False
        if details:
            new_rating = self._created_rating(details)
            state = True if new_rating else False
        return state, self._compute_likes_dislikes(video)

    def remove_like_or_dislike(self, request, video, method):
        rating_for = RatingFor.VIDEO
        if method == 'comment':
            rating_for = RatingFor.COMMENT

        if method == 'reply':
            rating_for = RatingFor.REPLY

        logic = (
            Q(rating_type=RatingTypes.LIKE) |
            Q(rating_type=RatingTypes.DISLIKE) &
            Q(user=request.user) &
            Q(video__reference=video.reference) &
            Q(rating_for=rating_for)
        )
        try:
            rating = self.get(logic)
        except:
            return False
        else:
            rating = rating.delete()
            return True, self._compute_likes_dislikes(video)

    def switch_rating(self, request, video):
        """
        Switches a rating from Like to Dislike
        or inversely

        Parameters
        ----------

                request (type): HTTP request
                video (type): video ID

        Returns
        -------

                tuple: state and likes/dislikes count
        """
        logic = (
            Q(user=request.user) &
            Q(video__reference=video.reference)
        )
        try:
            rating = self.get(logic)
        except:
            rating = False
        else:
            if rating.rating_type == RatingTypes.LIKE.value:
                rating.rating_type = RatingTypes.DISLIKE
            else:
                rating.rating_type = RatingTypes.LIKE
            rating.save()
            rating = True
        return rating, self._compute_likes_dislikes(video)
