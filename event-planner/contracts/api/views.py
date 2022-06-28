from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .contractSerializer import ContractSerializer
from ..models import Contract


@api_view(['GET'])
def ApiOverview(request):
    api_urls = {
        'all_contracts': '/',
        'Add': '/create',
        'Update': 'update/pk',
        'Delete': '/contract/pk/delete'
    }

    return Response(api_urls)


@api_view(['POST'])
def add_contract(request):
    contract = ContractSerializer(data=request.data)
    if contract.is_valid():
        contract.save()
        return Response(contract.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def all_contracts(request):
    # checking for the parameters from the URL
    contracts = Contract.objects.all()
    serializer = ContractSerializer(contracts, many=True)

    # if there is something in items else raise error
    if contracts:
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['PUT'])
def update_contracts(request, pk):
    contract = Contract.objects.get(pk=pk)
    data = ContractSerializer(instance=contract, data=request.data)
    if data.is_valid():
        data.save()
        return Response(data.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
