from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status
from .models import Operation
from .serializers import OperationSerializer


# @api_view(['GET'])
# def home(request):

#     ops = Operation.objects.all()
#     serializer = OperationSerializer(ops, many=True)
#     return Response(serializer.data)

@api_view(['POST'])
def calculate(request):
    context = {
        "slackUsername" : "maestro",
    }

    ADDITION = ['addition', 'add', 'sum', 'summation']
    SUBRACTION = ['difference', 'subtraction', 'reduce', 'decrease', 'minus']
    MULTIPLICATION = ['times', 'multiply', 'product', 'multiplication']

    serializer = OperationSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()

        # add words in operation_type in lower case to list
        wordList = [x.lower() for x in serializer.data['operation_type'].split(' ')]

        for x in wordList:
            if x in ADDITION:
                result = serializer.data['x'] + serializer.data['y']
                context['operation_type'] = 'addition'
                context['result'] = result
            
            elif x in SUBRACTION:
                result = serializer.data['x'] - serializer.data['y']
                context['operation_type'] = 'subtraction'
                context['result'] = result

            elif x in MULTIPLICATION:
                result = serializer.data['x'] * serializer.data['y']
                context['operation_type'] = 'multiplication'
                context['result'] = result

        # # Using model enum/choicefield
        # if serializer.data['operation_type'] == "addition":
        #     result = serializer.data['x'] + serializer.data['y']
        #     context['operation_type'] = serializer.data['operation_type']
        #     context['result'] = result
        #     # return Response(context)

        # if serializer.data['operation_type'] == "multiplication":
        #     result = serializer.data['x'] * serializer.data['y']
        #     context['operation_type'] = serializer.data['operation_type']
        #     context['result'] = result
        #     # return Response(context)

        # if serializer.data['operation_type'] == "subtraction":
        #     result = serializer.data['x'] - serializer.data['y']
        #     context['operation_type'] = serializer.data['operation_type']
        #     context['result'] = result
        #     # return Response(context)

        return Response(context)

    # If data is not valid
    else:
        print('Wahala!!')
        return Response(status=status.HTTP_404_NOT_FOUND)