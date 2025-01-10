// @ts-nocheck
import Link from "'next/link'"
import { ArrowLeft, ArrowUpDown } from "'lucide-react'"

import { Button } from "@/components/ui/button"
import { Card, CardContent, CardDescription, CardHeader, CardTitle } from "@/components/ui/card"
import { Table, TableBody, TableCell, TableHead, TableHeader, TableRow } from "@/components/ui/table"
import {
  Chart,
  ChartArea,
  ChartAxisOptions,
  ChartGrid,
  ChartLine,
  ChartLinear,
  ChartTooltip,
} from "@/components/ui/chart"

// Mock data for the account
const accountData = {
  id: 1,
  name: "Account 1",
  value: 125000,
  performance: [
    { date: "'2023-01-01'", value: 100000 },
    { date: "'2023-02-01'", value: 102000 },
    { date: "'2023-03-01'", value: 105000 },
    { date: "'2023-04-01'", value: 103000 },
    { date: "'2023-05-01'", value: 110000 },
    { date: "'2023-06-01'", value: 115000 },
    { date: "'2023-07-01'", value: 125000 },
  ],
}

// Mock data for S&P 500
const spData = [
  { date: "'2023-01-01'", value: 3800 },
  { date: "'2023-02-01'", value: 3900 },
  { date: "'2023-03-01'", value: 3950 },
  { date: "'2023-04-01'", value: 4100 },
  { date: "'2023-05-01'", value: 4150 },
  { date: "'2023-06-01'", value: 4200 },
  { date: "'2023-07-01'", value: 4300 },
]

// Mock data for trades
const trades = [
  { id: 1, date: "'2023-07-15'", symbol: "'AAPL'", type: "'Buy'", quantity: 10, price: 150.25 },
  { id: 2, date: "'2023-07-14'", symbol: "'GOOGL'", type: "'Sell'", quantity: 5, price: 2750.10 },
  { id: 3, date: "'2023-07-13'", symbol: "'MSFT'", type: "'Buy'", quantity: 15, price: 305.75 },
  { id: 4, date: "'2023-07-12'", symbol: "'AMZN'", type: "'Buy'", quantity: 8, price: 3400.50 },
  { id: 5, date: "'2023-07-11'", symbol: "'TSLA'", type: "'Sell'", quantity: 20, price: 650.75 },
]

export function AccountDetail() {
  return (
    <div className="min-h-screen bg-black text-gray-100">
      <main className="container mx-auto px-4 py-8">
        <div className="flex items-center mb-8">
          <Link href="/" passHref>
            <Button variant="outline" size="icon" className="mr-4">
              <ArrowLeft className="h-4 w-4" />
            </Button>
          </Link>
          <h1 className="text-3xl font-bold text-white">{accountData.name}</h1>
        </div>

        <Card className="bg-gradient-to-br from-gray-900 to-gray-800 border-gray-700 shadow-lg mb-8">
          <CardHeader>
            <CardTitle className="text-white">Performance Overview</CardTitle>
            <CardDescription className="text-gray-400">
              Account value: ${accountData.value.toLocaleString()}
            </CardDescription>
          </CardHeader>
          <CardContent>
            <Chart className="w-full aspect-[4/3]">
              <ChartTooltip />
              <ChartGrid x={{ strokeDasharray: "'10 5'" }} y={{ strokeDasharray: "'10 5'" }} />
              <ChartArea />
              <ChartAxisOptions
                x={{
                  type: "'time'",
                  tickFormat: "'%b %Y'",
                  tickCount: 5,
                }}
                y={{
                  type: "'linear'",
                  tickFormat: (value) => `$${value.toLocaleString()}`,
                  tickCount: 5,
                }}
              />
              <ChartLine
                data={accountData.performance}
                xField="date"
                yField="value"
                stroke="hsl(var(--primary))"
                strokeWidth={2}
              />
              <ChartLine
                data={spData}
                xField="date"
                yField="value"
                stroke="hsl(var(--secondary))"
                strokeWidth={2}
              />
              <ChartLinear />
            </Chart>
            <div className="flex justify-center mt-4 space-x-4">
              <div className="flex items-center">
                <div className="w-3 h-3 bg-neutral-900 rounded-full mr-2 dark:bg-neutral-50" />
                <span className="text-sm text-gray-300">Account Performance</span>
              </div>
              <div className="flex items-center">
                <div className="w-3 h-3 bg-neutral-100 rounded-full mr-2 dark:bg-neutral-800" />
                <span className="text-sm text-gray-300">S&P 500</span>
              </div>
            </div>
          </CardContent>
        </Card>

        <Card className="bg-gradient-to-br from-gray-900 to-gray-800 border-gray-700 shadow-lg">
          <CardHeader>
            <CardTitle className="text-white">Recent Trades</CardTitle>
          </CardHeader>
          <CardContent>
            <Table>
              <TableHeader>
                <TableRow>
                  <TableHead className="text-gray-300">Date</TableHead>
                  <TableHead className="text-gray-300">Symbol</TableHead>
                  <TableHead className="text-gray-300">Type</TableHead>
                  <TableHead className="text-gray-300">Quantity</TableHead>
                  <TableHead className="text-gray-300">Price</TableHead>
                  <TableHead className="text-gray-300 text-right">Total</TableHead>
                </TableRow>
              </TableHeader>
              <TableBody>
                {trades.map((trade) => (
                  <TableRow key={trade.id}>
                    <TableCell className="text-gray-400">{trade.date}</TableCell>
                    <TableCell className="text-gray-400">{trade.symbol}</TableCell>
                    <TableCell className="text-gray-400">{trade.type}</TableCell>
                    <TableCell className="text-gray-400">{trade.quantity}</TableCell>
                    <TableCell className="text-gray-400">${trade.price.toFixed(2)}</TableCell>
                    <TableCell className="text-gray-400 text-right">
                      ${(trade.quantity * trade.price).toFixed(2)}
                    </TableCell>
                  </TableRow>
                ))}
              </TableBody>
            </Table>
          </CardContent>
        </Card>
      </main>
    </div>
  )
}