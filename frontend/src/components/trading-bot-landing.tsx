import Link from "'next/link'"
import { ArrowRight, BarChart2, Bot, DollarSign, LineChart, TrendingUp } from "lucide-react"

import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"

export function TradingBotLandingComponent() {
  return (
    <div className="min-h-screen bg-black text-gray-100">
      <main className="container mx-auto px-4 py-8">
        <h1 className="text-4xl font-bold mb-8 text-center text-white">TradeMaster AI</h1>
        
        <div className="grid md:grid-cols-3 gap-6 mb-12">
          <Card className="bg-gradient-to-br from-gray-900 to-gray-800 border-gray-700 shadow-lg hover:shadow-xl transition-shadow duration-300">
            <CardHeader>
              <CardTitle className="flex items-center text-white">
                <DollarSign className="mr-2" />
                Portfolio Summary
              </CardTitle>
            </CardHeader>
            <CardContent className="bg-opacity-50 backdrop-filter backdrop-blur-sm">
              <div className="h-40 bg-gradient-to-r from-gray-800 to-gray-700 rounded-md mb-4 flex items-center justify-center">
                <LineChart className="w-20 h-20 text-white" />
              </div>
              <p className="text-sm text-gray-300">Current Value: $125,000</p>
              <p className="text-sm text-gray-300">Assets: 15</p>
              <p className="text-sm text-gray-300">Recent Trades: 7</p>
              <Button className="w-full mt-4 bg-gray-700 hover:bg-gray-600 text-white border-gray-600">
                View Details
                <ArrowRight className="ml-2 h-4 w-4" />
              </Button>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-br from-gray-900 to-gray-800 border-gray-700 shadow-lg hover:shadow-xl transition-shadow duration-300">
            <CardHeader>
              <CardTitle className="flex items-center text-white">
                <Bot className="mr-2" />
                Bot Summary
              </CardTitle>
            </CardHeader>
            <CardContent className="bg-opacity-50 backdrop-filter backdrop-blur-sm">
              <div className="h-40 bg-gradient-to-r from-gray-800 to-gray-700 rounded-md mb-4 flex items-center justify-center">
                <BarChart2 className="w-20 h-20 text-white" />
              </div>
              <p className="text-sm text-gray-300">Performance: +15.2%</p>
              <p className="text-sm text-gray-300">Strategy Adjustments: 3</p>
              <p className="text-sm text-gray-300">Trading Volume: $50,000/day</p>
              <Button className="w-full mt-4 bg-gray-700 hover:bg-gray-600 text-white border-gray-600">
                View Details
                <ArrowRight className="ml-2 h-4 w-4" />
              </Button>
            </CardContent>
          </Card>

          <Card className="bg-gradient-to-br from-gray-900 to-gray-800 border-gray-700 shadow-lg hover:shadow-xl transition-shadow duration-300">
            <CardHeader>
              <CardTitle className="flex items-center text-white">
                <TrendingUp className="mr-2" />
                Live Market Data
              </CardTitle>
            </CardHeader>
            <CardContent className="bg-opacity-50 backdrop-filter backdrop-blur-sm">
              <div className="h-40 bg-gradient-to-r from-gray-800 to-gray-700 rounded-md mb-4 overflow-hidden">
                <div className="p-2">
                  <p className="text-xs text-gray-300">AAPL: $150.25 (+1.2%) - Buy</p>
                  <p className="text-xs text-gray-300">GOOGL: $2,750.10 (-0.5%) - Hold</p>
                  <p className="text-xs text-gray-300">MSFT: $305.75 (+0.8%) - Buy</p>
                  <p className="text-xs text-gray-300">AMZN: $3,400.50 (+2.1%) - Strong Buy</p>
                </div>
              </div>
              <p className="text-sm text-gray-300">S&P 500 Index: 4,200.50</p>
              <p className="text-sm text-gray-300">Market Trend: Bullish</p>
              <Button className="w-full mt-4 bg-gray-700 hover:bg-gray-600 text-white border-gray-600">
                View All Data
                <ArrowRight className="ml-2 h-4 w-4" />
              </Button>
            </CardContent>
          </Card>
        </div>

        <section className="mb-12 bg-gradient-to-br from-gray-900 to-gray-800 p-6 rounded-lg shadow-lg hover:shadow-xl transition-shadow duration-300">
          <h2 className="text-2xl font-semibold mb-4 text-white">How It Works</h2>
          <p className="text-gray-300 mb-4">
            TradeMaster AI is an advanced trading bot that uses machine learning algorithms to analyze market trends, 
            company fundamentals, and global economic indicators. Our AI-powered system makes data-driven decisions 
            to optimize your investment portfolio and maximize returns while managing risk.
          </p>
          <p className="text-gray-300 mb-4">
            The bot continuously learns from market behavior and adjusts its strategies in real-time. It can execute 
            trades automatically or provide suggestions for manual trading, giving you full control over your 
            investment approach.
          </p>
          <p className="text-gray-300">
            With TradeMaster AI, you get the benefits of algorithmic trading combined with the flexibility to 
            customize strategies based on your investment goals and risk tolerance.
          </p>
        </section>

        <div className="text-center">
          <Button size="lg" className="bg-white text-black hover:bg-gray-200">
            Get Started
            <ArrowRight className="ml-2 h-5 w-5" />
          </Button>
        </div>
      </main>
    </div>
  )
}