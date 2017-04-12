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
  val signals = new HashMap[Int, Vector[BuySignal]]

  def getBuySignals(date_id: Int): Vector[BuySignal] = {
    return signals.get(date_id).get
  }
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
  def main(args: Array[String]): Unit = {
    println("Hello, world!")

    val allSignals = HashMap[Int, Vector[BuySignal]]()
    var dailySignals = Vector[BuySignal]()
    dailySignals = dailySignals :+ (new BuySignal("ABC", 0))
    dailySignals = dailySignals :+ (new BuySignal("XYZ", 0))
    println(dailySignals.size)
    println(dailySignals.count((x: BuySignal) => true))

    //    allSignals.+((0, dailySignals))
//    allSignals.++(dailySignals)

//    dailySignals.+:(new BuySignal("ABC", 1))
//    dailySignals.+:(new BuySignal("XYZ", 1))


  }
}
