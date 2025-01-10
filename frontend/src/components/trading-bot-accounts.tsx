// @ts-nocheck
import { BarChart2, DollarSign } from "lucide-react"

import { useState, useEffect } from 'react'
import Chart from '@/components/ui/lineChart';
import { Card, CardContent, CardHeader, CardTitle } from "@/components/ui/card"
import { Carousel, CarouselContent, CarouselItem, CarouselNext, CarouselPrevious } from "@/components/ui/carousel"

import Github from "../assets/github.png";

const defaultAccounts = [
  { id: 1, name: "Optimized SMA-2", value: 100000, lastPurchase: "AAPL", lastPurchaseAmount: 5000, history: null },
  { id: 2, name: "Optimized SMA-2 [Backtest]", value: 100000, lastPurchase: "GOOGL", lastPurchaseAmount: 3000, history: null },
  { id: 3, name: "Basic Momentum-3", value: 100000, lastPurchase: "TSLA", lastPurchaseAmount: 2000, history: null  },
  { id: 4, name: "Momentum-3 [Backtest]", value: 100000, lastPurchase: "VTI", lastPurchaseAmount: 10000, history: null },
  { id: 5, name: "Neural network 1 [In Progress]", value: 100000, lastPurchase: "NVDA", lastPurchaseAmount: 4000, history: null },
]

export function TradingBotAccountsComponent() {
  const [accounts, setAccounts] = useState(defaultAccounts)

  useEffect(() => {
    async function fetchAccounts() {
      try {
        const response = await fetch('http://54.210.189.120:5000/api/accounts')
        if (!response.ok) {
          throw new Error(`Error fetching accounts: ${response.statusText}`)
        }
        const data = await response.json()
        setAccounts(data)
      } catch (error) {
        console.error(error)
      }
    }

    fetchAccounts()
  }, [])

  return (
    <div className="bg-black text-gray-100 flex justify-center items-center min-h-screen">
      <main className="mx-auto px-4 py-8 items-center justify-center">
        <h1 className="text-center text-4xl font-bold mb-8 text-white">NestTrade Accounts</h1>
        
        <Carousel className="w-full max-w-7xl mx-auto">
          <CarouselContent>
            {accounts.map((account) => (
              <CarouselItem key={account.id} className="md:basis-1/3">
                <Card className="bg-gradient-to-br from-gray-900 to-gray-800 border-gray-700 shadow-lg hover:shadow-xl transition-shadow duration-300 cursor-pointer h-full">
                  <CardHeader>
                    <CardTitle className="flex items-center justify-between text-white">
                      <span>{account.name}</span>
                      <DollarSign className="w-5 h-5" />
                    </CardTitle>
                  </CardHeader>
                  <CardContent className="bg-opacity-50 backdrop-filter backdrop-blur-sm">
                    <div className="h-32 bg-gradient-to-r from-gray-800 to-gray-700 rounded-md mb-4 flex items-center justify-center">
                      {
                        account.history ?
                        <Chart data={account.history}/> :
                        <>
                          Server might 
                          <BarChart2 className="w-16 h-16 text-white" /> 
                          <p>be down</p>
                        </>
                      }
                    </div>
                    <p className="text-sm text-gray-300 mb-2">Current Value: ${account.value.toLocaleString()}</p>
                    <p className="text-sm text-gray-300 mb-2">Last Purchase: {account.lastPurchase}</p>
                    <p className="text-sm text-gray-300">Amount: ${account.lastPurchaseAmount.toLocaleString()}</p>
                  </CardContent>
                </Card>
              </CarouselItem>
            ))}
          </CarouselContent>
          <div className="flex justify-center mt-4 space-x-2">
            <CarouselPrevious />
            <CarouselNext />
          </div>
        </Carousel>
  
        <section className="mt-12 mx-20 mb-12 bg-gradient-to-br from-gray-900 to-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
          <p className="text-gray-300 mb-4">
            NestTrade is a personal project which aims to test algorithmic and neural network strategies with a focus on clean UI and modular strategy. NestTrade runs 3 accounts using Alpaca.
          </p>
          <p className="text-gray-300 mb-4">
            Currently:
          </p>
          <p className="text-gray-300 mb-4">
            - SMA (50-day) crossovers to identify trend reversals, optimized with backtesting.py
          </p>
          <p className="text-gray-300 mb-4">
            - Momentum strategy (12-month, RSI: 70)
          </p>
          <p className="text-gray-300 mb-4">
            - In progress TensorFlow LSTM neural network trained on historical OHLCV
          </p>
          <a className="text-gray-300" href="https://github.com/gavin-St/trading-bot" target="_blank" rel="noopener noreferrer">
            <img src={Github} alt="GitHub Logo" className="w-11" />
          </a>
        </section>
      </main>
    </div>
  );  
}