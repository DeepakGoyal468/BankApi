from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import BankSerializer, BranchSerializer
from .models import Bank, Branch
from rest_framework.permissions import IsAuthenticated

# Create your views here.


class BankDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        banks = Bank.objects.all()
        code = request.GET.get('ifsc', '')
        limit = request.GET.get('limit', '')
        offset = request.GET.get('offset', '0')
        if code != '':
            bank_id = Branch.objects.get(ifsc_code__exact=code).bank_id
            banks = banks.filter(pk=bank_id)

        banks = pagination(banks, limit, offset)
        banks_json = BankSerializer(banks, many=True)

        return Response(banks_json.data)


class BranchDetail(APIView):
    permission_classes = (IsAuthenticated,)

    def get(self, request):
        branches = Branch.objects.all()
        bank_name = request.GET.get('bank', '')
        city_name = request.GET.get('city', '')
        limit = request.GET.get('limit', '')
        offset = request.GET.get('offset', '0')
        if bank_name != '':
            bank_id = Bank.objects.get(name=bank_name.upper()).id
            branches = branches.filter(bank_id=bank_id)
        if city_name != '':
            branches = branches.filter(city=city_name.upper())

        branches = pagination(branches, limit, offset)
        branches_json = BranchSerializer(branches, many=True)
        return Response(branches_json.data)


def pagination(data, limit, offset):
    if limit != '':
        data = data[int(offset):int(offset) + int(limit)]
    elif offset != '' and limit == '':
        data = data[int(offset):]

    return data
