from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from .models import Stake, UserBalance
from .serializers import StakeSerializer
from authentication.authentication import CustomAuthentication
import random
from decimal import Decimal

# Create your views here.

class StakeCreateView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        user = request.user
        amount = request.data.get('amount')
        prediction = request.data.get('prediction')
        user_balance, _ = UserBalance.objects.get_or_create(user=user)

        if not prediction:
            return Response({'error': 'Prediction is required.'}, status=status.HTTP_400_BAD_REQUEST)

        if not amount:
            return Response({'error': 'Amount is required.'}, status=status.HTTP_400_BAD_REQUEST)

        # Ensure amount is a positive number
        try:
            amount = Decimal(amount)
            if amount <= 0:
                raise ValueError
        except ValueError:
            return Response({'error': 'Amount must be a positive number.'}, status=status.HTTP_400_BAD_REQUEST)

        # Simulate coin toss
        coin_toss_result = random.choice(['HEAD', 'TAIL'])
        if coin_toss_result == prediction:
            # User wins, double the stake amount
            winning_amount = amount * Decimal('2')
            user_balance.balance += winning_amount
            user_balance.save()
            result = 'WIN'
        else:
            # User loses, deduct the stake amount
            user_balance.balance -= amount
            user_balance.save()
            result = 'LOSS'

        # Create stake record
        Stake.objects.create(user=user, amount=amount, prediction=prediction, result=result)

        return Response({'result': coin_toss_result, 'balance': user_balance.balance}, status=status.HTTP_200_OK)



class StakeHistoryView(APIView):
    permission_classes = [IsAuthenticated]
    authentication_classes = [CustomAuthentication]

    def get(self, request):
        stakes = Stake.objects.filter(user=request.user)
        serializer = StakeSerializer(stakes, many=True)
        return Response(serializer.data)
    
    