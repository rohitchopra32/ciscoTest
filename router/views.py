import traceback
import datetime
from django.utils import timezone

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.renderers import TemplateHTMLRenderer
from oauth2_provider.contrib.rest_framework import TokenHasReadWriteScope
from oauth2_provider.models import Application, AccessToken
from oauthlib.common import generate_token

from router.models import Router
from router.serializer import RouterSerializer


class RouterView(APIView):
    serializer_class = RouterSerializer
    model = Router
    permission_classes = [TokenHasReadWriteScope]

    def get_queryset(self):
        return self.model.objects.filter(is_active=True)

    def get(self, request):
        try:
            queryset = self.get_queryset()

            router_type = request.GET.get("router_type")
            if router_type:
                queryset = queryset.filter(router_type=router_type)

            input1 = request.GET.get("input1")
            input2 = request.GET.get("input2")

            if input1 and input2:
                queryset = queryset.filter(loopback__range=[input1, input2])

            response_data = self.serializer_class(queryset, many=True)

            return Response({'success': True, 'data': response_data.data}, status=200)
        except Exception as error:
            traceback.print_exc()
            return Response({"success": False, "error": error}, status=400)

    def post(self, request):
        try:
            data = request.data
            serailized_data = self.serializer_class(data=data)
            if not serailized_data.is_valid():
                error = serailized_data.errors.copy()
                error.update({
                    "success": False
                })
                return Response(error, status=400)
            serailized_data.save()
            return Response({'success': True, 'data': serailized_data.validated_data}, status=200)
        except Exception as error:
            traceback.print_exc()
            return Response({"success": False, "error": error}, status=400)

    def put(self, request):
        try:
            data = request.data
            print(data)
            router_obj = Router.objects.get(id=data["id"])
            serailized_data = self.serializer_class(router_obj, data=data)
            if not serailized_data.is_valid():
                error = serailized_data.errors.copy()
                error.update({
                    "success": False
                })
                return Response(error, status=400)
            serailized_data.update(router_obj, serailized_data.validated_data)
            return Response({'success': True, 'data': serailized_data.validated_data}, status=200)
        except Exception as error:
            traceback.print_exc()
            return Response({"success": False, "error": str(error)}, status=400)

    def delete(self, request):
        try:
            obj_id = request.GET.get("id")
            if not obj_id:
                return Response({"success": False, "error": "Router id not provided"}, status=400)
            router_obj = Router.objects.get(id=obj_id)
            router_obj.is_active = False
            router_obj.save()
            return Response({"success": True, "data": "Router Deleted"}, status=200)
        except Exception as error:
            traceback.print_exc()
            return Response({"success": False, "error": str(error)}, status=400)


class GetToken(APIView):
    def get(self, request):
        from django.contrib.auth.models import User
        user = User.objects.all()[0]
        application = Application.objects.get_or_create(user=user)[0]
        token_obj = AccessToken.objects.get_or_create(
            user=user,
            token=generate_token(),
            application=application,
            scope="read write",
            expires=timezone.now() + datetime.timedelta(days=365)
        )[0]
        return Response({"Token": token_obj.token})


class RouterTemplate(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self,request):
        return Response(template_name='home_page.html')


class SearchByIpAddrRange(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self,request):
        return Response(template_name='ip_addr_range.html')


class SearchByRouterType(APIView):
    renderer_classes = [TemplateHTMLRenderer]

    def get(self,request):
        return Response(template_name='router_type.html')