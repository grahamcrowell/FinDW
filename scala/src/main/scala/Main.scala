import java.util.Date

import scala.collection.immutable.HashMap
import scala.collection.immutable.Vector
import scala.io.Source

/**
  * Created by gcrowell on 4/11/2017.
  */
class PriceSeries(symbol: String, values: Iterator[Float]) {
  override def toString: String =
    s"($symbol)"
}

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

object Bot {
  val rng = new Range(0, 10, 1)

}

object CsvReader {
  def read_data: Unit = {
    val f = "3stocks.csv"
    val src = Source.fromFile(f).getLines
    val getValue = (line: String) => line.split(',')(1).toFloat

    val ps = new PriceSeries("ABC", values = src.map(getValue))
    println(ps)

    val headerLine = src.take(1).next
    println(headerLine)
    //    println(getBuy0(headerLine)(0))
    //    println(getBuy1(headerLine)(0))
    //    println(getBuy2(headerLine)(0))

  }
}

object Main {

  def simulate(): HashMap[Int, Vector[BuySignal]] = {
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
    assert(allSignals.size == 3)
    assert(allSignals contains date_id)
    println("buy signal simulation complete")

    return allSignals
  }

  def main(args: Array[String]): Unit = {
    println("\nhello")

    val buySignals = simulate()
    val crystalBall = CrystalBall
    crystalBall.signals = buySignals
    println(crystalBall)
    println(crystalBall.getBuySignals(0))


    println("\n\ngoodbye")
  }
}
