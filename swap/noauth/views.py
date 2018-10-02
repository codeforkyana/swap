from django.conf import settings
from django.forms import ValidationError
from django.shortcuts import redirect, render
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _
from django.views import View
from django.views.generic.edit import FormView

from noauth.models import AuthCode

from .forms import CodeForm, LoginForm
from .models import AuthCode, User


class CodeView(View):
    form_class = CodeForm
    template_name = "code.html"
    success_url = "/"

    def get(self, request, *args, **kwargs):
        email = self.request.GET.get("email")
        code = self.request.GET.get("code")

        if email and code:
            next_page = self._validate_and_redirect(email, code)
            if next_page:
                return redirect(next_page)

        form = self.form_class(initial={"email": email})
        return render(request, self.template_name, {"form": form})

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data["email"]
            code = form.cleaned_data["code"]
            next_page = self._validate_and_redirect(email, code)
            if next_page:
                return redirect(next_page)

            form.add_error(
                None,
                ValidationError(
                    _("Invalid e-mail address or code."), code="invalid_email_or_code"
                ),
            )

        return render(request, self.template_name, {"form": form})

    @classmethod
    def _validate_and_redirect(cls, email, code):
        auth_code = AuthCode.get_auth_code(email, code)
        if not auth_code:
            return None
        auth_code.delete()
        return auth_code.next_page or "/"


class LoginView(FormView):
    """Handled the login form where users enter their email addresses to start the login process.
    After entering an email address, the user will be sent a log in link and code they can use to log in without a password.
    If a user doesn't exist, a user is created."""

    template_name = "login.html"
    form_class = LoginForm
    success_url = reverse_lazy("noauth:code")

    def form_valid(self, form):
        email = form.cleaned_data["email"]
        district = form.cleaned_data["district"]
        user = self.get_user(email)
        if not user:
            user = self.create_user(email, district)

        if AuthCode.send_auth_code(user):
            self.success_url += f"?email={user.username}"
            return super().form_valid(form)
        else:
            form.add_error(
                None,
                _(
                    f"Please check your inbox and spam folder for a previously-sent code."
                ),
            )
            return super().form_invalid(form)

    def create_user(self, email, district):
        return User.objects.create_user(email, email, "NOPE", district=district)

    def get_user(self, email):
        try:
            return User.objects.get(email=email)
        except User.DoesNotExist:
            return None
