from django.contrib.admin import AdminSite


class CustomAdminSite(AdminSite):
    """Base custom admin site that implements
    custom authentication forms"""

    # INFO: For now just use the classic username login
    # login_form = forms.CustomAdminAuthenticationForm


# Create a custom admin which allows authenticating
# with the custom created email authentication model
custom_admin_site = CustomAdminSite(name='VideoPlatform')
