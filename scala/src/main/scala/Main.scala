import java.util.Date

import scala.collection.immutable.{HashMap, Vector}
import scala.io.Source
import scala.util.Random

//aws ecr get-login --region us-east-1
//docker build -t findw .
//docker tag findw:latest 086582756756.dkr.ecr.us-east-1.amazonaws.com/findw:latest
//docker push 086582756756.dkr.ecr.us-east-1.amazonaws.com/findw:latest


/**
  * Created by gcrowell on 4/11/2017.
  */

//TODO create holding class
//TODO create book value class

class BuySignal(val symbol: String, val date_id: Int, val signal_strength: Double = 1.0) {
  override def toString: String =
    s"Buy Signal: $symbol on $date_id"
}

case class BuyTransaction(symbol: String, date_id: Int, quantity: Double, book_price: Double, book_value: Double) {}


object CrystalBall {
  var signals = new HashMap[Int, Vector[BuySignal]]

  def getBuySignals(date_id: Int): Vector[BuySignal] = {
    return signals.get(date_id).get
  }

  override def toString: String =
    s"Crystal Ball: date_id (${signals.keys.min} to ${signals.keys.max})"

}

object Market {
  var priceData = new HashMap[String, HashMap[Int, Double]]

  def getStart(): Int = {
    return 0
  }

  def getEnd(): Int = {
    return 3
  }

  def getPrice(symbol: String, date_id: Int): Double = {
    return priceData.get(symbol).get.get(date_id).get
  }

  def getPrices(symbols: Vector[String], date_id: Int): Iterable[Double] = {
    //    priceData.filter( (x: String, HashMap[Int, Float])=>true)
    val symbolFilterFn = (symbol: String) => symbols.contains(symbol)
    val dateFilterFn = (in_date_id: Int) => in_date_id == date_id
    val tmp = priceData.filterKeys(symbolFilterFn).map(_._2.get(date_id))
    return tmp.map(_.get)
    //    val outPriceData = priceData.filterKeys(symbolFilterFn).valuesIterator.map((priceData:HashMap[Int, Float])=>)
    //      filterKeys(dateFilterFn)

  }
}


object Bot {
  var portfolioBookValue = HashMap[Int, Double]()
  var portfolioTransactions = HashMap[Int, List[BuyTransaction]]()
  val market = Market
  val crystalBall = CrystalBall
  //TODO store holdings, list of stocks bought yesterday

  def execute_sells(buyTransactions: List[BuyTransaction], date_id: Int): Double = {
    println(s"executing sells (date_id: $date_id)...")
    val market_values = buyTransactions.view.map {
      case (trans) =>
        (market.getPrice(trans.symbol, date_id) / trans.book_price) * trans.book_value
    }
    portfolioBookValue += (date_id -> market_values.sum)
    println(s"\tportfolioBookValue: $portfolioBookValue")
    return market_values.sum
  }

  def execute_buys(buySignals: Vector[BuySignal], available_cash: Double, date_id: Int): List[BuyTransaction] = {
    println(s"executing buys...")
    println(s"\tbuy signals: ${buySignals}")
    val symbols = buySignals.view.map(_.symbol)
    val denom = buySignals.view.map(_.signal_strength).sum
    val weights = buySignals.view.map(_.signal_strength / denom)
    val cash_allocations = weights.view.map(_ / available_cash)
    val stock_prices = market.getPrices(buySignals.map(_.symbol), date_id)
    println(s"\tstock prices: ${stock_prices}")
    val trade_qtys = cash_allocations.zip(stock_prices).view.map { case (cash, price) => cash / price }
    println(s"\ttrade_qtys: ${trade_qtys.toList}")
    val book_values = trade_qtys.zip(stock_prices).view.map { case (qty, price) => qty * price }
    val date_ids = List.fill(symbols.size)(date_id)

    val buyTransactions = for {
      List(symbol: String, date_id: Int, quantity: Double, book_price: Double, book_value: Double)
      <- List(symbols, date_ids, trade_qtys, stock_prices, book_values).transpose
    } yield BuyTransaction(symbol, date_id, quantity, book_price, book_value)

    println(s"\tbuyTransactions: $buyTransactions")
    return buyTransactions
  }

  def execute_bot(): Unit = {
    println(s"\n\nexecuting backtesting bot")
    portfolioBookValue += (0 -> 1.0)

    for (date_id <- market.getStart().to(market.getEnd()-1)) {
      println(s"\non date_id: ${date_id}:")
      if (date_id > 0) {
        val portfolio_ = execute_sells(portfolioTransactions.get(date_id - 1).get, date_id)
      }

      //      println(s"\tportfolio is worth: ${portfolioBookValue.get(date_id).get}")

      val buySignals = crystalBall.getBuySignals(date_id)
      println(s"\tbuySignals: $buySignals")

      //      val buySignalCount = buySignals.size
      //      println(s"\tbuySignalCount = $buySignalCount")

      if (buySignals.size > 0) {
        val buyTransactions = execute_buys(buySignals, portfolioBookValue.get(date_id).get, date_id)
        portfolioTransactions += (date_id -> buyTransactions)
      }
    }
  }


}

case class mkme(a: Int, b: String, c: Int) {}


object Main {

  def foo(): Unit = {
    val A = List(1, 2, 3, 4, 5)
    val B = List("bob", "jim", "hank", "sally", "jody")
    val C = List(5, 4, 3, 2, 1)

    val X = A.zip(B)
    println(X)
    val Y = A.zip(B).zip(C)
    println(Y)
    val mades = for {
      List(a: Int, b: String, c: Int) <- List(A, B, C).transpose
    } yield mkme(a, b, c)
    println(mades)

  }

  def simulate_market(): HashMap[String, HashMap[Int, Double]] = {

    var market = HashMap[String, HashMap[Int, Double]]()
    var pS = HashMap[Int, Double]()
    pS += (0 -> 100)
    pS += (1 -> 115)
    pS += (2 -> 110)
    pS += (3 -> 95)
    market += ("XYZ" -> pS)

    pS = HashMap[Int, Double]()
    pS += (0 -> 50)
    pS += (1 -> 60)
    pS += (2 -> 70)
    pS += (3 -> 40)
    market += ("ABC" -> pS)

    pS = HashMap[Int, Double]()
    pS += (0 -> 10)
    pS += (1 -> 9)
    pS += (2 -> 7)
    pS += (3 -> 15)
    market += ("FOO" -> pS)


    return market
  }

  def simulate_signals(): HashMap[Int, Vector[BuySignal]] = {
    println("simulating buy signals...")

    //
    // date_id = 0
    //
    // create 2 buy signals on date_id = 0
    var date_id = 0
    var buySignalAbc = new BuySignal("ABC", date_id)
    var buySignalXyz = new BuySignal("XYZ", date_id)
    // create a daily buy signal collection
    var dailySignals = Vector[BuySignal]()
    // append the 2 buy signals
    dailySignals = dailySignals :+ buySignalAbc
    dailySignals = dailySignals :+ buySignalXyz
    // check and confirm
    println(s"dailySignals: ${dailySignals.size}")
    assert(dailySignals.size == 2)
    var allSignals = HashMap[Int, Vector[BuySignal]]()
    allSignals += (date_id -> dailySignals)
    // check and confirm
    println(s"allSignals has size: ${allSignals.size}")
    assert(allSignals.size == 1)
    assert(allSignals contains date_id)

    //
    // date_id = 1
    //
    date_id = 1
    buySignalAbc = new BuySignal("ABC", date_id)
    buySignalXyz = new BuySignal("XYZ", date_id)
    var buySignalFoo = new BuySignal("FOO", date_id)
    // create a (?new?) daily buy signal collection
    dailySignals = Vector[BuySignal]()
    // append the 3 buy signals
    dailySignals = dailySignals :+ buySignalAbc
    dailySignals = dailySignals :+ buySignalXyz
    dailySignals = dailySignals :+ buySignalFoo
    // check and confirm
    println(s"dailySignals: ${dailySignals.size}")
    assert(dailySignals.size == 3)
    allSignals += (date_id -> dailySignals)
    // check and confirm
    println(s"allSignals has size: ${allSignals.size}")
    assert(allSignals.size == 2)
    assert(allSignals contains date_id)

    //
    // date_id = 2: assume no buy signals
    //
    date_id = 2
    dailySignals = Vector[BuySignal]()
    allSignals += (date_id -> dailySignals)

    //
    // date_id = 3
    //
    date_id = 3
    buySignalFoo = new BuySignal("FOO", date_id)
    // create a (?new?) daily buy signal collection
    dailySignals = Vector[BuySignal]()
    // append the 1 buy signals
    dailySignals = dailySignals :+ buySignalFoo
    // check and confirm
    println(s"dailySignals: ${dailySignals.size}")
    assert(dailySignals.size == 1)
    allSignals += (date_id -> dailySignals)
    // check and confirm
    println(s"allSignals has size: ${allSignals.size}")
    assert(allSignals.size == 4)
    assert(allSignals contains date_id)
    println("buy signal simulation complete")

    return allSignals
  }

  def setup(): Unit = {
    println("setting up...")

    val buySignals = simulate_signals()
    val crystalBall = CrystalBall
    crystalBall.signals = buySignals
    println(crystalBall)
    //    println(crystalBall.getBuySignals(0))

    val priceData = simulate_market()
    val market = Market
    market.priceData = priceData
    println("setup complete")

  }

  def main(args: Array[String]): Unit = {
    println("\nhello")

    setup()
    val market = Market
    market.getPrices(Vector[String]("XYZ", "FOO"), 0)

    var bot = Bot
    bot.execute_bot()

    //    foo()
    println("\n\ngoodbye")
  }
}
