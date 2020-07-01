from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status, viewsets, mixins
from .models import Banks, Branches
from .serializers import BranchSerializer
import json

class BranchViewSet(mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    """
    A simple ViewSet for getting branch details using IFSC code.
    """
    queryset = Branches.objects.all()
    serializer_class = BranchSerializer


class AllBanksInCityView(APIView):
    """
    A Viewset for getting all branches of a bank in a city
    """

    def post(self,request):
        
        bank_name = request.POST.get("name",False)
        city = request.POST.get("city",False)

        if bank_name and city:
            
            bank = Banks.objects.get(name=bank_name.upper())
            banks_in_city = Branches.objects.filter(bank_id = bank.id, city = city.upper()).values('ifsc','branch','address','city','district','state')
            resultData = json.dumps(list(banks_in_city))
            #print(resultData)
            return Response({'result':resultData})

        else:
            return Response({'message':'Bank Name or City not found in the request'},status=status.HTTP_400_BAD_REQUEST)
