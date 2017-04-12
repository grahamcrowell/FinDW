import java.util.Date

import scala.collection.immutable.HashMap
import scala.collection.immutable.Vector
import scala.io.Source
import scala.util.Random

/**
  * Created by gcrowell on 4/11/2017.
  */

//TODO create holding class
//TODO create book value class

class BuySignal(symbol: String, date_id: Int) {
  override def toString: String =
    s"Buy Signal: $symbol on $date_id"
}

object CrystalBall {
  var signals = new HashMap[Int, Vector[BuySignal]]

  def getBuySignals(date_id: Int): Vector[BuySignal] = {
    return signals.get(date_id).get
  }

  override def toString: String =
    s"Crystal Ball: date_id (${signals.keys.min} to ${signals.keys.max})"

}

object Market {
  var priceData = new HashMap[String, HashMap[Int, Float]]

  def getStart(): Int = {
    return 0
  }

  def getEnd(): Int = {
    return 3
  }

  def getPrice(symbol: String, date_id: Int): Float = {
    return priceData.get(symbol).get.get(date_id).get
  }

}


object Bot {
  var portfolioBookValue = HashMap[Int, Double]()
  //TODO store book value of each all holdings

  def execute_bot(): Unit = {
    println(s"\n\nexecuting backtesting bot")
    portfolioBookValue += (0 -> 1.0)
    val market = Market
    val crystalBall = CrystalBall
    for (elem <- market.getStart().to(market.getEnd())) {
      println(s"\non date_id: ${elem}:")
      val buySignals = crystalBall.getBuySignals(elem)
      println(s"\tbuySignals: $buySignals")
      val buySignalCount = buySignals.size
      println(s"\tbuySignalCount = $buySignalCount")
      if (buySignalCount > 0) {
        val perSignalWeighting = 1.0 / buySignalCount
        println(s"\tperSignalWeighting = $perSignalWeighting")

      }
    }
  }


}


object Main {

  def simulate_market(): HashMap[String, HashMap[Int, Float]] = {

    var market = HashMap[String, HashMap[Int, Float]]()
    var pS = HashMap[Int, Float]()
    pS += (0 -> 100)
    pS += (1 -> 115)
    pS += (2 -> 110)
    pS += (3 -> 95)
    market += ("XYZ" -> pS)

    pS = HashMap[Int, Float]()
    pS += (0 -> 50)
    pS += (1 -> 60)
    pS += (2 -> 70)
    pS += (3 -> 40)
    market += ("ABC" -> pS)

    pS = HashMap[Int, Float]()
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
    val buySignals = simulate_signals()
    val crystalBall = CrystalBall
    crystalBall.signals = buySignals
    println(crystalBall)
    //    println(crystalBall.getBuySignals(0))

    val priceData = simulate_market()
    val market = Market
    market.priceData = priceData
  }

  def main(args: Array[String]): Unit = {
    println("\nhello")

    setup()
    var bot = Bot
    bot.execute_bot()

    println("\n\ngoodbye")
  }
}
